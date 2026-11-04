from cv_pipeline.exercise_analyzer import ExerciseAnalyzer

analyzer = ExerciseAnalyzer()

# (name, a, b, c, expected angle)
cases = [
    ("right angle", (1, 0), (0, 0), (0, 1), 90),
    ("straight joint", (1, 0), (0, 0), (-1, 0), 180),
    ("fully folded", (1, 0), (0, 0), (2, 0), 0),
    ("the bug", (-1, -1), (0, 0), (-1, 1), 90),
    ("negative difference", (0, 1), (0, 0), (1, 0), 90),
]

for name, a, b, c, expected in cases:
    result = analyzer.calculate_angle(a, b, c)
    status = "PASS" if abs(result - expected) < 0.001 else "FAIL"
    print(f"{status}  {name}: got {result:.1f}, expected {expected}")
