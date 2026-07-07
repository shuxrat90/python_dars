# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 13:33:38 2026

@author: ANVAR
"""

# son = 0
# if son < 0 :
#     print("Manfiy son")
# else:
#     print("Musbat son") 

# yosh = int(input("Yoshingiz nechida? "))
# if yosh<=4:
#     print('Sizga kirish bepul.')
# elif yosh<=12:
#     print('Sizga kirish 5000 so\'m')
# elif yosh<=18:
#     print('Sizga kirish 8000 so\'m')    
# else:
#     print('Sizga kirish 10000 so\'m')    

# yosh = int(input("Yoshingiz nechida? "))
# if yosh<=4:
#     narh = 0
# elif yosh<=12:
#     narh = 5000     
# elif yosh<=18:
#     narh = 8000    
# else:
#     narh = 10000    
    
# print(f"Sizga kirish {narh} so'm")    

# kun = input("Bugun nima kun?>>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print('Bugun dam olish kuni.')
# else:
#     print("Bugun ish kuni.")   

# kun = input("Bugun nima kun? ")
# harorat = float(input("Havo harorati qanday? "))

# if kun.lower()=='yakshanba' and harorat>=30:
#     print("Chomilgani ketdik!")
# elif kun.lower()=='yakshanba' and harorat<30:
#     print("Uyda dam olamiz!")    
    
# kun = input("Bugun nima kun? ")
# harorat = float(input("Havo harorati qanday? "))

# if (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>=30:
#     print("Chomilgani ketdik!")
# elif (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat<30:
#     print("Uyda dam olamiz!")

# narh = 15000
# choy = True
# salat =  False

# if choy and salat:
#     narh = narh + 10000
# elif choy or salat:
#     narh = narh + 5000 

# print(f"Jami {narh} so'm")    

# narh = 15000
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False

# if choy:
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
    
# if salat:
#     print("Mijoz salat oldi.") 
#     narh = narh + 5000
    
# if non:
#     print("Mijoz non oldi.")
#     narh = narh + 2000

# if kompot:
#     print("Mijoz kompot oldi.")
#     narh = narh + 5000
    
# if assorti:
#     print("Mijoz assorti oldi.")
#     narh = narh + 15000
    
# print(f"Jami {narh} so'm")    
        

# narh = 15000
# choy = 1
# salat = 0
# non = 1
# kompot = 1
# assorti = 1

# if choy:
#     print("Mijoz choy oldi 3000.")
#     narh = narh + 3000
    
# if salat:
#     print("Mijoz salat oldi 5000.") 
#     narh = narh + 5000
    
# if non:
#     print("Mijoz non oldi 2000.")
#     narh = narh + 2000

# if kompot:
#     print("Mijoz kompot oldi 5000.")
#     narh = narh + 5000
    
# if assorti:
#     print("Mijoz assorti oldi 15000.")
#     narh = narh + 15000
    
# print(f"Jami {narh} so'm")    


# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# 'manti' in menu 


# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() in menu:
#     print('Buyurtma qabul qilindi.')
# else:
#     print('Afsuski bizda bunday ovqat yo\'q')    

# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() not in menu:
#     print('Afsuski bizda bunday ovqat yo\'q')
# else:
#     print('Buyurtma qabul qilindi.')


# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# buyurtmalar = ["osh", "somsa", "manti", "shashlik"]

# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menyuda {taom} bor")
#     else:
#         print(f"Kechirasiz, menuda {taom} yo'q")        

# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# buyurtmalar = ["osh", "somsa", "manti", "shashlik"]

# if buyurtmalar: 
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menyuda {taom} bor")
#         else:
#             print(f"Kechirasiz, menuda {taom} yo'q")    
# else: 
#     print("Savatigiz bo'sh!")  

11
# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     print('Sizga kirish bepul.')
# elif yosh<=12:
#     print('Sizga kirish 5000 so\'m')
# else:
#     print('Sizga kirish 10000 so\'m')

# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# else:
#     price = 10000
# print(f"Sizga kirish {price} so'm")          
        
# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4: # yosh bolalarga bepul
#     price = 0
# elif yosh<=12: # 4 dan 12 yoshgacha 5000 so'm
#     price = 5000
# elif yosh<65: # 12 dan katta va 65 dan kichiklarga narh 10000 so'm
#     price = 10000
# else: # qariyalarga esa 8000 so'm
#     price = 8000
# print(f"Sizga kirish {price} so'm")

# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# elif yosh<65:
#     price = 10000
# elif yosh>=65:
#     price = 8000    
# print(f"Sizga kirish {price} so'm")

# kun = input("Bugun nima kun?>>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print('Bugun dam olish kuni.')
# else:
#     print('Bugun ish kuni.')

# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if kun.lower()=='yakshanba' and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif kun.lower()=='yakshanba' and harorat<30:
#     print("Uyda dam olamiz!")

# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
#     print("Uyda dam olamiz!")

# narh = 15000 # mijoz 15000 so'mga taom oldi.
# choy = True # mijoz choy ham oldi
# salat = False # mijoz salat olmadi

# if choy and salat: # agar mijoz choy ham salat ham olgan bo'lsa
#     narh = narh + 10000 # narhga 10000 so'm qo'shamiz
# elif choy or salat: # agar choy yoki salat olgan bo'lsa
#     narh = narh + 5000 # narhga 5000 so'm qo'shamiz

# print(f"Jami {narh} so'm") # yakuniy narhni chiqaramiz

# narh = 15000 # mijoz 15 so'mga ovqat oldi
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
# #Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
# if choy:   # agar choy olsa
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat:  # agar salat olsa
#     print("Mijoz salat oldi.")
#     narh = narh + 5000
# if non:    # agar non olsa
#     print("Mijoz non oldi.")
#     narh = narh + 2000
# if kompot: # agar kompot olsa
#     print("Mijoz kompot oldi.")
#     narh = narh + 5000
# if assorti: # agar assorti olsa
#     print("Mijoz assorti oldi.")
#     narh = narh + 15000
    
# print(f"Jami {narh} so'm")

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# 'manti' in menu # menu da manti bormi?

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() in menu:
#     print('Buyurtma qabul qilindi.')
# else:
#     print('Afsuski bizda bunday ovqat yo\'q')

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# 'manti' not in menu # menu da manti yo'qmi?

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# 'osh' not in menu # menu da osh yo'qmi?

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input('Nima ovqat yeysiz?>>>')
# if ovqat.lower() not in menu:
#     print('Afsuski bizda bunday ovqat yo\'q')
# else:
#     print('Buyurtma qabul qilindi.')

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]

# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Kechirasiz, menuda {taom} yo'q")

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]

# if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz, menuda {taom} yo'q")
# else: # agar ro'yxat bo'sh bo'lsa
#     print("Savatchangiz bo'sh!")

# AMALIYOT
# Quyidagi dasturlarni alohida fayllarga yozing va bajaring:

# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa
#  "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.

# son = int(input('Juft son kriting: '))
# if son % 2 == 0:
#     print('Rahmat')
# else:
#     print('Bu son juft emas')

# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini 
# quyidagicha  chiqaring:
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm    
    
# yosh = int(input('Yoshingiz nechida? '))
# if yosh <= 4: 
#     print('Sizga kirish bepul')
# elif yosh >= 60:
#     print('Sizga kirish bepul')    
# elif yosh < 18:
#     print('Sizga kirish 10000 so\'m')    
# elif yosh > 18:
#     print('Sizga kirish 20000 so\'m') 

# yosh = int(input('Yoshingiz nechida? '))
# if yosh <= 4 or yosh >= 60:
#     narh = 0
# elif yosh < 18:
#     narh = 10000
# elif yosh >= 18:
#     narh = 20000

# print(f"Sizga kirish {narh} so'm")    

# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring 
# va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
# son_1 = float(input('Birinchi sonni kiriting: '))
# son_2 = float(input('Ikkinchi sonni kiriting: '))
# if son_1 > son_2:
#     print(f"{son_1} > {son_2}")
# elif son_1 < son_2:
#     print(f"{son_1} < {son_2}")   
# elif son_1 == son_2:
#     print(f"{son_1} = {son_2}")  
    
# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. 
# Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 
# 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati 
# bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" 
# aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
# mahsulotlar = ['un', 'tuz', 'piyoz', 'kartoshka', 'anor', 'shaftoli', 'olma', 'gilos', 'suv', 'ichimlik' ]    
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []
# for n in range(5):
#     mahsulot = input(f"Savatga {n+1}-mahsulotni qo'shing: ").lower()
#     savat.append(mahsulot)
# for mahsulot in savat:
#     if mahsulot.lower() in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#         bor_mahsulotlar.append(mahsulot)    
#     else:
#         print(f"Do'konimizda {mahsulot} yoq") 
#         mavjud_emas.append(mahsulot)

      
# # Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot 
# # kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang,
# #  bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas
# #  degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa,
# #  "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, 
# #  aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: .....
# #  " degan xabarni chiqaring.
# if mavjud_emas == []:
#     print('Siz soragan barcha mahsulotlar dokonimiza bor')
# if bor_mahsulotlar == []:     
#     print('Quyidagi mahsulotlar Do\'konimizda yoq')

# mahsulotlar = ['un', 'tuz', 'piyoz', 'kartoshka', 'anor', 'shaftoli', 'olma', 'gilos', 'suv', 'ichimlik' ]    
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []
# for n in range(5):
#     mahsulot = input(f"Savatga {n+1}-mahsulotni qo'shing: ").lower()
#     savat.append(mahsulot)
# for mahsulot in savat:
#     if mahsulot.lower() in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)    
# if mavjud_emas == []: # 1
#     print('Siz soragan barcha mahsulotlar dokonimizada bor')
#     for mahsulot in savat:
#         if mahsulot.lower() in mahsulotlar:
#             print(mahsulot)
# else:
#     print("Quyidagi mahsulotlar do'konimizda yo'q:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)            
# # for mahsulot in savat:
# #      if mahsulot.lower() in mahsulotlar:
# #          print(f"Do'konimizda {mahsulot} bor")
          
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#     print("Savatingiz bo'sh")       
         
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
  
  
#   foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. 
#   Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan 
#   loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. 
#   Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!"
#   aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
# foydalanuvchilar = ['anvar', 'jamshid', 'sevara', 'hasan', 'komil']
# foydalanuvchi = (input("Yangi logen tanlang: ").lower())
# if foydalanuvchi in foydalanuvchilar:
#     print('Logen band yangi logen tanlang!')
# else:   
#     print('Xush kelibsiz foydalanuvchi!')    
    

# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan 
# sonni 2 dan 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini 
# konsolga chiqaring.
son = int(input('Butun son kiriting: '))

for n in range(2, 11):
    if son % n == 0:
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
       