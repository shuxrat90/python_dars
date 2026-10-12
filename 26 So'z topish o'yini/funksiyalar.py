# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 06:19:07 2026

@author: ANVAR
"""

import random
from uzwords import words

def get_word():
    word = random.choice(words)
    while "-" in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def display(user_letters,word):
    display_letter=""
    for letter in word:
        if letter in user_letters.upper():
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter        

def play():
    
    word = get_word()
    # So'zdagi harflar
    word_letters = set(word)
    # Foydalanuvchi kiritgan harflar
    user_letters = ''
    print(f"Мен {len(word)} хонали сўз ўйладим. Топа оласизми?")
    # print(word)
    while len(word_letters)>0:
        print(display(user_letters,word))
        if len(user_letters)>0:
            print(f"Шу вақтгача киритган хафларингиз: {user_letters}")
            
        letter = input("Харф киритинг: ").upper()
        if letter in user_letters:
            print("Бу харфни аввал киритгансиз")
            continue
        elif letter in word:
            word_letters.remove(letter) 
            print(f"{letter} харф тўғри.")
        else:
            print("Бундай харф йўқ.")
        user_letters += letter
    print(f"Табриклайман! {word} сўзини {len(user_letters)} та урунишда топдингиз. ")            
    
                        
            
        