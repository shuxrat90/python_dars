# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 17:29:37 2026

@author: ANVAR
"""

"SON TOPISH O'YINI"

import random as r


# while True:

#     r_son = r.sample(range(1,11),1)

#     print("\nKeling o'ylagan sonni topish o'ynaymiz!")
#     print("1 dan 10 gacha son o'yladim. Topa olasizmi?:")

#     sonlar = []

#     while True:
#         son = int(input('>>'))
#         sonlar.append(son)
#         if son == r_son[0]:
#             break
        
#         if son > r_son[0]:
#             print("Xato men o'ylagan son bundan kichikroq. Yana harakat qiling: ")
            
#         if son < r_son[0]:
#             print("Xato men o'ylagan son bundan kattaroq. Yana harakat qiling: ")
        
#     urunish = len(sonlar)        
#     print(f"TOPDINGIZ! {r_son[0]} sonini o'ylagan edim {urunish} ta taxmin bilan topdingiz. Tabriklayman!!")      
    
     
    
#     print("\n1 dan 10 gacha son o'ylang. Men topishga harakat qilaman.")
#     input("\nSon o'ylagan bo'lsangiz istalgan tugmani bosing.")
    
    
#     min_son = 1
#     max_son = 10
#     sonlar2 = []
    
    

#     r_son2 = r.sample(range(min_son, max_son + 1),1)

#     while True:
    
     
#         javob = input(f"\nSiz {r_son2[0]} sonini o'ylagansiz: To'g'ri (T),men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)?? ")
        
#         sonlar2.append(r_son2[0])
        
#         if javob == 't':
#             break
        
        
#         if javob == '+':
#             min_son = r_son2[0] + 1
            
            
#         elif javob == '-':
#             max_son = r_son2[0] - 1
            
            
#         if min_son > max_son:
#             print("\nSiz bergan javoblarda xatolik bor.")
#             break        
        
#         r_son2 = r.sample(range(min_son, max_son + 1),1)
        
    
#     urunish2 = len(sonlar2)
    
#     print(f"\nSoningizni {urunish2} ta taxmin bilan topdim!")    
    
#     if urunish == urunish2:
#         print(f"Durrang ikkimiz ham {urunish} ta taxmin bilan topdik.")
        
#     if urunish < urunish2:    
#         print(f"Siz {urunish} ta taxmin bilan topdingiz va yutdingiz")
    
#     if urunish > urunish2:
#         print(f"Men {urunish2} ta taxmin bilan topdim va yutdim")
    
#     oyin = int(input("\nYana o'naysizmi: ha(1) / yo'q(0):  "))   

#     if oyin == 1:
#         continue
    
#     if oyin == 0:
#         break
       
    
    


# def son_top(x=10):    
#     """o'in 1-qism"""
    
#     r_son = r.sample(range(1,x+1),1)
    
#     print("\nKeling o'ylagan sonni topish o'ynaymiz!")
#     print(f"1 dan {x} gacha son o'yladim. Topa olasizmi?:")
    
#     sonlar = []
    
#     while True:
#         son = int(input('>>'))
#         sonlar.append(son)
#         if son == r_son[0]:
#             break
        
#         if son > r_son[0]:
#             print("Xato men o'ylagan son bundan kichikroq. Yana harakat qiling: ")
            
#         if son < r_son[0]:
#             print("Xato men o'ylagan son bundan kattaroq. Yana harakat qiling: ")
        
#     urunish = len(sonlar)        
#     print(f"TOPDINGIZ! {r_son[0]} sonini o'ylagan edim {urunish} ta taxmin bilan topdingiz. Tabriklayman!!")      
    
#     return urunish

# # urunish = son_top(10)
# # print(urunish)
    


# def son_top_pc(x=10):
#     """o'yin 2-qism"""
#     print(f"\n1 dan {x} gacha son o'ylang. Men topishga harakat qilaman.")
#     input("\nSon o'ylagan bo'lsangiz istalgan tugmani bosing.")
#     min_son = 1
#     max_son = x
#     sonlar2 = []
#     r_son2 = r.sample(range(min_son, max_son + 1),1)

#     while True:
#         javob = input(f"\nSiz {r_son2[0]} sonini o'ylagansiz: To'g'ri (T),men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)?? ")
#         sonlar2.append(r_son2[0])
#         if javob == 't':
#             break
#         if javob == '+':
#             min_son = r_son2[0] + 1
#         elif javob == '-':
#             max_son = r_son2[0] - 1
#         if min_son > max_son:
#             print("\nSiz bergan javoblarda xatolik bor.")
#             break        
#         r_son2 = r.sample(range(min_son, max_son + 1),1)
#     urunish2 = len(sonlar2)
#     print(f"\nSoningizni {urunish2} ta taxmin bilan topdim!")    
    
#     return urunish2

# # urunish2 = son_top_pc(10)
# # print(urunish2)
    

# def play_(x=10):
    
#     while True:    
        
#         urunish = son_top(x)
        
#         urunish2 = son_top_pc(x)
        
#         if urunish == urunish2:
#             print(f"Durrang ikkimiz ham {urunish} ta taxmin bilan topdik.")
            
#         if urunish < urunish2:    
#             print(f"Siz {urunish} ta taxmin bilan topdingiz va yutdingiz")
        
#         if urunish > urunish2:
#             print(f"Men {urunish2} ta taxmin bilan topdim va yutdim")
#         oyin = int(input("\nYana o'naysizmi: ha(1) / yo'q(0):  "))   
    
#         if oyin == 1:
#             continue
            
#         if oyin == 0:
#             break




import random

def sontop(x=10):
    tasodifiy_son = random.randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin<tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kattaroq. Yana harakat qiling:")
        elif taxmin>tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kichikroq. Yana harakat qiling:")
        else:
            break
    
    print(f"Tabriklaymiz. {tasodifiy_son} sonini o'ylagan edim {taxminlar} ta taxmin bilan topdingiz!")        
    return taxminlar   


def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi,yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
                      f"Men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim!")
    return taxminlar                    
            
            
def play(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        
        if taxminlar_user>taxminlar_pc:
            print("Men yutdim!")
        elif taxminlar_user<taxminlar_pc:
            print("Siz yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaysizmi? Ha(1)/Yo'q(0):"))                     
            
    
                
                                                 