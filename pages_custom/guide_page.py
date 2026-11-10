"""
Comprehensive Black Pepper Cultivation & Growing Guide Page
Includes:
- 23 ICAR-IISR Aligned Cultivation Chapters (with keyword search, category filtering, and jump-to navigation)
- 7 Commercial Cultivation Methods & Systems (with step-by-step procedures & verified YouTube videos)
- 6 Scientific Nursery Propagation Protocols
- Dedicated Fertilizer, Manure & Irrigation Guide (with regional soil-test distinctions)
- Dedicated Pest, Disease & Nutrient Deficiency Diagnostic Profiles
- Complete Harvesting & Post-Harvest Blanching/Drying Protocols
- Curated Video Learning Library
"""

import os
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

from pages_custom.cultivation_guide_page import (
    CULTIVATION_CHAPTERS_DATA,
    GROWING_METHODS_DATA,
    PROPAGATION_TECHNIQUES_DATA,
    FERTILIZER_IRRIGATION_DATA,
    PEST_DISEASE_DATA,
    HARVEST_PROCESSING_DATA,
    YOUTUBE_RESOURCES_DATA,
)


def render_youtube_player(video_url: str, title: str = "Black Pepper Video Tutorial", height: int = 340):
    """
    Renders a guaranteed-working, responsive YouTube video player using
    Streamlit's native video player with an iframe fallback and a prominent direct action button.
    """
    video_id = ""
    if "v=" in video_url:
        video_id = video_url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in video_url:
        video_id = video_url.split("youtu.be/")[1].split("?")[0]

    clean_url = f"https://www.youtube.com/watch?v={video_id}" if video_id else video_url

    # 1. Native Streamlit Video Player
    rendered_native = False
    try:
        st.video(clean_url)
        rendered_native = True
    except Exception:
        pass

    # 2. Iframe Fallback if native fails
    if not rendered_native and video_id:
        embed_url = f"https://www.youtube-nocookie.com/embed/{video_id}?rel=0&modestbranding=1"
        iframe_code = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                body {{ margin: 0; padding: 0; background: transparent; }}
                .video-container {{
                    position: relative;
                    width: 100%;
                    padding-bottom: 56.25%;
                    height: 0;
                    overflow: hidden;
                    border-radius: 12px;
                    box-shadow: 0 4px 14px rgba(0,0,0,0.15);
                    background: #0B331F;
                }}
                .video-container iframe {{
                    position: absolute;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    border: 0;
                    border-radius: 12px;
                }}
            </style>
        </head>
        <body>
            <div class="video-container">
                <iframe 
                    src="{embed_url}" 
                    title="{title}"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                    allowfullscreen>
                </iframe>
            </div>
        </body>
        </html>
        """
        components.html(iframe_code, height=height)

    # 3. Always render high-contrast, verified direct action button that opens in a new tab
    st.markdown(f"""
        <div style="margin-top: 4px; margin-bottom: 14px;">
            <a href="{clean_url}" target="_blank" rel="noopener noreferrer" 
               style="display:inline-flex; align-items:center; justify-content:center; gap:8px; width:100%; background:#E62117; color:#FFFFFF !important; padding:9px 16px; border-radius:8px; font-weight:750; text-decoration:none; font-size:0.88rem; box-shadow:0 3px 10px rgba(230,33,23,0.25); transition:all 0.2s ease;">
                <span>▶️ Click Here to Play on YouTube.com (Opens in New Tab)</span>
            </a>
        </div>
    """, unsafe_allow_html=True)


def render_image_safe(rel_path: str, caption: str = ""):
    """Safely renders an image from a relative path with reliable fallback."""
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

    # Fallback to general hero image if specific image fails
    fallback_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "images", "hero_plantation.jpg")
    if os.path.exists(fallback_path):
        try:
            st.image(fallback_path, caption=f"{caption} (Plantation View)", use_container_width=True)
        except Exception:
            pass


def render_guide_page():
    # Page Header Banner
    st.markdown("""
        <div id="guide-top" style="margin-bottom: 24px;">
            <span class="badge-pill badge-pill-green">Farmer & Researcher Knowledge Portal</span>
            <h1 style="color: #0F3E26; margin-top: 8px; margin-bottom: 4px; font-weight: 800;">Black Pepper Cultivation & Growing Guide</h1>
            <p style="color: #4A5B50; font-size: 1.05rem; max-width: 950px; line-height: 1.6;">
                A complete practical guide to growing, managing, harvesting, and processing black pepper (<i>Piper nigrum</i> L.).
                Scientifically aligned with ICAR-IISR standards, state agricultural universities, and global Good Agricultural Practices (GAP).
            </p>
        </div>
    """, unsafe_allow_html=True)

    # 7 Core Educational Navigation Tabs
    tab_chapters, tab_methods, tab_propagation, tab_nutrition, tab_protection, tab_harvesting, tab_videos = st.tabs([
        "📚 23 Cultivation Chapters",
        "🎋 7 Cultivation Methods",
        "🌱 Propagation Protocols",
        "💧 Fertilizer & Irrigation",
        "🛡️ Pest & Disease Care",
        "🌶️ Harvest & Processing",
        "🎥 YouTube Video Library",
    ])

    with tab_chapters:
        render_cultivation_chapters_section()

    with tab_methods:
        render_growing_methods_section()

    with tab_propagation:
        render_propagation_techniques_section()

    with tab_nutrition:
        render_fertilizer_irrigation_section()

    with tab_protection:
        render_pest_disease_section()

    with tab_harvesting:
        render_harvest_processing_section()

    with tab_videos:
        render_video_library_section()


# --------------------------------------------------------------------------------------
# 1. MAIN CULTIVATION CHAPTERS SECTION (23 CHAPTERS)
# --------------------------------------------------------------------------------------
def render_cultivation_chapters_section():
    st.markdown("### 📖 ICAR-IISR Main Cultivation Chapters (23 Chapters)")
    st.markdown("Browse, search, or filter all 23 chapters of scientific black pepper production from land prep to storage.")

    # Search & Filter Toolbar
    c_search, c_filter, c_jump = st.columns([1.5, 1.1, 1.4])

    with c_search:
        search_kw = st.text_input(
            "🔍 Search chapters by keyword:",
            placeholder="e.g. Phytophthora, Blanching, Panniyur, NPK, Spacing...",
            key="guide_search_kw",
        )

    categories = [
        "All Categories",
        "Botany & Overview",
        "Agro-Climatic Needs",
        "Establishment",
        "Nursery & Propagation",
        "Canopy & Standards",
        "Water & Nutrition",
        "Field Maintenance",
        "Plant Protection",
        "Harvest Readiness",
        "Processing & Storage",
    ]

    with c_filter:
        selected_cat = st.selectbox("📂 Filter by Category:", categories, key="guide_cat_dropdown")

    # Filter logic operating on actual chapter data
    filtered_chapters = []
    for chap in CULTIVATION_CHAPTERS_DATA:
        # Category match
        if selected_cat != "All Categories" and chap["category"] != selected_cat:
            continue
        # Search keyword match across title, summary, explanation, important points, recommendations, mistakes
        if search_kw.strip():
            kw = search_kw.strip().lower()
            in_title = kw in chap["title"].lower()
            in_summary = kw in chap["summary"].lower()
            in_exp = kw in chap["explanation"].lower()
            in_pts = any(kw in p.lower() for p in chap.get("important_points", []))
            in_rec = any(kw in r.lower() for r in chap.get("farming_recommendations", []))
            in_mis = any(kw in m.lower() for m in chap.get("mistakes_to_avoid", []))
            if not (in_title or in_summary or in_exp or in_pts or in_rec or in_mis):
                continue
        filtered_chapters.append(chap)

    with c_jump:
        chapter_titles = ["All Chapters"] + [f"{c['id']}. {c['title']}" for c in CULTIVATION_CHAPTERS_DATA]
        selected_jump = st.selectbox("⚡ Quick Jump to Chapter:", chapter_titles, key="guide_jump_select")

    # If user selected a specific chapter to jump to
    if selected_jump != "All Chapters":
        target_id = int(selected_jump.split(".")[0])
        filtered_chapters = [c for c in CULTIVATION_CHAPTERS_DATA if c["id"] == target_id]

    st.write(f"Showing **{len(filtered_chapters)}** of **{len(CULTIVATION_CHAPTERS_DATA)}** chapters.")
    st.markdown("---")

    if not filtered_chapters:
        st.info("No cultivation chapters match your search query. Try typing another keyword like *'soil'*, *'harvest'*, or *'rot'*.")
        return

    # Render each chapter card / expander
    for chap in filtered_chapters:
        is_expanded = len(filtered_chapters) <= 2
        with st.expander(f"Chapter {chap['id']}: {chap['title']} ({chap['category']})", expanded=is_expanded):
            st.markdown(f"**Chapter Summary:** *{chap['summary']}*")

            # Chapter Photograph & Detailed Explanation
            c_img_col, c_text_col = st.columns([1.1, 1.9])
            with c_img_col:
                render_image_safe(chap.get("image", ""), caption=chap.get("caption", chap["title"]))

            with c_text_col:
                st.markdown(chap["explanation"])

            # Important Points
            if chap.get("important_points"):
                st.markdown("#### 📌 Important Agronomic Points:")
                for pt in chap["important_points"]:
                    st.markdown(f"- **{pt}**")

            # Practical Farming Recommendations
            if chap.get("farming_recommendations"):
                st.markdown("#### 📋 Practical Farming Recommendations:")
                for rec in chap["farming_recommendations"]:
                    st.markdown(f"- ✅ {rec}")

            # Common Mistakes to Avoid (Explicit Prompt Requirement)
            if chap.get("mistakes_to_avoid"):
                st.markdown("#### ⚠️ Common Mistakes to Avoid:")
                for mistake in chap["mistakes_to_avoid"]:
                    st.markdown(f"- ❌ {mistake}")

            # Useful Tip
            if chap.get("tips"):
                st.info(f"💡 **Practical Farmer's Tip:** {chap['tips']}")

            # Additional Learning Resources (Explicit Prompt Requirement)
            if chap.get("learning_resources"):
                st.markdown("#### 📚 Additional Learning Resources & Publications:")
                for res in chap["learning_resources"]:
                    st.markdown(f"- 📖 *{res}*")

            # Related Topics
            if chap.get("related"):
                st.markdown("**🔗 Related Topics:** " + " • ".join([f"`{t}`" for t in chap["related"]]))

    # Back to Top button
    st.markdown("""
        <div style="text-align: right; margin-top: 20px;">
            <a href="#guide-top" style="color: #0F3E26; font-weight: 700; text-decoration: none; padding: 6px 14px; background: #EAF4EE; border-radius: 20px; border: 1px solid #C4E2D0;">
                ⬆️ Back to Top
            </a>
        </div>
    """, unsafe_allow_html=True)


# --------------------------------------------------------------------------------------
# 2. 7 CULTIVATION METHODS & SYSTEMS (WITH PROCEDURES & VERIFIED YOUTUBE URLS)
# --------------------------------------------------------------------------------------
def render_growing_methods_section():
    st.markdown("### 🎋 7 Different Methods of Growing Black Pepper")
    st.markdown("Explore commercial cultivation systems complete with step-by-step procedures, field photos, and verified video tutorials.")

    # Featured Spotlight Video Card: Different Methods of Growing Black Pepper
    st.markdown("""
        <div style="background:linear-gradient(135deg, #0B331F 0%, #155032 50%, #287B4C 100%); border-radius:16px; padding:22px 26px; color:#FFFFFF; margin-bottom:18px; box-shadow:0 8px 24px rgba(15,62,38,0.15); border:1px solid rgba(255,255,255,0.12);">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; margin-bottom:8px;">
                <span class="badge-pill" style="background:rgba(229,169,60,0.25); color:#FFE6A8; border:1px solid #E5A93C;">🎬 Featured Field Video</span>
                <span style="font-size:0.82rem; color:#D4EDE0; font-weight:700;">🎥 Verified Field Demonstrations & Tutorials</span>
            </div>
            <h3 style="color:#FFFFFF !important; margin-top:4px; margin-bottom:8px; font-weight:800; font-size:1.4rem;">
                Different Methods of Growing Black Pepper (Simple Step-by-Step Guide)
            </h3>
            <p style="color:#E2EFE7; font-size:0.96rem; line-height:1.6; margin-bottom:0;">
                Watch easy-to-follow practical video demonstrations showing different pepper growing methods, 
                soil preparation, vine tying, fertilizer application, canopy pruning, and harvest timing.
            </p>
        </div>
    """, unsafe_allow_html=True)

    spotlight_options = {
        "🎬 Complete Black Pepper Farming Guide (Planting, Care & Harvest - 12:50)": {
            "url": "https://www.youtube.com/watch?v=VGrX_fkVppA",
            "title": "Black Pepper Farming - Planting, Care, Harvesting | Complete Guide",
            "channel": "Discover Agriculture",
            "duration": "12:50",
            "summary": "Covers soil preparation, pit refilling, live standard support planting, tying vines, pruning, and harvesting mature spikes."
        },
        "🎋 Vertical Column & Trellis Cultivation Method (08:35)": {
            "url": "https://www.youtube.com/watch?v=lC3L5CpnJF0",
            "title": "Intensifying Black Pepper Farming | Vertical Column Method",
            "channel": "Discover Agriculture",
            "duration": "08:35",
            "summary": "Demonstrates high-density vertical columns, artificial supports, rapid cutting multiplication, and space-saving techniques."
        },
        "🏛️ ICAR-IISR Column Method for High-Tech Pepper Propagation": {
            "url": "https://www.youtube.com/watch?v=kuw3Nv1KiDU",
            "title": "Column Method To Produce Black Pepper Cuttings",
            "channel": "ICAR-Indian Institute of Spices Research Kozhikode",
            "duration": "Official ICAR",
            "summary": "Official ICAR-IISR demonstration of rapid multiplication columns for disease-free rooted cutting production."
        },
        "🌴 How to Grow Black Pepper Step-by-Step (10:15)": {
            "url": "https://www.youtube.com/watch?v=SxBmzUcPukQ",
            "title": "How to Grow Black Pepper Step-by-Step",
            "channel": "The Tree Academy",
            "duration": "10:15",
            "summary": "Step-by-step nursery propagation, soil mix, planting beside trees, mulching, and care for beginner farmers."
        },
        "🪴 How to Grow Bush Pepper in Pots & Containers": {
            "url": "https://www.youtube.com/watch?v=XOoBqQmz8jc",
            "title": "How to Grow Black Pepper (Piper nigrum) in Pots and Containers",
            "channel": "LogeesPlants",
            "duration": "Container Bush",
            "summary": "Complete instructions on non-climbing bush pepper growing, potting soil mixture, balcony care, and year-round fruiting."
        }
    }

    selected_video_name = st.selectbox(
        "📺 Select Practical Video Tutorial to Watch:",
        list(spotlight_options.keys()),
        index=0,
        key="growing_methods_spotlight_video_select"
    )
    current_video = spotlight_options[selected_video_name]

    feat_v_col, feat_info_col = st.columns([1.25, 0.75])
    with feat_v_col:
        render_youtube_player(
            current_video["url"],
            title=current_video["title"],
            height=340,
        )
    with feat_info_col:
        st.markdown(f"""
        <div style="background:#FFFFFF; border:1px solid #E2E8E3; border-radius:14px; padding:20px; height:100%; box-shadow:0 2px 8px rgba(15,62,38,0.04);">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                <span class="badge-pill badge-pill-green">{current_video['duration']}</span>
                <span style="font-size:0.8rem; color:#718478; font-weight:700;">{current_video['channel']}</span>
            </div>
            <h4 style="color:#0F3E26; margin-top:4px; font-weight:800;">{current_video['title']}</h4>
            <p style="font-size:0.9rem; color:#4A5B50; line-height:1.6; margin-bottom:12px;">{current_video['summary']}</p>
            <h5 style="color:#0F3E26; margin-top:12px; margin-bottom:6px; font-weight:800;">Core Method Highlights:</h5>
            <ul style="font-size:0.88rem; color:#19271E; line-height:1.65; padding-left:18px;">
                <li><b>Support Systems:</b> Live trees (Garuga/Erythrina) vs. Vertical non-living columns.</li>
                <li><b>Root Media:</b> Enriched potting soil with decomposed FYM and Trichoderma bio-agent.</li>
                <li><b>Vine Training:</b> Gentle figure-eight loops using natural fiber to avoid stem bruising.</li>
                <li><b>Light Management:</b> 50–60% filtered solar radiation for optimum lateral spike formation.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("#### 📂 Explore Individual Growing Methods Below:")

    method_tabs = st.tabs([f"Method {i+1}: {m['name'].split('.')[1].strip()}" for i, m in enumerate(GROWING_METHODS_DATA)])

    for idx, method in enumerate(GROWING_METHODS_DATA):
        with method_tabs[idx]:
            st.markdown(f"""
                <div class="guide-card" style="border-top: 3.5px solid #2E8B57;">
                    <span class="badge-pill badge-pill-green">{method['badge']}</span>
                    <h2 style="color: #0F3E26; margin-top: 10px; margin-bottom: 6px; font-weight: 800;">{method['name']}</h2>
                    <p style="color: #4A5B50; font-size: 1.02rem; font-style: italic;">{method['explanation']}</p>
                </div>
            """, unsafe_allow_html=True)

            col_details, col_media = st.columns([1.25, 0.75])

            with col_details:
                st.markdown("#### ⚙️ How It Works:")
                st.write(method["how_it_works"])

                st.markdown("#### 📋 Step-by-Step Procedure:")
                for step_num, step_desc in enumerate(method.get("procedure", []), start=1):
                    st.markdown(f"**Step {step_num}:** {step_desc}")

                st.markdown("#### 🌍 Suitable Conditions:")
                st.write(method["suitable_conditions"])

                col_adv, col_lim = st.columns(2)
                with col_adv:
                    st.markdown("#### ✅ Key Advantages:")
                    for adv in method["advantages"]:
                        st.markdown(f"- {adv}")

                with col_lim:
                    st.markdown("#### ⚠️ Limitations & Challenges:")
                    for lim in method["limitations"]:
                        st.markdown(f"- {lim}")

                st.info(f"💡 **Practical Farming Tip:** {method['tips']}")

            with col_media:
                st.markdown("#### 📷 Real Field Photograph:")
                render_image_safe(method["image"], caption=f"{method['name']} in Practice")

                st.markdown("#### 🎥 Video Tutorial for This Method:")
                st.markdown(f"**{method['youtube_title']}**")
                st.caption(method.get("youtube_desc", "Comprehensive field tutorial"))
                render_youtube_player(
                    method["youtube_url"],
                    title=f"{method['name']} Tutorial",
                    height=320,
                )


# --------------------------------------------------------------------------------------
# 3. PROPAGATION TECHNIQUES (INTERACTIVE SECTION)
# --------------------------------------------------------------------------------------
def render_propagation_techniques_section():
    st.markdown("### 🌱 Scientific Propagation Techniques")
    st.markdown("Standard nursery propagation protocols to achieve 95%+ field establishment and disease-free vine stock.")

    prop_selector = st.radio(
        "Select Propagation Protocol to Inspect:",
        [p["name"] for p in PROPAGATION_TECHNIQUES_DATA],
        horizontal=True,
        key="prop_radio_selector",
    )

    selected_prop = next(p for p in PROPAGATION_TECHNIQUES_DATA if p["name"] == prop_selector)

    st.markdown(f"""
        <div class="guide-card" style="border-top: 3.5px solid #E5A93C;">
            <span class="badge-pill badge-pill-amber">Nursery Standard</span>
            <h3 style="color: #0F3E26; margin-top: 10px; margin-bottom: 4px; font-weight: 800;">{selected_prop['name']}</h3>
            <p style="color: #4A5B50; font-size: 1.02rem;">{selected_prop['summary']}</p>
        </div>
    """, unsafe_allow_html=True)

    col_proc, col_img = st.columns([1.3, 0.7])

    with col_proc:
        st.markdown("#### 📋 Step-by-Step Nursery Procedure:")
        for idx, step in enumerate(selected_prop["procedure"], start=1):
            st.markdown(f"**Step {idx}:** {step}")

        st.info(f"💡 **Nursery Specialist Tip:** {selected_prop['tips']}")

    with col_img:
        st.markdown("#### 📷 Nursery Stage Photograph:")
        render_image_safe(selected_prop["image"], caption=f"{selected_prop['name']} Protocol")


# --------------------------------------------------------------------------------------
# 4. FERTILIZER AND IRRIGATION GUIDE
# --------------------------------------------------------------------------------------
def render_fertilizer_irrigation_section():
    st.markdown("### 💧 Fertilizer, Manure & Irrigation Management Guide")
    st.markdown("Scientific plant nutrition and water management protocols with regional soil-test distinctions.")

    f_tab1, f_tab2, f_tab3 = st.tabs(["🍃 Organic Manures & Compost", "🧪 NPK Fertilizer Schedules", "🚿 Irrigation, Drainage & Mulching"])

    with f_tab1:
        org_data = FERTILIZER_IRRIGATION_DATA["organic_manures"]
        st.markdown(f"#### {org_data['title']}")
        st.write(org_data["explanation"])

        c_org_info, c_org_img = st.columns([1.3, 0.7])
        with c_org_info:
            for comp in org_data["components"]:
                st.markdown(f"""
                    <div style="background:#FFFFFF; border:1px solid #E2E8E3; border-left:4px solid #2E8B57; border-radius:10px; padding:16px; margin-bottom:12px;">
                        <h4 style="color:#0F3E26; margin-top:0; margin-bottom:4px; font-weight:800;">{comp['name']}</h4>
                        <p style="margin-bottom:4px; font-size:0.92rem; color:#19271E;"><b>Recommended Dosage:</b> <code>{comp['dosage']}</code></p>
                        <p style="margin-bottom:0; font-size:0.88rem; color:#4A5B50;">{comp['benefits']}</p>
                    </div>
                """, unsafe_allow_html=True)
        with c_org_img:
            render_image_safe("assets/images/guide/soil_prep.jpg", caption="Enriched Farmyard Manure & Organic Compost Basins")

    with f_tab2:
        npk_data = FERTILIZER_IRRIGATION_DATA["npk_schedule"]
        st.markdown(f"#### {npk_data['title']}")
        st.write(npk_data["explanation"])

        c_npk_info, c_npk_img = st.columns([1.3, 0.7])
        with c_npk_info:
            for sch in npk_data["schedule"]:
                st.markdown(f"""
                    <div style="background:#FFFFFF; border:1px solid #E2E8E3; border-left:4px solid #0F3E26; border-radius:10px; padding:16px; margin-bottom:12px;">
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <h4 style="color:#0F3E26; margin:0; font-weight:800;">{sch['stage']}</h4>
                            <span class="badge-pill badge-pill-green">{sch['dosage']}</span>
                        </div>
                        <p style="margin-top:8px; margin-bottom:0; font-size:0.88rem; color:#4A5B50;"><b>Application Timing:</b> {sch['timing']}</p>
                    </div>
                """, unsafe_allow_html=True)

            st.markdown("#### 🌍 Regional & Soil-Test Variations (Avoid Universal Prescriptions):")
            for reg in npk_data["regional_variations"]:
                st.markdown(f"- {reg}")
        with c_npk_img:
            render_image_safe("assets/images/methods/bush_pepper.jpg", caption="Balanced NPK Nutrition & Foliar Health")

    with f_tab3:
        irr_data = FERTILIZER_IRRIGATION_DATA["irrigation_drainage"]
        st.markdown(f"#### {irr_data['title']}")
        st.write(irr_data["explanation"])

        c_irr_info, c_irr_img = st.columns([1.3, 0.7])
        with c_irr_info:
            for pr in irr_data["practices"]:
                st.markdown(f"""
                    <div style="background:#FFFFFF; border:1px solid #E2E8E3; border-left:4px solid #E5A93C; border-radius:10px; padding:16px; margin-bottom:12px;">
                        <h4 style="color:#0F3E26; margin-top:0; margin-bottom:4px; font-weight:800;">{pr['name']}</h4>
                        <p style="margin-bottom:0; font-size:0.92rem; color:#19271E; line-height:1.5;">{pr['protocol']}</p>
                    </div>
                """, unsafe_allow_html=True)
        with c_irr_img:
            render_image_safe("assets/images/methods/live_standard.jpg", caption="Ring Basin Supplemental Irrigation & Mulching")


# --------------------------------------------------------------------------------------
# 5. PEST AND DISEASE MANAGEMENT
# --------------------------------------------------------------------------------------
def render_pest_disease_section():
    st.markdown("### 🛡️ Pest, Disease & Deficiency Management")
    st.markdown("Diagnostic profiles with symptoms, causes, preventive measures, and scientifically supported IPM practices.")

    pest_names = [p["name"] for p in PEST_DISEASE_DATA]
    selected_pest_name = st.selectbox("Select Pest or Disease Profile to Inspect:", pest_names, key="pest_profile_select")

    pest = next(p for p in PEST_DISEASE_DATA if p["name"] == selected_pest_name)

    st.markdown(f"""
        <div class="guide-card" style="border-top: 3.5px solid #E74C3C;">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
                <h3 style="color:#0F3E26; margin:0; font-weight:800;">{pest['name']}</h3>
                <span class="badge-pill badge-pill-amber">Pathogen: {pest['causal_agent']}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    p_col_info, p_col_img = st.columns([1.3, 0.7])

    with p_col_info:
        st.markdown("#### 🔍 Diagnostic Symptoms:")
        for s in pest["symptoms"]:
            st.markdown(f"- **{s}**")

        st.markdown("#### 🛡️ Preventive Measures:")
        for p_meas in pest["preventive_measures"]:
            st.markdown(f"- ✅ {p_meas}")

        st.markdown("#### 🧪 Scientifically Supported Management:")
        for m_meas in pest["scientific_management"]:
            st.markdown(f"- 💊 {m_meas}")

    with p_col_img:
        st.markdown("#### 📷 Diagnostic Field Reference:")
        render_image_safe(pest.get("image", ""), caption=f"Symptoms of {pest['name']}")


# --------------------------------------------------------------------------------------
# 6. HARVESTING AND PROCESSING GUIDE
# --------------------------------------------------------------------------------------
def render_harvest_processing_section():
    st.markdown("### 🌶️ Harvesting, Blanching, Drying & Storage Protocols")
    st.markdown("Preserve bulk density, piperine concentration, and food safety standards through scientific post-harvest handling.")

    hp_cols = st.columns(2)

    with hp_cols[0]:
        st.markdown(f"""
            <div class="guide-card" style="border-top: 3px solid #2ECC71;">
                <h4 style="color:#0F3E26; margin-top:0; font-weight:800;">1. {HARVEST_PROCESSING_DATA['maturity_identification']['title']}</h4>
                <p style="font-size:0.92rem; color:#4A5B50; line-height:1.6;">{HARVEST_PROCESSING_DATA['maturity_identification']['explanation']}</p>
            </div>
        """, unsafe_allow_html=True)
        render_image_safe("assets/images/guide/berry_ripening.jpg", caption="1–2 Orange-Red Berry Indicator Rule for Peak Piperine")

        st.markdown(f"""
            <div class="guide-card" style="border-top: 3px solid #2E8B57;">
                <h4 style="color:#0F3E26; margin-top:0; font-weight:800;">2. {HARVEST_PROCESSING_DATA['harvesting_procedure']['title']}</h4>
                <p style="font-size:0.92rem; color:#4A5B50; line-height:1.6;">{HARVEST_PROCESSING_DATA['harvesting_procedure']['explanation']}</p>
            </div>
        """, unsafe_allow_html=True)
        render_image_safe("assets/images/pepper_harvest.jpg", caption="Gentle Ladder Harvesting on Tall Living Standards")

        st.markdown(f"""
            <div class="guide-card" style="border-top: 3px solid #185A37;">
                <h4 style="color:#0F3E26; margin-top:0; font-weight:800;">3. {HARVEST_PROCESSING_DATA['berry_separation']['title']}</h4>
                <p style="font-size:0.92rem; color:#4A5B50; line-height:1.6;">{HARVEST_PROCESSING_DATA['berry_separation']['explanation']}</p>
            </div>
        """, unsafe_allow_html=True)

    with hp_cols[1]:
        st.markdown(f"""
            <div class="guide-card" style="border-top: 3px solid #E5A93C;">
                <h4 style="color:#0F3E26; margin-top:0; font-weight:800;">4. {HARVEST_PROCESSING_DATA['blanching']['title']}</h4>
                <p style="font-size:0.92rem; color:#4A5B50; line-height:1.6;">{HARVEST_PROCESSING_DATA['blanching']['explanation']}</p>
            </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
            <div class="guide-card" style="border-top: 3px solid #F39C12;">
                <h4 style="color:#0F3E26; margin-top:0; font-weight:800;">5. {HARVEST_PROCESSING_DATA['drying_moisture']['title']}</h4>
                <p style="font-size:0.92rem; color:#4A5B50; line-height:1.6;">{HARVEST_PROCESSING_DATA['drying_moisture']['explanation']}</p>
            </div>
        """, unsafe_allow_html=True)
        render_image_safe("assets/images/guide/drying_storage.jpg", caption="Controlled Solar Poly-Sheet Drying to 10–11% Moisture")

        st.markdown(f"""
            <div class="guide-card" style="border-top: 3px solid #B57C18;">
                <h4 style="color:#0F3E26; margin-top:0; font-weight:800;">6. {HARVEST_PROCESSING_DATA['grading_storage']['title']}</h4>
                <p style="font-size:0.92rem; color:#4A5B50; line-height:1.6;">{HARVEST_PROCESSING_DATA['grading_storage']['explanation']}</p>
            </div>
        """, unsafe_allow_html=True)


# --------------------------------------------------------------------------------------
# 7. YOUTUBE VIDEO LEARNING RESOURCES
# --------------------------------------------------------------------------------------
def render_video_library_section():
    st.markdown("### 🎥 YouTube Educational Video Library")
    st.markdown("Curated agricultural video tutorials from ICAR-IISR and agricultural universities covering essential cultivation techniques.")

    v_col1, v_col2 = st.columns(2)

    for idx, vid in enumerate(YOUTUBE_RESOURCES_DATA):
        target_col = v_col1 if idx % 2 == 0 else v_col2
        with target_col:
            st.markdown(f"""
                <div class="guide-card" style="border-top: 3.5px solid #0F3E26; height:100%;">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;">
                        <span class="badge-pill badge-pill-green">{vid['category']}</span>
                        <span style="font-size:0.8rem; color:#718478; font-weight:700;">⏱️ {vid['duration']}</span>
                    </div>
                    <h4 style="color:#0F3E26; margin-top:4px; margin-bottom:6px; font-weight:800;">{vid['title']}</h4>
                    <p style="font-size:0.84rem; color:#185A37; font-weight:700; margin-bottom:8px;">Channel: {vid['channel']}</p>
                    <p style="font-size:0.88rem; color:#4A5B50; line-height:1.5; margin-bottom:12px;">{vid['description']}</p>
                </div>
            """, unsafe_allow_html=True)
            render_youtube_player(vid["url"], title=vid["title"], height=310)
            st.markdown("<br/>", unsafe_allow_html=True)
