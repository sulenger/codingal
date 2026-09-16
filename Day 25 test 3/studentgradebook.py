students = {"John": 85, "Max": 92, "Marcus": 78, "Mike": 95, "Jake": 89}

total = sum(students.values())
average = total/ len(students)

top_scorer = max(students,key=students.get)

print("Student Grades:")
print(students)

print("Average:", average)
print("Top Scorer:", top_scorer)
print("Top Grade:",students[top_scorer])