#Ideas - I'd like to use this for a command input method
#.. user sees 5x5 with icons on it. Host the "menu pad" on your phone.

row1=["a","b","c"]
row2=["d","e","f"]
row3=["g","h","i"]

map= [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}\n")

position=input("Type two ints: (50)")

row=int(position[0])
col=int(position[1])


print(map[row][col])