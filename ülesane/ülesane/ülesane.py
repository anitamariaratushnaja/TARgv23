from math import *
#1.
#Kirjuta enda esimene programm, mis väljastab käsureale teksti: “Tere, maailm!”. 

#Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: “Tere, maailm! Tervitav sind Mati”, kui kasutaja nimi on Mati.

#Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:

#“Tere, maailm! Tervitav sind Mati! Ma olen N aastat vana.”

#print("Tere, maailm!")
#nimi=input("Mis su nimi on? ") #str nimi
#print("Tere, maailm! Tervitav sind {0}!".format(nimi))
#vanus=int(input("Kui vana sa oled"))
#print("Tere maailm!Tervitan sind {0}! Sa oled {1} aasta vana.".format(nimi,vanus))


#2

#Mis tüüpi on järgnevad muutujad:

#a) vanus = 18 #type(vanus) int

#b) eesnimi = "Jaak"str

#c) pikkus = 16.5 float

#d) kas_käib_koolis = True bool

#Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida?

#Kirjuta kood tüüpide kontrollimiseks.


#3

#Kirjuta enda mängu koodis laual olevate kommide arv muutujasse. Seejärel kuva muutujas olev kommide arv ekraanile kasutades print() käsku.
#Küsi kasutajalt sisendit, mitu kommi ta soovib laualt ära võtta. Eemalda soovitud kommide arv laual olevate kommide arvust ja kuva ekraanile, kui palju komme laual nüüd on.

#kommide_arv=int(input("Laual olevate kommide arv: "))
#print("Laua peal on {0}".format(kommide_arv))
#mitu=int(input("Mitu kommi sa soovid süüa: "))
#kommide_arv-=mitu
#print("Nüüd laua peal on ",kommide_arv)

#4
#Puu läbimõõdu arvutamine
#Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu.

import math

#C=float(input("ümbermõõt: ")) #c=2*pi*R
#d=round(C/pi,2)
#print("läbimõõt: ",d)

## Запрос длины окружности от пользователя
#ümbermõõdu = float(input("Введите длину окружности дерева в сантиметрах: "))

## Вычисление диаметра по формуле: диаметр = длина_окружности / pi
#diameter = ümbermõõdu / math.pi

## Вывод результата
#print(f"Диаметр дерева: {diameter:.2f} сантиметров")


#5.
#Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.
#a=float(input("Esimene mõõt: ")) #A*A+B*B=C*C
#b=float(input("Teine mõõt: "))
#c=sqrt(a**2+b**2)
#print("diagonaal= ",c)


#6
#Leidke järgnevast näiteprogrammist semantiline viga:

#aeg = float(input("Mitu tundi kulus sõiduks? "))
#teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
#kiirus = aeg / teepikkus
#print("sinu kiirus kiirus: "+ str(kiirus) + km/h)
#try:  #try tab
#    aeg=float(input("Mitu tundi kulus sõiduks? "))
#    teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
#    kiirus = teepikkus/aeg
#    print("sinu kiirus kiirus: "+ str(kiirus) + km/h)
#except :
#    print("andmetüübi viga!")

#7.
#Koostada programm, mis arvutab aritmeetilise keskmise suvalisest etteantud 5 täis arvust
# Запрос пяти целых чисел от пользователя
#num1 = int(input("Введите первое целое число: "))
#num2 = int(input("Введите второе целое число: "))
#num3 = int(input("Введите третье целое число: "))
#num4 = int(input("Введите четвертое целое число: "))
#num5 = int(input("Введите пятое целое число: "))

## Вычисление среднего арифметического
#average = (num1 + num2 + num3 + num4 + num5) / 5

## Вывод результата
#print(f"Среднее арифметическое введенных чисел: {average}")


#from random import *
#a1=randint(1,100)
#b1=randint(1,100)
#c1=randint(1,100)
#d1=randint(1,100)
#e1=randint(1,100)
#print("Arvude {0},{1},{2},{3},{4} Aritmeetiline keskmine on{5}".format(a1,b1,c1,d1,e1,(a1+b1+c1+d1+e1)/5))

#8.
#Joonista samasugune konn
 #  @..@
  # (----)
 # ( \__/ )
##^^ "" ^^  
#print("@..@".center(7))
#print("(----)".center(7))
#print("( \__/ )")
#print("^^ "" ^^".center(7))
#9.
#Arvutame kolmnurga ümbermõõdu. Loo kolm täisarvulist muutujat a, b, c. Loo valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)
from random import *
#a=randint(1,100)
#b=randint(1,100)
#c=randint(1,100)
#P=a+b+c
#print("Arvude {0},{1},{2}")
#print("ümbermõõd: ",P)
##10.
#Pitsa

 #   Võtsite P sõbraga suure pitsa hinnaga 12,90€
  #  Jätate teenindajale 10% jootraha
   # Koosta programm, mis leiab kui palju peab igaüks maksma
   # Цена пиццы
hind=12.9
print("pitsa hind 12,90€")

# Процент чаевых
a = 10

# Расчет общей суммы с учетом чаевых
summa = hind * (1+ a / 100)

# Вывод результата
print(f"Jätate teenindajale 10% jootraha: ", summa)

# Количество людей
b= randint(1,10)
print("kukku inimesed: ",b)

# Расчет суммы, которую каждый должен заплатить
summa_na_cheloveka = summa / b

# Вывод результата
print("igaüks maksma peab maksma: ",summa_na_cheloveka )

