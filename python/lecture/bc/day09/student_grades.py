student_grades = {
    "Alice": 89,
    "Bob": 72,
    "Charlie": 85,
    "David": 91,
    "Eve": 82
}

for student in student_grades:
    if student_grades[student] > 90:
        print(f"{student} has an A")
    elif student_grades[student] > 80:
        print(f"{student} has a B")
    elif student_grades[student] > 70:
        print(f"{student} has a C")
    elif student_grades[student] > 60:
        print(f"{student} has a D")
    else:
        print(f"{student} has an F")
