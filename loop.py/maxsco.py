student_score=input("List of student score").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)
score=0
for max in student_score:
   if  max>score:
       score=max
print("the maximum score is: " ,score)

    