"""
Gemini AI Farming Assistant Page for Pepper Harvest AI
Powered by Google Gemini (gemini-2.5-flash / gemini-flash-lite) providing dedicated agronomic counsel for black pepper farming.
Features:
- Real-time conversational advisory strictly aligned with ICAR-IISR scientific standards
- Latest Scan Context Advisor (Vision-to-Language bridge with Roboflow detection results)
- Categorized agronomic question explorer (Core, Cultivation, Protection, Post-Harvest)
- Chat transcript export and conversation management
"""

import os
import json
from datetime import datetime
import streamlit as st

from modules.gemini_assistant import GeminiAssistant, SUGGESTED_QUESTIONS
from modules.history_manager import get_all_history


# Additional categorized agronomic suggestion prompts
EXTENDED_QUESTIONS = {
    "🌿 Cultivation & Nutrition": [
        "What is the recommended NPK fertilizer schedule for adult yielding vines?",
        "Which live support trees are best and how should canopy lopping be scheduled?",
        "How should drip irrigation and organic mulching be managed during summer dry spells?",
    ],
    "🛡️ Pest & Disease Care": [
        "How do I identify and treat Quick Wilt (Phytophthora foot rot) with Trichoderma?",
        "How can I control Pollu beetles and berry borers biologically without heavy chemicals?",
        "What are the diagnostic symptoms and remedies for zinc and magnesium deficiency?",
    ],
    "🌶️ Harvest & Post-Harvest": [
        "How do I recognize the exact 1-2 red berry maturity stage on pepper spikes?",
        "What is the scientific 60-second hot water blanching protocol at 80-90°C?",
        "How do I achieve the mandatory 10-11% export moisture content and prevent aflatoxin?",
    ],
}


def render_assistant_page():
    # 1. Header Banner
    st.markdown("""
        <div style="margin-bottom: 22px;">
            <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px; flex-wrap:wrap;">
                <span class="badge-pill badge-pill-green">Interactive Agronomist</span>
                <span class="badge-pill" style="background:#EBF3EF; color:#185A37; border:1px solid #C2DFCE;">ICAR-IISR Aligned</span>
                <span class="badge-pill" style="background:#FFF8E7; color:#B7791F; border:1px solid #F6E05E;">24/7 Crop Doctor</span>
            </div>
            <h1 style="color: #0F3E26; margin-top: 4px; margin-bottom: 6px; font-weight: 800;">
                Pepper Farming Assistant (Gemini AI)
            </h1>
            <p style="color: #4A5B50; font-size: 1.04rem; line-height: 1.6; max-width: 950px; margin-bottom: 0;">
                Your dedicated agricultural AI advisor powered by Google Gemini. Ask any question regarding black pepper 
                (<i>Piper nigrum</i> L.) cultivation, vine training, <i>Phytophthora</i> foot rot prevention, bio-fertilizers, 
                harvest readiness indicators, or post-harvest blanching and drying protocols.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # 2. Check Gemini API Configuration
    api_key = st.session_state.get("runtime_gemini_key") or os.getenv("GEMINI_API_KEY", "").strip()
    assistant = GeminiAssistant(api_key=api_key)
    is_conf, conf_msg = assistant.is_configured()

    # System Status Indicator Bar
    status_col1, status_col2 = st.columns([1.2, 0.8])
    with status_col1:
        if is_conf:
            st.markdown(f"""
                <div style="background:#F4FAF6; border:1px solid #D1EAD9; border-radius:10px; padding:10px 16px; margin-bottom:18px; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap;">
                    <div style="display:flex; align-items:center; gap:8px;">
                        <span class="status-dot-pulse"></span>
                        <span style="font-weight:750; color:#0F3E26; font-size:0.9rem;">Gemini AI Assistant Online</span>
                    </div>
                    <span style="font-size:0.8rem; color:#4A5B50; background:#E2EFE7; padding:2px 8px; border-radius:6px; font-family:monospace;">
                        model: {assistant.model_name}
                    </span>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div style="background:#FFF9E6; border:1px solid #F9E2A0; border-radius:10px; padding:10px 16px; margin-bottom:18px; display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap;">
                    <span style="font-weight:750; color:#975A16; font-size:0.9rem;">⚠️ Gemini API Key Required</span>
                    <span style="font-size:0.8rem; color:#7B6A45;">Enter key below to activate</span>
                </div>
            """, unsafe_allow_html=True)

    with status_col2:
        with st.expander("⚙️ Gemini API Key Settings", expanded=not is_conf):
            entered_key = st.text_input(
                "Gemini API Key:",
                type="password",
                value=api_key if is_conf else "",
                placeholder="AIzaSy...",
                key="gemini_key_input",
                help="Obtain a free API key at https://aistudio.google.com/",
            )
            if st.button("Save API Key for Session", key="save_gem_key_btn", use_container_width=True):
                if entered_key.strip():
                    st.session_state["runtime_gemini_key"] = entered_key.strip()
                    st.success("API key updated successfully!")
                    st.rerun()
                else:
                    st.error("Please enter a valid Gemini API key.")

    # 3. Vision-to-Language Bridge: Latest Scan Context Advisor
    history_records = get_all_history()
    prompt_from_scan = None

    if history_records:
        latest = history_records[0]
        st.markdown(f"""
            <div style="background:#FFFFFF; border:1px solid #D5E8DC; border-left:4.5px solid #2E8B57; border-radius:12px; padding:16px 20px; margin-bottom:20px; box-shadow:0 3px 10px rgba(15,62,38,0.04);">
                <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; margin-bottom:6px;">
                    <div style="display:flex; align-items:center; gap:8px;">
                        <span style="font-size:1.1rem;">📊</span>
                        <span style="font-weight:800; color:#0F3E26; font-size:0.95rem;">Latest Harvest Scan Context: <code>{latest['filename']}</code></span>
                    </div>
                    <span class="badge-pill badge-pill-green">{latest['status']}</span>
                </div>
                <p style="font-size:0.88rem; color:#4A5B50; margin-bottom:10px;">
                    Scan Metrics: <b>{latest['maturity_pct']:.1f}% Mature</b> • 
                    <b>{latest['matured_count']}</b> mature spikes • 
                    <b>{latest['immatured_count']}</b> immature spikes • 
                    Scanned on {latest['timestamp']}
                </p>
                <div style="font-size:0.84rem; font-weight:700; color:#185A37; margin-bottom:6px;">
                    ⚡ Ask Gemini to analyze this scan:
                </div>
            </div>
        """, unsafe_allow_html=True)

        sc_cols = st.columns(3)
        with sc_cols[0]:
            if st.button(
                "🎯 Interpret Harvest Readiness",
                key="btn_scan_interpret",
                use_container_width=True,
                help="Ask Gemini for an agronomic interpretation of this scan's maturity percentage.",
            ):
                prompt_from_scan = (
                    f"Based on my recent harvest scan of '{latest['filename']}': "
                    f"The AI model detected {latest['matured_count']} matured spikes and {latest['immatured_count']} immatured spikes "
                    f"({latest['maturity_pct']:.1f}% maturity rate), classified as '{latest['status']}'. "
                    f"What specific agronomic interpretation and harvest actions do you recommend for this plot?"
                )

        with sc_cols[1]:
            if st.button(
                "🌶️ Step-by-Step Blanching & Curing Plan",
                key="btn_scan_blanch",
                use_container_width=True,
                help="Ask Gemini for post-harvest blanching instructions for this batch.",
            ):
                prompt_from_scan = (
                    f"I have harvested a batch of black pepper evaluated at {latest['maturity_pct']:.1f}% maturity rate "
                    f"('{latest['status']}'). Please provide a step-by-step hot water blanching protocol (temperature, timing, drying) "
                    f"to ensure export-grade jet black color and 10-11% safe moisture storage."
                )

        with sc_cols[2]:
            if st.button(
                "🛡️ Caring for Remaining Immature Crop",
                key="btn_scan_immature",
                use_container_width=True,
                help="Ask Gemini how to nourish vines with immature spikes for the next flush.",
            ):
                prompt_from_scan = (
                    f"In my pepper plantation, {latest['immatured_count']} spikes ({100 - latest['maturity_pct']:.1f}%) "
                    f"are currently immature and green. How should I manage irrigation, shade, and nutrition to support their "
                    f"development for the subsequent picking round in 2 weeks?"
                )

        st.markdown("<div style='margin-bottom: 12px;'></div>", unsafe_allow_html=True)

    # 4. Categorized Suggested Farming Questions
    st.markdown("##### 💡 Suggested Farming Questions:")
    cat_tab1, cat_tab2, cat_tab3, cat_tab4 = st.tabs([
        "⭐ Core Questions",
        "🌿 Cultivation & Soils",
        "🛡️ Pest & Disease Care",
        "🌶️ Harvest & Post-Harvest",
    ])

    clicked_suggestion = None

    with cat_tab1:
        pill_cols = st.columns(3)
        for idx, q_text in enumerate(SUGGESTED_QUESTIONS):
            col_target = pill_cols[idx % 3]
            with col_target:
                if st.button(q_text, key=f"sugg_core_{idx}", use_container_width=True):
                    clicked_suggestion = q_text

    with cat_tab2:
        for idx, q_text in enumerate(EXTENDED_QUESTIONS["🌿 Cultivation & Nutrition"]):
            if st.button(f"🌿 {q_text}", key=f"sugg_cult_{idx}", use_container_width=True):
                clicked_suggestion = q_text

    with cat_tab3:
        for idx, q_text in enumerate(EXTENDED_QUESTIONS["🛡️ Pest & Disease Care"]):
            if st.button(f"🛡️ {q_text}", key=f"sugg_pest_{idx}", use_container_width=True):
                clicked_suggestion = q_text

    with cat_tab4:
        for idx, q_text in enumerate(EXTENDED_QUESTIONS["🌶️ Harvest & Post-Harvest"]):
            if st.button(f"🌶️ {q_text}", key=f"sugg_post_{idx}", use_container_width=True):
                clicked_suggestion = q_text

    st.markdown("---")

    # 5. Initialize Chat History in Session State
    if "chat_messages" not in st.session_state:
        st.session_state["chat_messages"] = [
            {
                "role": "assistant",
                "content": (
                    "Hello! I am your **Pepper Farming Assistant**, specialized in black pepper (*Piper nigrum* L.) cultivation, "
                    "support tree lopping, *Phytophthora* foot rot diagnostics, harvest maturity indicators, and post-harvest blanching standards. "
                    "How can I assist your pepper plantation or research today?"
                ),
            }
        ]

    # 6. Render Chat Message History
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state["chat_messages"]:
            if msg["role"] == "user":
                with st.chat_message("user", avatar="🧑‍🌾"):
                    st.write(msg["content"])
            else:
                with st.chat_message("assistant", avatar="🌿"):
                    st.markdown(msg["content"])

    # 7. Chat Input Field
    user_input = st.chat_input("Ask a question about black pepper cultivation, pests, irrigation, or harvesting...")

    # Determine Active Prompt
    active_prompt = user_input or clicked_suggestion or prompt_from_scan

    # 8. Process Message
    if active_prompt:
        if not is_conf and not st.session_state.get("runtime_gemini_key"):
            st.error("Please configure your Gemini API Key in the settings box above before asking questions.")
        else:
            # Add user message to conversation
            st.session_state["chat_messages"].append({"role": "user", "content": active_prompt})

            # Call Gemini API with agricultural context
            with st.chat_message("assistant", avatar="🌿"):
                with st.spinner("Consulting ICAR-IISR black pepper agronomic knowledge base..."):
                    context_history = [
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state["chat_messages"][-8:]
                    ]
                    success, response_text = assistant.generate_response(active_prompt, history=context_history)

                    if success:
                        st.session_state["chat_messages"].append({"role": "assistant", "content": response_text})
                    else:
                        st.error(f"Gemini API Error: {response_text}")
            st.rerun()

    # 9. Conversation Utility Toolbar (Export & Clear)
    st.markdown("<br/>", unsafe_allow_html=True)
    util_cols = st.columns([1.5, 1.5, 1.0])

    with util_cols[0]:
        # Generate formatted transcript text for download
        transcript_lines = [
            "=" * 60,
            "BLACK PEPPER HARVEST READINESS AI - GEMINI AGRONOMIC CONSULTATION",
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "=" * 60,
            "",
        ]
        for m in st.session_state["chat_messages"]:
            speaker = "FARMER / USER" if m["role"] == "user" else "PEPPER FARMING ASSISTANT (GEMINI AI)"
            transcript_lines.append(f"[{speaker}]:")
            transcript_lines.append(m["content"])
            transcript_lines.append("-" * 40)

        transcript_data = "\n".join(transcript_lines)
        st.download_button(
            label="📥 Download Consultation Transcript (.txt)",
            data=transcript_data,
            file_name=f"pepper_agronomy_consultation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain",
            use_container_width=True,
        )

    with util_cols[2]:
        if st.button("🗑️ Clear Chat", use_container_width=True, help="Reset the chat session"):
            st.session_state["chat_messages"] = [
                {
                    "role": "assistant",
                    "content": "Conversation cleared. How can I assist with your black pepper crop today?",
                }
            ]
            st.rerun()
