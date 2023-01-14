# funksiya nomi - salom 
# ( ) - funksiya argumenti
# print - funksiyaga tegishli bulgan uzgaruvchi
# def salom():
#     print("Wassup man")
# salom()

# def malumot(ism, sharif):
#     print("Salom hurmatli",ism, sharif)

# malumot("Durbek", "Turaev")   

# def bilol(name, surname, age):
#     print("Hi my name is", name, "My surname is", surname, "and I am ", age, "years old")

# bilol("Aisha", "Shavkatova", "half") 

# def get_even_numbers():
#     for number in range(1, 11):
#         print(number * 2)

# get_even_numbers()


# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")

# salom_ber()
# def salom_ber(ism):
#     """Fodyalanuvchi ismini qabul qilib, 
#         unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
# salom_ber("Durbek")   
# def get_even_numbers():
#     for number in range(1, 11):
#         print(number * 2)

# get_even_numbers()

# Eng katta yigindini topish !!!

# def yigindi(son1, son2, son3):
#     if son1 + son2 > son3:
#         return son1 + son2
#     elif son1 + son3 > son2:
#         return son1+son3
#     else:
#         return son2 + son3
# a=int(input("son1 = "))
# b=int(input("son2 = "))
# c=int(input("son3 = "))
# print(a+b+c-min(a,b,c))

# Eng kichik yigindini topish!!!
# def yigindi(son1, son2, son3):
#     if son1 + son2 > son3:
#         return son1 + son2
#     elif son1 + son3 > son2:
#         return son1+son3
#     else:
#         return son2 + son3
# a=int(input("son1 = "))
# b=int(input("son2 = "))
# c=int(input("son3 = "))
# print(a+b+c-max(a,b,c))

# def uch_xonali_son(bir):
#     return bir
# bir = str(input("son = "))
# print(f"{bir} = {bir[0]}00 + {bir[1]}0 + {bir[2]}")

# def tort_xonali(number):
#     if len(number)== 4:
#         print(f"✅ {number[0]}000 + {number[1]}00 + {number[2]}0 + {number[3]}")
#     elif len(number) < 4:
#         print("Wrong number")  
#     elif len(number) > 4:
#         print("Wrong") 
               
    
# tort_xonali(input("Enter your number: "))        


#Bankdan qarz
def qarz(pul):
    print(pul)
pul = input("Qarz summasini kiriting: ")
foiz = input("Foiz qiymati: ")
