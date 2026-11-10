"""
Report Generator Module for Pepper Harvest AI
Generates professional, publication-quality PDF and CSV harvest readiness reports using ReportLab and Pandas.
"""

import os
import io
import tempfile
from datetime import datetime
from typing import List, Dict, Any, Optional
from PIL import Image
import pandas as pd

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image as RLImage,
    KeepTogether,
    HRFlowable,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

REPORTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "reports")


def generate_pdf_report(
    filename: str,
    media_type: str,
    summary: Dict[str, Any],
    detections: List[Dict[str, Any]],
    annotated_image: Optional[Image.Image] = None,
    output_path: Optional[str] = None,
) -> bytes:
    """
    Generates a comprehensive PDF harvest report using ReportLab.
    Returns the PDF content as bytes.
    """
    os.makedirs(REPORTS_DIR, exist_ok=True)
    buffer = io.BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36,
    )

    styles = getSampleStyleSheet()

    # Custom color palette matching design system
    primary_color = colors.HexColor("#174D32")
    secondary_color = colors.HexColor("#3D8B50")
    accent_color = colors.HexColor("#E8B54A")
    bg_subtle = colors.HexColor("#F7F8F3")
    text_dark = colors.HexColor("#202923")
    border_color = colors.HexColor("#D5D8DC")

    title_style = ParagraphStyle(
        "DocTitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        textColor=primary_color,
        alignment=0,
    )
    subtitle_style = ParagraphStyle(
        "DocSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=13,
        textColor=secondary_color,
        alignment=0,
    )
    heading_style = ParagraphStyle(
        "SectionHeading",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=16,
        textColor=primary_color,
        spaceAfter=6,
    )
    body_style = ParagraphStyle(
        "DocBody",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9,
        leading=12,
        textColor=text_dark,
    )
    body_bold = ParagraphStyle(
        "DocBodyBold",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=9,
        leading=12,
        textColor=text_dark,
    )
    table_header_style = ParagraphStyle(
        "TableHeader",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=9,
        leading=11,
        textColor=colors.white,
    )
    table_cell_style = ParagraphStyle(
        "TableCell",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=11,
        textColor=text_dark,
    )
    disclaimer_style = ParagraphStyle(
        "Disclaimer",
        parent=styles["Normal"],
        fontName="Helvetica-Oblique",
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor("#5D6D7E"),
    )

    story = []

    # 1. Header Banner
    story.append(Paragraph("PEPPER HARVEST AI", title_style))
    story.append(Paragraph("Black Pepper Harvest Readiness & Maturity Diagnostic Report", subtitle_style))
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=2, color=accent_color, spaceBefore=2, spaceAfter=10))

    # 2. Metadata Section Table
    analysis_time = datetime.now().strftime("%B %d, %Y - %H:%M:%S")
    meta_data = [
        [
            Paragraph("<b>Target Sample:</b>", body_style), Paragraph(str(filename), body_style),
            Paragraph("<b>Analysis Date:</b>", body_style), Paragraph(analysis_time, body_style),
        ],
        [
            Paragraph("<b>Media Modality:</b>", body_style), Paragraph(str(media_type), body_style),
            Paragraph("<b>Model Architecture:</b>", body_style), Paragraph("YOLO26 Nano (Roboflow Hosted TRT)", body_style),
        ]
    ]
    meta_table = Table(meta_data, colWidths=[1.3 * inch, 2.3 * inch, 1.3 * inch, 2.3 * inch])
    meta_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg_subtle),
        ("BOX", (0, 0), (-1, -1), 0.5, border_color),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, border_color),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 12))

    # 3. Executive Harvest Summary Box
    story.append(Paragraph("EXECUTIVE HARVEST READINESS SUMMARY", heading_style))

    matured_count = summary.get("matured_count", 0)
    immatured_count = summary.get("immatured_count", 0)
    total_spikes = summary.get("total_detections", 0)
    maturity_pct = summary.get("maturity_pct", 0.0)
    status_label = summary.get("status", "Unknown")
    recommendation = summary.get("recommendation", "No specific recommendation.")

    summary_cards_data = [
        [
            Paragraph("<b>Total Spikes Detected</b>", body_style),
            Paragraph("<b>Matured Spikes (Ripe)</b>", body_style),
            Paragraph("<b>Immatured Spikes</b>", body_style),
            Paragraph("<b>Maturity Ratio</b>", body_style),
        ],
        [
            Paragraph(f"<font size=13 color='#174D32'><b>{total_spikes}</b></font>", body_style),
            Paragraph(f"<font size=13 color='#2ECC71'><b>{matured_count}</b></font>", body_style),
            Paragraph(f"<font size=13 color='#E8B54A'><b>{immatured_count}</b></font>", body_style),
            Paragraph(f"<font size=13 color='#174D32'><b>{maturity_pct:.1f}%</b></font>", body_style),
        ]
    ]
    summary_table = Table(summary_cards_data, colWidths=[1.8 * inch, 1.8 * inch, 1.8 * inch, 1.8 * inch])
    summary_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EAECEE")),
        ("BACKGROUND", (0, 1), (-1, 1), colors.white),
        ("BOX", (0, 0), (-1, -1), 1, border_color),
        ("INNERGRID", (0, 0), (-1, -1), 0.5, border_color),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(summary_table)
    story.append(Spacer(1, 8))

    # Harvest Verdict Box
    verdict_data = [
        [Paragraph(f"<b>Harvest Status:</b> {status_label}", body_bold)],
        [Paragraph(f"<b>Agronomic Advisory:</b> {recommendation}", body_style)],
    ]
    verdict_table = Table(verdict_data, colWidths=[7.2 * inch])
    verdict_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F2F9F4")),
        ("BOX", (0, 0), (-1, -1), 1, secondary_color),
        ("LINEBELOW", (0, 0), (-1, 0), 0.5, border_color),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ]))
    story.append(verdict_table)
    story.append(Spacer(1, 12))

    # 4. Annotated Visual Evidence
    if annotated_image is not None:
        try:
            story.append(Paragraph("COMPUTER VISION ANNOTATED EVIDENCE", heading_style))

            # Save temporary image for ReportLab flowable
            temp_img = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
            temp_img_path = temp_img.name
            temp_img.close()

            # Resize keeping aspect ratio to fit max width ~6.5 inch
            img_w, img_h = annotated_image.size
            aspect = img_h / float(img_w)
            display_w = 6.2 * inch
            display_h = display_w * aspect
            if display_h > 3.5 * inch:
                display_h = 3.5 * inch
                display_w = display_h / aspect

            annotated_image.convert("RGB").save(temp_img_path, format="JPEG", quality=90)
            rl_img = RLImage(temp_img_path, width=display_w, height=display_h)
            story.append(rl_img)
            story.append(Spacer(1, 10))
        except Exception:
            pass

    # 5. Genuine Detection Breakdown Table
    if detections:
        story.append(Paragraph("GENUINE DETECTION BREAKDOWN (ROBOFLOW YOLO26 NANO)", heading_style))
        det_rows = [
            [
                Paragraph("<b>#</b>", table_header_style),
                Paragraph("<b>Detected Class</b>", table_header_style),
                Paragraph("<b>Confidence</b>", table_header_style),
                Paragraph("<b>Center (X, Y)</b>", table_header_style),
                Paragraph("<b>Bounding Box (W × H)</b>", table_header_style),
            ]
        ]
        # Show up to 15 detections in PDF to preserve clean pagination
        for i, d in enumerate(detections[:15], start=1):
            cls_text = d.get("normalized_class", "immatured").upper()
            conf_val = d.get("confidence", 0.0) * 100
            cx, cy = round(d.get("x", 0.0), 1), round(d.get("y", 0.0), 1)
            bw, bh = round(d.get("width", 0.0), 1), round(d.get("height", 0.0), 1)

            det_rows.append([
                Paragraph(str(i), table_cell_style),
                Paragraph(cls_text, table_cell_style),
                Paragraph(f"{conf_val:.1f}%", table_cell_style),
                Paragraph(f"({cx}, {cy})", table_cell_style),
                Paragraph(f"{bw} × {bh} px", table_cell_style),
            ])

        det_table = Table(det_rows, colWidths=[0.5 * inch, 1.8 * inch, 1.3 * inch, 1.8 * inch, 1.8 * inch])
        det_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), primary_color),
            ("BOX", (0, 0), (-1, -1), 0.5, border_color),
            ("INNERGRID", (0, 0), (-1, -1), 0.5, border_color),
            ("TOPPADDING", (0, 0), (-1, -1), 3),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, bg_subtle]),
        ]))
        story.append(det_table)
        story.append(Spacer(1, 10))

    # 6. Agronomic Best Practices
    guidance_text = (
        "<b>Commercial Post-Harvest Advisory:</b><br/>"
        "• <b>Harvesting Window:</b> Commercial harvesting begins when 1 or 2 berries on a spike turn orange/red.<br/>"
        "• <b>Blanching (Recommended):</b> Dipping harvested green spikes in boiling water (80°C to 90°C) for 1 minute accelerates "
        "polyphenol oxidase, ensuring uniform dark jet-black color, cleaner surface, and faster drying.<br/>"
        "• <b>Moisture Target:</b> Sun-dry on clean polythene sheets for 4-5 days until berry moisture drops to 10-12%."
    )
    story.append(Paragraph(guidance_text, body_style))
    story.append(Spacer(1, 10))

    # 7. AI Disclaimer
    disclaimer_text = (
        "<b>AI Diagnostic Disclaimer:</b> This report was generated automatically by Pepper Harvest AI using genuine "
        "inference from YOLO26 Nano. Results are intended as decision-support guidance for farmers and agronomists. "
        "Always cross-examine field conditions and prevailing weather prior to bulk harvesting operations."
    )
    story.append(Paragraph(disclaimer_text, disclaimer_style))

    doc.build(story)
    pdf_bytes = buffer.getvalue()
    buffer.close()

    # Save to disk if requested
    if output_path:
        with open(output_path, "wb") as f:
            f.write(pdf_bytes)

    return pdf_bytes


def generate_csv_report(
    filename: str,
    summary: Dict[str, Any],
    detections: List[Dict[str, Any]],
) -> bytes:
    """
    Generates a structured CSV export containing metadata and all genuine detections.
    """
    df = pd.DataFrame([
        {
            "Report_Timestamp": datetime.now().isoformat(),
            "Source_File": filename,
            "Detection_Index": idx,
            "Class": d.get("class", ""),
            "Normalized_Class": d.get("normalized_class", ""),
            "Confidence_Score": d.get("confidence", 0.0),
            "Confidence_Percent": round(d.get("confidence", 0.0) * 100, 2),
            "BBox_Center_X": d.get("x", 0.0),
            "BBox_Center_Y": d.get("y", 0.0),
            "BBox_Width": d.get("width", 0.0),
            "BBox_Height": d.get("height", 0.0),
            "Maturity_Ratio_Overall": summary.get("maturity_pct", 0.0),
            "Harvest_Status": summary.get("status", ""),
        }
        for idx, d in enumerate(detections, start=1)
    ])

    return df.to_csv(index=False).encode("utf-8")

