"""
Home Dashboard for Black Pepper Harvest Readiness AI (Pepper Harvest AI)
Modern agricultural dashboard with plantation hero section, system status indicators,
feature cards, farmer instructions, and harvest recommendations.
"""

import os
import streamlit as st
from PIL import Image

from modules.roboflow_service import RoboflowService
from modules.gemini_assistant import GeminiAssistant
from modules.history_manager import get_all_history


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
    if caption:
        st.info(f"📷 {caption}")


def render_home_page():
    # Hero Banner
    st.markdown("""
        <div class="hero-banner">
            <span class="hero-badge">🌿 AI Precision Agriculture System</span>
            <h1>Black Pepper Harvest Readiness AI</h1>
            <p>Smart AI-powered maturity detection and cultivation guidance for black pepper farmers. 
            Identify mature and immature pepper spikes instantly to harvest at peak piperine and essential oil concentration.</p>
        </div>
    """, unsafe_allow_html=True)

    # Hero image and CTA row
    col1, col2 = st.columns([1.1, 0.9])

    with col1:
        hero_img_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "images", "hero_plantation.jpg")
        if os.path.exists(hero_img_path):
            try:
                hero_img = Image.open(hero_img_path)
                st.image(hero_img, caption="Black Pepper (Piper nigrum) Plantation Canopy", use_container_width=True)
            except Exception:
                st.info("🌿 Black Pepper Plantation Canopy")
        else:
            st.info("🌿 Black Pepper Plantation Canopy")

    with col2:
        st.markdown("""
        <div style="background:#FFFFFF; border:1px solid #E2E8E3; border-radius:16px; padding:24px; box-shadow:0 4px 14px rgba(15,62,38,0.05); height:100%;">
            <span class="badge-pill badge-pill-green" style="margin-bottom:12px;">Cash Crop Optimization</span>
            <h3 style="color:#0F3E26; margin-top:10px; margin-bottom:10px; font-weight:800;">Empowering Spice Farmers with Precision Vision</h3>
            <p style="font-size:0.95rem; color:#4A5B50; line-height:1.65; margin-bottom:16px;">
                Black pepper (<i>Piper nigrum</i>), globally celebrated as the <b>"King of Spices"</b>, demands scientific harvesting timing to maximize dry recovery, pungency (piperine), and export bulk density (500–600 g/L).
            </p>
            <div style="background:#F6FAF7; border-left:4px solid #2E8B57; border-radius:8px; padding:12px 14px; margin-bottom:20px; font-size:0.88rem; color:#19271E;">
                <b>YOLO26 Nano Detection Target Classes:</b><br/>
                🟢 <b>Matured Spikes</b>: Spikes with berries exhibiting yellow-orange blush ready for picking.<br/>
                🟡 <b>Immatured Spikes</b>: Green berries requiring continued vine photosynthesis.
            </div>
        </div>
        """, unsafe_allow_html=True)

        btn_c1, btn_c2 = st.columns(2)
        with btn_c1:
            if st.button("🌿 Analyze Pepper Spikes", type="primary", use_container_width=True):
                st.session_state["nav_selection"] = "Detect Maturity"
                st.rerun()
        with btn_c2:
            if st.button("📖 Cultivation Guide", use_container_width=True):
                st.session_state["nav_selection"] = "Cultivation & Growing Guide"
                st.rerun()

    st.markdown("---")

    # Real-Time System Status Indicators
    st.markdown("### 🔌 Real-Time AI System Status")
    s_col1, s_col2, s_col3 = st.columns(3)

    # Check Roboflow
    rf = RoboflowService()
    rf_ok, _ = rf.is_configured()

    # Check Gemini
    gem_key = st.session_state.get("runtime_gemini_key") or os.getenv("GEMINI_API_KEY", "").strip()
    gem = GeminiAssistant(api_key=gem_key)
    gem_ok, _ = gem.is_configured()

    # Check History
    total_saved_scans = len(get_all_history())

    with s_col1:
        if rf_ok:
            st.markdown(f"""
            <div class="metric-card" style="border-top: 4px solid #2ECC71;">
                <div class="metric-lbl">Vision Model Status</div>
                <div style="font-size:1.2rem; font-weight:800; color:#0F3E26; margin: 6px 0;">
                    <span class="status-dot-pulse"></span>YOLO26 Nano Online
                </div>
                <div style="font-size:0.8rem; color:#718478;">Workspace: <code>{rf.workspace}</code> | v{rf.version}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="metric-card" style="border-top: 4px solid #E74C3C;">
                <div class="metric-lbl">Vision Model Status</div>
                <div style="font-size:1.2rem; font-weight:800; color:#E74C3C; margin: 6px 0;">🔴 Roboflow Offline</div>
                <div style="font-size:0.8rem; color:#718478;">Configure API key in settings</div>
            </div>
            """, unsafe_allow_html=True)

    with s_col2:
        if gem_ok:
            st.markdown(f"""
            <div class="metric-card" style="border-top: 4px solid #2E8B57;">
                <div class="metric-lbl">Farming Assistant</div>
                <div style="font-size:1.2rem; font-weight:800; color:#0F3E26; margin: 6px 0;">
                    <span class="status-dot-pulse"></span>Gemini AI Active
                </div>
                <div style="font-size:0.8rem; color:#718478;">Model: <code>{gem.model_name}</code></div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="metric-card" style="border-top: 4px solid #F39C12;">
                <div class="metric-lbl">Farming Assistant</div>
                <div style="font-size:1.2rem; font-weight:800; color:#F39C12; margin: 6px 0;">🟡 Gemini Key Needed</div>
                <div style="font-size:0.8rem; color:#718478;">Activate in assistant tab</div>
            </div>
            """, unsafe_allow_html=True)

    with s_col3:
        st.markdown(f"""
        <div class="metric-card" style="border-top: 4px solid #E5A93C;">
            <div class="metric-lbl">Field Database Log</div>
            <div style="font-size:1.2rem; font-weight:800; color:#0F3E26; margin: 6px 0;">
                <span style="color:#2E8B57;">📁</span> SQLite Storage
            </div>
            <div style="font-size:0.8rem; color:#718478;"><b>{total_saved_scans}</b> audit scans archived</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Core Features Row (Section 3 Required Feature Cards)
    st.markdown("### 🌾 Core System Capabilities")
    fcol1, fcol2, fcol3, fcol4 = st.columns(4)

    with fcol1:
        render_image_safe("assets/images/pepper_harvest.jpg", caption="AI Spike Detection")
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🔍</div>
            <h4 style="color:#0F3E26; margin-bottom:8px; font-weight:800;">1. Harvest Detection</h4>
            <p style="font-size:0.88rem; color:#4A5B50; margin-bottom:16px;">Dual photo & video canopy analysis detecting matured and immatured spikes with real YOLO26 Nano inference.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Launch Detection ➔", key="btn_f1", use_container_width=True):
            st.session_state["nav_selection"] = "Detect Maturity"
            st.rerun()

    with fcol2:
        render_image_safe("assets/images/guide/botany_pepper.jpg", caption="23 ICAR-IISR Chapters")
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📖</div>
            <h4 style="color:#0F3E26; margin-bottom:8px; font-weight:800;">2. Cultivation Guide</h4>
            <p style="font-size:0.88rem; color:#4A5B50; margin-bottom:16px;">23 ICAR-IISR cultivation chapters, 7 modern growing methods with video guides, and propagation protocols.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Explore Guide ➔", key="btn_f2", use_container_width=True):
            st.session_state["nav_selection"] = "Cultivation & Growing Guide"
            st.rerun()

    with fcol3:
        render_image_safe("assets/images/methods/support_tree.jpg", caption="Gemini AI Advisor")
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <h4 style="color:#0F3E26; margin-bottom:8px; font-weight:800;">3. Gemini Assistant</h4>
            <p style="font-size:0.88rem; color:#4A5B50; margin-bottom:16px;">24/7 Google Gemini agronomist answering questions on Phytophthora, fertilizers, and curing methods.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Consult AI ➔", key="btn_f3", use_container_width=True):
            st.session_state["nav_selection"] = "Gemini AI Assistant"
            st.rerun()

    with fcol4:
        render_image_safe("assets/images/guide/drying_storage.jpg", caption="Field Scan Reports")
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📜</div>
            <h4 style="color:#0F3E26; margin-bottom:8px; font-weight:800;">4. Scan History & Reports</h4>
            <p style="font-size:0.88rem; color:#4A5B50; margin-bottom:16px;">Persistent audit log tracking lifetime scans, maturity averages, and downloadable PDF & CSV diagnostic reports.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View History ➔", key="btn_f4", use_container_width=True):
            st.session_state["nav_selection"] = "Analysis History"
            st.rerun()

    st.markdown("---")

    # Simple Instructions for Farmers (Section 3 Requirement)
    st.markdown("### 👨‍🌾 How Farmers Can Use This Application")
    st.markdown("""
    Follow these simple steps in your plantation to accurately assess harvest readiness and protect spice quality:
    """)

    inst1, inst2, inst3, inst4 = st.columns(4)

    with inst1:
        st.markdown("""
        <div style="background:#FFFFFF; border:1px solid #E2E8E3; border-radius:14px; padding:20px; height:100%; box-shadow:0 2px 6px rgba(15,62,38,0.04);">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <div style="font-size:1.8rem;">📸</div>
                <span style="font-size:0.75rem; font-weight:800; color:#2E8B57; background:#EAF5EE; padding:2px 8px; border-radius:10px;">01</span>
            </div>
            <h4 style="color:#0F3E26; margin-top:12px; margin-bottom:6px; font-weight:800;">Step 1: Capture Spikes</h4>
            <p style="font-size:0.88rem; color:#4A5B50; margin-bottom:0;">
                Walk along pepper vine rows and snap a photo or record a short video of spike clusters in natural daylight.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with inst2:
        st.markdown("""
        <div style="background:#FFFFFF; border:1px solid #E2E8E3; border-radius:14px; padding:20px; height:100%; box-shadow:0 2px 6px rgba(15,62,38,0.04);">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <div style="font-size:1.8rem;">⚡</div>
                <span style="font-size:0.75rem; font-weight:800; color:#2E8B57; background:#EAF5EE; padding:2px 8px; border-radius:10px;">02</span>
            </div>
            <h4 style="color:#0F3E26; margin-top:12px; margin-bottom:6px; font-weight:800;">Step 2: Run AI Scan</h4>
            <p style="font-size:0.88rem; color:#4A5B50; margin-bottom:0;">
                Upload the media or use camera capture. The <b>YOLO26 Nano</b> model automatically pinpoints each spike.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with inst3:
        st.markdown("""
        <div style="background:#FFFFFF; border:1px solid #E2E8E3; border-radius:14px; padding:20px; height:100%; box-shadow:0 2px 6px rgba(15,62,38,0.04);">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <div style="font-size:1.8rem;">📊</div>
                <span style="font-size:0.75rem; font-weight:800; color:#2E8B57; background:#EAF5EE; padding:2px 8px; border-radius:10px;">03</span>
            </div>
            <h4 style="color:#0F3E26; margin-top:12px; margin-bottom:6px; font-weight:800;">Step 3: Read Verdict</h4>
            <p style="font-size:0.88rem; color:#4A5B50; margin-bottom:0;">
                View the maturity index percentage, ratio of ripe vs. unripe spikes, and the clear agronomic advisory.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with inst4:
        st.markdown("""
        <div style="background:#FFFFFF; border:1px solid #E2E8E3; border-radius:14px; padding:20px; height:100%; box-shadow:0 2px 6px rgba(15,62,38,0.04);">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <div style="font-size:1.8rem;">📄</div>
                <span style="font-size:0.75rem; font-weight:800; color:#2E8B57; background:#EAF5EE; padding:2px 8px; border-radius:10px;">04</span>
            </div>
            <h4 style="color:#0F3E26; margin-top:12px; margin-bottom:6px; font-weight:800;">Step 4: Export & Consult</h4>
            <p style="font-size:0.88rem; color:#4A5B50; margin-bottom:0;">
                Download your printable <b>PDF Field Report</b> and ask the Gemini Assistant for custom blanching and drying advice.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Agronomic Harvesting Insights
    st.markdown("### 🌶️ Agronomic Harvesting Rules of Thumb")
    rule_col1, rule_col2 = st.columns(2)

    with rule_col1:
        st.markdown("""
        <div style="background:#FFFFFF; border:1px solid #E2E8E3; border-radius:14px; padding:22px; height:100%; box-shadow:0 2px 6px rgba(15,62,38,0.04);">
            <h4 style="color:#0F3E26; margin-top:0; font-weight:800;">🌶️ The 1-2 Berry Ripening Indicator</h4>
            <p style="font-size:0.92rem; color:#4A5B50; line-height:1.6;">
                In commercial black pepper cultivation:
            </p>
            <ul style="font-size:0.9rem; color:#19271E; margin-bottom:0;">
                <li>Harvesting must commence as soon as <b>one or two berries per spike turn yellow to orange-red</b>.</li>
                <li>Waiting for all berries on a spike to turn red leads to berry drop, bird damage, and loss of piperine.</li>
                <li>Spikes harvested at this stage produce the heaviest dry black pepper berries with superior bulk density (500–600 g/L).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with rule_col2:
        st.markdown("""
        <div style="background:#FFFFFF; border:1px solid #E2E8E3; border-radius:14px; padding:22px; height:100%; box-shadow:0 2px 6px rgba(15,62,38,0.04);">
            <h4 style="color:#0F3E26; margin-top:0; font-weight:800;">♨️ Hot Water Blanching Treatment</h4>
            <p style="font-size:0.92rem; color:#4A5B50; line-height:1.6;">
                For premium jet-black color, microbial disinfection, and rapid solar drying:
            </p>
            <ul style="font-size:0.9rem; color:#19271E; margin-bottom:0;">
                <li>Dip harvested green berries in boiling water (<b>80°C – 90°C</b>) for <b>1 minute</b> before spreading for sun drying.</li>
                <li>This activates polyphenol oxidase enzymes, killing surface mold spores and shortening sun-drying time from 8 days to 4–5 days.</li>
                <li>Resulting pepper berries have a glossy dark black skin and command high market valuations.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Final-Year Engineering Project Documentation Banner
    st.info(
        "💡 **Final-Year Engineering Project Documentation:** "
        "Review model performance, TRT fp16 architecture, and research scope on the dedicated **ℹ️ About Project** page."
    )
    if st.button("Open Full Project Documentation & Technical Architecture ➔", key="btn_about_open"):
        st.session_state["nav_selection"] = "About Project"
        st.rerun()
