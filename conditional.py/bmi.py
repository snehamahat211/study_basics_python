height=float(input("enter the height of your."))
weight=float(input("enter the weight of yours."))
bmi=round(weight/(height*height))
print(bmi)
if bmi<=18.5:
    print(f"your bmi is {bmi},you are underweight")
elif 25>=bmi>=18.5:
    print(f"your bmi is {bmi},you are normal")
elif(25<=bmi<=30):
    print(f"your bmi is {bmi},you are overweight")
elif(30<=bmi<=35):
    print(f"your bmi is {bmi},you are obuse")
else:
    print(f"your bmi is {bmi},you are clinically obuse")