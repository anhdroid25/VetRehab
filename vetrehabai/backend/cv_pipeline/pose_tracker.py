import mediapipe as mp

class PoseTracker:
    def __init__(self):
        self.pose = mp.solutions.pose.Pose()
    
    def track(self, frame):
        return self.pose.process(frame)