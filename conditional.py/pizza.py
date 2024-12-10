print("welcome to domato")
size=input("what size pizza do you want ?S,M or L")
add_pepparoni=input("Do you want pepperoni?Y or N)? ")
extra_cheese=input("do you want extra cheese ?Y or N")
if size == "S":
    pay=15
    print(f"small size pizza costs ${pay}")
elif size == "M":
    pay=20
    print(f"medium size pizza costs ${pay}")
elif size == "L":
    pay=25
    print(f"large size pizza costs ${pay}")
if add_pepparoni == "Y": 
     if size=="S":
         pay+=2
         print(f"total payment for small pizza: ${pay}")
     if size=="M"or size=="L":
         pay+=3
         print(f"total payment f: ${pay}")
# if add_pepparoni == "N":
#     print (f"total payment ${pay}")

if extra_cheese=="Y":
    if size=="S" or size=="M"or size=="L":
        pay+=1
        print("with extra cheese it costs $",pay)




