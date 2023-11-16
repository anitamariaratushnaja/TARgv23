#1.
#Kirjuta enda esimene programm, mis väljastab käsureale teksti: “Tere, maailm!”. 

#Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: “Tere, maailm! Tervitav sind Mati”, kui kasutaja nimi on Mati.

#Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:

#“Tere, maailm! Tervitav sind Mati! Ma olen N aastat vana.”

print("Tere, maailm!")
nimi=input("Mis su nimi on?: ").capitalize() #str nimi
print("Tere, maailm! Tervitav sind"+nimi+)


#2

#Mis tüüpi on järgnevad muutujad:

#a) vanus = 18 int

#b) eesnimi = "Jaak"str

#c) pikkus = 16.5 float

#d) kas_käib_koolis = True bool

#Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida?

#Kirjuta kood tüüpide kontrollimiseks.


#3

#Kirjuta enda mängu koodis laual olevate kommide arv muutujasse. Seejärel kuva muutujas olev kommide arv ekraanile kasutades print() käsku.
#Küsi kasutajalt sisendit, mitu kommi ta soovib laualt ära võtta. Eemalda soovitud kommide arv laual olevate kommide arvust ja kuva ekraanile, kui palju komme laual nüüd on.
#4
#Puu läbimõõdu arvutamine
#Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu.

#5.
#Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt.

#6
#Leidke järgnevast näiteprogrammist semantiline viga:

#aeg = float(input("Mitu tundi kulus sõiduks? "))
#teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
#kiirus = aeg / teepikkus

#print("Sinu kiirus oli " + str(kiirus) + " km/h")

#7.
#Koostada programm, mis arvutab aritmeetilise keskmise suvalisest etteantud 5 täis arvust.

#8.
#Joonista samasugune konn
 #  @..@
  # (----)
 # ( \__/ )
#^^ "" ^^  
#9.
#Arvutame kolmnurga ümbermõõdu. Loo kolm täisarvulist muutujat a, b, c. Loo valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)

#10.
#Pitsa

 #   Võtsite P sõbraga suure pitsa hinnaga 12,90€
  #  Jätate teenindajale 10% jootraha
   # Koosta programm, mis leiab kui palju peab igaüks maksma
