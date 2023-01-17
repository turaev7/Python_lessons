# OOP bu obektga yo'naltrilgan dasturlash yunalishi bolib chiziqli dasturlashdan farqli o'laroq turli vazifalar obektlar va funksiyalar bn ixtiyoriy ravishda ishlaydigan dasturlash yo'nalishidir

#Ob'ekt - bu malum bir fuhnksiyalarni o'z ichiga olgan ko'rinish
#Klass - shu ob'ektlar tuzilmasidan hosil bo'lgan jamlanma
# Ob'ektni 2 ta turi bor :
# hususiyati - uning ichki tuzilishi va ko'rinishi bo'lsa 
# ob'ekt methodi - u bajaroladigan qobiliyat va hususiyat'

#Klass ya'ni sinf bu ob'ektlar bilan ishlovchi qolipdir
# Avtomobil bilan class yaratilganda misol uchun avtomobil deb nomlangan klassdagi obekt husisiyatlari modef narxi va rangi,methodi esa o'chishi yonishi tezlashishi va haraktga doir bajarilgan vazifalari

#Classlar yaratish undan funksiya qabul qilish, ularning umumiy ko;rinishi - INKAPSULATSIYA deyiladi
#ABSTRAKSIYA 

# __VORISLIK__
#Super class bu - Asosiy vazifani bajarib husiusiyat va method orqali boshqa class bn boglanadigan class turkumidir

#Voris class esa super classdan hususiyat va metod meros qabul qilgan holda uning amallarini bajaradi

# _Afzalliklari_
# -Parallel dasturlash – bir loyihaning turli qismlari bir vaqtda yaratilishi mumkin
# -Vorislik tamoyili klasslardan qayta foydanalish imkonini beradi
# -Polimorfizm tamoyili klasslarni moslashuvchan qiladi
# -Klasslardan boshqa dastur va loyihalarda qayta-qayta foydalanish mumkin 
# _Kamchiliklari_
# -Dasturlashga yangi qadam qo’yganlar uchun biroz tushunarsiz
 
# -Har doim ham samarali emas
# -Ba’zida dasturimizni haddan tashqari murakkablashtirib yuborishi mumkin


# class Talaba:
#     def __init__(self, ism, familiya, *malumotlar):
#         self.ism = ism
#         self.familiya = familiya
#         self.malumotlar = malumotlar

# talaba1 = Talaba("Abdulla", "Abduhoshimov")
# #print(talaba1.ism)
# talaba2 = Talaba("Doniyor", "Akromov", "Qarshi")
# print(talaba2.ism)
# print(talaba2.familiya)
# print(talaba2.malumotlar)


# class web_user:
#     def __init__(self, name, surname, email, *other):
#         self.name = name
#         self.surname = surname
#         self.email = email
#         self.other = other

#     # def get_info(self):
#     #     return f"Your name is {self.name} {self.surname} with main email of {self.email}"
    
# user1 = web_user("Axad", "Bahodirov", "Abahodirov7@gmail.com", "Qarshi shahar")
# print(user1)

# class books:
#     def __init__(self, name, author, date, price):
#         self.name = name
#         self.author = author
#         self.date = date
#         self.price = price
        
#     def __repr__(self):
#          return f"{self.name} was written by {self.author} in {self.date}, you can buy it for ${self.price}"

   

# book1 = books("How to win friends and influence people", "Dale Carnegi", input("When it was written?: "), input("How much is it in your city?: "))
# print(book1)





#masala_1

class Ishchilar:
    num_ishchilar = 0
    def __init__(self, ishchi_fio, oylik, stavka, lavozim):
        self.fio = ishchi_fio
        self.oylik = oylik
        self.stavka = stavka
        self.lavozim = lavozim
        Ishchilar.num_ishchilar += 1
    
    def __repr__(self):
        return f"{self.fio}, {self.stavka} stavka ish bilan {self.lavozim} lavozimida ishlaydi va maoshi ${self.oylik}"

    @classmethod
    def get_num_ishchilar(cls):
        return cls.num_ishchilar

ishchi1 = Ishchilar("Sardor Umirzoqov", 4000, 1, "Rahbar")
print(ishchi1)
print(Ishchilar.get_num_ishchilar())

#masala_2
# Qiymat deb nomlangan class yaratilsin va unga 3ta dunder metodi (ya'ni - init , str , add) funksiya metodlari orqali ishlatilsin, shunday algoritm tuzilsinki, a1 = Qiymat(1,10) a2 = Qiymat(5,10) Natija esa a1 va a2 elementlarini yig'indisini topsin. Masalan javob: Qiymat(6,20) qaytsin
# class Qiymat:
#     def __init__(self, a1, a2):
#         self.a = a1
#         self.b = a2
        
#     def __str__(self):
#         return self.a, self.b

#     def __add__(self):
#         print(f"{self.a[0]} + {self.b[0]}")

# Qiymat((5, 10), (1, 10))