import cv2
from ultralytics import YOLO

model = YOLO('yolov8s.pt')

cap = cv2.VideoCapture(0)  

if not cap.isOpened():
    print("Error: Webcam not accessible.")
    exit()

cv2.namedWindow('YOLOv8 Detection', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('YOLOv8 Detection', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to grab frame.")
        break

    results = model(frame)
    
    annotated_frame = results[0].plot()
    
    cv2.imshow('YOLOv8 Detection', annotated_frame)

    if cv2.waitKey(1) & 0xFF == 13:
        break

cap.release()
cv2.destroyAllWindows()
