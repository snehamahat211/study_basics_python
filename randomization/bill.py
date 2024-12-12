import random
give=input("give me a list of people they are going to pay")
names=give.split(";")
# length=len(names)
# print(length)
# random_choice=random.randint(0, length-1)
# payby=names[random_choice]
# print(f"{payby} will pay the bill")

person=random.choice(names)
print(f"{person} will pay the bill :)")


