'''
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi
reverse=True.
'''

luvut = []
luku = input("Anna luku tai lopeta tyhjällä merkkijonolla: ")
while luku != "":
    luvut.append(luku)
    luku = input("Anna seuraava luku tai lopeta tyhjällä merkkijonolla: ")

for luku in luvut:
    print ()