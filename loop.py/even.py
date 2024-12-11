total=0
for even in range(2,101,2):
    total+=even
    # print(even)
print(total)

total=0
for number in range(1,101):
    if number%2==0: 
        total+=number
print(total)