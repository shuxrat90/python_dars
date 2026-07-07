# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 14:03:50 2026

@author: ANVAR
"""

# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#     print('salom', mehmon)
#     print('Hayr,', mehmon)

# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
#     print("Hurmat bilan, Palonchiyevlar oilasi\n") 

# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")

# sonlar = list(range(11))
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
        
# print(sonlar)
# print(sonlar_kvadrati)

# dostlar = []
# print("5 ta eng yaqin do'stingizni kim?")
# for n in range(5):
#     dostlar.append(input(f"\n{n+1}-do'stingizning ismini kiriting: "))
# print(dostlar)    

# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(mehmon)

# # 1 Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, 
# # va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
# ismlar = ['Anvar', 'Jamshid', 'Nargiza', 'Bonu', 'Jumavoy']
# for dostlar in ismlar:
#     print('Salom', dostlar)
    
# # 2 Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" 
# # degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing) 
# print(f'Kod  {(len(ismlar))}  martda takrorlandi')   

# # 3  10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. 
# # Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
# sonlar = list(range(11,101,2))  
# sonlar_kubi = []
# for son in sonlar:
#     sonlar_kubi.append(son**3)  
# for s in sonlar_kubi:
    # print(s)    
    
# 4 Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, 
# va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.    
# kinolar = []
# print("5 ta eng sevimli kinoyingiz?")
# for kino in range(5):
#     kinolar.append(input(f"\n{kino+1}-kino: "))
# print(kinolar)    

# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang,
#  va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing.
#  Ro'yxatni konsolga chiqaring.
suhbatlar = []
son = int(input("Bugun nechta odam bilan suhbat qildigiz?>>> "))
for n in range(son):
    suhbatlar.append(input(f"\n{n+1}-suhbat qilgan odamingiz kim edi: "))
print(suhbatlar)    
    


