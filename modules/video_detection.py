"""
Video Detection Module for Pepper Harvest AI
Processes black pepper plantation video streams using OpenCV and genuine Roboflow YOLO26 Nano inference.
"""

import os
import cv2
import tempfile
import pandas as pd
from typing import Dict, Any, List, Optional, Callable
from PIL import Image

from modules.roboflow_service import RoboflowService
from modules.image_processing import annotate_image


class VideoDetectionService:
    def __init__(self, roboflow_service: Optional[RoboflowService] = None):
        self.rf_service = roboflow_service or RoboflowService()

    def process_video(
        self,
        video_bytes_or_path,
        sample_interval_sec: float = 1.0,
        max_frames: int = 20,
        confidence_threshold: float = 0.30,
        progress_callback: Optional[Callable[[float, str], None]] = None,
    ) -> Dict[str, Any]:
        """
        Samples video frames at defined intervals and runs genuine Roboflow inference.
        """
        # Save bytes to a temporary video file if input is bytes
        temp_video_file = None
        if isinstance(video_bytes_or_path, (bytes, bytearray)):
            temp_video_file = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False)
            temp_video_file.write(video_bytes_or_path)
            temp_video_file.close()
            video_path = temp_video_file.name
        elif hasattr(video_bytes_or_path, "read"):
            temp_video_file = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False)
            temp_video_file.write(video_bytes_or_path.read())
            temp_video_file.close()
            video_path = temp_video_file.name
        else:
            video_path = str(video_bytes_or_path)

        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            if temp_video_file and os.path.exists(temp_video_file.name):
                try:
                    os.remove(temp_video_file.name)
                except Exception:
                    pass
            return {
                "success": False,
                "error": "Could not open video file. Please check video format (MP4, AVI, MOV supported).",
                "frames_analyzed": 0,
                "summary": {},
                "timeline": [],
                "annotated_keyframes": [],
            }

        fps = cap.get(cv2.CAP_PROP_FPS) or 25.0
        total_video_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration_sec = total_video_frames / fps if fps > 0 else 0.0

        frame_step = max(1, int(fps * sample_interval_sec))
        target_frame_indices = list(range(0, total_video_frames, frame_step))[:max_frames]

        timeline_records = []
        annotated_keyframes = []
        total_matured = 0
        total_immatured = 0
        all_detections = []

        total_targets = len(target_frame_indices)
        if total_targets == 0:
            cap.release()
            return {
                "success": False,
                "error": "Video contains 0 valid frames.",
                "frames_analyzed": 0,
                "summary": {},
                "timeline": [],
                "annotated_keyframes": [],
            }

        for idx, frame_idx in enumerate(target_frame_indices):
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
            ret, frame = cap.read()
            if not ret or frame is None:
                continue

            current_time_sec = round(frame_idx / fps, 2)
            progress_val = (idx + 1) / total_targets
            if progress_callback:
                progress_callback(
                    progress_val,
                    f"Analyzing frame {idx + 1} of {total_targets} at {current_time_sec}s..."
                )

            # Convert BGR to RGB PIL image
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_img = Image.fromarray(rgb_frame)

            # Run genuine inference
            res = self.rf_service.infer_image(pil_img, confidence=confidence_threshold)
            if res.get("success"):
                dets = res.get("detections", [])
                summary = res.get("summary", {})
                m_count = summary.get("matured_count", 0)
                im_count = summary.get("immatured_count", 0)
                tot_count = summary.get("total_detections", 0)
                mat_pct = summary.get("maturity_pct", 0.0)

                total_matured += m_count
                total_immatured += im_count
                all_detections.extend(dets)

                # Annotate frame
                ann_img = annotate_image(pil_img, dets)
                if len(dets) > 0 or idx == 0 or idx == (total_targets - 1):
                    annotated_keyframes.append({
                        "frame_index": frame_idx,
                        "time_sec": current_time_sec,
                        "image": ann_img,
                        "matured": m_count,
                        "immatured": im_count,
                        "total": tot_count,
                        "maturity_pct": mat_pct,
                    })

                timeline_records.append({
                    "Frame": idx + 1,
                    "Timestamp (s)": current_time_sec,
                    "Total Spikes": tot_count,
                    "Matured": m_count,
                    "Immatured": im_count,
                    "Maturity (%)": mat_pct,
                    "Avg Confidence (%)": summary.get("avg_confidence", 0.0),
                })

        cap.release()
        if temp_video_file and os.path.exists(temp_video_file.name):
            try:
                os.remove(temp_video_file.name)
            except Exception:
                pass

        total_detected_all = total_matured + total_immatured
        overall_maturity_pct = round((total_matured / total_detected_all) * 100.0, 2) if total_detected_all > 0 else 0.0

        aggregate_summary = {
            "total_frames_analyzed": len(timeline_records),
            "video_duration_sec": round(duration_sec, 2),
            "total_detections": total_detected_all,
            "matured_count": total_matured,
            "immatured_count": total_immatured,
            "maturity_pct": overall_maturity_pct,
        }

        # Calculate overall verdict
        if total_detected_all == 0:
            aggregate_summary["status"] = "No Pepper Spikes Detected in Video"
            aggregate_summary["recommendation"] = "No pepper spikes detected across the sampled video frames. Ensure steady camera focus close to pepper vines."
            aggregate_summary["badge_color"] = "#7F8C8D"
        elif overall_maturity_pct >= 35.0:
            aggregate_summary["status"] = "Ready for Harvest (Commercial Prime)"
            aggregate_summary["recommendation"] = (
                f"Video inspection indicates {overall_maturity_pct:.1f}% maturity across sampled vines. "
                "The plantation plot is in peak harvest condition."
            )
            aggregate_summary["badge_color"] = "#1E824C"
        elif overall_maturity_pct >= 15.0:
            aggregate_summary["status"] = "Early Harvest / Selective Picking"
            aggregate_summary["recommendation"] = (
                f"Video inspection indicates {overall_maturity_pct:.1f}% maturity. "
                "Selective picking of ripe spikes is recommended to avoid drop losses."
            )
            aggregate_summary["badge_color"] = "#D4AC0D"
        else:
            aggregate_summary["status"] = "Immature - Allow to Develop"
            aggregate_summary["recommendation"] = (
                f"Video inspection indicates only {overall_maturity_pct:.1f}% mature spikes. "
                "Allow 2-4 more weeks of development."
            )
            aggregate_summary["badge_color"] = "#E67E22"

        return {
            "success": True,
            "summary": aggregate_summary,
            "timeline": timeline_records,
            "timeline_df": pd.DataFrame(timeline_records),
            "annotated_keyframes": annotated_keyframes,
            "all_detections": all_detections,
        }

