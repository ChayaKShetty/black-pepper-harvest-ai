"""
Automated Test Suite for Black Pepper Harvest Readiness AI
Validates all modules, database integrity, report generation, and guide data.
"""

import os
import sys
import json
import pandas as pd

# Ensure UTF-8 output on Windows terminals
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

def run_tests():
    print("=" * 60)
    print("RUNNING BLACK PEPPER HARVEST READINESS AI TEST SUITE")
    print("=" * 60)

    # 1. Test Roboflow Service Configuration
    print("\n[1/6] Testing Roboflow Service Configuration...")
    from modules.roboflow_service import RoboflowService
    rf = RoboflowService()
    configured, msg = rf.is_configured()
    assert configured, f"Roboflow not configured: {msg}"
    assert rf.workspace == "chaya-shetty", f"Unexpected workspace: {rf.workspace}"
    assert str(rf.version) == "3", f"Unexpected version: {rf.version}"
    print(f"  ✓ Roboflow Service configured: Workspace='{rf.workspace}', Version='{rf.version}'")

    # 2. Test Gemini Assistant
    print("\n[2/6] Testing Gemini Assistant...")
    from modules.gemini_assistant import GeminiAssistant, SUGGESTED_QUESTIONS
    gem = GeminiAssistant()
    assert len(SUGGESTED_QUESTIONS) == 6, f"Expected 6 suggested questions, got {len(SUGGESTED_QUESTIONS)}"
    print(f"  ✓ Suggested questions verified ({len(SUGGESTED_QUESTIONS)} items)")
    for q in SUGGESTED_QUESTIONS:
        print(f"    - {q}")

    # 3. Test Database Integrity & History Records
    print("\n[3/6] Testing Database & History Records...")
    from modules.history_manager import get_all_history, filter_history
    records = get_all_history()
    print(f"  ✓ Database query successful: {len(records)} existing scan records preserved")
    assert len(records) >= 17, f"Expected at least 17 records, found {len(records)}"
    filtered = filter_history("", "All", "All")
    assert len(filtered) == len(records), "Filter mismatch for All/All"
    filtered_prime = filter_history("", "All", "Prime")
    print(f"  ✓ Filter tested: {len(filtered_prime)} scans classified as Prime")

    # 4. Test Report Generation (PDF & CSV)
    print("\n[4/6] Testing Report Generation Engines...")
    from modules.report_generator import generate_pdf_report, generate_csv_report
    sample_summary = {
        "total_detections": 10,
        "matured_count": 7,
        "immatured_count": 3,
        "maturity_pct": 70.0,
        "status": "Prime Harvest Readiness",
        "recommendation": "Harvest ripe spikes immediately using clean ladders.",
        "avg_confidence": 88.5,
    }
    sample_detections = [
        {"normalized_class": "matured", "confidence": 0.92, "x": 100, "y": 150, "width": 50, "height": 80},
        {"normalized_class": "immatured", "confidence": 0.85, "x": 200, "y": 250, "width": 45, "height": 75},
    ]
    pdf_bytes = generate_pdf_report("test_sample.jpg", "Image", sample_summary, sample_detections)
    assert len(pdf_bytes) > 1000, "PDF generation produced empty or too small byte stream"
    assert pdf_bytes.startswith(b"%PDF"), "Generated output is not a valid PDF file"
    print(f"  ✓ ReportLab PDF generated successfully: {len(pdf_bytes)} bytes")

    csv_bytes = generate_csv_report("test_sample.jpg", sample_summary, sample_detections)
    assert len(csv_bytes) > 100, "CSV generation produced too small byte stream"
    print(f"  ✓ Pandas CSV generated successfully: {len(csv_bytes)} bytes")

    # 5. Test Cultivation & Growing Guide Data Structure
    print("\n[5/6] Testing Cultivation & Growing Guide Data Structures...")
    from pages_custom.cultivation_guide_page import (
        CULTIVATION_CHAPTERS_DATA,
        GROWING_METHODS_DATA,
        PROPAGATION_TECHNIQUES_DATA,
        FERTILIZER_IRRIGATION_DATA,
        PEST_DISEASE_DATA,
        HARVEST_PROCESSING_DATA,
        YOUTUBE_RESOURCES_DATA,
    )
    assert len(CULTIVATION_CHAPTERS_DATA) == 23, f"Expected 23 chapters, got {len(CULTIVATION_CHAPTERS_DATA)}"
    print(f"  ✓ All 23 Cultivation Chapters present and validated")
    for ch in CULTIVATION_CHAPTERS_DATA:
        assert ch["title"], f"Chapter {ch['id']} has no title"
        assert ch["summary"], f"Chapter {ch['id']} has no summary"
        assert ch["explanation"], f"Chapter {ch['id']} has no explanation"
        assert len(ch["important_points"]) > 0, f"Chapter {ch['id']} has no important points"
        assert len(ch["farming_recommendations"]) > 0, f"Chapter {ch['id']} has no recommendations"
        assert len(ch.get("mistakes_to_avoid", [])) > 0, f"Chapter {ch['id']} has no mistakes to avoid"
        assert len(ch.get("learning_resources", [])) > 0, f"Chapter {ch['id']} has no learning resources"
        assert ch["tips"], f"Chapter {ch['id']} has no tips"

    assert len(GROWING_METHODS_DATA) == 7, f"Expected 7 growing methods, got {len(GROWING_METHODS_DATA)}"
    print(f"  ✓ All 7 Growing Methods present and validated")
    for gm in GROWING_METHODS_DATA:
        assert gm["name"], "Method missing name"
        assert gm["how_it_works"], "Method missing how_it_works"
        assert len(gm.get("procedure", [])) > 0, f"Method {gm['id']} missing step-by-step procedure"
        assert gm["youtube_url"].startswith("https://www.youtube.com"), f"Method {gm['id']} missing youtube URL"
        assert len(gm["advantages"]) > 0, "Method missing advantages"
        assert len(gm["limitations"]) > 0, "Method missing limitations"

    assert len(PROPAGATION_TECHNIQUES_DATA) == 6, f"Expected 6 propagation techniques, got {len(PROPAGATION_TECHNIQUES_DATA)}"
    print(f"  ✓ All 6 Propagation Protocols present and validated")
    for pt in PROPAGATION_TECHNIQUES_DATA:
        assert pt["name"], "Protocol missing name"
        assert len(pt["procedure"]) > 0, "Protocol missing procedure steps"
        assert pt["tips"], "Protocol missing tips"

    assert len(PEST_DISEASE_DATA) == 7, f"Expected 7 pest/disease profiles, got {len(PEST_DISEASE_DATA)}"
    print(f"  ✓ All 7 Pest & Disease profiles validated")

    assert len(YOUTUBE_RESOURCES_DATA) >= 6, f"Expected at least 6 video resources, got {len(YOUTUBE_RESOURCES_DATA)}"
    print(f"  ✓ Curated YouTube Video Resources validated ({len(YOUTUBE_RESOURCES_DATA)} videos)")

    assert "organic_manures" in FERTILIZER_IRRIGATION_DATA and "npk_schedule" in FERTILIZER_IRRIGATION_DATA
    print(f"  ✓ Specialized Fertilizer & Irrigation data validated")

    assert "maturity_identification" in HARVEST_PROCESSING_DATA and "blanching" in HARVEST_PROCESSING_DATA
    print(f"  ✓ Specialized Harvesting & Processing data validated")

    # 6. Test App Navigation & CSS
    print("\n[6/6] Testing App Navigation & Style System...")
    from app import PAGES
    assert len(PAGES) == 6, f"Expected 6 navigation pages, found {len(PAGES)}"
    print(f"  ✓ Navigation menu has {len(PAGES)} top-level sections:")
    for label, val in PAGES.items():
        print(f"    - {label} -> {val}")

    css_path = os.path.join("assets", "styles", "main.css")
    assert os.path.exists(css_path), "main.css missing"
    with open(css_path, "r", encoding="utf-8") as f:
        css_content = f.read()
    assert ".hero-banner" in css_content, "Missing .hero-banner in CSS"
    assert ".metric-card" in css_content, "Missing .metric-card in CSS"
    assert ".feature-card" in css_content, "Missing .feature-card in CSS"
    print("  ✓ Modern Agricultural CSS style system verified")

    print("\n" + "=" * 60)
    print("ALL 6 TEST SUITE PHASES PASSED WITH ZERO ERRORS!")
    print("=" * 60)

if __name__ == "__main__":
    run_tests()
