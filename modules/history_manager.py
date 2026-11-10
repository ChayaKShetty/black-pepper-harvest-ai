"""
History Manager Module for Pepper Harvest AI
Manages persistent local SQLite storage for all image and video harvest readiness analyses.
"""

import sqlite3
import json
import os
from datetime import datetime
from typing import List, Dict, Any, Optional

DB_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
DB_PATH = os.path.join(DB_DIR, "history.db")


def get_db_connection() -> sqlite3.Connection:
    """Creates directory if needed and returns SQLite connection."""
    os.makedirs(DB_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initializes SQLite database schema."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analysis_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            filename TEXT NOT NULL,
            media_type TEXT NOT NULL,
            total_detections INTEGER NOT NULL,
            matured_count INTEGER NOT NULL,
            immatured_count INTEGER NOT NULL,
            maturity_pct REAL NOT NULL,
            status TEXT NOT NULL,
            recommendation TEXT,
            avg_confidence REAL,
            details_json TEXT,
            annotated_image_path TEXT
        )
    """)
    conn.commit()
    conn.close()


def add_history_entry(
    filename: str,
    media_type: str,
    total_detections: int,
    matured_count: int,
    immatured_count: int,
    maturity_pct: float,
    status: str,
    recommendation: str = "",
    avg_confidence: float = 0.0,
    details: Optional[List[Dict[str, Any]]] = None,
    annotated_image_path: str = "",
) -> int:
    """Inserts a new analysis record into the database."""
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    timestamp_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    details_str = json.dumps(details) if details is not None else "[]"

    cursor.execute("""
        INSERT INTO analysis_history (
            timestamp, filename, media_type, total_detections,
            matured_count, immatured_count, maturity_pct, status,
            recommendation, avg_confidence, details_json, annotated_image_path
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        timestamp_str,
        filename,
        media_type,
        int(total_detections),
        int(matured_count),
        int(immatured_count),
        float(maturity_pct),
        status,
        recommendation,
        float(avg_confidence),
        details_str,
        annotated_image_path,
    ))

    conn.commit()
    inserted_id = cursor.lastrowid
    conn.close()
    return inserted_id


def get_all_history() -> List[Dict[str, Any]]:
    """Retrieves all analysis history ordered by newest first."""
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM analysis_history ORDER BY id DESC")
    rows = cursor.fetchall()
    results = [dict(row) for row in rows]
    conn.close()
    return results


def filter_history(
    search_query: str = "",
    media_type_filter: str = "All",
    status_filter: str = "All",
) -> List[Dict[str, Any]]:
    """Filters records by filename keyword, media type, and status."""
    all_records = get_all_history()
    filtered = []

    q = search_query.strip().lower()

    for r in all_records:
        # Match media type
        if media_type_filter != "All" and r["media_type"].lower() != media_type_filter.lower():
            continue

        # Match status
        if status_filter != "All" and status_filter.lower() not in r["status"].lower():
            continue

        # Match keyword in filename or recommendation
        if q:
            match_filename = q in r["filename"].lower()
            match_status = q in r["status"].lower()
            match_recom = q in (r["recommendation"] or "").lower()
            if not (match_filename or match_status or match_recom):
                continue

        filtered.append(r)

    return filtered


def delete_history_entry(entry_id: int) -> bool:
    """Deletes a specific history record by ID."""
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM analysis_history WHERE id = ?", (entry_id,))
    conn.commit()
    deleted = cursor.rowcount > 0
    conn.close()
    return deleted


def clear_all_history() -> bool:
    """Clears all records in analysis_history table."""
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM analysis_history")
    conn.commit()
    conn.close()
    return True

