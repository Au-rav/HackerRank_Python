from collections import namedtuple

n = int(input())
rows = input().split()

total_marks = 0
for i in range(n):
    s = namedtuple('student',rows)
    ID, NAME, MARKS, CLASS = input().split()
    student = s(ID,NAME,MARKS,CLASS)
    total_marks = total_marks+int(student.MARKS)

print(str(round(total_marks/n, 2)))