height=int(input("what is the height of the person? \n\n-"))
if height>=120:
    print("congratulations! you can ride our rollercoaster\n")
    age=int(input("please enter the age to get access. \n\n-") )
    if 45>=age>=18:
        total=12
        print("you are adult.please pay $12\n")
    elif age<=12:
        total=5
        print("you are child.please pay $5\n")
    elif 55>=age>=45:
        total=0
        print("you are at your midlife.so,you get free entry")
    else:
        total=7
        print("you are minor.please pay $7 \n")
    photos=input("do you want photoes in rollercoaster? \n\n-")
    if photos=="yes"or photos=="ok":
         if total==12:
            total1=12+3
            print(f"pay total ${total1} ")
         if total==5:
            total2=5+3
            print(f"pay total ${total2}")
         if total==7:
            total3=7+3
            print(f"you pay total ${total3}")
         if total==0:
             total4=+3
             print(f"you pay total ${total4}")
         
         print("Thank you!.you may wait or join.")
    elif photos=="no":
        print(f" your total bill is ${total}")
else:
    print("can't ride")