number_of_students = int(input())
all_students = {}
for _ in range(number_of_students):
    student, grade = input().split(" ")
    if student not in all_students:
        all_students[student] = []
    all_students[student].append(float(grade))
for student, grades in all_students.items():
    convert_float_to_string = " ".join(map(lambda grade: f"{grade:.2f}", grades))
    average_grade = sum(grades) / len(grades)
    print(f"{student} -> {convert_float_to_string} (avg: {average_grade:.2f})")

