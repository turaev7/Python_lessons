

# def avto_info(kompaniya, model, rangi, yili, narxi):
#     avto = {
#         'kompaniya':kompaniya,
#         'model':model,
#         'rangi':rangi,
#         'yili':yili,
#         'narxi':narxi
#     }
#     return avto

# print("Avtomobillar ro'yxatini tuzish : ")
# avtolar = []
# while True:
#     print("Avtomobillar ma'lumotlarini kiriting : ")
#     kompaniya = input("Kompaniya nomi = ")
#     model = input("Modelni kiriting = ")
#     rangi = input("Rangini kiriting = ")
#     narxi = input("Narxini kiriting = ")
#     yili = input("Yilini kiriting = ")
#     avtolar.append(avto_info(kompaniya,model,rangi,narxi,yili))

#     break

# print("Barcha ma'lumotlar : \n")
# print(f"Malumot kompaniya - {kompaniya} \n Avto modeli - {model} \n Avto rangi - {rangi} \n Avto narxi - {narxi} \n Avto yili - {yili}")









# def car_info(company, model, color, release_date, price):
#     auto = {
#         'company_name' : company,
#         'model' : model,
#         'color': color,
#         'release year': release_date,
#         'cost': price,
#     }
#     return auto

# print("List of automobiles: ") 
# cars = []
# while True:
#     print("Enter your car's info: ")
#     company = input("A name of the company: ")
#     model = input("A model of the car: ")
#     color = input("A color of the car: ")
#     release_date = input("A date the car has been released: ")
#     price = input("How much is your car costs? ")
#     cars.append(car_info(company,model,color, release_date, price))

#     break

# print(f"The company of the car: {company} \nThe model of the car: {model} \nThe color of the car: {color} \nThe released year of the car: {release_date} \nThe price of the car: {price}")


def talaba(ism, familiya, yosh, kurs, institut, joy):
     tala = {'ism': ism,
     'familya': familiya,
     'yosh': yosh,
     'kurs': kurs,
     'institut': institut,
     'joy': joy}
     return tala

print("Talaba haqida shaxsiy ma'lumotlar: ")
malumotlar = []
while True:
    print("Talaba ma'lumotlarini kiriting: ")
    ism = input("Talabaning ismi: ")
    familiya = input("Talabaning familiyasi: ")
    yosh = input("Talabaning yoshi: ")
    kurs = input("Nechanchi kursda uqiydi: ")
    institut = input("Qaysi intitut: ")
    joy = input("Turar joy manzili: ")
    malumotlar.append(talaba(ism, familiya, yosh, kurs, institut, joy))

    javob = input("Boshqa talaba haqida ma'lumot kirgizasizmi? Y/N : ")
    if javob == "N":
        break

print("O'quvchi haqida toliq malumot!  \n")
print(f"Talabaning ismi: {ism} \nFamiliyasi: {familiya} \nYoshi: {yosh} \nKursi : {kurs} \nInstituti: {institut} \nTurar joy manzili: {joy}")