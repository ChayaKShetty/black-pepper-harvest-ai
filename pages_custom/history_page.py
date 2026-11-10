"""
Enhanced Scan History and Field Reports Page for Pepper Harvest AI
Displays persistent SQLite inspection records as modern cards with thumbnails,
confidence metrics, and instant PDF/CSV report exports.
"""

import os
import streamlit as st
import pandas as pd
import json
from PIL import Image

from modules.history_manager import (
    get_all_history,
    filter_history,
    delete_history_entry,
    clear_all_history,
)
from modules.report_generator import generate_pdf_report, generate_csv_report
from modules.image_processing import COLOR_MATURED_HEX, COLOR_IMMATURED_HEX


def find_preview_image(filename: str):
    """Attempts to find a saved or sample image corresponding to the filename."""
    if not filename:
        return None
    # Check sample_images
    p1 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "sample_images", filename)
    if os.path.exists(p1):
        try:
            return Image.open(p1)
        except Exception:
            pass
    # Check assets/images
    p2 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets", "images", filename)
    if os.path.exists(p2):
        try:
            return Image.open(p2)
        except Exception:
            pass
    return None


def render_history_page():
    st.markdown("""
        <div style="margin-bottom: 22px;">
            <span class="badge-pill badge-pill-green">Field Audit Log</span>
            <h1 style="color: #174D32; margin-top: 6px; margin-bottom: 4px;">Scan History & Field Reports</h1>
            <p style="color: #4A5568; font-size: 1.05rem;">
                Browse, search, and download past black pepper harvest readiness diagnostics stored in your local SQLite database.
            </p>
        </div>
    """, unsafe_allow_html=True)

    all_records = get_all_history()
    total_records = len(all_records)
    total_spikes_detected = sum(r["total_detections"] for r in all_records)
    avg_maturity = (
        sum(r["maturity_pct"] for r in all_records) / total_records if total_records > 0 else 0.0
    )

    # Top KPI Metrics Row
    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.markdown(f"""
        <div class="metric-card" style="border-top: 3px solid #0F3E26;">
            <div class="metric-lbl">Total Scans Saved</div>
            <div class="metric-val" style="color:#0F3E26;">{total_records}</div>
            <div style="font-size:0.75rem; color:#718478;">Database Audit Logs</div>
        </div>
        """, unsafe_allow_html=True)
    with k2:
        st.markdown(f"""
        <div class="metric-card" style="border-top: 3px solid #2E8B57;">
            <div class="metric-lbl">Total Spikes Inspected</div>
            <div class="metric-val" style="color:#2E8B57;">{total_spikes_detected}</div>
            <div style="font-size:0.75rem; color:#718478;">Spikes Across All Scans</div>
        </div>
        """, unsafe_allow_html=True)
    with k3:
        st.markdown(f"""
        <div class="metric-card" style="border-top: 3px solid #E5A93C;">
            <div class="metric-lbl">Average Maturity Index</div>
            <div class="metric-val" style="color:#B57C18;">{avg_maturity:.1f}%</div>
            <div style="font-size:0.75rem; color:#718478;">Mean Field Readiness</div>
        </div>
        """, unsafe_allow_html=True)
    with k4:
        # Master CSV export for entire history
        if all_records:
            df_all = pd.DataFrame(all_records)
            if "details_json" in df_all.columns:
                df_all_clean = df_all.drop(columns=["details_json"])
            else:
                df_all_clean = df_all
            master_csv = df_all_clean.to_csv(index=False).encode("utf-8")
            st.markdown("""
            <div class="metric-card" style="border-top: 3px solid #185A37;">
                <div class="metric-lbl">Export All History</div>
                <div style="margin-top: 6px; margin-bottom: 4px;">
            """, unsafe_allow_html=True)
            st.download_button(
                "📥 Master CSV Export",
                data=master_csv,
                file_name="All_Pepper_Scan_History.csv",
                mime="text/csv",
                use_container_width=True,
                key="btn_master_csv",
            )
            st.markdown("</div><div style='font-size:0.75rem; color:#718478;'>All Audit Scans</div></div>", unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="metric-card" style="border-top: 3px solid #718478;">
                <div class="metric-lbl">Export Data</div>
                <div class="metric-val" style="font-size:1.1rem; color:#718478; margin-top:14px;">No Scans Yet</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    # Search and Filter Toolbar
    fcol1, fcol2, fcol3 = st.columns([1.6, 1.0, 1.2])
    with fcol1:
        search_query = st.text_input("🔍 Search history by filename, status, or advisory:", "", placeholder="e.g. sample, Prime, Immature...")
    with fcol2:
        media_filter = st.selectbox("Media Modality:", ["All", "Image", "Video"])
    with fcol3:
        status_filter = st.selectbox("Harvest Classification:", ["All", "Prime", "Early", "Immature"])

    records = filter_history(search_query, media_filter, status_filter)

    st.write(f"Displaying **{len(records)}** of **{total_records}** inspection records.")

    if not records:
        st.info("No inspection records match the current filter. Perform a new image or video scan to add entries.")
        return

    # Visual Scan Cards List
    for r in records:
        rec_id = r["id"]
        status_str = r["status"]
        mat_pct = r["maturity_pct"]
        conf_val = r.get("avg_confidence", 0.0)

        # Determine border color based on status
        if "prime" in status_str.lower() or mat_pct >= 35.0:
            border_cls = "prime"
            badge_color = "#2ECC71"
            status_badge_text = "READY FOR HARVEST"
        elif "early" in status_str.lower() or mat_pct >= 15.0:
            border_cls = "early"
            badge_color = "#E8B54A"
            status_badge_text = "EARLY HARVEST (SELECTIVE)"
        else:
            border_cls = "immature"
            badge_color = "#E67E22"
            status_badge_text = "IMMATURE (NOT READY)"

        st.markdown(f"""
            <div class="history-card" style="border-left: 5px solid {badge_color};">
                <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; margin-bottom:10px;">
                    <div>
                        <span style="background:{badge_color}; color:#FFFFFF; font-weight:800; font-size:0.75rem; padding:4px 12px; border-radius:20px; letter-spacing:0.5px;">
                            {status_badge_text}
                        </span>
                        <span style="color:#718478; font-size:0.85rem; margin-left:12px;">
                            📅 <b>{r['timestamp']}</b> &nbsp;|&nbsp; 🏷️ Scan #{rec_id} ({r['media_type']})
                        </span>
                    </div>
                    <div style="font-weight:800; color:#0F3E26; font-size:1.15rem;">
                        Maturity: {mat_pct:.1f}%
                    </div>
                </div>
                <h4 style="color:#0F3E26; margin-top:4px; margin-bottom:6px; font-weight:800;">📄 File: {r['filename']}</h4>
                <p style="color:#4A5B50; font-size:0.95rem; margin-bottom:8px; line-height:1.5;">
                    <b>Agronomic Advisory:</b> {r['recommendation'] or 'Standard advisory'}
                </p>
            </div>
        """, unsafe_allow_html=True)

        # Card Action and Details Row
        card_c1, card_c2, card_c3, card_c4 = st.columns([1.2, 1.2, 1.2, 0.8])

        with card_c1:
            st.markdown(f"**Spikes:** 🟢 **{r['matured_count']}** Matured &nbsp;|&nbsp; 🟡 **{r['immatured_count']}** Immatured (Total: **{r['total_detections']}**)")
            if conf_val > 0:
                st.markdown(f"**Avg Model Confidence:** `{conf_val:.1f}%`")

        with card_c2:
            # Download PDF Report
            try:
                dets = json.loads(r["details_json"]) if r["details_json"] else []
                summary_dict = {
                    "total_detections": r["total_detections"],
                    "matured_count": r["matured_count"],
                    "immatured_count": r["immatured_count"],
                    "maturity_pct": r["maturity_pct"],
                    "status": r["status"],
                    "recommendation": r["recommendation"],
                    "avg_confidence": conf_val,
                }
                pdf_bytes = generate_pdf_report(
                    filename=r["filename"],
                    media_type=r["media_type"],
                    summary=summary_dict,
                    detections=dets,
                )
                st.download_button(
                    label=f"📄 Download PDF #{rec_id}",
                    data=pdf_bytes,
                    file_name=f"Harvest_Report_{rec_id}_{r['filename'].split('.')[0]}.pdf",
                    mime="application/pdf",
                    key=f"hist_pdf_{rec_id}",
                    use_container_width=True,
                )
            except Exception as e:
                st.error(f"PDF error: {e}")

        with card_c3:
            # Download CSV
            try:
                dets = json.loads(r["details_json"]) if r["details_json"] else []
                csv_bytes = generate_csv_report(r["filename"], summary_dict, dets)
                st.download_button(
                    label=f"📊 Export CSV #{rec_id}",
                    data=csv_bytes,
                    file_name=f"Scan_Data_{rec_id}_{r['filename'].split('.')[0]}.csv",
                    mime="text/csv",
                    key=f"hist_csv_{rec_id}",
                    use_container_width=True,
                )
            except Exception as e:
                st.error(f"CSV error: {e}")

        with card_c4:
            if st.button(f"🗑️ Delete", key=f"del_btn_{rec_id}", use_container_width=True):
                delete_history_entry(rec_id)
                st.success(f"Deleted scan #{rec_id}")
                st.rerun()

        # View Full Detection Details expander
        dets = json.loads(r["details_json"]) if r["details_json"] else []
        if dets:
            with st.expander(f"🔍 View {len(dets)} Detected Bounding Boxes for Scan #{rec_id}"):
                df_boxes = pd.DataFrame([
                    {
                        "Index": i,
                        "Class": d.get("normalized_class", d.get("class", "immatured")).capitalize(),
                        "Confidence (%)": round(d.get("confidence", 0.0) * 100, 2),
                        "Center X": round(d.get("x", 0.0), 1),
                        "Center Y": round(d.get("y", 0.0), 1),
                        "Width (px)": round(d.get("width", 0.0), 1),
                        "Height (px)": round(d.get("height", 0.0), 1),
                    }
                    for i, d in enumerate(dets, start=1)
                ])
                st.dataframe(df_boxes, use_container_width=True)

        st.markdown("<br/>", unsafe_allow_html=True)

    # Danger Zone: Clear all history
    st.markdown("---")
    with st.expander("⚠️ Danger Zone: Clear History"):
        st.warning("This will permanently remove all saved inspection records from `history.db`.")
        if st.button("Permanently Clear All History", type="secondary", key="clear_all_history_btn"):
            clear_all_history()
            st.success("All history records cleared!")
            st.rerun()
