# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 10:01:31 2026

@author: ANVAR
"""

# ism = "Anvar"

# shahar = "Қўқон"
# viloyat = "Фарғона"

# matn = "Men yangi 📲 oldim" # https://symbl.cc/en
# smayl = "😖"  # https://symbl.cc/en
# print(matn)

# STRING USTIDA AMALLAR

# ism = "Ahmad"
# print("Mening ismim " + ism)
    
# ism = "Ahad"
# familiya = "Qayum"
# # print(ism + familiya)
# print(ism + " " + familiya)

# f string

# ism = "Ahad"
# familiya = "Qayum"
# ism_sharif = f"{ism} {familiya}" 
# print(ism_sharif)

# ism = "James"
# familiya = "Bond"
# print(f"Salom, mening ismim {familiya}. {ism} {familiya}!")

# MAXSUS BELGILAR

# print("Hello World!")
# print("Hello \tWorld!")
# print("Hello \nWorld!")

# STRING METODLAR 

# ism = "james"
# familiya = "bond"
# ism_sharif = f"{ism} {familiya}"
# ism_sharif = ism_sharif.upper() 
# # print(ism_sharif.lower())
# # print(ism_sharif.title())
# print(ism_sharif.capitalize())

# meva = "     olma     "
# print(meva)
# print("Men " + meva.lstrip() + " yahshi ko`raman")
# print("Men " + meva.rstrip() + " yahshi ko`raman")
# print("Men " + meva.strip() + " yahshi ko`raman")
# print("Men " + meva + " yahshi ko`raman")

# INPUT

# ism = input("Ismingiz nima?")
# print("Assalomu alaykum, " + ism)  

# ism = input("Ismingiz nima?\n>>>") # yangi qatorga yozish 
# print("Assalomu alaykum, " + ism.title())  

# AMALIYOT

# Quyidagi mashqlarni bajaring:

# Quyidagi o'zgaruvchilarni yarating: 

kocha="Bog'bon"

mahalla="Sog'bon"

tuman="Bodomzor" 

viloyat="Samarqand"

# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:

# Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati

print(kocha + " ko'chasi," + " " + mahalla + " " + "mahallasi," + " " + tuman + " " + "tumani," + " " + viloyat + " " + "viloyati")

# Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.

print("Iltimos, quyidagi ma'lumotlarni kiriting:")
kocha = input("Ko'changiz: ")
mahalla = input("Mahallangiz: ")
tuman = input("Tumaningiz: ")
viloyat = input("Viloyatingiz: ")

# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
print()
# print(kocha + " ko'chasi,\n" + "" + mahalla + " " + "mahallasi,\n" + "" + tuman + " " + "tumani,\n" + "" + viloyat + " " + "viloyati")

# Yuqoridagi o'zgaruvchilarni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang

manzil = f"{kocha} kochasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
# print(manzil.upper()) KATTA HARF
# print(manzil.lower()) # KICHKINA HARF
print(manzil.title()) # SUZLARNING BOSH HARIFI KATTA
# print(manzil.capitalize()) # BIRINCHI SOZNING BOSH HARIFI KATTA