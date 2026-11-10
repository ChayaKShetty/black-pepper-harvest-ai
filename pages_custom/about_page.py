"""
About Project Page for Pepper Harvest AI
Comprehensive academic documentation of the final-year engineering project,
model specifications, technical architecture, and real field photographs.
"""

import os
import streamlit as st
from PIL import Image


def render_image_safe(rel_path: str, caption: str = ""):
    """Safely opens and renders an image with error handling."""
    if not rel_path:
        return
    full_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), rel_path)
    if os.path.exists(full_path):
        try:
            img = Image.open(full_path)
            st.image(img, caption=caption, use_container_width=True)
            return
        except Exception:
            pass
    st.info(f"📷 {caption}")


def render_about_page():
    # 1. Page Header Banner
    st.markdown("""
        <div style="margin-bottom: 24px;">
            <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px; flex-wrap:wrap;">
                <span class="badge-pill badge-pill-green">Academic Documentation</span>
                <span class="badge-pill" style="background:#EBF3EF; color:#185A37; border:1px solid #C2DFCE;">Final-Year B.E. Project</span>
                <span class="badge-pill" style="background:#FFF8E7; color:#B7791F; border:1px solid #F6E05E;">Computer Vision & AgTech</span>
            </div>
            <h1 style="color: #0F3E26; margin-top: 6px; margin-bottom: 6px; font-weight: 800;">
                About Project: Black Pepper Harvest Readiness AI
            </h1>
            <p style="color: #4A5B50; font-size: 1.05rem; line-height: 1.6; max-width: 950px; margin-bottom: 0;">
                Engineering Project Documentation — An AI-powered precision computer vision and decision support platform 
                engineered specifically for black pepper (<i>Piper nigrum</i> L.) harvest maturity identification and post-harvest optimization.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # 2. Main Documentation Tabs
    tab_overview, tab_model, tab_arch, tab_stack, tab_future = st.tabs([
        "📋 Project Overview",
        "🎯 Trained AI Model (YOLO26 Nano)",
        "🏗️ System Architecture",
        "💻 Technology Stack",
        "🚀 Future Scope & Evolution",
    ])

    # ----------------------------------------------------------------------------------
    # TAB 1: PROJECT OVERVIEW
    # ----------------------------------------------------------------------------------
    with tab_overview:
        st.markdown("""
        <div class="guide-card" style="border-top: 3.5px solid #0F3E26;">
            <h3 style="color:#0F3E26; margin-top:0; font-weight:800;">1. Problem Statement & Agronomic Motivation</h3>
            <p style="color:#4A5B50; font-size:0.98rem; line-height:1.65;">
                Black pepper (<i>Piper nigrum</i> L.), globally celebrated as the <b>"King of Spices"</b>, is a high-value 
                commercial cash crop across tropical agriculture. However, smallholder farmers face severe practical challenges 
                at harvest time that directly degrade market price and crop quality.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col_prob_text, col_prob_img = st.columns([1.2, 0.8])
        with col_prob_text:
            st.markdown("""
            #### ⚠️ The Critical Triad of Harvest Challenges:
            
            1. **Premature Picking Losses:**
               - Harvesting spikes prematurely (when berries are completely dark green and soft) yields shriveled, low-density peppercorns with dry recovery rates dropping below 25% (normal is 33–36%).
               - Immature berries lack the necessary accumulation of **piperine** (alkaloid responsible for pungency) and volatile essential oils.

            2. **Over-Ripening & Crop Shattering:**
               - Leaving spikes on vines until all berries turn dark red causes fruit detachment (shattering). Berries fall onto damp plantation soil where mold spores (*Aspergillus*, *Fusarium*) immediately infect the harvest.

            3. **Canopy Height & Manual Inspection Limitations:**
               - Pepper vines climb living support trees (Erythrina, Silver Oak) up to **6 to 8 meters**. Inspecting ripening spikes manually from ground level through dense shade is subjective and prone to human error.
            """)

        with col_prob_img:
            render_image_safe(
                "assets/images/pepper_harvest.jpg",
                caption="Manual Harvesting Challenges: Tall Vine Canopy (6-8m) on Live Support Trees",
            )

        st.markdown("---")

        st.markdown("""
        <div class="guide-card" style="border-top: 3.5px solid #2E8B57;">
            <h3 style="color:#0F3E26; margin-top:0; font-weight:800;">2. Project Objectives & Solution Overview</h3>
            <p style="color:#4A5B50; font-size:0.98rem; line-height:1.65;">
                To solve these problems, <b>Pepper Harvest AI</b> introduces an end-to-end computer vision and decision support platform 
                engineered to automate harvest readiness evaluation directly from field photography and video walkthroughs.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col_sol_img, col_sol_text = st.columns([0.8, 1.2])
        with col_sol_img:
            render_image_safe(
                "assets/images/hero_plantation.jpg",
                caption="Black Pepper (Piper nigrum) Commercial Plantation Canopy",
            )

        with col_sol_text:
            st.markdown("""
            #### 🎯 Primary Engineering Deliverables:
            
            - **Automated Spike Detection:** Real-time localized object detection using a trained **YOLO26 Nano** neural network to identify spike clusters in field images and videos.
            - **Dual-Class Physiological Ripening Classification:** Segregates detected spikes into 🟢 **`matured`** (ready for picking) and 🟡 **`immatured`** (requiring continued growth).
            - **Quantitative Maturity Index:** Calculates exact batch harvest readiness percentage:
            """)
            st.latex(r"\text{Maturity Index (\%)} = \left(\frac{N_{\text{matured}}}{N_{\text{total}}}\right) \times 100")
            st.markdown("""
            - **GenAI Agronomic Advisor:** Conversational agronomic reasoning powered by **Google Gemini** for pest diagnostics, NPK nutrition, and post-harvest blanching.
            - **Field Audit Trails & PDF Reports:** Generates formal, publication-grade **PDF Diagnostic Reports** and persists lifetime field logs in an ACID-compliant local **SQLite** database.
            """)

    # ----------------------------------------------------------------------------------
    # TAB 2: TRAINED AI MODEL (YOLO26 NANO)
    # ----------------------------------------------------------------------------------
    with tab_model:
        st.markdown("""
        <div class="guide-card" style="border-top: 3.5px solid #0F3E26;">
            <h3 style="color:#0F3E26; margin-top:0; font-weight:800;">Trained Computer Vision Architecture & Specifications</h3>
            <p style="color:#4A5B50; font-size:0.98rem; line-height:1.65;">
                This application interfaces with an authentic, GPU-trained computer vision model deployed on Roboflow Cloud Infrastructure 
                with TensorRT fp16 acceleration.
            </p>
        </div>
        """, unsafe_allow_html=True)

        m_col1, m_col2, m_col3 = st.columns(3)
        with m_col1:
            st.markdown("""
            <div class="metric-card" style="border-top: 3px solid #2ECC71;">
                <div class="metric-lbl">Model Architecture</div>
                <div class="metric-val" style="color:#0F3E26; font-size:1.3rem;">YOLO26 Nano</div>
                <div style="font-size:0.75rem; color:#718478;">Edge-optimized TRT fp16</div>
            </div>
            """, unsafe_allow_html=True)
        with m_col2:
            st.markdown("""
            <div class="metric-card" style="border-top: 3px solid #2E8B57;">
                <div class="metric-lbl">Roboflow Endpoint</div>
                <div class="metric-val" style="color:#2E8B57; font-size:1.3rem;">v3 (TRT)</div>
                <div style="font-size:0.75rem; color:#718478;">Workspace: <code>chaya-shetty</code></div>
            </div>
            """, unsafe_allow_html=True)
        with m_col3:
            st.markdown("""
            <div class="metric-card" style="border-top: 3px solid #E5A93C;">
                <div class="metric-lbl">Target Classes</div>
                <div class="metric-val" style="color:#B57C18; font-size:1.3rem;">2 Classes</div>
                <div style="font-size:0.75rem; color:#718478;"><code>matured</code> & <code>immatured</code></div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("#### 🔬 Target Class Visual Definitions & Ripening Biology:")

        v_col_mat, v_col_immat = st.columns(2)

        with v_col_mat:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #D1EAD9; border-top:4px solid #2ECC71; border-radius:12px; padding:18px; height:100%; box-shadow:0 3px 10px rgba(15,62,38,0.04);">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                    <span class="badge-pill badge-pill-green">Class 01</span>
                    <span style="font-weight:750; color:#2ECC71; font-size:0.9rem;">🟢 matured</span>
                </div>
                <h4 style="color:#0F3E26; margin-top:4px; margin-bottom:6px; font-weight:800;">Mature Black Pepper Spike</h4>
                <p style="font-size:0.88rem; color:#4A5B50; line-height:1.6; margin-bottom:12px;">
                    <b>Visual Marker:</b> Spikes where at least 1 to 2 berries display yellow to orange-red coloration. 
                    Remaining green berries on the same spike have achieved full dry matter accumulation and firm perisperm seeds.
                </p>
            </div>
            """, unsafe_allow_html=True)
            render_image_safe(
                "assets/images/guide/berry_ripening.jpg",
                caption="Class 'matured': 1–2 Orange/Red Ripening Markers on Spike Axis",
            )

        with v_col_immat:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #F9E2A0; border-top:4px solid #F39C12; border-radius:12px; padding:18px; height:100%; box-shadow:0 3px 10px rgba(15,62,38,0.04);">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                    <span class="badge-pill badge-pill-amber">Class 02</span>
                    <span style="font-weight:750; color:#B7791F; font-size:0.9rem;">🟡 immatured</span>
                </div>
                <h4 style="color:#0F3E26; margin-top:4px; margin-bottom:6px; font-weight:800;">Immature Green Pepper Spike</h4>
                <p style="font-size:0.88rem; color:#4A5B50; line-height:1.6; margin-bottom:12px;">
                    <b>Visual Marker:</b> Entire spike is uniformly dark or tender green with soft berries. 
                    Crushing a berry yields watery fluid rather than firm starchy perisperm. Requires 2–4 additional weeks of photosynthesis.
                </p>
            </div>
            """, unsafe_allow_html=True)
            render_image_safe(
                "sample_images/sample_spikes_1.jpg",
                caption="Class 'immatured': Uniformly Green, Soft Developing Spikes",
            )

        st.markdown("---")
        st.markdown("""
        #### 🛡️ Scientific Model Integrity Assurance:
        - **Zero Simulated Predictions:** All bounding box coordinates `[x, y, width, height]` and confidence probabilities are received directly from genuine inference responses.
        - **Robust In-Field Generalization:** Trained across varying natural lighting conditions: direct tropical sunlight, heavy forest canopy shadows, and overcast monsoon breaks.
        - **Color Annotation Standard:** High-contrast visual overlay featuring **Emerald Green (`#2ECC71`)** for matured spikes and **Amber Gold (`#F39C12`)** for immatured spikes.
        """)

    # ----------------------------------------------------------------------------------
    # TAB 3: SYSTEM ARCHITECTURE
    # ----------------------------------------------------------------------------------
    with tab_arch:
        st.markdown("""
        <div class="guide-card" style="border-top: 3.5px solid #0F3E26;">
            <h3 style="color:#0F3E26; margin-top:0; font-weight:800;">End-to-End System Pipeline & Decoupled Architecture</h3>
            <p style="color:#4A5B50; font-size:0.98rem; line-height:1.65;">
                The platform is architected around decoupled, high-cohesion modules spanning input ingestion, computer vision inference, 
                generative reasoning, and transactional audit logging.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.code("""
+---------------------------------------------------------------------------------------------------------+
|                                        FRONTEND PRESENTATION LAYER                                      |
|            Streamlit Multi-Page Framework • Modern Agricultural CSS • Responsive HTML Components        |
+---------------------------------------------------------------------------------------------------------+
                                    |                                           |
                [Field Images & Video Streams]                        [Agronomic User Inquiries]
                                    v                                           v
+-------------------------------------------------------+   +---------------------------------------------+
|               MEDIA INGESTION PIPELINE                |   |        GEMINI AI ASSISTANT BRIDGE           |
|  - PIL Image Rescaling & JPEG Normalization           |   |  - Scan Context Injection (Maturity Metrics)|
|  - OpenCV Video Frame Extractor (Temporal Stride)     |   |  - ICAR-IISR Aligned System Prompt          |
+-------------------------------------------------------+   +---------------------------------------------+
                            |                                                   |
             HTTP Multipart | (Base64 / Bytes)                    Google GenAI  | (gRPC / HTTPS)
                            v                                                   v
+-------------------------------------------------------+   +---------------------------------------------+
|           ROBOFLOW CLOUD INFERENCE SERVICE            |   |           GOOGLE GEMINI FLASH AI            |
|  - YOLO26 Nano Neural Network                         |   |  - gemini-flash-lite-latest / 2.5-flash     |
|  - TensorRT fp16 GPU Server                           |   |  - Multi-Turn Agronomic Conversational Log  |
|  - Non-Maximum Suppression (NMS) Filtering            |   |  - Scientific Disease / Curing Advice       |
+-------------------------------------------------------+   +---------------------------------------------+
                            |
           Bounding Boxes & Class Confidences
                            v
+---------------------------------------------------------------------------------------------------------+
|                                        BUSINESS LOGIC & REPORT ENGINE                                   |
|  - Maturity Ratio Heuristic Classification (Prime / Moderate / Early Stage Readiness)                   |
|  - Annotated Image Bounding Box Compositor (PIL ImageDraw)                                              |
|  - Automated PDF Report Generation (ReportLab Canvas) & CSV Vectorization (Pandas)                      |
|  - ACID Transactional Field Audit Persistence (SQLite3 history.db)                                      |
+---------------------------------------------------------------------------------------------------------+
        """, language="text")

        st.markdown("#### 🔄 The 4-Stage Operational Data Pipeline:")
        step_cols = st.columns(4)

        with step_cols[0]:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #E2E8E3; border-top:3px solid #0F3E26; border-radius:10px; padding:16px; height:100%;">
                <span class="badge-pill badge-pill-green">01. Capture</span>
                <h4 style="color:#0F3E26; margin-top:8px; font-weight:800;">Media Acquisition</h4>
                <p style="font-size:0.86rem; color:#4A5B50; line-height:1.5;">Field photos via file upload, camera, or video sweeps across canopy height.</p>
            </div>
            """, unsafe_allow_html=True)

        with step_cols[1]:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #E2E8E3; border-top:3px solid #2E8B57; border-radius:10px; padding:16px; height:100%;">
                <span class="badge-pill badge-pill-green">02. Inference</span>
                <h4 style="color:#0F3E26; margin-top:8px; font-weight:800;">YOLO26 Nano Run</h4>
                <p style="font-size:0.86rem; color:#4A5B50; line-height:1.5;">GPU inference detects spike clusters with bounding boxes and confidence scores.</p>
            </div>
            """, unsafe_allow_html=True)

        with step_cols[2]:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #E2E8E3; border-top:3px solid #E5A93C; border-radius:10px; padding:16px; height:100%;">
                <span class="badge-pill badge-pill-amber">03. Synthesis</span>
                <h4 style="color:#0F3E26; margin-top:8px; font-weight:800;">Maturity Scoring</h4>
                <p style="font-size:0.86rem; color:#4A5B50; line-height:1.5;">Heuristic engine computes maturity ratio and triggers tailored harvest advisories.</p>
            </div>
            """, unsafe_allow_html=True)

        with step_cols[3]:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #E2E8E3; border-top:3px solid #185A37; border-radius:10px; padding:16px; height:100%;">
                <span class="badge-pill badge-pill-green">04. Audit & AI</span>
                <h4 style="color:#0F3E26; margin-top:8px; font-weight:800;">Report & Advice</h4>
                <p style="font-size:0.86rem; color:#4A5B50; line-height:1.5;">Instant PDF diagnostic export, SQLite audit logging, and Gemini chatbot counseling.</p>
            </div>
            """, unsafe_allow_html=True)

    # ----------------------------------------------------------------------------------
    # TAB 4: TECHNOLOGY STACK
    # ----------------------------------------------------------------------------------
    with tab_stack:
        st.markdown("""
        <div class="guide-card" style="border-top: 3.5px solid #0F3E26;">
            <h3 style="color:#0F3E26; margin-top:0; font-weight:800;">Complete Technology Stack Breakdown</h3>
            <p style="color:#4A5B50; font-size:0.98rem; line-height:1.65;">
                Every component is chosen for stability, edge-readiness, memory efficiency, and seamless deployment across Windows and Linux.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st_c1, st_c2 = st.columns(2)

        with st_c1:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #E2E8E3; border-left:4px solid #FF4B4B; border-radius:12px; padding:18px; margin-bottom:14px; box-shadow:0 2px 8px rgba(0,0,0,0.03);">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <h4 style="color:#0F3E26; margin:0; font-weight:800;">🖥️ Streamlit (v1.35+)</h4>
                    <span class="badge-pill badge-pill-green">Application Engine</span>
                </div>
                <p style="font-size:0.88rem; color:#4A5B50; line-height:1.6; margin-top:8px; margin-bottom:0;">
                    Reactive web framework providing high-speed single-page application routing, session-state management, 
                    responsive container widths, and custom CSS agricultural theme injection.
                </p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #E2E8E3; border-left:4px solid #6706CE; border-radius:12px; padding:18px; margin-bottom:14px; box-shadow:0 2px 8px rgba(0,0,0,0.03);">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <h4 style="color:#0F3E26; margin:0; font-weight:800;">👁️ Roboflow YOLO26 Nano</h4>
                    <span class="badge-pill badge-pill-green">Vision Model</span>
                </div>
                <p style="font-size:0.88rem; color:#4A5B50; line-height:1.6; margin-top:8px; margin-bottom:0;">
                    Hosted TensorRT fp16 accelerated deep learning model specialized in agricultural spike detection, 
                    producing real coordinates and confidence scores under variable canopy illumination.
                </p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #E2E8E3; border-left:4px solid #4285F4; border-radius:12px; padding:18px; margin-bottom:14px; box-shadow:0 2px 8px rgba(0,0,0,0.03);">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <h4 style="color:#0F3E26; margin:0; font-weight:800;">🤖 Google Gemini AI (Flash)</h4>
                    <span class="badge-pill badge-pill-green">Agronomic LLM</span>
                </div>
                <p style="font-size:0.88rem; color:#4A5B50; line-height:1.6; margin-top:8px; margin-bottom:0;">
                    Generative AI foundation model via <code>google-genai</code>. Pre-conditioned with extensive ICAR-IISR 
                    agronomic domain instructions for accurate, hallucination-resistant crop doctoring.
                </p>
            </div>
            """, unsafe_allow_html=True)

        with st_c2:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #E2E8E3; border-left:4px solid #5C3EBA; border-radius:12px; padding:18px; margin-bottom:14px; box-shadow:0 2px 8px rgba(0,0,0,0.03);">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <h4 style="color:#0F3E26; margin:0; font-weight:800;">📹 OpenCV (cv2) & Pillow (PIL)</h4>
                    <span class="badge-pill badge-pill-green">Image Pipeline</span>
                </div>
                <p style="font-size:0.88rem; color:#4A5B50; line-height:1.6; margin-top:8px; margin-bottom:0;">
                    OpenCV manages high-efficiency video frame extraction across temporal intervals. Pillow draws 
                    crisp, anti-aliased bounding boxes and text labels on analyzed images.
                </p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #E2E8E3; border-left:4px solid #D9381E; border-radius:12px; padding:18px; margin-bottom:14px; box-shadow:0 2px 8px rgba(0,0,0,0.03);">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <h4 style="color:#0F3E26; margin:0; font-weight:800;">📄 ReportLab PDF Generator</h4>
                    <span class="badge-pill badge-pill-green">Report Engine</span>
                </div>
                <p style="font-size:0.88rem; color:#4A5B50; line-height:1.6; margin-top:8px; margin-bottom:0;">
                    Dynamic programmatic generation of formal PDF diagnostic reports with metadata tables, maturity scores, 
                    class breakdowns, and agronomic recommendations.
                </p>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #E2E8E3; border-left:4px solid #003B57; border-radius:12px; padding:18px; margin-bottom:14px; box-shadow:0 2px 8px rgba(0,0,0,0.03);">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <h4 style="color:#0F3E26; margin:0; font-weight:800;">🗄️ SQLite3 & Pandas</h4>
                    <span class="badge-pill badge-pill-green">Data Persistence</span>
                </div>
                <p style="font-size:0.88rem; color:#4A5B50; line-height:1.6; margin-top:8px; margin-bottom:0;">
                    Embedded relational database (<code>data/history.db</code>) ensuring persistent local field logs with zero 
                    external cloud storage dependencies. Pandas handles data filtering and master CSV exports.
                </p>
            </div>
            """, unsafe_allow_html=True)

    # ----------------------------------------------------------------------------------
    # TAB 5: FUTURE SCOPE & COMMERCIAL EVOLUTION
    # ----------------------------------------------------------------------------------
    with tab_future:
        st.markdown("""
        <div class="guide-card" style="border-top: 3.5px solid #0F3E26;">
            <h3 style="color:#0F3E26; margin-top:0; font-weight:800;">Future Scope & Commercial Agro-Tech Roadmap</h3>
            <p style="color:#4A5B50; font-size:0.98rem; line-height:1.65;">
                Planned technological evolutions transforming this academic prototype into an industrial-scale precision farming ecosystem.
            </p>
        </div>
        """, unsafe_allow_html=True)

        f_col1, f_col2 = st.columns(2)

        with f_col1:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #E2E8E3; border-top:4px solid #2E8B57; border-radius:12px; padding:20px; margin-bottom:16px; box-shadow:0 3px 10px rgba(15,62,38,0.04);">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                    <span class="badge-pill badge-pill-green">Phase 1</span>
                    <span style="font-weight:750; color:#2E8B57; font-size:0.85rem;">Autonomous Aerial Scouting</span>
                </div>
                <h4 style="color:#0F3E26; margin-top:4px; font-weight:800;">1. Agricultural Drone Integration</h4>
                <p style="font-size:0.9rem; color:#4A5B50; line-height:1.6;">
                    Deploying lightweight multi-rotor agricultural drones equipped with optical zoom cameras to fly along 
                    pepper tree rows at 6 to 8 meters. Eliminates risky manual ladder climbing and surveys entire hectares in minutes.
                </p>
            </div>
            """, unsafe_allow_html=True)
            render_image_safe(
                "assets/images/methods/live_standard.jpg",
                caption="High-Altitude Vine Scouting Along Standard Tree Columns",
            )

        with f_col2:
            st.markdown("""
            <div style="background:#FFFFFF; border:1px solid #E2E8E3; border-top:4px solid #E5A93C; border-radius:12px; padding:20px; margin-bottom:16px; box-shadow:0 3px 10px rgba(15,62,38,0.04);">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                    <span class="badge-pill badge-pill-amber">Phase 2</span>
                    <span style="font-weight:750; color:#B7791F; font-size:0.85rem;">IoT Solar Post-Harvest</span>
                </div>
                <h4 style="color:#0F3E26; margin-top:4px; font-weight:800;">2. Smart Solar Drying & Curing</h4>
                <p style="font-size:0.9rem; color:#4A5B50; line-height:1.6;">
                    Interfacing the application with IoT-enabled solar tunnel dryers equipped with real-time temperature, 
                    relative humidity, and grain moisture sensors to guarantee the critical 10–11% moisture threshold and eradicate aflatoxin.
                </p>
            </div>
            """, unsafe_allow_html=True)
            render_image_safe(
                "assets/images/guide/drying_storage.jpg",
                caption="Controlled Solar Tunnel Drying and Clean Poly-Sheet Curing",
            )
