"""
Unified Spike Maturity Detection Page for Pepper Harvest AI
Supports both Image-based and Video-based detection using real Roboflow YOLO26 Nano inference.
"""

import os
import streamlit as st
from PIL import Image, ImageOps
from io import BytesIO

from modules.roboflow_service import RoboflowService
from modules.video_detection import VideoDetectionService
from modules.image_processing import (
    annotate_image,
    detections_to_dataframe,
    pil_to_bytes,
    create_maturity_chart,
    COLOR_MATURED_HEX,
    COLOR_IMMATURED_HEX,
)
from modules.report_generator import generate_pdf_report, generate_csv_report
from modules.history_manager import add_history_entry

def load_uploaded_image(uploaded_file):
    """Load phone or laptop images and correct camera orientation."""
    image_bytes = uploaded_file.getvalue()

    with Image.open(BytesIO(image_bytes)) as img:
        img.load()
        corrected_image = ImageOps.exif_transpose(img)
        return corrected_image.convert("RGB")


def render_video_detection(rf_service: RoboflowService):
    st.markdown("### Video Stream Canopy Inspection")

    input_mode = st.radio(
        "Select Video Source:",
        ["📁 Upload Video from Device", "🌿 Use Preloaded Sample Plantation Video"],
        horizontal=True,
        key="vid_input_radio",
    )

    video_bytes = None
    video_filename = "sample_pepper_video.mp4"

    if input_mode == "📁 Upload Video from Device":
        uploaded_video = st.file_uploader(
            "Upload plantation inspection video (MP4, AVI, MOV)",
            type=["mp4", "avi", "mov"],
            key="vid_file_uploader",
        )
        if uploaded_video is not None:
            video_bytes = uploaded_video.read()
            video_filename = uploaded_video.name
    else:
        sample_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "sample_images", "sample_pepper_video.mp4")
        if os.path.exists(sample_path):
            with open(sample_path, "rb") as f:
                video_bytes = f.read()
            st.info("Loaded preloaded sample plantation video: `sample_pepper_video.mp4`")

    with st.expander("⚙️ Video Processing Parameters", expanded=True):
        v1, v2, v3 = st.columns(3)
        with v1:
            sample_interval = st.select_slider("Sample Interval (Seconds)", options=[0.5, 1.0, 1.5, 2.0, 3.0], value=1.0, key="v_sample_int")
        with v2:
            max_frames = st.slider("Max Sampled Frames", min_value=5, max_value=30, value=15, key="v_max_frames")
        with v3:
            conf_threshold = st.slider("Detection Confidence", min_value=0.15, max_value=0.80, value=0.25, step=0.05, key="v_conf_thresh")

    if video_bytes is not None:
        st.video(video_bytes)

        if st.button("🎬 Run Video Harvest Analysis", type="primary", width="stretch", key="btn_run_vid_analysis"):
            v_service = VideoDetectionService(rf_service)
            pbar = st.progress(0.0)
            stext = st.empty()

            def update_progress(val: float, message: str):
                pbar.progress(min(1.0, max(0.0, val)))
                stext.info(message)

            with st.spinner("Processing video frames through Roboflow YOLO26 Nano..."):
                res = v_service.process_video(
                    video_bytes_or_path=video_bytes,
                    sample_interval_sec=sample_interval,
                    max_frames=max_frames,
                    confidence_threshold=conf_threshold,
                    progress_callback=update_progress,
                )

            stext.empty()
            pbar.empty()

            if not res.get("success"):
