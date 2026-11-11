from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    name, score = "", 0
    for student in scores:
        student_name, student_score = student
        if student_score > score:
            name, score = student
    return name


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
