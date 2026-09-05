# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 09:36:04 2026

@author: ANVAR
"""

# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"\ntalaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism] = int(baho)
#     return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(baholar)
# print(talabalar)
        
    
    
# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"\ntalaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism] = int(baho)
#     return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar[:])
# print(baholar)
# print(talabalar)    

# talabalar2 = talabalar
# print(talabalar2)
# talabalar2.pop()
# print(talabalar2)
# print(talabalar)




# Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning 
# birinchi harfini katta harfga o'zgatiruvchi funksiya yozing. 
# def katta_harf(ismlar):
#     katta_harflar = []
    
#     for ism in ismlar:
#         katta_harflar.append(ism.title())

#     return katta_harflar



# ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf(ismlar)
# print(ismlar)

# print(katta_harf(ismlar))



# def katta_harf(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i] = matnlar[i].title()


# ismlar = ["ali", "vali", "hasan", "husan"]
# katta_harf(ismlar)
# print(ismlar)

# ismlar2 = ["bobojon", "durusjon"]
# katta_harf(ismlar2)
# print(ismlar2)



# Yuoqirdagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat
#  qaytaradigan qilib o'zgartiring
# def katta_harf(matnlar):
#     katta_harflar = []
    
#     for matn in matnlar:
#         matn = matn.title()
#         katta_harflar.append(matn)                 
        
#     return katta_harflar


# ismlar = ["ali", "vali", "hasan", "husan"]    

# yangi_ismlar = katta_harf(ismlar)

# print("Eski ro'yxat:", ismlar)
# print("Yangi ro'yxat:", ismlar)


# def katta_harf(matnlar):
#     matnlar = matnlar[:]
#     for i in range(len(matnlar)):
#         matnlar[i] = matnlar[i].title()
#     return matnlar


# ismlar = ["ali", "vali", "hasan", "husan"]
# yangi_ismlar = katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)



# Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan 
# va asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib
#  yozing.
def bahola(ismlar):
    baholar = {}

    for ism in ismlar:
        baho = input(f"\n{ism.title()}ning bahosini kiriting: ")
        baholar[ism] = int(baho)

    return baholar


talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)

print(baholar)
print(talabalar)   

