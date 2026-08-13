# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 18:32:23 2026

@author: ANVAR
"""

# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# ismlar = []
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"\n{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("\nYana ism qo'shasizmi? (ha/yo'q)")
#     n+=1
#     if takrorlash != 'ha':
#         break
    

# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())    
    


# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("\nDo'stingiz ismini kiriting: ")
#     yosh = input(f"\n{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)
    
#     javob = input("\nYana ma'lumot qoshasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False
        
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda ")   


# cars = ['lacetti', 'nexia', 'toyota', 'nexia', 'auda', 'malibu', 'nexia']
# while 'nexia' in cars:
#     cars.remove('nexia')
# print(cars)          
    

# cars = ['lacetti', 'nexia', 'toyota', 'nexia', 'auda', 'malibu', 'nexia']
# car = 'lacetti'
# while car in cars:
#     cars.remove(car)
# print(cars)         


# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"\n{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = int(baho)
    
    
    

# ismlar = []

# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break    
    
    
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title()) 
    
    
    
# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh) # ism kalit, yosh qiymat
    
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False

# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")    


# cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
# while 'nexia' in cars: # toki nexia cars ro'yxati ichida ekan...
#     cars.remove('nexia') # nexia ni ro'yxatdan olib tashla
# print(cars)


# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho



# AMALIYOT
# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini
#  birma-bir qabul qilib, yangi ro'yxatga joylang.
# print("Buyurtma kiriting: ")
# mahsulotlar = []
# n=1
# while True:
#     savol = f"\n{n}-mahsulot: "
#     mahsulot = input(savol)
#     mahsulotlar.append(mahsulot)
#     takrorlash = input("\nYana ism qo'shasizmi? (ha/yo'q)")
#     n+=1    
#     if takrorlash != 'ha':
#         break
        

# print("Mahsulotlar ro'yxati:")
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())    
    

# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi 
# dastur yozing. Foydalanuvchidan lug'atga bir nechta elementlar 
# (mahsulot va uning narhi) kiritishni so'rang.    
# print("e-bozor uchun mahsulotlar saqlaymiz.")
# mahsulotlar = {}
# ishora = True
# while ishora:
#     mahsulot = input("\nmahsulot kiriting: ")
#     narh = input(f"{mahsulot.title()}ning narhini kiriting: ")
#     mahsulotlar[mahsulot] = int(narh) # ism kalit, yosh qiymat
    
#     javob = input("Yana mahsulot qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False

# for mahsulot, narh in mahsulotlar.items():
#     print(f"\n{mahsulot.title()} {narh} so'm")    
    
    
    
# Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi 
# har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor 
# ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot
# narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni 
# kor'sating.
# bor_mahsulotlar = {'olma': 5000, 'nok': 6500, 'baban': 9000}
# print("e-bozor uchun mahsulotlar saqlaymiz.")

# mahsulotlar = {}
# ishora = True
# while ishora:
#     mahsulot = input("\nmahsulot kiriting: ")
#     if mahsulot in bor_mahsulotlar:
#         print(f"{mahsulot.title()}ning narhi {bor_mahsulotlar[mahsulot]} so'm")
#     else:
#         print("Bizda bu mahsulot yo'q")
        
        
buyurtmalar = ["olma", "anjir", "uzum", "qovun"]
mahsulotlar = {"olma": 20000, "shaftoli": 25000, "tarvuz": 18000, "uzum": 22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")        

    