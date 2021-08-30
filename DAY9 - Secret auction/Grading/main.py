student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}


student_grades = {}

for student in student_scores:
    score = student_scores[student]  # extracting the score (value) from each student in dictionary
    if score > 90:
        student_grades[student] = "Outstanding"
    elif 91 > score > 80:
        student_grades[student] = "Exceeds expectations"
    elif 79 > score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

    # 🚨 Don't change the code below 👇
print(student_grades)

