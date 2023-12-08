import cv2
import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', path='/home/matheus/Projects/Processamento_de_imagens/yolov5/runs/train/wheights/best.pt')  
model.conf = 0.25  
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break
    
    results = model(frame)

    for det in results.xyxy[0]:  
        x1, y1, x2, y2, conf, cls = det  
        label = f'{int(cls)} {conf:.2f}'
        color = (0, 0, 255) if cls == 0 else (0, 255, 0)  # Red for 'person', green for 'person-like'
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)  
        cv2.putText(frame, label, (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)  

    cv2.imshow('YOLOv5 Real-Time Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()