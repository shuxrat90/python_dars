car_0 = {'model':'ferrari', 'rang':'qizil'}
# print(car_0['model'])
# print(car_0['rang'])


en_uz = {'apple': 'olma', 'apricot': "o'rik", 'banana': 'banan'}


mevalar = {'olma': '10000', 'tarvuz': '8000', 'qovun': '10000'}
# print(f"Olma narhi {mevalar['olma']} so'm")


# talaba_0 = {'ism': 'murod olimov', 'yosh': 20, 't_yil': '2000'}
# print(f"{talaba_0['ism'].title()},\
#  {talaba_0['t_yil']}-yilda tug'ilgan,\
#  {talaba_0['yosh']} yoshda")
 
# talaba_0['kurs'] = 4
# talaba_0['fakultet'] = 'informatika' 

# talaba_0['kurs'] = 4 # yangi, 'kurs' nomli kalit so'zga 4 qiymatini yuklaymiz
# talaba_0['fakultet'] = 'informatika' # 'fakultet' ga esa 'informatika' 


talaba_1 = {}
talaba_1['ism'] = 'qobul rasulov'
talaba_1['kurs'] = 3
talaba_1['yosh'] = 20
# print(talaba_1 )
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

talaba_1['kurs'] = 4
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# talaba_1['kurs'] = 4 # 'kurs' ni 4 ga o'zgartiramiz.
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")


talaba_0 = {'ism': 'murod olimov', 'yosh': 20, 't_yil': '2000'}

del talaba_0['yosh']
# print(talaba_0)

# talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
# print(talaba_0)
# del talaba_0['yosh'] # yosh degan kalit so'z (va qiymatni) o'chiramiz
# print(talaba_0)


telefonlar = {
    'ali': 'iphone x',
    'vali': 'galaxy s9',
    'olim': 'mi 10 pro',
    'orif': 'nokia 3310',
    'anvar': 'pixel 3xl'
    }


phone = telefonlar.get('ali', 'Bunday ism mavjud emas')
# print(phone)


meva = en_uz.get('apple', 'Bunday ism mavjud emas')
# print(meva)


meva = en_uz.get('pineapple', 'Bunday meva mavjud emas')
# print(meva)


# phone = telefonlar.get('hasan')
# print(phone)


# AMALIYOT
# otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson
#  haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va
#  hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring :Otamning ismi
#     Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
otam = {'ism': 'nasim', 't_yil': 1956, 't_joyi': 'toshkent'}
print(f"Otamning ismi {otam['ism'].title()}, {otam['t_yil']}-yilda,\
 {otam['t_joyi'].title()} viloyatida tug'ilgan  ")
 
 
 # Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta
 # ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga 
 # chiqaring: Alining sevimli taomi osh
taomlar = {'otam': 'shashlik',
           'onam': 'osh',
           'akam': 'shorva',
           'shuhrat': 'tabaka',
           'kenoyim': 'mastava'
                     }
print(f"Otamning sevimli taomi {taomlar['otam']}, \
 akamning sevimli taomi {taomlar['akam']}, \
 Shuhratning sevili taomi {taomlar['shuhrat']}.")
 
 
 # Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z 
 # (atamani) kiriting (masalan integer, float, string, if, else va hokazo) 
 # va har birining qisqacha tarjimasini yozing.
lugat = {'dictionary': "lug'at", 'string': 'matn', 'integer': 'butun son', \
         'float': "o'nlik son", 'list': "ro'yhat", 'for': 'takrorlash', \
             'if': 'agarda', 'else': 'aks holda', 'elif': 'agarda aks holda', \
                 'temp': "o'zgarmas ro'yhat"} 


# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini 
# yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa,
#  "Bunda so'z mavjud emas" degan xabarni chiqaring.
soz = input("Kalit so'z kiriting: ").lower()  
# javob = lugat.get(soz, "Bunday so'z mavjud emas")
# print(javob.capitalize())


# Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga
#  tushunarli ko'rinishda chiqaring.
# if soz in lugat:
#     print(f"{soz.title()} so'zi  {lugat[soz].capitalize()} dep tarjima qilinadi")
# else:
#     print("Bunday so'z mavjud emas")    
javob = lugat.get(soz)
if javob == None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{soz.title()} so'zi {javob.capitalize()} dep tarjima qilinadi")    



    