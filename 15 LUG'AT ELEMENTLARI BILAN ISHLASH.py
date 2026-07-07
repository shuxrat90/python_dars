# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 18:05:55 2026

@author: ANVAR
"""

talaba_0 = {
    'ism': 'alijon',
    'familiya': 'shamshiyev',
    'yosh': 22,
    'fakultet': 'matematika',
    'kurs': 4,
        }

# print(talaba_0.items())  kalit soz qiymatni ko'rish

# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat} \n")


telefonlar = {
    'ali': 'iphone x',
    'vali': 'galaxy s9',
    'olim': 'mi 10 pro',
    'orif': 'nokia 3310',
    }

# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")
    

# .keys()
mahsulotlar = {
    'olma': 10000,
    'anor': 20000,
    'uzum': 40000,
    'anjir': 25000,
    'shaftoli': 30000
    }    

# print(mahslotlar.keys())

# print('Do\'kondagi mahsotlar:')
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())
    
# print('Do\'kondagi mahusotlar:')
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())

# bozorlik = ['anor', 'uzum', 'non', 'baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
        
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos dokonga {buyum} ham olib keling")


# print("Do'konimizdagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())      


# values()
# print(telefonlar.values()) 

# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in telefonlar.values():
#     print(tel)


telefonlar = {
    'ali': 'iphone x',
    'vali': 'galaxy s9',
    'olim': 'mi 10 pro',
    'orif': 'nokia 3310',
    'hamida': 'galaxy s9',
    'maryam': 'huawei p30',
    'tohir': 'iphone x',
    'umar': 'iphone x'
    }

# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in telefonlar.values():
#     print(tel)
    
    
# set
# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in set(telefonlar.values()):
#     print(tel)


toys = {"ball", "car", "lamp", "ball", "bear", 'car'}   


# AMALIYOT
# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing.
#  Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo 
#  ketma-ketligida chiroyli qilib konsolga chiqaring.  
pay_izohli_lugat = {'boolean':'mantiqiy qiymat',
                    'float': 'o\'nlik son',
                    'for': 'biror amalni qayta-qayta bajarish tsikli',
                    'if': 'shartlarni bajarish operatori',
                    'else': 'aks holda',
                    'integer': 'butun son',
                    'string': 'matn',
                    'list': 'ro\'yhat',
                    'dictyanary': 'kalit so\'z va qiymat',
                    'set': 'filtr qoyish'
                    }
 
# for kalit, qiymat in sorted(pay_izohli_lugat.items()):
    # print(f"{kalit.title()} - {qiymat.capitalize()}")
    
    

# Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni,
#  keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.
davlatlar_poytaxtlar = {'aqsh': 'washington d.c.',
             'italiya': 'rim',
             'malayziya': 'kuala - lumpur',
             'o\'zbekiston': 'toshkent',
             "qirg'iziston": 'bishkek',
             "qozog'iston": 'nursulton',
             'rossiya': 'moskva',
             'singapur': 'sungapur',
             'tojikiston': 'dushanbe',
             "avg'oniston": 'qobul'
             }    
# print("Dunyo davlatlari:")
# for d in sorted(davlatlar_poytaxtlar.keys()):
#     print((d.upper()))
    
# print("Davlatlarning poytaxtlari:") 
# for p in sorted(davlatlar_poytaxtlar.values()):
#     print(p.title())
    
    
# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini
#  konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, 
#  "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.    
# davlat = input("Qaysi davlatning poytaxtini bilishni istaysiz? : ").lower()
# if davlat in davlatlar_poytaxtlar:  
#     if davlat == 'aqsh':
#         print(f"{davlat.upper()}ning poytaxti {davlatlar_poytaxtlar[davlat].title()} \
# shahri  ")
#     elif davlat != 'aqsh':    
#         print(f"{davlat.capitalize()}ning poytaxti \
# {davlatlar_poytaxtlar[davlat].title()} shahri")
# else:
#     print("Kechirasiz, bizda bu haqida ma'lumot yoq")


# country = input("Qaysi davlatning poytaxtini bilishni istaysiz?:").lower()
# capital = davlatlar_poytaxtlar.get(country)
# if capital == None:
#     print("Kechirasiz, bizda bu haqida ma'lumot yo'q")
# else:
#     print(f"{country.upper()}ning poytaxti {capital.title()} shahri")

    
    
# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting).
#  Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan 
#  taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, 
#  aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
restaran = {'osh': 20000,
            'non': 4000,
            'salat': 5000,
            'shashlik': 10000,
            'tabaka': 40000,
            'somsa': 10000,
            'norin': 40000,
            'nohot shorak': 22000,
            'shorva': 15000,
            'choy': 4000
            }
# print("3 ta taom buyurtma bering.")
# print()
# taom_1 = input("1-taom: ").lower()
# print()
# taom_2 = input("2-taom: ").lower()
# print()
# taom_3 = input("3-taom: ").lower()
# if taom_1 in restaran:
#     print(f"{taom_1.title()} {restaran[taom_1]} so'm")
# else:
#     print(f"Kechirasiz, bizda {taom_1} yo'q.")    
    
# if taom_2 in restaran:
#     print(f"{taom_2.title()} {restaran[taom_2]} so'm")
# else:
#     print(f"Kechirasiz, bizda {taom_2} yo'q.")
    
# if taom_3 in restaran:
#     print(f"{taom_3.title()} {restaran[taom_3]} so'm")
# else:
#     print(f"Kechirasiz, bizda {taom_3} yo'q.") 

   
print("3 ta taom buyurtma bering.")
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())

for buyurtma in buyurtmalar:
    if buyurtma in restaran:
        print(f"{buyurtma.title()} {restaran[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")
    

    