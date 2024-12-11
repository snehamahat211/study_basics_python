student_heights=input("List of student heights").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
total=0
for sum in student_heights:
   total=total+sum
print(total)
divide=0
for divide in student_heights:
    divide+=1
average_height=total/divide
print(average_height)
