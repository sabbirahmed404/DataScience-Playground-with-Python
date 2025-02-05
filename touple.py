students = (
    ("Sabbir", 22, 3.6),
    ("Jiyon", 23, 3.8),
    ("Ishaq", 24, 3.7),
    ("Rakib", 22, 3.5),
    ("Sakib", 23, 3.6)
)

def student_sort(student):
    return student[2]

sorted_students_1 = sorted(students, key=lambda student: student[2])
sorted_students = sorted(students, key=student_sort)

print("sorted_students_1: ", sorted_students_1)
print("sorted_students: ", sorted_students)

