# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 09:52:02 2026

@author: ANVAR
"""

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# narhlar = [12000, 18000,10900, 22000, 25000, 36000, -25, 63.2]
# sonlar = ['bir', 'ikki', 3, 4, 5]
# ismlar = []

# # appent metod listga ohiriga qoshish
# # insert metod [0] belgilab qoshish 
# # del metod ochirish
# # remove metod royhatdan yozib 
# pop metodi boshqa royhatga yuklash

# hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']

# bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
# mahsulot = bozorlik.pop(3) # Ro'yhatdan banani sug'urib olamiz
# print("Men " + mahsulot + " sotib oldim")
# print("Olinmagan mahsulotlar: ", bozorlik)

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
# sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
# ismlar = [] # bo'sh ro'yxat

# print("Birinchi meva: ", mevalar[0])
# print("Ikkinchi meva: ", mevalar[1])

# print("Birinchi meva: ", mevalar[0].title())
# print("Ikkinchi meva: ", mevalar[1].upper())

# print(narhlar[2] + narhlar[3])

# car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
# print(car_models[-1]) # Listning eng oxirgi elementiga -1 bilan murojat qilamiz 

# narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
# narhlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
# narhlar[3] = narhlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
# print(narhlar)

# mevalar.append("tarvuz") # mevalar ga tarvuz qo'shamiz
# print(mevalar)

# cars = [] # bo'sh ro'yxat yaratamiz
# cars.append('Lacetti') # ro'yxatga Lacetti mashinasini qo'shamiz
# cars.append('Nexia 3') # ro'yxatga Nexia 3 mashinasini qo'shamiz
# cars.append('Cobalt')  # ro'yxatga Cobalt  mashinasini qo'shamiz
# print(cars)

# cars.insert(0, 'Malibu') # 1-o'ringa yangi qiymat qo'shamiz
# print(cars)

# cars.insert(2, 'Damas') # 3-o'ringa yangi qiymat qo'shamiz
# print(cars)

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# del mevalar[1] # 2-element (anjir) ni o'chirib tashlaymiz
# print(mevalar)

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# mevalar.remove('shaftoli') # Ro'yxatdan shaftolini o'chirdik
# print(mevalar)

# hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
# hayvonlar.remove("mushuk") # Ro'yxatda 2 ta mushuk bor, ulardan birinchisi o'chadi
# print(hayvonlar)

# bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
# mahsulot = bozorlik.pop(3) # Ro'yxatdan banan ni sug'urib olamiz
# print("Men " + mahsulot + " sotib oldim")
# print("Olinmagan mahsulotlar: ", bozorlik)

# ismlar = ["Abror", "Mahmud", "Anvar aka"]
# print("Salom" + " " + ismlar[0] + ", bugun choyxona bormi?" )
# print(ismlar[1] + ", choyxonaga boramizmi?")
# print(ismlar[2] + ", ahvolariz qanaqa, charchamiyapsizmi?")

# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring.
# Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 
# sonlar = [100, 210, 15.8, -5]
# sonlar[0] = 125
# sonlar[1] = sonlar[1] - 50
# del sonlar[2] 
# sonlar.append(3)
# sonlar.insert(0, 12)
# sonlar.remove(3)
# yuk_sonlar = sonlar.pop(3)

# t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va 
# biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning,
# ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 

# t_shaxslar = ["Bobur", "Amir Temur", "Tesla"]
# z_shaxslar = ["Bil Gates", "Anvar aka", "Lukoshenka"]

# Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib
# (.pop()), quyidagi ko'rinishda chiqaring:
# tanlangan = []
# tanlangan.append(t_shaxslar.pop(0)) 
# tanlangan.append(z_shaxslar.pop(2))
# print("Men tarixiy shaxslardan " + tanlangan[0] + " bilan, Zamonaviy shaxslardan esa " + tanlangan[1] + " bilan suhbat qurishni istar edim" )

# friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 
frends = []
frends.append("Anvar")
frends.append("Zuhra")
frends.append("Jamshid")
frends.append("Shovkat")
frends.append("Komil")

# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
frends.remove("Jamshid")

# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing
frends.insert(0, "Yashin")
frends.append("Bek")
frends.insert(2, "Lobar")

# Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() 
# metodlari yordamida mehmonga kelgan do'stlaringizning 
# ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar = []
mehmonlar.append(frends.pop(2))
mehmonlar.append(frends.pop(1))
print("Kelgan mehmonlar ",  mehmonlar[0],  mehmonlar[1])
