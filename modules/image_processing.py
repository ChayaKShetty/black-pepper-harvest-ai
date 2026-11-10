"""
Image Processing Module for Pepper Harvest AI
Handles bounding box drawing, annotation formatting, and image conversion.
Strictly maps genuine detection coordinates to the source image.
"""

import io
from typing import List, Dict, Any, Tuple, Optional
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")  # Non-interactive backend for server deployment
import matplotlib.pyplot as plt


# Palette definition as specified in prompt:
# Green for matured (#2ECC71 / #3D8B50)
# Amber for immatured (#E8B54A / #F39C12)
COLOR_MATURED_RGB = (46, 204, 113)       # #2ECC71 Vibrant Green
COLOR_IMMATURED_RGB = (232, 181, 74)     # #E8B54A Warm Golden Amber
COLOR_MATURED_HEX = "#2ECC71"
COLOR_IMMATURED_HEX = "#E8B54A"
COLOR_BG_HEX = "#F7F8F3"
COLOR_TEXT_HEX = "#202923"


def create_maturity_chart(summary: Dict[str, Any]):
    """
    Creates an elegant, publication-quality Matplotlib chart showing
    maturity distribution (Donut chart & comparative bar chart).
    """
    matured = summary.get("matured_count", 0)
    immatured = summary.get("immatured_count", 0)
    total = summary.get("total_detections", 0)

    if total == 0:
        return None

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.5, 3.0), facecolor=COLOR_BG_HEX)
    fig.subplots_adjust(wspace=0.35)

    # 1. Donut Chart
    labels = ["Matured", "Immatured"]
    sizes = [matured, immatured]
    colors = [COLOR_MATURED_HEX, COLOR_IMMATURED_HEX]

    # Filter out 0 slices if any
    valid_data = [(l, s, c) for l, s, c in zip(labels, sizes, colors) if s > 0]
    if valid_data:
        v_labels, v_sizes, v_colors = zip(*valid_data)
        wedges, texts, autotexts = ax1.pie(
            v_sizes,
            labels=v_labels,
            autopct="%1.1f%%",
            startangle=140,
            colors=v_colors,
            wedgeprops={"width": 0.45, "edgecolor": "white", "linewidth": 2},
            textprops={"fontsize": 9, "color": COLOR_TEXT_HEX, "weight": "bold"},
        )
        for autotext in autotexts:
            autotext.set_color("#1C2833")
            autotext.set_fontsize(8.5)
    
    # Center text in donut
    ax1.text(0, 0, f"{total}\nSpikes", ha="center", va="center", fontsize=10, weight="bold", color=COLOR_TEXT_HEX)
    ax1.set_title("Maturity Ratio", fontsize=10.5, weight="bold", color=COLOR_TEXT_HEX, pad=10)

    # 2. Bar Chart
    bars = ax2.bar(
        ["Matured", "Immatured"],
        [matured, immatured],
        color=[COLOR_MATURED_HEX, COLOR_IMMATURED_HEX],
        width=0.45,
        edgecolor="#D5D8DC",
        linewidth=1,
    )
    ax2.set_facecolor("white")
    ax2.grid(axis="y", linestyle="--", alpha=0.4)
    ax2.set_title("Spike Count Comparison", fontsize=10.5, weight="bold", color=COLOR_TEXT_HEX, pad=10)
    ax2.set_ylabel("Number of Spikes", fontsize=8.5, color=COLOR_TEXT_HEX)
    ax2.tick_params(colors=COLOR_TEXT_HEX, labelsize=9)

    # Annotate bar values
    for bar in bars:
        h = bar.get_height()
        ax2.annotate(
            f"{int(h)}",
            xy=(bar.get_x() + bar.get_width() / 2, h),
            xytext=(0, 3),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=9.5,
            weight="bold",
            color=COLOR_TEXT_HEX,
        )

    # Clean borders
    for spine in ax2.spines.values():
        spine.set_color("#BDC3C7")

    return fig


def get_class_color(normalized_class: str) -> Tuple[int, int, int]:
    """Returns RGB tuple for the detection class."""
    if normalized_class.lower() == "matured":
        return COLOR_MATURED_RGB
    return COLOR_IMMATURED_RGB


def annotate_image(
    image: Image.Image,
    detections: List[Dict[str, Any]],
    show_confidence: bool = True,
    box_thickness: int = 3,
) -> Image.Image:
    """
    Draws authentic bounding boxes and labels onto the image using actual Roboflow coordinates.
    """
    # Create an editable copy of the image in RGB mode
    annotated = image.convert("RGB").copy()
    draw = ImageDraw.Draw(annotated)
    width, height = annotated.size

    # Try loading a readable system TTF font, fallback to default
    try:
        font = ImageFont.truetype("arial.ttf", size=max(14, int(min(width, height) * 0.022)))
    except Exception:
        try:
            font = ImageFont.truetype("DejaVuSans.ttf", size=max(14, int(min(width, height) * 0.022)))
        except Exception:
            font = ImageFont.load_default()

    for idx, det in enumerate(detections):
        cls_norm = det.get("normalized_class", "immatured")
        conf = det.get("confidence", 0.0)
        color = get_class_color(cls_norm)

        # Coordinate parsing
        x1 = det.get("x1", 0)
        y1 = det.get("y1", 0)
        x2 = det.get("x2", 0)
        y2 = det.get("y2", 0)

        # Clamp coordinates to image boundaries
        x1 = max(0, min(width - 1, x1))
        y1 = max(0, min(height - 1, y1))
        x2 = max(0, min(width - 1, x2))
        y2 = max(0, min(height - 1, y2))

        # Skip invalid zero-size boxes
        if x2 <= x1 or y2 <= y1:
            continue

        # Draw outer rectangle
        for offset in range(box_thickness):
            draw.rectangle(
                [x1 - offset, y1 - offset, x2 + offset, y2 + offset],
                outline=color,
            )

        # Construct label text
        label_name = "MATURED" if cls_norm == "matured" else "IMMATURED"
        if show_confidence:
            label_text = f"{label_name} {conf * 100:.1f}%"
        else:
            label_text = label_name

        # Calculate text bounding box
        try:
            bbox = font.getbbox(label_text)
            text_w = bbox[2] - bbox[0]
            text_h = bbox[3] - bbox[1]
        except Exception:
            text_w = len(label_text) * 8
            text_h = 14

        pad = 4
        # Position label above bounding box if space allows, else inside
        if y1 - text_h - (pad * 2) >= 0:
            label_y0 = y1 - text_h - (pad * 2)
            label_y1 = y1
        else:
            label_y0 = y1
            label_y1 = y1 + text_h + (pad * 2)

        label_x0 = x1
        label_x1 = min(width - 1, x1 + text_w + (pad * 2))

        # Draw label background pill
        draw.rectangle([label_x0, label_y0, label_x1, label_y1], fill=color)

        # Draw text with contrasting color (dark slate for high readability on bright colors)
        text_color = (20, 30, 25)
        draw.text((label_x0 + pad, label_y0 + pad), label_text, fill=text_color, font=font)

    return annotated


def detections_to_dataframe(detections: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Converts detection list into a clean pandas DataFrame for visualization and CSV export.
    """
    if not detections:
        return pd.DataFrame(columns=[
            "Index", "Class", "Stage", "Confidence (%)", "Center X", "Center Y", "Width", "Height"
        ])

    records = []
    for idx, d in enumerate(detections, start=1):
        norm_cls = d.get("normalized_class", "immatured")
        stage_desc = "Ripe (Ready for harvest)" if norm_cls == "matured" else "Unripe (Developing spike)"
        records.append({
            "Index": idx,
            "Class": norm_cls.capitalize(),
            "Stage": stage_desc,
            "Confidence (%)": round(d.get("confidence", 0.0) * 100, 2),
            "Center X": round(d.get("x", 0.0), 1),
            "Center Y": round(d.get("y", 0.0), 1),
            "Width": round(d.get("width", 0.0), 1),
            "Height": round(d.get("height", 0.0), 1),
        })

    return pd.DataFrame(records)


def pil_to_bytes(image: Image.Image, format: str = "JPEG", quality: int = 95) -> bytes:
    """Converts a PIL Image to raw bytes."""
    buf = io.BytesIO()
    if format.upper() == "JPEG":
        image = image.convert("RGB")
    image.save(buf, format=format, quality=quality)
    return buf.getvalue()

