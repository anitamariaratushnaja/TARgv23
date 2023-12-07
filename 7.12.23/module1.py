
#text=input("Sisesta tekst: ") #text-("t","e",...) num-(1,2,3)
#text_list=list(text)
#k=len(text_list)
#if text.isdigit(): # когда вы хотите проверить, состоит ли строка из цифр
#    for t in range(k):
#        num=int(text_list[t])
#        text_list.pop(t)
#        text_list.insert(t,num)
#        print(text_list)

#    summa=0
#    for e in text_list:
#        summa+=e
#        print("Summa : ", summa)
#print(text_list)
#e=input("Element: ")
#try:
#    if e.iaslpha():
#      indeks:text_list.index(e)
#    else:
#        indks=text_list.index(int(e))
#    print("Element: {0} on {1} positsioonil". format(e, indeks+1))
#except :
#    print("Element puudub")

#1 Sõna/Lause

#Sisestage sõna või laise klaviatuurilt ja loendage, mitu vokaali ja mitu konsonanti selles on.

#Kui on sisestatud lause, loendage ka kirjavahemärgid ja tühikud.
#vokaali=["a","e","u","o","i","ü","ö","õ","ä"]
#v=0
#k=0
#while True

#vokaalid = "aeiouüõöäAEIOUÜÕÖÄ"
#konsonandid = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
#kirjavahemargid_tuhikud = " ,.!?"

#sisend_sona = input("Sisestage sõna või lause: ")

#vokaalide_arv = sum(1 for t2ht in sisend_sona if t2ht in vokaalid)
#konsonantide_arv = sum(1 for t2ht in sisend_sona if t2ht in konsonandid)
#muu_arv = sum(1 for t2ht in sisend_sona if t2ht in kirjavahemargid_tuhikud)

#print(f"Vokaalide arv: {vokaalide_arv}")
#print(f"Konsonantide arv: {konsonantide_arv}")
#print(f"Tühikud ja kirjavahemärgid: {muu_arv}")

#import string 

#vokaalid="aeiouüõöäAEIOUÜÕÖÄ"
#konsonandid = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
#signs = string.punctuation
#vokaalid_count=0
#konsonandid_count=0
#spaces_count=0
#signs_count=0
#numbers_count=0
#sentence = input("Sisestage sõna või lause: ")
#for element in sentence:
#    if element==" ":
#        spaces_count += 1
#    elif element in signs:
#        signs_count 

#Küsi kasutajalt viis nime. Salvesta need loendisse ja kuva tähestikulises järjekorras. Kuva eraldi viimati lisatud nimi.

#Lisa võimalist loendis olevaid nimesid muuta.

#Tekita loend, kuhu oled lisanud meelega mõned ühesugused nimed. opilased = [‘Juhan’,’Kati’,’Mario’,’Mario’,’Mati’,’Mati’]

#Loo kood, mis ei väljasta kordusi.

#Loo vanuste loend. Leia numbrite suurim ja väikseim arv, kogusumma, keskmine.

# Küsi kasutajalt viis nime
#nimed = []
#for i in range(5):
#    nimi = input("Sisestage nimi: ")
#    nimed.append(nimi)

## Kuva nimed tähestikulises järjekorras
#nimed.sort()
#print("Nimed tähestikulises järjekorras:", nimed)

## Kuva viimati lisatud nimi
#viimane_nimi = nimed[-1]
#print("Viimati lisatud nimi:", viimane_nimi)

## Lisa võimalus loendis olevaid nimesid muuta
#muuda_nimi = input("Millist nime soovite muuta? ")
#if muuda_nimi in nimed:
#    uus_nimi = input(f"Sisestage uus nimi {muuda_nimi} asemel: ")
#    nimed[nimed.index(muuda_nimi)] = uus_nimi
#    print("Nimed pärast muutmist:", nimed)
#else:
#    print("Nime ei leitud loendist.")

## Tekita loend, kus on mõned ühesugused nimed
#opilased = ['Juhan', 'Kati', 'Mario', 'Mario', 'Mati', 'Mati']

## Loo kood, mis ei väljasta kordusi
#unikaalsed_opilased = list(set(opilased))
#print("Unikaalsed õpilased:", unikaalsed_opilased)

## Loo vanuste loend
#vanused = [21, 25, 18, 30, 22]

## Leia numbrite suurim ja väikseim arv, kogusumma, keskmine
#suurim_arv = max(vanused)
#vahim_arv = min(vanused)
#kogusumma = sum(vanused)
#keskmine = kogusumma / len(vanused)

#print("Suurim vanus:", suurim_arv)
#print("Väikseim vanus:", vahim_arv)
#print("Kogusumma vanustest:", kogusumma)
#print("Keskmine vanus:", keskmine)

#    Kasuta loendis olevate arvude väärtusi ning loo tärnide abil lintdiagramm. Näiteks:

#******************
#*******************
#********************************
#*****************************************
#****************************************************
#************

## Loendis olevad arvud
#arvud = [10, 12, 15, 20, 30, 10]

## Loo tärnide abil lintdiagramm
#for arv in arvud:
#    print('*' * arv)


l=[11,1,1,1,1,1,1,1,2,3,4,1,2,33]
l_set=set(l)
print(l_set)
for e in l_set:
    print(e*"*")
