year=int(input("which year do you want to check?"))
leap1=(year%4)
print(leap1)
if year% 4==0 :
    if year%100==0 :
        if year%400==0:
            print("leap year")
        else:
            print("not leap year")
    else :
        print(" leap year")
else:
    print(" not leap year")


