import cv2
import torch
from ultralytics import YOLO

def load_model(model_path="models/best.pt"):
    """Load the trained YOLO model."""
    if not torch.cuda.is_available():
        print("CUDA not available, running on CPU.")
    return YOLO(model_path)

def draw_boxes(frame, results):
    """Draw bounding boxes on the detected PPE objects."""
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0].item()
            label = result.names[box.cls[0].item()]
            text = f"{label}: {conf:.2f}"
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return frame
