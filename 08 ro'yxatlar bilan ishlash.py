# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 09:34:55 2026

@author: ANVAR
"""

# cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)

# my_cars = cars[:] # nusxa

# toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')

# cars.sort() # royxatni tartiblash alifbo boyicha
# print(cars) 

# cars = ['Bmw','mercedes benz', 'volvo', 'gm', 'tesla', 'audi']
# cars.sort() # royxat tartiblash alifbo boyicha katta harf birinchi chiqadi
# print(cars)

# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort(reverse=True) # royxatni teskari tartibda saqlash
# print(cars) 

# mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
# print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
# print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)

# print(sorted(mehmonlar, reverse=True)) # teskar royhxat

# ages = [12, 98, 34, 65, 34, 76, 11]
# ages.sort()
# print(ages)
# print(sorted(ages, reverse=True))

# fruits = ['pear','banana','apple','watermelon','lemon']
# fruits.reverse() # royxatni aylantirish
# print(fruits)

# fruits = ['pear','banana','apple','watermelon','lemon']
# print("Elementlar soni:",len(fruits)) # len(fruits) ro'yxat uzunligini qaytaradi

# sonlar = list(range(0,10)) # Natija: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(sonlar)

# juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
# toq_sonlar = list(range(1,20,2))  # 1 dan 20 gacha 2 qadam bilan
# print("Juft sonlar: ", juft_sonlar)
# print("Toq sonlar: ", toq_sonlar)

# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)

# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars = cars[0:3] # 0-indeskdan boshlab 3 ta element ajratib olamiz
# print(my_cars) 

# print(cars[2:5]) # 2-3-4-elementlarni ajratib olamiz (5 kirmaydi)

# print(cars[:4]) # Ro'yxat boshidan 4-gacha kesadi (0,1,2,3)
# print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi

# sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
# sonlar2 = sonlar # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)

# sonlar  = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
# sonlar2 =sonlar[:] # [:] ro'yxatni to'liq ko'chirib oladi
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7)i # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxat:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)

# tomonlar = (20, 30, 55.2)
# print(tomonlar)

# toys = ('bus','car','bear','dino','snake','lizard')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])

# toys = ('bus','car','bear','dino','snake','lizard')
# toys[3] = 'dragon'

# toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
# toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# # Ro'yxatga o'zgartirishlar kiritamiz
# toys.append('dragon')
# toys.remove('bus')
# toys[1] = 'mcqueen'
# toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
# print(toys)

# 1 O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar = ["O'zbekiston", "Qozog'iston", "Rassiya", "Avg'joniston", "Qirg'iziston" ]
print("Davlatlar" ,davlatlar)

# 2 Ro'yxatning uzunligini konsolga chiqaring
print("Soni", len(davlatlar))

# 3 sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
print("sorted",(sorted(davlatlar)))

# 4 sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print("sorted teskari",(sorted(davlatlar, reverse=True)))

# 5 Asl ro'yxatni qaytadan konsolga chiqaring
print("Davlatlar", davlatlar)

# 6 reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar.reverse()

# 7 sort() metodi yordamida ro'yxatni avval alifbo bo'yicha,
# keyin esa alifboga teskari tartibda konsolga chiqaring.
davlatlar.sort()
print("sort", davlatlar)
davlatlar.sort(reverse=True)
print("sort teskari", davlatlar)

# 8 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
juft_sonlar = list(range(120,1201,2))  

# 9 Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
jami = sum(juft_sonlar)
print("jami", jami)

# 10 Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang 
# va konsolga chiqaring
katta = max(juft_sonlar)
kichik = min(juft_sonlar)
print(f"{katta} - {kichik} =",katta-kichik)

# 11 Ro'yxatdagi elementlar sonini hisoblang
print("Elementlart soni",(len(juft_sonlar)))

# 12 Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
print("Boshidan",(juft_sonlar[:20]))
print("O'rtasidan", (juft_sonlar[270:290]))
print("Ohiridan",(juft_sonlar[521:]))

# 13 taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ["Osh", "Shashik", "Somsa", "Manti", "Shorva"]

# 14 nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]

# 15 Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, 
# va qo'shimcha 2 ta taom qo'shing
nonushta.remove("Osh")
nonushta.remove("Manti")
nonushta.append("Tuhum")
nonushta.append("Gumma")

# 16 Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print("Taomlar", taomlar)
print("Nonushta", nonushta)

# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring
# va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = tuple(nonushta)
nonushta[0] = ("Qaymoq va non")




