import cv2
from utils import load_model, draw_boxes

# Load the trained YOLO model
model = load_model("models/best.pt")

# Start webcam capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform inference
    results = model(frame)

    # Draw bounding boxes
    frame = draw_boxes(frame, results)

    # Display the frame
    cv2.imshow("PPE Detection", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
