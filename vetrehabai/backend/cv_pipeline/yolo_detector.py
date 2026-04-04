from ultralytics import YOLO


class YOLODetector:
    def __init__(self):
        self.model = YOLO("yolo11n.pt")
    
    def detect(self, frame):
        return self.model(frame)
    
