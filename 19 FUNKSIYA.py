# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 05:55:56 2026

@author: ANVAR
"""

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")
    
# salom_ber()  




# def salom_ber(ism):
#     """Foydalanuvchi ismini qabul qilib,
#     unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
    
# salom_ber('hasam')
# salom_ber('olim')  

 
# print(salom_ber.__doc__)




# def toliq_ism(ism, familiya):
#     """Foydalanuvchini ismini va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiysi: {familiya.title()}")
    
# toliq_ism('olim', 'hakimov')
# toliq_ism('hakimov', 'olim' )



# def yosh_hisobla(ism, tugilgan_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2026-tugilgan_yil} yoshda")
    
# yosh_hisobla('olim', 1997)
# yosh_hisobla(1997, 'olim')
    
# yosh_hisobla(ism='olim', t_yil=1997)
# toliq_ism(familiya='hakimov', ism='olim')



# def yosh_hisobla(tugilgan_yil, joriy_yil=2026):
#     """Foydalanuvchi tug'ilgan yildan uni yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
# # yosh_hisobla(1995, 2020)    
# yosh_hisobla(1993)    




# def yosh_hisobla(tugilgan_yil, joriy_yil=2026):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
# tyil = int(input("Tug'ilgan yilingizni kiriting: "))
# yosh_hisobla(tyil)



# def yosh_hisobla(tugilgan_yil, joriy_yil):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

# yosh_hisobla(1993,2026)



# def salom_ber(ism):
#     """Salom beruvchi funksiya"""
#     print(f"Assalomu alaykum {ism.title()}")

# salom_ber('hasan')



# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
 
# toliq_ism('olim', 'hakimov')



# AMALIYOT
# Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan
#  funksiya yozing.
# def ism_va_yoshni_hisobla(ism, tugilgan_yil):
#     """Foydalanuvchi ismi va yoshini so'rab, 
#     uning tug'ilgan yilini hisoblaydigan funksiya"""
#     print(f"Foydalanuvchi ismi {ism.title()} yoshi {2026-tugilgan_yil} da")

# ism = input("Ismingiz nima?: ")
# tugulgan_yil = int(input("Tug'ilgan yilingiz?: "))    
# ism_va_yoshni_hisobla(ism, tugulgan_yil)    


# Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
# def tyil_hisobla(ism, yosh):
#     """Foydalanuvchi tugilgan yilini hisoblovchi funksiya"""
#     print(f"{ism.title()} {2020-yosh}-yilda tug'ilgan")


# tyil_hisobla("olim", 32)



# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi 
# funksiya yozing.
# def son_kv_kub_hisobla(son):
#     """Foydalanuvchidan son olib, uning kvadrati va kubini konsolga 
#     chiqaruvchi funksiya"""
#     print(f"{son} ning kvadrati {son**2} ga teng \n"
#           f"{son} ning kubi {son**0.5} ga teng ") 
    
# son = int(input("Son kiriting: "))  
# son_kv_kub_hisobla(son)  


# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
# def kv_kub(son):
#     """Kiritilgan sonning kvadrati va kubini konsolga chiqaruvchi funksiya"""
#     print(f"{son} ning kvadrati {son**2} ga, kubi {son**3} ga teng")


# kv_kub(-4)



# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi 
# funksiya yozing.
# son = 0
# def son_juft_yoki_toqligini_top(son):
#     """Foydalanuvchidan son olib, son juft yoki toqligini konsolga 
#     chiqaruvchi funksiya"""
#     if son % 2 == 0:
#         print(f"{son} soni juft son")
#     if son % 2 == 1:
#         print(f"{son} soni toq son")
    

# son = int(input("Son kiriting: "))   
# son_juft_yoki_toqligini_top(son) 


# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
# def juftmi(son):
#     """Kiritilgan son juft yoki toqligini konsolga chiqaruvchi funksiya"""
#     if son % 2:
#         print(f"{son} toq son")
#     else:
#         print(f"{son} juft son")


# juftmi(20)
# juftmi(123)



# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi 
# funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni 
# chiqaring.
# son_1 = 0
# son_2 = 0
# def ikki_son_solishtir(son_1, son_2):
#     """Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga 
#     chiqaruvchi funksiya"""
#     if son_1 == son_2:
#         print(f"{son_1} = {son_2} sonlar teng")
#     if son_1 > son_2:
#         print(f"{son_1} > {son_2} birinchi son katta")
#     if son_1 < son_2:
#         print(f"{son_1} < {son_2} ikkinchi son katta")

# son_1 = int(input("birinchi sonni kiriting: "))        
# son_2 = int(input("ikkinchi sonni kiriting: "))
# ikki_son_solishtir(son_1, son_2)    


# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing.
# Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
# def solishtir(x, y):
#     """Ikki sonni solishtiruvchi funksiya"""
#     if x > y:
#         print(f"{x}>{y}")
#     elif x < y:
#         print(f"{y}>{x}")
#     else:
#         print(f"{x}={y}")


# solishtir(10, 20)
# solishtir(-9, 12)
# solishtir(1223 * 5, 5 ** 4)



# Foydalanuvchidan x va y sonlarini olib, 
# (x) ni (y) darjaisinini konsolga chiqaruvchi funksiya yozing.
# son_1 = 0
# son_2 = 0
# def son_darajasini_top(son_1, son_2):
#     """Foydalanuvchidan x va y sonlarini olib, 
#     (x) ni (y) darjaisinini konsolga chiqaruvchi funksiya"""
#     print(f"{son_1} sonining {son_2} darajasi {son_1**son_2} ga teng")
    

# son_1 = int(input("birinchi sonni kiriting: "))        
# son_2 = int(input("ikkinchi sonni kiriting: "))
# son_darajasini_top(son_1, son_2)        


# Foydalanuvchidan x va y sonlarini olib, x^y ni konsolga chiqaruvchi funksiya yozing.
# def daraja(x, y):
#     """x ni y-darajaga oshiruvchi funksiya"""
#     print(f"{x} ning {y}-darajasi {x**y} ga teng")


# daraja(5, 2)
# daraja(3, 3)
# daraja(94, 4)



# Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
# def son_darajasini_top(x, y = 2):
#     """Foydalanuvchidan x va y sonlarini olib, 
#     (x) ni (y) darjaisinini konsolga chiqaruvchi funksiya"""
#     print(f"{x} sonining {y} darajasi {x**y} ga teng")
    


# son_darajasini_top(5, 3) 
# son_darajasini_top(5, ) 


# Foydalanuvchidan x va y sonlarini olib, x^y ni konsolga chiqaruvchi funksiya yozing.
# Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
# def daraja(x, y=2):
#     print(f"{x} ning {y}-darajasi {x**y} ga teng")


# daraja(5, 2)
# daraja(3, 3)
# daraja(94, 4)
# daraja(6)



# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga
#  qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga 
#  chiqaring.
# def bolinish_alomatlari(son):
#     """Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan 
#     sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya"""
#     for n in range(2,11):
#         if son % n == 0:
#             print(f"{son} {n} ga qoldiqsiz bo'linadi")
        

# bolinish_alomatlari(70)



# Foydalanuvchidan son qabul qilib, sonni 2, 3, 4 va 5 ga qoldiqsiz bo'linishini tekshiruvchi
# funksiya yozing.
# Natijalarni konsolga chiqaring ("15 soni 3 ga qoldiqsiz bo'linadi" ko'rinishida)
def bolinish_alomatlari(son):
    for n in range(2, 11):
        if not son % n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")


bolinish_alomatlari(20)
