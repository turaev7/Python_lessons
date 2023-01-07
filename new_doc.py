first = input("Enter your first number: ")
second = input("Enter your second number: ")
third = input("Enter your third number: ")
if first > second > third:
    print(f"sonlarning kattasi {first}\n Eng kichigi {third}")
    print("o'rta arifmetigi: ", float(first + second + third), "/3")
elif first > third > second:
    print(f"sonlarning kattasi {first} \n kichigi {second}")
    print("o'rta arifmetigi: ", float(first + second + third), "/3")
elif second > first > third:
    print(f"sonlarning kattasi {second} \n kichigi {third}")
    print("o'rta arifmetigi: ", float(first + second + third), "/3")
elif second > third > first:
    print(f"sonlarning kattasi {second} \n kichigi {first}")
    print("o'rta arifmetigi: ", float(first + second + third), "/3")    
elif third > first > second:
    print(f"sonlarning kattasi {third} \n kichigi {second}")
    print("o'rta arifmetigi: ", float(first + second + third), "/3") 
elif third > second > first:
    print(f"sonlarning kattasi {third} \n kichigi {first}")  
    print("o'rta arifmetigi: ", float(first + second + third), "/3")     
 
