first = input("Enter your first number: ")
second = input("Enter your second number: ")
third = input("Enter your third number: ")
if first > second > third:
    print(f"sonlarning kattasi {first}\n Eng kichigi {third}")
elif first > third > second:
    print(f"sonlarning kattasi {first} \n kichigi {second}")
elif second > first > third:
    print(f"sonlarning kattasi {second} \n kichigi {third}")
elif second > third > first:
    print(f"sonlarning kattasi {second} \n kichigi {first}")    
elif third > first > second:
    print(f"sonlarning kattasi {third} \n kichigi {second}")    