# while True:
#     selected_option = input("Please enter the name of the days which are:\n 'Monday'\n'Tuesday'\n'Wensday'\n'Thursday'\n'Friday'\n'Saturday'\n'Sunday'\n select: ")
#     if selected_option == "Monday":
#         print("You selected the 1st day of the week!")
#     elif selected_option == "Tuesday":
#         print("You selected the 2nd day of the week!")
#     elif selected_option == "Wednesday":
#         print("You selected the 3rd day of the week!")
#     elif selected_option == "Thursday":
#         print("You selected the 4th day of the week!")
#     elif selected_option == "Friday":
#         print("You selected the 5th day of the week")
#     elif selected_option == "Saturday":
#         print("You selected the 6th day of the week")
#     elif selected_option == "Sunday":
#         print("You selected the 7th day of the week")
#     else:
#         print("You selected an invalid option.") 

# while True:
#     given_number = input("Inter a number to see its rome form: ")
#     if given_number == "1":
#         print("I")
#     elif given_number == "2":
#         print("II")
#     elif given_number == "3":
#         print("III")
#     elif given_number == "4":
#         print("IV")
#     elif given_number == "5":
#         print("V")
#     elif given_number == "6":
#         print("VI")
#     elif given_number == "7":
#         print("VII")
#     elif given_number == "8":
#         print("VIII")
#     elif given_number == "9":
#         print("IX")
#     elif given_number == "10":
#         print("X")
#     else:
#         print("YOU INTERED AN INVALID OPTION!!!")  

# 1
# number = int(input("Please enter any number: "))
# sum = 0
# for b in range(0, number + 1):
#     sum+=b
# print(sum)

# 2
# a = input("Uchburchakning birinchi tomonini kiriting: ")
# b = input("Uchburchakning ikkinchi tomonini kiritng: ")
# c = input("Uchburchakning uchinchi tomonini kiriting: ")
# if a + b > c or a + c > b and b + c > a:
#     print("You are good to go")
# else:
#     print("You cannot make an triangle!!!")          

# 4
# for i in range(11):
#     print(str(i)*i) 


# number1 = input("Please enter your first number: ")
# number2 = input("Please enter your second number: ")
# while True:
#     if number1 == number2:

#        print("These two numbers are equal !!!")
#        break
#     else:
#             print("These numbers are not equal !!! :)")

# a = input("Please enter a number: ")
# a = int("".join(reversed(str(a))))
# print(a)

hi = input("enter a number : ")
print("".join(reversed(str(hi))))