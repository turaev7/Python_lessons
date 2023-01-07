# li = input("What is your Listening score?: ")
# r = input("What is your Reading score?: ")
# s = input("What is your Speaking score?: ")
# w = input("What is your Writing score?: ")
# overall = float(print((li + r + s + w) / 4))

li = float(input("What is your Listening score?: "))
r = float(input("What is your Reading score?: "))
s = float(input("What is your Speaking score?: "))
w = float(input("What is your Writing score?: "))
overall = (li + r + s + w) / 4
print(round(overall))
if   1<overall < 4:
    print("You are B1")
elif 4.5 >= overall <= 6:
    print("You are B2")  
else:
    print("You are geniuos")        