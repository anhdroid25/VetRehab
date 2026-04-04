import numpy as np

class ExerciseAnalyzer:
    def calculate_angle(self, a, b, c):
        angle = np.degrees(np.arctan2(c[1] - b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0]))
        return abs(angle)