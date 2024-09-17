#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta

import random

round_counter = 0
arpakuutiot = int(input("Anna arpakuutioiden lukumäärä: "))
while round_counter < arpakuutiot:
    round_counter += 1
    arpa = random.randint(1, 6)
print(sum({arpakuutiot}))
