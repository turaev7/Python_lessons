
# def kopaytmasi(a, b, c, d):
#     return a*b*c*d
# print(kopaytmasi(2,3,4,3))

# import math
# def kopaytma(*sonlar):
#     return math.prod(sonlar)
# print(kopaytma(2,3,4,3))

def aksessuarlar(**data):
    return data

print(aksessuarlar(Model = "Iphone_14", Yil = 2022, Kompaniya = "Apple ", Manzi = "California USA ", Narxi = "$1300 ", Kamera_soni = " 3 ta ", Ekran_dyumi = "100 mpx"))