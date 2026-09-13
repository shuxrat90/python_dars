# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 09:48:14 2026

@author: ANVAR
"""
# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi} 
#     return avto
    
# avto1 = avto_info('GM', 'Malibu', 'Qora', 'Avtomat', 2018) 
# avto2 = avto_info('GM', 'Gentra', 'Oq', 'Mexanika', 2016, 15000, turi='sedan')
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomashinalar:')

# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"   
    

#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}") 



# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi

# print(summa(1,2))
# print(summa(1,2,3,4,5))
# print(summa(4,5,6,7))        
    
    
         
# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return sum(sonlar)

# print(summa(2))
# print(summa(1,2,3,4,5))
# print(summa(4,5,6,7))       



# def summa(x,y,*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return x+y+sum(sonlar)

# print(summa(1,2))
# print(summa(1,2,3,4,5))
# print(summa(4,5,6,7))    
# print(summa(2))



# def avto_info(kompaniya,model,**malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar

# avto1 = avto_info('GM', 'malibu', rang='qora', yil=2018)
# avto2 = avto_info('Kia', 'K5', rang='qizil', narh=35000, yil=2020, korobka='avtomat')
    



# AMALIYOT
# Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi 
# funksiya yozing
# def kop_summa(*sonlar):
#     """Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi 
#     funksiya"""
#     kopaytma = 1
#     for son in sonlar:
#         kopaytma *= son
     
#     return kopaytma
    
# print(kop_summa(4, 5, 6))     




# Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya 
# yozing. Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar
#  esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.
def talaba_info(ism,familiya,**kwargs):
    """Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya"""
    kwargs['ism']=ism
    kwargs['familiyal']=familiya
    return kwargs

talaba = talaba_info('Shuhrat', 'Arifdjanov', yosh=36, t_joy='Toshkent', lefofoni='redmi10')