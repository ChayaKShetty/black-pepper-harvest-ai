"""
Image Detection Orchestrator Module for Pepper Harvest AI
Coordinates genuine Roboflow YOLO26 Nano inference, image annotation,
and agronomic maturity calculations.
"""

from typing import Dict, Any, Optional
from PIL import Image
import pandas as pd

from modules.roboflow_service import RoboflowService
from modules.image_processing import (
    annotate_image,
    detections_to_dataframe,
    pil_to_bytes,
)


class ImageDetectionPipeline:
    def __init__(self, service: Optional[RoboflowService] = None):
        self.service = service or RoboflowService()

    def process_image(
        self,
        image_input,
        confidence: float = 0.25,
        overlap: float = 0.45,
    ) -> Dict[str, Any]:
        """
        Executes end-to-end detection on an input image:
        1. Validates configuration and image
        2. Calls genuine Roboflow YOLO26 Nano model
        3. Parses detections and calculates harvest summary
        4. Generates annotated image with color-coded bounding boxes
        5. Builds structured pandas DataFrame
        """
        result = self.service.infer_image(
            image_input=image_input,
            confidence=confidence,
            overlap=overlap,
        )

        if not result.get("success"):
            return {
                "success": False,
                "error": result.get("error", "Unknown inference error"),
                "detections": [],
                "summary": result.get("summary", {}),
                "annotated_image": None,
                "dataframe": pd.DataFrame(),
                "raw_response": result.get("raw_response"),
            }

        detections = result.get("detections", [])
        summary = result.get("summary", {})

        # Load image as PIL for annotation
        if isinstance(image_input, Image.Image):
            pil_img = image_input
        else:
            try:
                pil_img = Image.open(image_input)
            except Exception:
                pil_img = None

        annotated_img = None
        if pil_img is not None:
            annotated_img = annotate_image(pil_img, detections)

        df = detections_to_dataframe(detections)

        return {
            "success": True,
            "error": None,
            "detections": detections,
            "summary": summary,
            "annotated_image": annotated_img,
            "dataframe": df,
            "inference_time": result.get("inference_time", 0.0),
            "model_id": result.get("model_id", "YOLO26 Nano"),
            "raw_response": result.get("raw_response"),
        }


def detect_spikes_in_image(
    image_input,
    confidence: float = 0.25,
    overlap: float = 0.45,
    service: Optional[RoboflowService] = None,
) -> Dict[str, Any]:
    """Convenience function for image detection."""
    pipeline = ImageDetectionPipeline(service=service)
    return pipeline.process_image(image_input, confidence=confidence, overlap=overlap)

