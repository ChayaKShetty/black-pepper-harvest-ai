"""
Roboflow Service Module for Pepper Harvest AI
Connects to the real Roboflow YOLO26 Nano model deployment for black pepper harvest readiness detection.
Strictly uses genuine inference responses without synthetic or simulated results.
"""

import os
import io
import requests
from typing import Dict, Any, List, Tuple, Optional
from PIL import Image
import dotenv

# Load environment variables
dotenv.load_dotenv(override=True)


class RoboflowService:
    def __init__(
        self,
        api_key: Optional[str] = None,
        workspace: Optional[str] = None,
        project: Optional[str] = None,
        version: Optional[str] = None,
    ):
        self.api_key = api_key or os.getenv("ROBOFLOW_API_KEY", "").strip()
        self.workspace = workspace or os.getenv("ROBOFLOW_WORKSPACE", "chaya-shetty").strip()
        self.project = project or os.getenv("ROBOFLOW_PROJECT", "project-shhni").strip()
        self.version = str(version or os.getenv("ROBOFLOW_VERSION", "3")).strip()
        self.workflow_id = os.getenv("ROBOFLOW_WORKFLOW_ID", "").strip()

        # Possible project slugs if user configured generic "project"
        self.candidate_projects = [self.project]
        if self.project.lower() == "project":
            self.candidate_projects = ["project-shhni", "project"]
        elif "project-shhni" not in self.candidate_projects:
            self.candidate_projects.append("project-shhni")

    def is_configured(self) -> Tuple[bool, str]:
        """Checks if required Roboflow credentials are configured."""
        if not self.api_key:
            return False, "ROBOFLOW_API_KEY is not set. Please add it in your .env file or configuration panel."
        if not self.project:
            return False, "ROBOFLOW_PROJECT is missing."
        if not self.version:
            return False, "ROBOFLOW_VERSION is missing."
        return True, "Configuration present"

    def normalize_class_name(self, raw_class: str) -> str:
        """
        Normalizes dataset classes to the standard project classes:
        - 'matured'
        - 'immatured'
        """
        cls_lower = str(raw_class).strip().lower()
        if cls_lower in ["matured", "mature", "ready", "partially mature", "partiallymature"]:
            # Note: in Roboflow model for black pepper, matured indicates readiness
            return "matured"
        elif cls_lower in ["immatured", "immature", "not_ready"]:
            return "immatured"
        return cls_lower

    def calculate_harvest_summary(self, detections: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Calculates agronomic harvest readiness metrics based on genuine detections.
        """
        total = len(detections)
        matured_count = sum(1 for d in detections if d["normalized_class"] == "matured")
        immatured_count = sum(1 for d in detections if d["normalized_class"] == "immatured")

        if total > 0:
            maturity_ratio = (matured_count / total) * 100.0
            avg_confidence = sum(d["confidence"] for d in detections) / total
        else:
            maturity_ratio = 0.0
            avg_confidence = 0.0

        # Agronomic recommendation based on commercial black pepper harvesting standards:
        # Standard: In field practice, pepper spikes are harvested when 10-20% or more berries on a spike turn yellow/orange
        if total == 0:
            status = "No Spikes Detected"
            recommendation = "No pepper spikes detected. Please upload a clearer close-up photograph of the pepper vine."
            color = "#7F8C8D"
        elif maturity_ratio >= 35.0:
            status = "Ready for Harvest (Commercial Prime)"
            recommendation = (
                f"Harvest Recommended! {matured_count} out of {total} detected spikes ({maturity_ratio:.1f}%) "
                "show ripe maturity. Harvesting at this stage preserves maximum piperine content, high bulk density, "
                "and superior black pepper grade."
            )
            color = "#1E824C"
        elif maturity_ratio >= 15.0:
            status = "Early Harvest / Selective Picking"
            recommendation = (
                f"Early Harvest Window. {matured_count} of {total} spikes ({maturity_ratio:.1f}%) have reached maturity. "
                "Selective hand-picking of mature spikes is advised to avoid berry shedding while giving remaining spikes time to develop."
            )
            color = "#D4AC0D"
        else:
            status = "Immature - Allow to Develop"
            recommendation = (
                f"Not Ready for Harvest. Only {maturity_ratio:.1f}% matured spikes detected. "
                f"Majority ({immatured_count}/{total}) are still immature. Allow 2 to 4 weeks of further ripening "
                "to achieve proper berry weight and essential oil concentration."
            )
            color = "#E67E22"

        return {
            "total_detections": total,
            "matured_count": matured_count,
            "immatured_count": immatured_count,
            "maturity_pct": round(maturity_ratio, 2),
            "avg_confidence": round(avg_confidence * 100, 2),
            "status": status,
            "recommendation": recommendation,
            "badge_color": color,
        }

    def infer_image(
        self,
        image_input,
        confidence: float = 0.30,
        overlap: float = 0.45,
    ) -> Dict[str, Any]:
        """
        Sends an image to the real Roboflow YOLO26 Nano deployment and parses actual detections.
        
        image_input can be:
        - PIL.Image.Image
        - bytes / BytesIO
        - path to file (str)
        """
        configured, msg = self.is_configured()
        if not configured:
            return {
                "success": False,
                "error": msg,
                "detections": [],
                "summary": self.calculate_harvest_summary([]),
                "raw_response": None,
            }

        # Convert image_input to JPEG bytes
        try:
            if isinstance(image_input, str):
                with open(image_input, "rb") as f:
                    image_bytes = f.read()
            elif isinstance(image_input, bytes):
                image_bytes = image_input
            elif hasattr(image_input, "read"):
                image_input.seek(0)
                image_bytes = image_input.read()
            elif isinstance(image_input, Image.Image):
                buf = io.BytesIO()
                # Ensure RGB mode for JPEG encoding
                rgb_img = image_input.convert("RGB")
                rgb_img.save(buf, format="JPEG", quality=95)
                image_bytes = buf.getvalue()
            else:
                return {
                    "success": False,
                    "error": f"Unsupported image input type: {type(image_input)}",
                    "detections": [],
                    "summary": self.calculate_harvest_summary([]),
                    "raw_response": None,
                }
        except Exception as e:
            return {
                "success": False,
                "error": f"Failed to read image data: {str(e)}",
                "detections": [],
                "summary": self.calculate_harvest_summary([]),
                "raw_response": None,
            }

        # Try candidate projects (e.g. project-shhni)
        last_error = ""
        last_response = None

        for proj in self.candidate_projects:
            endpoint_url = (
                f"https://detect.roboflow.com/{proj}/{self.version}"
                f"?api_key={self.api_key}"
                f"&confidence={int(confidence * 100)}"
                f"&overlap={int(overlap * 100)}"
            )

            try:
                response = requests.post(
                    endpoint_url,
                    files={"file": ("input_image.jpg", image_bytes, "image/jpeg")},
                    timeout=25,
                )
                last_response = response

                if response.status_code == 200:
                    data = response.json()
                    raw_predictions = data.get("predictions", [])
                    image_info = data.get("image", {})

                    parsed_detections = []
                    for p in raw_predictions:
                        cls_name = p.get("class", "unknown")
                        norm_cls = self.normalize_class_name(cls_name)
                        parsed_detections.append({
                            "class": cls_name,
                            "normalized_class": norm_cls,
                            "confidence": float(p.get("confidence", 0.0)),
                            "x": float(p.get("x", 0.0)),
                            "y": float(p.get("y", 0.0)),
                            "width": float(p.get("width", 0.0)),
                            "height": float(p.get("height", 0.0)),
                            # Compute top-left x1, y1 and bottom-right x2, y2 coordinates
                            "x1": float(p.get("x", 0.0)) - float(p.get("width", 0.0)) / 2.0,
                            "y1": float(p.get("y", 0.0)) - float(p.get("height", 0.0)) / 2.0,
                            "x2": float(p.get("x", 0.0)) + float(p.get("width", 0.0)) / 2.0,
                            "y2": float(p.get("y", 0.0)) + float(p.get("height", 0.0)) / 2.0,
                            "detection_id": p.get("detection_id", ""),
                        })

                    summary = self.calculate_harvest_summary(parsed_detections)

                    return {
                        "success": True,
                        "error": None,
                        "detections": parsed_detections,
                        "summary": summary,
                        "image_info": image_info,
                        "inference_time": data.get("time", 0.0),
                        "model_id": data.get("resolved_model", {}).get("model_id", f"{proj}/{self.version}"),
                        "raw_response": data,
                    }
                elif response.status_code == 404:
                    last_error = f"Model resource not found for project '{proj}' version '{self.version}'."
                    continue
                else:
                    try:
                        err_json = response.json()
                        err_msg = err_json.get("message") or err_json.get("error", str(response.status_code))
                    except Exception:
                        err_msg = response.text[:200]
                    last_error = f"Roboflow API error (HTTP {response.status_code}): {err_msg}"
            except requests.exceptions.Timeout:
                last_error = "Connection to Roboflow Inference API timed out. Please check your internet connection."
            except requests.exceptions.ConnectionError:
                last_error = "Network connection failed. Unable to reach Roboflow API server."
            except Exception as e:
                last_error = f"Inference execution error: {str(e)}"

        return {
            "success": False,
            "error": last_error or "Inference request failed.",
            "detections": [],
            "summary": self.calculate_harvest_summary([]),
            "raw_response": getattr(last_response, "text", None) if last_response else None,
        }

