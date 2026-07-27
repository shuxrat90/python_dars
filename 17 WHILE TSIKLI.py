# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 14:45:45 2026

@author: ANVAR
"""
# input()
# ism = input("Ismingiz nima? ")
# print(f'Salom, {ism.title()}')


# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)


# Sonlar va input()
# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)
# yosh = int(yosh) # yosh ni butun songa o'tkazamiz
# height = input("Bo'yingiz necha metr? ")
# height = float(height) # bo'yni o'nlik songa o'tkazamiz


# while
# son = 1 # son ga 1 qiymatini beramiz
# while son<=5: # toki son 5 dan kichik yoki teng ekan...
#     print(son, end=' ') # son ni konsolga chiqaramiz,
#     son = son+1 # songa 1 qo'shamiz.


# while va input()
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
        

# Ishora (flag)        
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)        


# BREAK OPERATORI
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True: # abadiy tsikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break # tsiklni to'xtatish
#     else:
#         print(float(qiymat)**2)


# sonlar = list(range(1,11))
# for son in sonlar: 
#     if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")


# CONTINUE OPERATORI
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")


# son = 0
# while son<10:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)


# ABADIY TSIKL TUZOG'I
# infinite loop
# son = 0
# while son<10:
#     # son += 1 # qolib ketgan
#     if son%2!=0:
#         continue
#     else:
#         print(son)
    

# son = 0
# while son<10:
#     son += 1 # tog'ri   
#     if son%2!=1:
#         continue
#     else:
#         print(son)
#     # son += 1 # xato
    
    
# son = 1
# while son<10: # xato while son>0:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)    


# AMALIYOT
# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang.
#  Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
# savol = "Sevgan kitobingizni kiriting"
# savol += "(barcha kitoblarni kiritib bo'lgach 'exit' deb yozing): "

# while True:
#     kitob = input(savol)
#     if kitob == "exit":
#         break
# print("Rahmat!")


# savol = "Sevgan kitobingizni kiriting"
# savol += "(barcha kitoblarni kiritib bo'lgach 'exit' deb yozing): "

# ishora = True
# while ishora:
#     kitob = input(savol)
#     if kitob == "exit":
#         ishora = False
# print("Rahmat")    


# savol = "Sevgan kitobingizni kiriting"
# savol += "(barcha kitoblarni kiritib bo'lgach 'exit' deb yozing): "

# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         print("Rahmat")
    

# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq:
#     7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm,
#     65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur
#     foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin.
#     Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin 
#     (ikkita shartni ham tekshiring).
# savol = "Yoshingizni kiriting: "

# while True:
#     qiymat = input(savol)
#     if qiymat == "exit" or qiymat == "quit":
#         break
#     yosh = int(qiymat)

#     if yosh < 7:
#         narh = 2000
#     elif 7 <= yosh < 18:
#         narh = 3000
#     elif 18 <= yosh < 65:
#         narh = 10000
#     else:
#         narh = 0

#     if narh == 0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Chipta {narh} so'm")


# savol = "Yoshingizni kiriting: "    

# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == "exit" or qiymat == "quit":
#         ishora = False
#     else:    
#         yosh = int(qiymat)

#         if yosh < 7:
#             narh = 2000
#         elif 7 <= yosh < 18:
#             narh = 3000
#         elif 18 <= yosh < 65:
#             narh = 10000
#         else:
#             narh = 0

#         if narh == 0:
#             print("Sizga chipta bepul")
#         else:
#             print(f"Chipta {narh} so'm")


# savol = "Yoshingizni kiriting: " 

# qiymat = ''
# while qiymat != 'exit' and qiymat != 'quit':
#     qiymat = input(savol)
#     if qiymat != 'exit' and qiymat != 'quit':
        
    
#         yosh = int(qiymat)

#         if yosh < 7:
#                 narh = 2000
#         elif 7 <= yosh < 18:
#                 narh = 3000
#         elif 18 <= yosh < 65:
#                 narh = 10000
#         else:
#                 narh = 0

#         if narh == 0:
#                 print("Sizga chipta bepul")
#         else:
#                 print(f"Chipta {narh} so'm")


# Quyidagi dasturda bir nechta mantiqiy xatolar bor. Jumladan, xusisiy 
# holatlarda tsikl abadiy qaytarilib qolmoqda. Xatolarni to'g'rilay olasizmi?
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
   
    elif float(qiymat)<0:
        print("Musbat son kiriting")
        continue # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
        
    else:        
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")        
        