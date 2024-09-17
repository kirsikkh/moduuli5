'''
Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
(käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä
kuin ne syötettiin.
käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.
'''

kaupungit = []
kierros = 0
kaupunki = input("Anna ensimmäinen kaupungin nimi: ")
while kierros < 5:
    kaupungit.append(kaupunki)
    kierros += 1
    kaupunki = input("Anna seuraavan kaupungin nimi: ")

for kaupunki in kaupungit:
    print(f"Kaupungin nimet: {kaupunki}")


'''
nimet = []
etunimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
while etunimi != "":
    nimet.append(etunimi)
    etunimi = input("Anna seuraava nimi tai lopeta painamalla Enter: ")

for nimi in nimet:
    print (f"Moi, {nimi}!")
    
    kaupunki3 = input("Anna kolmas kaupungin nimi: ")
kaupunki4 = input("Anna neljäs kaupungin nimi: ")
kaupunki5 = input("Anna viides kaupungin nimi: ")
'''