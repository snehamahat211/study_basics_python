row1=["🥹","🙂","🤣"]
row2=["🥹","🙂","🤣"]
row3=["🥹","🙂","🤣"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}\n")
position=input("where do you want to put the tressure")
horizontal =int(position[0])
print(horizontal)
vertical= int(position[1])
selected_row=map[vertical-1]
selected_row[horizontal-1]="XX"
print(f"{row1}\n{row2}\n{row3}\n")

      