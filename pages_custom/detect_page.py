"""
Unified Spike Maturity Detection Page for Pepper Harvest AI
Supports both Image-based and Video-based detection using real Roboflow YOLO26 Nano inference.
"""

import os
import streamlit as st
from PIL import Image, ImageOps
from io import BytesIO
import pandas as pd

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


def render_detect_page():
    st.markdown("""
        <div style="margin-bottom: 20px;">
            <h1 style="color: #174D32; margin-bottom: 4px;">Harvest Maturity Detection</h1>
            <p style="color: #4A5568; font-size: 1.05rem;">
                Evaluate black pepper spikes for physiological harvest readiness using your trained <b>YOLO26 Nano</b> model.
            </p>
        </div>
    """, unsafe_allow_html=True)

    rf_service = RoboflowService()
    is_conf, conf_msg = rf_service.is_configured()

    if not is_conf:
        st.warning(f"⚠️ Roboflow Configuration Notice: {conf_msg}")
        with st.expander("Configure Roboflow Credentials"):
            new_key = st.text_input("Roboflow API Key", value=rf_service.api_key, type="password")
            new_proj = st.text_input("Project Name / Slug", value=rf_service.project)
            new_ver = st.text_input("Model Version", value=rf_service.version)
            if st.button("Save & Update Config"):
                rf_service.api_key = new_key.strip()
                rf_service.project = new_proj.strip()
                rf_service.version = new_ver.strip()
                st.success("Configuration updated!")
                st.rerun()

    # Unified Modality Tabs
    tab_image, tab_video = st.tabs(["📷 Single Image Analysis", "📹 Video Scan Inspection"])

    with tab_image:
        render_image_detection(rf_service)

    with tab_video:
        render_video_detection(rf_service)


# ----------------------------------------------------------------------
# IMAGE DETECTION PIPELINE
# ----------------------------------------------------------------------
def render_image_detection(rf_service: RoboflowService):
    st.markdown("### Image-Based Spike Inspection")

    with st.expander("📷 Visual Maturity Reference Guide (Matured vs. Immatured Spikes)", expanded=False):
        st.markdown("Compare your field spikes with this scientific maturity reference:")
        ref_c1, ref_c2 = st.columns(2)
        with ref_c1:
            ref_p1 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "images", "guide", "berry_ripening.jpg")
            if os.path.exists(ref_p1):
                st.image(ref_p1, caption="🟢 Matured: 1–2 Berries Turn Yellow/Orange (Ready for Harvest)", width="stretch")
        with ref_c2:
            ref_p2 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "sample_images", "sample_spikes_1.jpg")
            if os.path.exists(ref_p2):
                st.image(ref_p2, caption="🟡 Immatured: Uniformly Green Spikes (Allow Further Ripening)", width="stretch")

    input_method = st.radio(
        "Choose Image Input Method:",
        ["📁 Upload from Device (File / Gallery)", "📷 Camera Capture", "🌿 Select Sample Plantation Photo"],
        horizontal=True,
        key="img_input_radio",
    )

    image_to_process = None
