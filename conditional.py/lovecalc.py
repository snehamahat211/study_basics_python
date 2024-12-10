   #lovecalculator
print("welcome to LOVE CALCULATOR")
name1=input("What is your name?\n\n-")
name2=input("What is your Love name?\n\n")
lowercase=name1.lower() + name2.lower()
count=lowercase.count("t")
print("T=",count)
lowercase=name1.lower()+name2.lower()
count1=lowercase.count("r")
print("R=",count1)
lowercase=name1.lower()+name2.lower()
count2=lowercase.count("u")
print("U=",count2)
lowercase=name1.lower()+name2.lower()
count3=lowercase.count("e")
print("E=",count3)
total=count+count1+count2+count3
print("Total=",total)
"\n \n\n"
lowercase=name1.lower() + name2.lower()
letter=lowercase.count("l")
print("L=",letter)
letter1=lowercase.count("o")
print("O=",letter1)
letter2=lowercase.count("v")
print("V=",letter2)
letter3=lowercase.count("e")
print("E=",letter3)
total1=letter+letter1+letter2+letter3
print("Total=",total1)
lovescore=str(total)+str(total1)
print("your lovescore is:",lovescore) 


if int(lovescore)<=10 or int(lovescore)>=90:
    print(f"your score is {lovescore},you go together like coke and mentos")
if 40<=int(lovescore)<=80:
    print(f"your score is {lovescore},you are alright together")
else:
    print(f"your score is {lovescore}")





