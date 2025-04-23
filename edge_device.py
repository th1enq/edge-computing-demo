import cv2
import requests
import torch

# Load YOLOv5 model from torch.hub
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # human detection
    results = model(frame)
    detections = results.pandas().xyxy[0]  # bounding boxes

    # draw bounding boxes
    for _, row in detections.iterrows():
        if row['name'] == 'person' and row['confidence'] > 0.5:
            x1, y1, x2, y2 = map(int, [row['xmin'], row['ymin'], row['xmax'], row['ymax']])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)

            # send data to server
            payload = {
                "label": "person",
                "confidence": float(row['confidence']),
                "bbox": [x1, y1, x2, y2]
            }
            try:
                requests.post("http://localhost:5000/receive", json=payload)
            except:
                pass  

    cv2.imshow("Edge Detection", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
