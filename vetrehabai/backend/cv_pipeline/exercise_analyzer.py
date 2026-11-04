import numpy as np

class ExerciseAnalyzer:
    def calculate_angle(self, a, b, c):
        angle = np.degrees(np.arctan2(c[1] - b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0]))
        angle = abs(angle)
        biggest_joint = 180
        if angle > biggest_joint:
            smaller = 360 - angle
            return smaller
        else:
            return angle