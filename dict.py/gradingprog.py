student_scores={
    "harry":81,
    "ron":78,
    "sunita":99,
    "nischay":65,
}
student_grades={}
for student in student_scores:
    score=student_scores[student]
    print(score)
    if score>90:
        student_grades[student]="outstanding" 
        # this goes in student grade list and add elements}
    elif score>80:
        student_grades[student]= "Exceed excellent"
    elif score>70:
        student_grades[student]= "aceptable" 
    elif score>60:
        student_grades[student]="fail"


print(student_grades)