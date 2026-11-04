import mediapipe as mp
import cv2


class PoseTracker:
    def __init__(self):
        self.pose = mp.solutions.pose.Pose()
    
    def track(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return self.pose.process(rgb_frame)