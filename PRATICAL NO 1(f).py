students = {
    "Amit": 78,
    "Sara": 92,
    "Ravi": 85,
    "Neha": 88,
    "Karan": 75
}

print("Student Details:")
for name, marks in students.items():
    print(name, ":", marks)

total_marks = sum(students.values())
average = total_marks / len(students)

print("\nClass Average Marks:", average)

top_student = max(students, key=students.get)
top_marks = students[top_student]

print("\nTop Scorer:")
print(top_student, "with", top_marks, "marks")
