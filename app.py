"""
Pepper Harvest AI - Black Pepper Harvest Readiness AI Web Application
Main application entry point and streamlined sidebar navigation controller.
"""

import os
import streamlit as st
import dotenv

# Load environment configuration
dotenv.load_dotenv(override=True)

# Streamlit Page Configuration
st.set_page_config(
    page_title="Pepper Harvest AI | Black Pepper Harvest Readiness",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load Custom CSS
css_path = os.path.join(os.path.dirname(__file__), "assets", "styles", "main.css")
if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Import Consolidated Page Modules
from pages_custom.home_page import render_home_page
from pages_custom.detect_page import render_detect_page
from pages_custom.history_page import render_history_page
from pages_custom.guide_page import render_guide_page
from pages_custom.assistant_page import render_assistant_page
from pages_custom.about_page import render_about_page
from modules.roboflow_service import RoboflowService
from modules.gemini_assistant import GeminiAssistant
from modules.history_manager import init_db

# Initialize database on startup
init_db()

# Streamlined Standard Navigation Pages Mapping
PAGES = {
    "🏠 Home Dashboard": "Home",
    "🔍 Harvest Detection (Image & Video)": "Detect Maturity",
    "📖 Cultivation & Growing Guide": "Cultivation & Growing Guide",
    "🤖 Gemini AI Farming Assistant": "Gemini AI Assistant",
    "📜 Scan History & Reports": "Analysis History",
    "ℹ️ About Project": "About Project",
}

# Sidebar Navigation
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 12px 0 18px 0;">
            <div style="display:inline-flex; align-items:center; justify-content:center; background:linear-gradient(135deg, #E8F4EE 0%, #D0E9DA 100%); width:56px; height:56px; border-radius:16px; font-size:28px; border: 1.5px solid #2E8B57; box-shadow: 0 4px 12px rgba(46, 139, 87, 0.15);">
                🌿
            </div>
            <h2 style="color: #0F3E26; margin-top: 10px; margin-bottom: 2px; font-size: 1.35rem; font-weight: 800; letter-spacing: -0.02em;">Pepper Harvest AI</h2>
            <div style="display:inline-block; background:#EAF5EE; color:#185A37; font-size:0.75rem; font-weight:700; padding:2px 10px; border-radius:12px; margin-top:2px; border:1px solid #C4E2D0;">
                Black Pepper Harvest Readiness
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Handle navigation selection with session state sync
    page_options = list(PAGES.keys())
    page_values = list(PAGES.values())

    default_index = 0
    if "nav_selection" in st.session_state and st.session_state["nav_selection"] in page_values:
        default_index = page_values.index(st.session_state["nav_selection"])

    nav_label = st.radio(
        "Navigation Menu",
        options=page_options,
        index=default_index,
        label_visibility="collapsed",
    )
    current_page = PAGES[nav_label]
    st.session_state["nav_selection"] = current_page

    st.markdown("---")

    # Real-Time Service Status Indicators
    st.markdown("<p style='font-size:0.78rem; font-weight:750; color:#718478; text-transform:uppercase; letter-spacing:0.7px; margin-bottom:10px;'>🔌 AI System Status</p>", unsafe_allow_html=True)

    # Roboflow Status
    rf = RoboflowService()
    rf_ok, _ = rf.is_configured()
    if rf_ok:
        st.markdown(f"""
            <div style="background:#F6FAF7; border:1px solid #D5E8DC; border-radius:10px; padding:10px 12px; margin-bottom:8px;">
                <div style="font-weight:700; font-size:0.86rem; color:#0F3E26;">
                    <span class="status-dot-pulse"></span>YOLO26 Nano Online
                </div>
                <div style="font-size:0.76rem; color:#5D6D7E; margin-top:2px;">
                    Workspace: <code>{rf.workspace}</code> | v{rf.version}
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style="background:#FDF5F5; border:1px solid #F5C6CB; border-radius:10px; padding:10px 12px; margin-bottom:8px;">
                <div style="font-weight:700; font-size:0.86rem; color:#C0392B;">
                    🔴 Roboflow Disconnected
                </div>
                <div style="font-size:0.76rem; color:#7F8C8D; margin-top:2px;">API key required</div>
            </div>
        """, unsafe_allow_html=True)

    # Gemini Status
    gem_key = st.session_state.get("runtime_gemini_key") or os.getenv("GEMINI_API_KEY", "").strip()
    gem = GeminiAssistant(api_key=gem_key)
    gem_ok, _ = gem.is_configured()
    if gem_ok:
        st.markdown(f"""
            <div style="background:#F6FAF7; border:1px solid #D5E8DC; border-radius:10px; padding:10px 12px; margin-bottom:8px;">
                <div style="font-weight:700; font-size:0.86rem; color:#0F3E26;">
                    <span class="status-dot-pulse"></span>Gemini Assistant Active
                </div>
                <div style="font-size:0.76rem; color:#5D6D7E; margin-top:2px;">
                    Model: <code>{gem.model_name}</code>
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style="background:#FEFBF0; border:1px solid #F9E79F; border-radius:10px; padding:10px 12px; margin-bottom:8px;">
                <div style="font-weight:700; font-size:0.86rem; color:#B7950B;">
                    🟡 Gemini Key Pending
                </div>
                <div style="font-size:0.76rem; color:#7F8C8D; margin-top:2px;">Activate in assistant tab</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
        <div style="font-size:0.74rem; color:#8C9B92; text-align:center; line-height:1.4;">
            <b>Final-Year Engineering Project</b><br/>
            Black Pepper Harvest Readiness AI<br/>
            <span style="display:inline-block; background:#EAF2ED; color:#2E8B57; padding:2px 8px; border-radius:10px; font-weight:700; margin-top:4px;">v2.0 Pro Edition</span>
        </div>
    """, unsafe_allow_html=True)


# Route to the selected standard page
if current_page == "Home":
    render_home_page()
elif current_page == "Detect Maturity":
    render_detect_page()
elif current_page == "Analysis History":
    render_history_page()
elif current_page == "Cultivation & Growing Guide":
    render_guide_page()
elif current_page == "Gemini AI Assistant":
    render_assistant_page()
elif current_page == "About Project":
    render_about_page()
