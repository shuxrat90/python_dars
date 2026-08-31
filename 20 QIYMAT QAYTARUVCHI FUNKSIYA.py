# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 19:03:54 2026

@author: ANVAR
"""

# def toliq_ism_yasa(ism, familiya):
#     """To'liq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     print(toliq_ism)
    
# toliq_ism_yasa('olim', 'olimov')    
    


# def toliq_ism_yasa(ism, familiya):
#     """To'liq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism
    
# talaba = toliq_ism_yasa('olim', 'hakimov')  



# def toliq_ism_yasa(ism, familiya):
#     """To'liq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism
        
# talaba1 = toliq_ism_yasa('olim', 'hakimov')
# talaba2 = toliq_ism_yasa('hakimov', 'olim')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
# print(f"{talaba1} darga kechikib keldi")



# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """To'liq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:   
#         toliq_ism = f"{ism} {familiya}"                
#     return toliq_ism.title()
        
# talaba1 = toliq_ism_yasa('olim', 'hakimov')
# talaba2 = toliq_ism_yasa('hakim', 'olimov', 'abrorovich')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")



# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#                  'model':model,
#                  'rang':rangi,
#                  'korobka':korobka,
#                  'yil':yili,
#                  'narh':narhi}
#     return avto

# avto1 = avto_info('GM', 'Malibu', 'Qora', 'Avtomat', 2018)
# avto2 = avto_info('GM', 'Gentra', 'Oq', 'Mexanika', 2016,15000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"     
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")     



# def oraliq(min, max):
#     sonlar = []
#     while min<max:  
#         sonlar.append(min) 
#         min += 1
#     return sonlar

# print(oraliq(0,10)) 
# print(oraliq(10,21))       


# def oraliq(min, max, oraliq=1):
#     sonlar = []
#     while min<max:  
#         sonlar.append(min) 
#         min += oraliq
         
#     return sonlar

# print(oraliq(0,10)) 
# print(oraliq(10,21,2))     


        
# def avto_info(kompaniya, model, rangi, korobka, yili, narh=None):
#     avto = {'kompaniya':kompaniya,
#                  'model':model,
#                  'rang':rangi,
#                  'korobka':korobka,
#                  'yil':yili,
#                  'narh':narhi}
#     return avto        

# print("Saytimizdagi avtolar o'yhatini shakllantiramiz")
# avtolar = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting:")
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("\nModeli: ")
#     rangi=input("\nRangi: ")
#     korobka=input("\nKorobka: ")
#     yili=input("\nIshlab chiqarilgan yili: ")
#     narhi=input("\nNarhi: ")
    
    
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili))
    
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break

# print("\nSalonimizdagi avtolar: ")
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang'].title()}, {avto['model'].title()}, {korobka} korobka. Narhi: {narh}")            
        
        
 
# def toliq_ism_yasa(ism, familiya):
#     """Toliq isma qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism # qiymat qaytarish uchun return operatorini ishlatamiz    
        

# talaba1 = toliq_ism_yasa('olim','hakimov')
# talaba2 = toliq_ism_yasa('hakim','olimov')

# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")


# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """Toliq isma qaytaruvchi funksiya"""
#     if otasining_ismi: # otasining_ismi mavjudligini tekshiramiz
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()


# talaba1 = toliq_ism_yasa('olim','hakimov') #otasining_ismi kiritilmadi
# talaba2 = toliq_ism_yasa('hakim','olimov','abrorovich')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")


# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto


# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")



# def oraliq(min,max):
#     sonlar = [] # bo'sh ro'yxat
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar


# print(oraliq(0,10))
# print(oraliq(10,21))



# def oraliq(min,max,oraliq=1):
#     sonlar = [] # bo'sh ro'yxat
#     while min<max:
#         sonlar.append(min)
#         min += oraliq
#     return sonlar


# print(oraliq(0,10))
# print(oraliq(10,21,5))


# def avto_info(kompaniya, model, rangi, korobka, yili, narh=None):
#     avto = {'kompaniya':kompaniya,
#                  'model':model,
#                  'rang':rangi,
#                  'korobka':korobka,
#                  'yil':yili,
#                  'narh':narhi}
#     return avto    


# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting",end='')
#     kompaniya=input(" Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
    
#     #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
#     #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
#     # Yana avto qo'shish-qo'shmaslikni so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break
    
# print("Salonimizdagi avtolar")  
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['kompaniya'].title()} {avto['model']} {avto['narh']}")


# AMALIYOT
# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email 
# manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi
#  funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi 
#  argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
# def foyda_info(ism, familiya, t_yil, t_joy, email, telefon):
#     """Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi,
#     email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida 
#     qaytaruvchi funksiya"""
#     foydalanuvchi = {'ism': ism,
#                      'familiya': familiya,
#                      't_yil': t_yil,
#                      't_joy': t_joy,
#                      'email': email,
#                      'telefon': telefon,
#                      'yosh': 2026-t_yil}
#     return foydalanuvchi


# print("Saytimizdagi foydalanuvchi ma'lumotlarini shakllantiramiz.")
# foyda = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting",end='')
#     ism = input(" Ismingiz: ")
#     familiya = input("Familiyangiz: ")
#     t_yil = input("Tug'ulgan yilingiz: ")
#     t_joy = input("Tug'ulgan joyingiz: ")
    
#     email = input("Email manzilingiz: ")
#     telefon = input("Telefoningiz: ")
#     t_yil = int(t_yil)
                                              
#     foyda.append(
#         foyda_info(ism, familiya, t_yil, t_joy, email, telefon)
#         )
        
    
#     javob = input("Yana foydalanuvchi qo'shasizmi? (yes/no): ")
#     if javob=='no':
#         break
    
# print("Foydalanuvchilar")
# for f in foyda:
#     print(
#         f"{f['ism'].title()} {f['familiya'].title()},"
#         f" {f['yosh']} yoshda telefoni: {f['telefon']} "
# )
    
    
    
# Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar
#  degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni
#  konsolga chiqaring.    
# def mijoz_info(ism, familiya, tyil, tjoy, email="", tel=None):
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     mijoz = {
#         "ism": ism,
#         "familiya": familiya,
#         "tyil": tyil,
#         "yoshi": 2020 - tyil,
#         "tjoy": tjoy,
#         "email": email,
#         "telefon": tel,
#     }
#     return mijoz


# print("Mijoz haqida ma'lumotlarni kiriting.")
# mijozlar = []
# while True:
#     ism = input("Ismi: ")
#     familiya = input("Familiyasi: ")
#     tyil = int(input("Tug'ilgan yili: "))
#     tjoy = input("Tug'ilgan joyi: ")
#     email = input("Email: ")
#     telefon = input("Telefon raqami: ")
#     mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
#     javob = input("Davom etasizmi? (ha/yo'q)")
#     if javob != "ha":
#         break

# print("Mijozlar:")
# for mijoz in mijozlar:
#     print(
#         f"{mijoz['ism'].title()} {mijoz['familiya'].title()},"
#         f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}"
#       )



# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
# def eng_katta(son1, son2, son3):
#     return max(son1, son2, son3)


# print(eng_katta(57, 34, 100))


# def kattasi(x, y, z):
#     max = x
#     if y >= max:
#         max = y
#     if z >= max:
#         max = z
#     return max


# print(kattasi(11, 1, 41))
# print(kattasi(99, 100, 81))



# Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini,
#  diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya
#  yozing
# def aylana_info(radius):
#     """Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini,
#     diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya"""
#     pi = 3.14159
#     diametr = 2 * radius
#     perimetr = 2 * pi * radius 
#     yuza = pi * radius ** 2
    
    
#     return {
#         'radius': radius,
#         'diametr': diametr,
#         'perimetr': perimetr,
#         'yuza': yuza
#         }
        
    
# print(aylana_info(5))    



# def aylana_info(radius, pi=3.14159):
#     aylana = {
#         "radius": radius,
#         "diametr": 2 * radius,
#         "perimetr": 2 * radius * pi,
#         "yuza": pi * radius ** 2
#     }
#     return aylana
    
# radius = (int(input("Aylana radiusini kiriting: ")))
# print(aylana_info(radius))
# print(aylana_info(radius)["perimetr"])    
# print("yuza", aylana_info(radius)["yuza"])     



# Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing 
# (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat 
#  sonlar)
# def tub_sonlar_topish(boshlanish, tugash):
#     tub_sonlar = []

#     for son in range(boshlanish, tugash + 1):
#         if son > 1:
#             for i in range(2, son):
#                 if son % i == 0:
#                     break
#             else:
#                 tub_sonlar.append(son)

#     return tub_sonlar


# print(tub_sonlar_topish(1, 20))  



# def tub_sonlar_top(min, max):
#     tub_sonlar = []
#     for n in range(min, max + 1):
#         tub = True
#         if n == 1:
#             tub = False
#         elif n == 2:
#             tub = True
#         else:
#             for x in range(2, n):
#                 if n % x == 0:
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)

#     return tub_sonlar

# print(tub_sonlar_top(1, 100))



# Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi 
# ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing.  Ta’rif:
#     Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan
#     ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had 
#     ko’pincha 1 deb olinadi.  1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
# def fibonacci_sonlar(miqdor):
#     sonlar = []

#     for i in range(miqdor):
#         if i == 0 or i == 1:
#             sonlar.append(1)
#         else:
#             yangi_son = sonlar[-1] + sonlar[-2]
#             sonlar.append(yangi_son)

#     return sonlar


# n = int(input("Nechta Fibonacci soni kerak? "))
# print(fibonacci_sonlar(n))


def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x - 1] + sonlar[x - 2])
    return sonlar


print(fibonacci(12))