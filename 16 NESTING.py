# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 08:02:19 2026

@author: ANVAR
"""

car0 = {
        'model': 'lacetti',
        'rang': 'oq',
        'yil': 2018,
        'narh': 13000,
        'km': 50000,
        'karobka': 'avtomat'
        }

car1 = {
        'model': 'nexia 3',
        'rang': 'qora',
        'yil': 2015,
        'narh': 9000,
        'km': 89000,
        'karobka': 'mexanika'
        }

car2 = {
        'model': 'gentra',
        'rang': 'qizil',
        'yil': 2019,
        'narh': 15000,
        'km': 20000,
        'karobka': 'mexanika'
        }
# car = car0
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang, "
#       f"{car['yil']}-yil, {car['narh']}$")

# car = car1
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang, "
#       f"{car['yil']}-yil, {car['narh']}$")

# car = car2
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang, "
#       f"{car['yil']}-yil, {car['narh']}$")


cars = [car0, car1, car2]
# for car in cars:
#     print(f"{car['model'].title()}, "
#           f"{car['rang']} rang, "
#           f"{car['yil']}-yil, {car['narh']}$")
    

# print(f"{cars[2]['rang'].title()} "
#       f"{cars[2]['model']}")


malibus = []
for n in range(10):
    new_car = {
        'model': 'malibu',
        'rang': None, # rangi noaniq
        'yil': 2020,
        'narh': None,
        'km': 0,
        'karobka': 'avto'
        }
    malibus.append(new_car)
    
# for malibu in malibus:
#     print(malibu)

for malibu in malibus[:3]:
    malibu['rang']='qizil'
    
# for malibu in malibus:
#     print(malibu)    

for malibu in malibus[3:6]:
    malibu['rang']='qora'
    
for malibu in malibus[6:]:
    malibu['rang']='qora'
    malibu['karobka']='mexanika'
    
# for malibu in malibus:
#     print(malibu)      

for malibu in malibus:
    if malibu['karobka']=='avto':
        malibu['narh'] = 40000
    else:   
        malibu['narh'] = 35000

# for malibu in malibus:
#     print(malibu)     


# LUG'AT ICHIDA ROYXAT 
dasturchilar = {
    'ali': ['python', 'c++'],
    'vali': ['html', 'css', 'js'],
    'hasan': ['php', 'sql'],
    'husan': ['python', 'php'],
    'maryam': ['c++', 'c#']
    }  

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidgi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper())
        
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidgi dasturlash tillarini biladi:", end=' ')
#     for til in tillar:
#         print(f'{til.upper()} ', end='' )    
#     print()    


hamkasblar = {
    'ali':{'familiya': 'valiyev',
           'tyil': 1995,
           'malumot': 'oliy',
           'tillar': ['python', 'c++']}, 
    'vali':{'familiya': 'aliyev',
            'tyil': 2001,
            'malumot': "o'rta maxsus",
            'tillar': ['html', 'css', 'js']},
    'hasan':{'familiya': 'husanov',
            'tyil': 1999,
            'malumot': 'maxsus',
            'tillar': ['python', 'php']}
    }

# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()}, "
#           f"{info['tyil']}-yilda tug'ulgan.\n"
#           f"Ma'lumoti: {info['malumot']}.\n"
#           "Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())
        
        
# AMALIYOT
# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi 
# ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang,
#  va har bir shaxs haqidagi ma'lumotni konsolga chiqaring. 
abu = {
    'ism': 'abu abdulloh mahammad ibn ismoil',
    'tyil': 810,
    'tjoy': 'buxoro',
    'yilumr': 60,
    'asar': ['Al-jome` as-sahih', 
             'Al-arab al-mufrad',
             'At-tarix al-kabir',
             "At-tarix as-sag'ir"]
    }      
abdulla = {
    'ism': 'abdulla qodiriy',
    'tyil': 1894,
    'tjoy': 'toshkent',
    'yilumr': 44,
    'asar': ["O'tkan kunlar", 'Mehrobdan Chayon', 'Obid ketmon']
    }      
erkin = {
    'ism': 'erkin vohidov',
    'tyil': 1936,
    'tjoy': "farg'ona",
    'yilumr': 80,
    'asar': ['Tong nafasi', "Qo'shiqlarim sizga", "O'zbegim", 'Qiziquvchan Matmusa']
    }  
alisher = {
    'ism': 'alisher navoiy',
    'tyil': 1441,
    'tjoy': 'xirotda',
    'yilumr': 60,
    'asar': ['Xamsa', 'Lison ut-Tayr', 'Mahbub Al-Qulub', 'Munojat']
    }          
shaxslar = [abu, abdulla, erkin, alisher]

# for shaxs in shaxslar:
#     print(f"{shaxs['ism'].title()} " 
#           f"{shaxs['tyil']}-yilda "
#           f"{shaxs['tjoy'].capitalize()}da tavallud topgan. "
#           f"{shaxs['yilumr']} yil umr ko'rgan.")
    
    
# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing.
#  For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.
# for shaxs in shaxslar:
#      print(f"{shaxs['ism'].title()}ning mashxur asarlari: ") 
#      for asar in shaxs['asar']: 
#          print(asar)
#      print()         
     

# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. 
#     Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida
#     lug'artga saqlang.  Natijani konsolga chiqaring.     
kinolar = {
    'ali': ['Terminator', 'Rambo', 'Titanic'],
    'vali': ['Tenet', 'Inception', 'Intersteller'],
    'hasan': ['Abdullajon', 'Bomba', 'Shaytanat'],
    'husan': ['Mahallada duv-duv gap', 'John Wick']
    } 

# for ism, kinolar in kinolar.items():
#     print(f"\n{ism.title()}ning sevimli kinolari: ")
#     for kino in kinolar:
#         print(f"{kino}")


# Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida 
# ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni
#  konsolga chiqaring.
davlatlar = {
    "o'zbekiston": {
        'poytaxt': 'toshkent',
        'hududi': '448978 kv.km',
        'aholisi': 33_000_000,
        'puli': "so'm" 
        },
    'rossiya': {
        'poytaxt': 'moskva',
        'hududi': '17098246 kv.km',
        'aholisi': 144_000_000,
        'puli': "rubl" 
        },
    'aqsh': {
        'poytaxt': 'vashington',
        'hududi': '9631418 kv.km',
        'aholisi': 144_000_000,
        'puli': "dollor"
        },
    'malayziya': {
        'poytaxt': 'kuala-lumpur',
        'hududi': '329750 kv.km',
        'aholisi': 25_000_000,
        'puli': "rinngit" }
    }

# for davlat, info in davlatlar.items():
#     if davlat.lower() == 'aqsh':
#         davlat = davlat.upper()
#     else:
#         davlat = davlat.capitalize()
#     print(
#         f"\n{davlat}ning poytaxti {info['poytaxt'].title()} "
#         f"\nHududi: {info['hududi']} "
#         f"\nAholisi: {info['aholisi']} "
#         f"\nPul birligi: {info['puli']} "
        # ) 
       
davlat = input("Davlat nomini kiriting: ").lower()    
if davlat in davlatlar:
    info = davlatlar[davlat]
            
    print(
                f"\n{davlat.capitalize()} {info['poytaxt'].title()} "
                f"\nHududi: {info['hududi']} "
                f"\nAholisi: {info['aholisi']} "
                f"\nPul birligi: {info['puli']} "
                )         
else: 
    print("Bizda bunday davlat haqida malumot mavjud emas")            
    