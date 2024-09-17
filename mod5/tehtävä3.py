'''
Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa,
onko se alkuluku. Tässä tehtävässä alkulukuja ovat luvut,
jotka ovat jaollisia vain ykkösellä ja itsellään.

Esimerkiksi luku 13 on alkuluku,
koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
Toisaalta esimerkiksi luku 21 ei ole alkuluku,
koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.
'''

luku = int(input("Anna kokonaisluku: "))
if luku / 1 == 0 and luku / luku == 0:
    print("Luku on alkuluku.")
else:
    print("Luku ei ole alkuluku.")

