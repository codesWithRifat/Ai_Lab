# Create a tuple of student records (name, age, grade) and sort by grade.
students = (
    ("Shermin", 20, "B"),
    ("Taposh", 19, "A"),
    ("Shuvo", 21, "C"),
    ("Milon", 20, "B"),
    ("Rifat", 22, "A")
)
studentList = list(students)
n = len(studentList)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if studentList[j][2] > studentList[j + 1][2]:
            studentList[j], studentList[j + 1] = studentList[j + 1], studentList[j]

result = tuple(studentList)
print(result)
