# 🌿 Pepper Harvest AI — Black Pepper Harvest Readiness Web Application
---

## 📌 Project Overview
**Pepper Harvest AI** is an agricultural computer vision and decision-support web application designed to help black pepper (*Piper nigrum*) farmers identify the exact physiological harvest maturity of black pepper spikes.

By evaluating field photographs and video streams through a trained **YOLO26 Nano** computer vision model, the application detects and classifies:
- 🟢 **`matured`**: Spike clusters showing ripe physiological maturity (yellow to orange-red coloration or firm mature perisperm) ready for harvest to ensure peak piperine concentration and optimal bulk density (500–600 g/L).
- 🟡 **`immatured`**: Unripe developing green spike clusters that should be left on the vine for continued development.

---

## 🚀 Key Modules & System Capabilities

1. **🏠 Home Dashboard:**
   - Authentic black pepper plantation hero banner.
   - Real-time status indicators for the Roboflow YOLO26 Nano model, Gemini Assistant, and local SQLite database.
   - Interactive feature navigation cards and beginner-friendly 4-step farmer instructions.
   - Agronomic rules of thumb (1–2 berry rule, hot-water blanching technique).

2. **🔍 Harvest Maturity Detection (Image & Video):**
   - **Single Image Analysis:** Device upload, live camera capture, and sample plantation photos.
   - **Video Inspection:** Automated temporal frame sampling, keyframe extraction, and maturity progression timeline graphs.
   - **Authentic Inference:** Zero simulation; real bounding box coordinates `[x, y, width, height]` and genuine confidence scores.
   - **Diagnostic Exports:** Matplotlib donut/bar charts, side-by-side original vs. annotated views, ReportLab PDF diagnostic reports, and Pandas CSV data tables.

3. **📖 Black Pepper Cultivation & Growing Guide (ICAR-IISR Aligned):**
   - **23 Main Cultivation Chapters:** Complete agronomic guide with category filtering, real-time keyword search, quick-jump dropdown, common mistakes to avoid, learning resources, and back-to-top shortcuts.
   - **7 Cultivation Methods:** Live Support Tree, Arecanut-Based, Coconut-Based, Artificial Trellis, Intercropping, Homestead, and Container Bush Pepper with step-by-step procedures, authentic photos, and verified YouTube video guides.
   - **6 Propagation Protocols:** Step-by-step procedures for runner shoots, terminal cuttings, rooted cuttings, bamboo nursery beds, polybags, and field transplanting.
   - **Specialized Fertilizer & Irrigation Section:** Organic manures, FYM, compost, NPK split schedules with regional variations, irrigation triggers, and drainage.
   - **Specialized Pest & Disease Care:** Detailed diagnostic profiles for Phytophthora foot rot, slow decline, pollu beetle, top shoot borer, scale insects, nematodes, and nutrient deficiencies.
   - **Specialized Harvest & Post-Harvest Processing:** 1-2 berry ripening rule, picking safety, mechanical threshing, 60-second hot water blanching, sun drying (10-11% moisture), grading, and warehouse storage.
   - **Curated Video Library:** Direct access to verified university and ICAR-IISR video lessons.

4. **🤖 Gemini AI Farming Assistant:**
   - 24/7 dedicated agronomic chatbot powered by Google Gemini.
   - Pre-configured with 6 quick-access suggested questions covering foot rot, soil, harvesting, drying, and propagation.

5. **📜 Scan History & Reports:**
   - Lifetime audit log powered by SQLite (`data/history.db`) with 17 verified historical scans preserved.
   - KPI metrics, keyword search, media/status filtering, and single-click **Master CSV Export**.
   - Re-download individual PDF field reports and CSV data tables for any saved scan.

6. **ℹ️ About Project:**
   - Dedicated documentation page covering Problem Statement, YOLO26 Nano model specifications, System Architecture diagram, Technology Stack breakdown, and Future Scope (agricultural drone surveys, edge AI hardware).

---

## 🎨 Color Palette & Design System
- **Primary:** `#174D32` (Deep Forest Green)
- **Secondary:** `#3D8B50` (Leaf Green)
- **Accent:** `#E8B54A` (Warm Golden Amber)
- **Background:** ` #000000' (Pure Black)
- **Text:** `#202923` (Charcoal Slate)
- **Matured Bounding Box:** `#2ECC71` / `#3D8B50` (Vibrant Green)
- **Immatured Bounding Box:** `#E8B54A` / `#F39C12` (Amber)

---

## 🗂️ Project Directory Structure
```text
project/
├── app.py                      # Main Streamlit application & sidebar navigation controller
├── requirements.txt            # Python dependencies
├── .env                        # Local environment credentials (API keys)
├── .env.example                # Example configuration template
├── README.md                   # Full documentation & execution instructions
├── test_full_suite.py          # Automated 6-phase test suite
│
├── modules/                    # Modular backend services
│   ├── roboflow_service.py     # Genuine Roboflow YOLO26 Nano inference engine
│   ├── image_detection.py      # Image detection coordinator
│   ├── image_processing.py     # Coordinate mapping, bounding boxes & Matplotlib charts
│   ├── video_detection.py      # OpenCV video frame extraction & temporal analysis
│   ├── gemini_assistant.py     # Google Gemini API pepper farming chatbot
│   ├── report_generator.py     # ReportLab PDF report & Pandas CSV generator
│   └── history_manager.py      # SQLite database manager for field logs
│
├── pages_custom/               # Dedicated page modules
│   ├── home_page.py            # Home dashboard, status badges & farmer guide
│   ├── detect_page.py          # Unified detection: Image & Video tabs
│   ├── history_page.py         # Searchable SQLite inspection history & exports
│   ├── guide_page.py           # Unified guide: 21 chapters, 7 methods & propagation
│   ├── cultivation_guide_page.py # Agronomic datasets for chapters, methods & propagation
│   ├── assistant_page.py       # Gemini AI agricultural chatbot interface
│   └── about_page.py           # Final-year project technical documentation
│
├── assets/
│   ├── images/                 # Plantation photographs, hero banners & method cards
│   │   ├── guide/              # Chapter photographs
│   │   ├── methods/            # Growing methods photographs
│   │   └── propagation/        # Nursery propagation photographs
│   └── styles/
│       └── main.css            # Custom responsive CSS design system
│
├── data/
│   └── history.db              # Local SQLite database (17 scans preserved)
│
├── sample_images/              # Verified sample pepper spike photos & test video
│
└── reports/                    # Exported PDF diagnostic field reports
```

---

## 🚀 Windows PowerShell Quickstart

### Step 1: Open PowerShell in the Project Folder
```powershell
cd "d:\7th sem\Antipepper\project"
```

### Step 2: Verify Python Environment
Ensure Python 3.10+ is installed:
```powershell
python --version
```

### Step 3: Install Required Dependencies
```powershell
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
Copy `.env.example` to `.env` and fill in your API credentials:
```powershell
cp .env.example .env
```
Inside `.env`:
```env
ROBOFLOW_API_KEY=your_roboflow_api_key_here
ROBOFLOW_WORKSPACE=chaya-shetty
ROBOFLOW_PROJECT=project-shhni
ROBOFLOW_VERSION=3
ROBOFLOW_WORKFLOW_ID=project-shhni-3-yolo26n-t1-vproject-shhni-3-yolo26n-t1-logic

GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.5-flash
```

### Step 5: Run Automated Test Suite
Verify that all 6 system phases pass without error:
```powershell
python test_full_suite.py
```

### Step 6: Launch the Streamlit Web Application
```powershell
python -m streamlit run app.py --server.port 8501
```

Open your browser and navigate to:
👉 **`http://localhost:8501`**

---

## 🎓 Academic Evaluation & Model Verification
- **Model Architecture:** YOLO26 Nano
- **Deployment Platform:** Roboflow Hosted Inference GPU Server (TensorRT fp16)
- **Target Classes:** `matured` (commercial harvest stage), `immatured` (unripe)
- **Authenticity Assurance:** Direct network inference against `https://detect.roboflow.com/project-shhni/3` returning genuine bounding boxes and confidence scores.
