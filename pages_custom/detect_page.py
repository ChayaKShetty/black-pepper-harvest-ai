"""
Unified Spike Maturity Detection Page for Pepper Harvest AI
Supports both Image-based and Video-based detection using real Roboflow YOLO26 Nano inference.
"""

import os
import streamlit as st
from PIL import Image
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
                st.image(ref_p1, caption="🟢 Matured: 1–2 Berries Turn Yellow/Orange (Ready for Harvest)", use_container_width=True)
        with ref_c2:
            ref_p2 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "sample_images", "sample_spikes_1.jpg")
            if os.path.exists(ref_p2):
                st.image(ref_p2, caption="🟡 Immatured: Uniformly Green Spikes (Allow Further Ripening)", use_container_width=True)

    input_method = st.radio(
        "Choose Image Input Method:",
        ["📁 Upload from Device (File / Gallery)", "📷 Camera Capture", "🌿 Select Sample Plantation Photo"],
        horizontal=True,
        key="img_input_radio",
    )

    image_to_process = None
    image_filename = "pepper_sample.jpg"

    if input_method == "📁 Upload from Device (File / Gallery)":
        uploaded_file = st.file_uploader(
            "Upload black pepper spike photograph (JPG, JPEG, PNG)",
            type=["jpg", "jpeg", "png"],
            key="img_file_uploader",
            help="For best detection, take a clear photo of pepper vine spikes with adequate lighting.",
        )
        if uploaded_file is not None:
            try:
                image_to_process = Image.open(uploaded_file)
                image_filename = uploaded_file.name
            except Exception as e:
                st.error(f"Failed to load uploaded image: {e}")

    elif input_method == "📷 Camera Capture":
        camera_image = st.camera_input("Capture pepper spikes photo using device camera", key="img_camera_input")
        if camera_image is not None:
            try:
                image_to_process = Image.open(camera_image)
                image_filename = "camera_capture.jpg"
            except Exception as e:
                st.error(f"Failed to read camera capture: {e}")

    else:
        sample_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "sample_images")
        sample_files = []
        if os.path.exists(sample_dir):
            sample_files = [f for f in os.listdir(sample_dir) if f.lower().endswith((".jpg", ".jpeg", ".png"))]

        if sample_files:
            selected_sample = st.selectbox("Select a verified sample photograph:", sample_files, key="img_sample_select")
            sample_path = os.path.join(sample_dir, selected_sample)
            try:
                image_to_process = Image.open(sample_path)
                image_filename = selected_sample
            except Exception as e:
                st.error(f"Failed to open sample image: {e}")

    with st.expander("⚙️ Advanced Detection Settings (Confidence & Overlap)"):
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            conf_threshold = st.slider(
                "Confidence Threshold",
                min_value=0.10,
                max_value=0.90,
                value=0.25,
                step=0.05,
                key="img_conf_slider",
            )
        with col_c2:
            overlap_threshold = st.slider(
                "Overlap Threshold (IOU)",
                min_value=0.10,
                max_value=0.80,
                value=0.45,
                step=0.05,
                key="img_overlap_slider",
            )

    if image_to_process is not None:
        width, height = image_to_process.size
        st.markdown(f"**Loaded Image:** `{image_filename}` | Dimensions: `{width} × {height}` pixels")

        col_prev, col_act = st.columns([1, 1])
        with col_prev:
            st.image(image_to_process, caption="Original Input Image", use_container_width=True)

        with col_act:
            st.markdown("""
            #### Ready for YOLO26 Nano Inference
            Click **"Analyze Image"** to transmit the image to your real **YOLO26 Nano** Roboflow model deployment.
            
            The model identifies:
            - 🟢 **Matured** spikes (commercial harvest window)
            - 🟡 **Immatured** spikes (underdeveloped)
            """)

            if st.button("🚀 Analyze Image", type="primary", use_container_width=True, key="btn_run_img_analysis"):
                with st.spinner("Connecting to Roboflow YOLO26 Nano model & running inference..."):
                    result = rf_service.infer_image(
                        image_input=image_to_process,
                        confidence=conf_threshold,
                        overlap=overlap_threshold,
                    )

                if not result.get("success"):
                    st.error(f"❌ Inference Request Failed: {result.get('error')}")
                    return

                detections = result.get("detections", [])
                summary = result.get("summary", {})
                inf_time = result.get("inference_time", 0.0)

                st.session_state["last_analysis"] = {
                    "filename": image_filename,
                    "original_image": image_to_process,
                    "detections": detections,
                    "summary": summary,
                    "inf_time": inf_time,
                    "model_id": result.get("model_id", "YOLO26 Nano"),
                }

                try:
                    add_history_entry(
                        filename=image_filename,
                        media_type="Image",
                        total_detections=summary.get("total_detections", 0),
                        matured_count=summary.get("matured_count", 0),
                        immatured_count=summary.get("immatured_count", 0),
                        maturity_pct=summary.get("maturity_pct", 0.0),
                        status=summary.get("status", "Analyzed"),
                        recommendation=summary.get("recommendation", ""),
                        avg_confidence=summary.get("avg_confidence", 0.0),
                        details=detections,
                    )
                except Exception as db_err:
                    print(f"History DB note: {db_err}")

        if "last_analysis" in st.session_state and st.session_state["last_analysis"]["filename"] == image_filename:
            st.markdown("---")
            render_image_results(st.session_state["last_analysis"])


def render_image_results(analysis_data: dict):
    original_img = analysis_data["original_image"]
    detections = analysis_data["detections"]
    summary = analysis_data["summary"]
    filename = analysis_data["filename"]
    inf_time = analysis_data.get("inf_time", 0.0)
    model_id = analysis_data.get("model_id", "YOLO26 Nano")

    st.subheader("🎯 Real Detection Results")

    if len(detections) == 0:
        st.warning("⚠️ No pepper spikes detected. Please upload a clearer image.")
        return

    annotated_img = annotate_image(original_img, detections)

    # Metric Cards
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(f"""
        <div class="metric-card" style="border-top: 3px solid #0F3E26;">
            <div class="metric-lbl">Total Spikes</div>
            <div class="metric-val" style="color:#0F3E26;">{summary.get('total_detections', 0)}</div>
            <div style="font-size:0.75rem; color:#718478;">Spikes in View</div>
        </div>
        """, unsafe_allow_html=True)
    with m2:
        st.markdown(f"""
        <div class="metric-card" style="border-top: 3px solid {COLOR_MATURED_HEX};">
            <div class="metric-lbl">Matured (Ripe)</div>
            <div class="metric-val" style="color:{COLOR_MATURED_HEX};">{summary.get('matured_count', 0)}</div>
            <div style="font-size:0.75rem; color:#2ECC71; font-weight:700;">Ready to Harvest</div>
        </div>
        """, unsafe_allow_html=True)
    with m3:
        st.markdown(f"""
        <div class="metric-card" style="border-top: 3px solid {COLOR_IMMATURED_HEX};">
            <div class="metric-lbl">Immatured (Unripe)</div>
            <div class="metric-val" style="color:{COLOR_IMMATURED_HEX};">{summary.get('immatured_count', 0)}</div>
            <div style="font-size:0.75rem; color:#E8B54A; font-weight:700;">Developing Vine</div>
        </div>
        """, unsafe_allow_html=True)
    with m4:
        st.markdown(f"""
        <div class="metric-card" style="border-top: 3px solid #2E8B57;">
            <div class="metric-lbl">Maturity Index</div>
            <div class="metric-val" style="color:#0F3E26;">{summary.get('maturity_pct', 0.0):.1f}%</div>
            <div style="font-size:0.75rem; color:#718478;">Canopy Ratio</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    # Harvest Verdict Banner
    mat_val = summary.get("maturity_pct", 0)
    if mat_val >= 35:
        verdict_class = "prime"
        v_icon = "🎉"
        v_badge = "READY FOR HARVEST"
        badge_bg = "#2ECC71"
    elif mat_val >= 15:
        verdict_class = "early"
        v_icon = "⚡"
        v_badge = "EARLY HARVEST (SELECTIVE)"
        badge_bg = "#F39C12"
    else:
        verdict_class = "immature"
        v_icon = "⏳"
        v_badge = "IMMATURE (NOT READY)"
        badge_bg = "#E67E22"

    st.markdown(f"""
        <div class="verdict-box {verdict_class}">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; margin-bottom:10px;">
                <div style="display:flex; align-items:center; gap:8px;">
                    <span style="font-size:1.6rem;">{v_icon}</span>
                    <h3 style="margin:0; color:#0F3E26; font-size:1.35rem; font-weight:800;">Harvest Status: {summary.get('status')}</h3>
                </div>
                <span style="background:{badge_bg}; color:#FFFFFF; font-weight:800; font-size:0.75rem; padding:4px 12px; border-radius:20px; letter-spacing:0.5px;">
                    {v_badge}
                </span>
            </div>
            <p style="font-size:1.02rem; margin-bottom:8px; color:#19271E; line-height:1.6;">
                <b>Agronomic Advisory:</b> {summary.get('recommendation')}
            </p>
            <div style="display:flex; gap:16px; font-size:0.8rem; color:#718478; margin-top:10px;">
                <span>🤖 Model: <code>{model_id}</code></span>
                <span>⏱️ Latency: <code>{inf_time:.3f}s</code></span>
                <span>📊 Confidence: <code>{summary.get('avg_confidence', 0.0):.1f}%</code></span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    tab_side, tab_ann, tab_orig = st.tabs(["Side-by-Side View", "Annotated Image", "Original Image"])
    with tab_side:
        c1, c2 = st.columns(2)
        with c1:
            st.image(original_img, caption="Original Input", use_container_width=True)
        with c2:
            st.image(annotated_img, caption="AI Annotated (Green: Matured | Amber: Immatured)", use_container_width=True)
    with tab_ann:
        st.image(annotated_img, caption="Annotated Result with Bounding Boxes", use_container_width=True)
    with tab_orig:
        st.image(original_img, caption="Original Image", use_container_width=True)

    # Matplotlib Chart
    st.subheader("📊 Maturity Stage Distribution Chart")
    chart_fig = create_maturity_chart(summary)
    if chart_fig:
        st.pyplot(chart_fig, use_container_width=False)

    st.subheader("Genuine Detection Coordinates & Confidence Scores")
    st.dataframe(detections_to_dataframe(detections), use_container_width=True)

    st.subheader("Export & Download Results")
    d1, d2, d3 = st.columns(3)
    with d1:
        st.download_button(
            "📥 Download Annotated Image",
            data=pil_to_bytes(annotated_img, format="JPEG"),
            file_name=f"annotated_{filename}",
            mime="image/jpeg",
            use_container_width=True,
            key="dl_img_btn",
        )
    with d2:
        try:
            pdf_bytes = generate_pdf_report(filename, "Image", summary, detections, annotated_image=annotated_img)
            st.download_button(
                "📄 Download PDF Field Report",
                data=pdf_bytes,
                file_name=f"Harvest_Report_{filename.split('.')[0]}.pdf",
                mime="application/pdf",
                use_container_width=True,
                key="dl_pdf_btn",
            )
        except Exception as e:
            st.error(f"PDF creation error: {e}")
    with d3:
        try:
            st.download_button(
                "📊 Download CSV Data",
                data=generate_csv_report(filename, summary, detections),
                file_name=f"detections_{filename.split('.')[0]}.csv",
                mime="text/csv",
                use_container_width=True,
                key="dl_csv_btn",
            )
        except Exception as e:
            st.error(f"CSV error: {e}")

    st.markdown("<br/>", unsafe_allow_html=True)
    if st.button("🔄 Analyze Another Image", use_container_width=True, key="reset_img_btn"):
        if "last_analysis" in st.session_state:
            del st.session_state["last_analysis"]
        st.rerun()


# ----------------------------------------------------------------------
# VIDEO DETECTION PIPELINE
# ----------------------------------------------------------------------
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

        if st.button("🎬 Run Video Harvest Analysis", type="primary", use_container_width=True, key="btn_run_vid_analysis"):
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
                st.error(f"Video analysis error: {res.get('error')}")
                return

            st.session_state["last_video_analysis"] = {
                "filename": video_filename,
                "summary": res["summary"],
                "timeline": res["timeline"],
                "timeline_df": res["timeline_df"],
                "annotated_keyframes": res["annotated_keyframes"],
                "all_detections": res["all_detections"],
            }

            try:
                summary = res["summary"]
                add_history_entry(
                    filename=video_filename,
                    media_type="Video",
                    total_detections=summary.get("total_detections", 0),
                    matured_count=summary.get("matured_count", 0),
                    immatured_count=summary.get("immatured_count", 0),
                    maturity_pct=summary.get("maturity_pct", 0.0),
                    status=summary.get("status", "Video Analyzed"),
                    recommendation=summary.get("recommendation", ""),
                    avg_confidence=0.0,
                    details=res["all_detections"][:30],
                )
            except Exception as e:
                print(f"Video history error: {e}")

    if "last_video_analysis" in st.session_state:
        st.markdown("---")
        render_video_results(st.session_state["last_video_analysis"])


def render_video_results(video_data: dict):
    summary = video_data["summary"]
    timeline_df = video_data["timeline_df"]
    keyframes = video_data["annotated_keyframes"]
    filename = video_data["filename"]
    all_detections = video_data["all_detections"]

    st.subheader("📊 Aggregate Video Inspection Summary")
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown(f"""
        <div class="metric-card" style="border-top: 3px solid #0F3E26;">
            <div class="metric-lbl">Frames Analyzed</div>
            <div class="metric-val" style="color:#0F3E26;">{summary.get('total_frames_analyzed', 0)}</div>
            <div style="font-size:0.75rem; color:#718478;">Temporal Samples</div>
        </div>
        """, unsafe_allow_html=True)
    with m2:
        st.markdown(f"""
        <div class="metric-card" style="border-top: 3px solid #2E8B57;">
            <div class="metric-lbl">Aggregate Spikes</div>
            <div class="metric-val" style="color:#0F3E26;">{summary.get('total_detections', 0)}</div>
            <div style="font-size:0.75rem; color:#718478;">Total Instances</div>
        </div>
        """, unsafe_allow_html=True)
    with m3:
        st.markdown(f"""
        <div class="metric-card" style="border-top: 3px solid {COLOR_MATURED_HEX};">
            <div class="metric-lbl">Matured Spikes</div>
            <div class="metric-val" style="color:{COLOR_MATURED_HEX};">{summary.get('matured_count', 0)}</div>
            <div style="font-size:0.75rem; color:#2ECC71; font-weight:700;">Ready Clusters</div>
        </div>
        """, unsafe_allow_html=True)
    with m4:
        st.markdown(f"""
        <div class="metric-card" style="border-top: 3px solid #E5A93C;">
            <div class="metric-lbl">Canopy Maturity</div>
            <div class="metric-val" style="color:#0F3E26;">{summary.get('maturity_pct', 0.0):.1f}%</div>
            <div style="font-size:0.75rem; color:#718478;">Mean Field Index</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    v_mat = summary.get("maturity_pct", 0)
    v_cls = "prime" if v_mat >= 35 else ("early" if v_mat >= 15 else "immature")
    v_icon = "🎉" if v_mat >= 35 else ("⚡" if v_mat >= 15 else "⏳")

    st.markdown(f"""
        <div class="verdict-box {v_cls}">
            <div style="display:flex; align-items:center; gap:8px; margin-bottom:8px;">
                <span style="font-size:1.6rem;">{v_icon}</span>
                <h3 style="margin:0; color:#0F3E26; font-size:1.35rem; font-weight:800;">Overall Harvest Status: {summary.get('status')}</h3>
            </div>
            <p style="font-size:1.02rem; margin-bottom:0; color:#19271E; line-height:1.6;">
                <b>Agronomic Advisory:</b> {summary.get('recommendation')}
            </p>
        </div>
    """, unsafe_allow_html=True)

    chart_fig = create_maturity_chart(summary)
    if chart_fig:
        st.pyplot(chart_fig, use_container_width=False)

    if not timeline_df.empty:
        st.subheader("📈 Maturity Progression Across Video Timeline")
        st.line_chart(
            timeline_df.set_index("Timestamp (s)")[["Matured", "Immatured"]],
            color=[COLOR_MATURED_HEX, COLOR_IMMATURED_HEX],
        )
        with st.expander("View Detailed Frame-by-Frame Data Table"):
            st.dataframe(timeline_df, use_container_width=True)

    if keyframes:
        st.subheader("🖼️ Sampled Keyframe Annotations")
        cols = st.columns(min(3, len(keyframes)))
        for idx, kf in enumerate(keyframes):
            with cols[idx % len(cols)]:
                st.image(kf["image"], caption=f"Time: {kf['time_sec']}s | Matured: {kf['matured']} | Immatured: {kf['immatured']}", use_container_width=True)

    st.subheader("Export Video Analysis")
    c1, c2 = st.columns(2)
    with c1:
        try:
            rep_img = keyframes[0]["image"] if keyframes else None
            pdf_bytes = generate_pdf_report(filename, "Video", summary, all_detections[:20], annotated_image=rep_img)
            st.download_button("📄 Download Video PDF Report", data=pdf_bytes, file_name=f"Video_Report_{filename.split('.')[0]}.pdf", mime="application/pdf", use_container_width=True, key="dl_v_pdf")
        except Exception as e:
            st.error(f"PDF creation error: {e}")
    with c2:
        try:
            st.download_button("📊 Download Timeline CSV Data", data=timeline_df.to_csv(index=False).encode("utf-8"), file_name=f"timeline_{filename.split('.')[0]}.csv", mime="text/csv", use_container_width=True, key="dl_v_csv")
        except Exception as e:
            st.error(f"CSV export error: {e}")

    st.markdown("<br/>", unsafe_allow_html=True)
    if st.button("🔄 Analyze Another Video", use_container_width=True, key="reset_vid_btn"):
        if "last_video_analysis" in st.session_state:
            del st.session_state["last_video_analysis"]
        st.rerun()
