# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:55:27 2026

@author: ANVAR
"""

# avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']

# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else: 
#         print(avto.title())
        
# ism = 'Ali'

# ism.lower()  == 'ali'        

# ism = input('Ismingiz nima?\n>>>')
# if ism.lower() != 'ali':
#     print(f"Uzr, {ism.title()} biz Alini kutyapmiz.")
# else: 
#     print("Salom, Ali")    

# javob = float(input("12x6 nechiga teng?>>>"))
# if javob != 72:
#     print("Javob xato")

# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh >= 18:
#     print("Xush kelibsiz!")
# else: 
#     print("Kirish mumkun emas!")

# login = input("Yangi login tanlang:")
# if len(login) <= 5:
#     print("Login 5 harfdan ko'proq bo'lishi shart!")

# yil = int(input("Tug'ulgan yilingizni kiriting:"))
# if 2026 - yil < 18:
#     print(f"Yoshingiz {2026 - yil} da ekan.")
#     print("Kirish mumkun emas!") 
# else:
#     print("Xush kelibsiz!")        

# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh > 65: print("Siz COVID-19 risk guruhida ekansiz")

# x, y = 50, 40
# print("x>y") if x>y else print("x<y")


# avtolar = ['audi','bmw','volvo','kia','hyundai']

# for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
#     if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
#         print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
#     else: # aks holda ... 
#         print(avto.title()) # avto nomini faqat birinchi harfini katta bilann yoz.
        
# ism = 'Ali'
# ism.lower() == 'ali'    

# AMALIYOT
# 1 Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing,
#  ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. 
# GM uchun ikkala harfni katta qiling.    
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] 
# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else:
#         print(car.title())
        
# 2 Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] 
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())
        

# 3 Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz,
#  Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring.
#  Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.   
# ism = input("login kiriting:\n>>>")
# if ism.lower() == 'shuhrat':
#     print("Hush kelibsiz Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {ism}! ")    
    
# 4 Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga 
# teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.    
# son_1 = int(input("Birinchi sonni kiriting: "))
# son_2 = int(input("Ikkinchi sonni kiriting: "))
# if son_1 == son_2:
#     print("Sonlar teng")
    
# 5 Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa 
# konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.     
# son = int(input("Istalgan son kiriting: "))
# if son < 0:
#     print("Manfiy son!")
# else:
#     print("Musbat son!")
    

# 6 Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa
#  uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa,
#  "Musbat son kiriting" degan xabarni chiqaring.     
son = int(input("Son kiriting: "))
if son >= 0:
    print(f"{son} soninig ildizi {son ** 0.5} teng")
else:
    print("Musbat son kiriting!")    

     

        

