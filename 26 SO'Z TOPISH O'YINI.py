# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 17:49:40 2026

@author: ANVAR
"""

import random
from uzwords import words


def get_word():
    tasodif_soz = random.choice(words).upper()
    return tasodif_soz



soz = get_word()

print(f"Мен {len(soz)} хоали сўз ўйладим. Топа оласизми?")


yashirin_soz = ["-"] * len(soz)

print("".join(yashirin_soz))

harflar = ""


for urunish in range(50):
    harf = input("\nХарф киритинг: ").upper()
    
    if harf in  harflar:
        print("Бу харфни аввал киритгансиз. Бошқа харф киритнг.")
    else:
        harflar += harf
        if harf in soz:
            print(f"{harf} Харфи тўғри.")
        else: 
            print("Бундай харф йўқ.")
    
   
    
    for i in range(len(soz)):
        if soz[i] == harf:
            yashirin_soz[i] = harf
    
    print("".join(yashirin_soz))      
    
    print(f"Шу вақтгача киритган харфларингиз: {harflar}")
    
    if "-" not in yashirin_soz:
        print(f"Табриклайман! {soz} сузни {urunish+1} та урунишда топдингиз. ")
        break
    

# def display(x, soz):
  
    
# input = ("Мен 5 хонали сон ўйладим. Топа оласизми? ")
