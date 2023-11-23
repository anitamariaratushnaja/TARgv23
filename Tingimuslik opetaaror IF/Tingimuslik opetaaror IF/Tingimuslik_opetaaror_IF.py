##1.a Kui eesnimi on Juku siis lähme Jukuga kinno.

#nimi=input("Kas sinu nimi on Juku?: ")
#if nimi=="jah":
#   print("Lähme kinno")
#else:
#    print("Ei lähe kinno")

##1.b Lisa valiku, kus Juku vanuse alusel otsustate mis pilet talle vaja osta.

##    <6 aastad  - tasuta
##    6-14 - lastepilet
##    15-65 - täispilet
##    >65 - sooduspilet
##    <0 ja >100 viga andmetega
#vanus = int(input("Mis on Juku vanus?: "))
#if vanus < 0 or vanus > 100:
#        print("Viga andmetega")
#elif vanus < 6:
#        print("Jukule on pilet tasuta")
#elif 6 <= vanus <= 14:
#        print("Jukule on vaja lastepiletit")
#elif 15 <= vanus <= 65:
#        print("Jukule on vaja täispiletit")
#else:
#        print("Jukule on vaja sooduspiletit") #elif (сокращение от "else if") используется в Python для проверки нескольких условий подряд. Когда у вас есть несколько условий, которые могут быть истинными, и вам нужно выполнить код блока, связанного с первым истинным условием, вы можете использовать elif.

##2 Küsi kahe inimese nimed ning teata, et nad on täna pinginaabrid
#nimi1=input("Mis sinu nimi on?: ")
#nimi2=input("Mis teine nimi on?: ")
#print(f"{nimi1} ja {nimi2} olete täna pinginaabrid")


#3 Küsi ristkülikukujulise toa seinte pikkused ning arvuta põranda pindala. Küsi kasutajalt remondi tegemise soov, kui ta on positiivne, siis küsi kui palju maksab ruutmeeter ja leia põranda vahetamise hind
#a=float(input("Mis esimine seine pikkus on?: "))
#b=float(input("Mis esimine teime pikkus on?: "))
#S=a*b 
#print(f"Põranda pindala on {S}")
#remont=input("Kas soovite teha remondi?(jah/ei): ")
#if remont=="jah":
#    hind=float(input("Kui palju maksab ruutmeeter?: "))
#    maksab=S*hind
#    print(f"Põranda vahetamise hind on {maksab}")
#else:
#    print("Heataega")

##4 Leia 30% hinnasoodustusega hinna, kui alghind on suurem kui 700
#alghind = float(input("Sisesta alghind: "))
#if alghind < 700:
   
#    soodustatud_hind = alghind - (alghind * 0.3)
#    print(f"30% soodustusega hind on {soodustatud_hind:.2f} eurot.")
#else:
#    print("Soodustust ei kehti, sest alghind on 700 eurot või vähem.")

#5 Küsi temperatuur ning teata, kas see on üle kaheksateistkümne kraadi (soovitav toasoojus talvel)
#temp=float(input("Mis temperatuur on?: "))
#if 18>temp<25:
#    print("See on soovitav toasoojus talvel ")
#elif temp>25:
#    print("Liiga palav!")
#else:
#    print("See on külm ")


#6 Küsi inimese pikkus ning teata, kas ta on lühike, keskmine või pikk (piirid pane ise paika)
#pikk=float(input("Tere! Mis on sinu pikkus?: "))
#if pikk<150:
#  print("Ma arvan sa oled lühike")
#elif 150<pikk<180:
#  print("Ma arvan sa oled keskmine")
#elif pikk>=180:
#  print (" Ma arvan sa oled pikk")
#else:
#  print()

#7 Küsi inimeselt pikkus ja sugu ning teata, kas ta on lühike, keskmine või pikk (mitu tingimusplokki võib olla üksteise sees).

##8 Küsi inimeselt poes eraldi kas ta soovib osta piima, saia, leiba. Löö hinnad kokku ning teata, mis kõik ostetud kraam maksma läheb.
#soovib_piima = input("Kas soovite osta piima? (jah/ei): ")
#soovib_saia = input("Kas soovite osta saia? (jah/ei): ")
#soovib_leiba = input("Kas soovite osta leiba? (jah/ei): ")


#hind_piim = 1.5  
#hind_saia = 2.0  
#hind_leiva = 2.5  

## Algse summa määramine
#kogusumma = 0

## Arvuta ja lisa summa vastavalt kasutaja valikule
#if soovib_piima.lower() == "jah":
#    kogusumma += hind_piim

#if soovib_saia.lower() == "jah":
#    kogusumma += hind_saia

#if soovib_leiba.lower() == "jah":
#    kogusumma += hind_leiva

## Prindi kogusumma
#print(f"Teie ostude kogusumma on {kogusumma} eurot.")


#9 Ruut

#        Kasutaja sisestab ruudu küljed ning programm tuvastab kas tegemist saab olla ruuduga.
#        Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.

#a1= float(input(" 1 külje: "))
#a2= float(input(" 2 külje: "))
#a3= float(input(" 3 külje: "))
#a4= float(input(" 4 külje: "))

#if a1==a2==a3==a4:
#    print("See on ruut")
#else:
#    print("See ei ole ruut")


#    10 Matemaatika
#        Kasutaja sisestab kaks arvu ning programm küsib kasutajalt, mis tehet ta soovib (+-*/) ning viib kasutaja valiku ellu.
#        Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.

#try:
#    a=float(input("Esimine arv:"))
#    try:
#        b=float(input("Teine arv:"))
#        t=input("Tehe(+-*/):")
#        if t in['+','-','/','*']: #""=''
#            if t=='+':
#                v=a+b
#            elif t=='-':
#                v=a-b 
#            elif t=='*' :
#                v=a*b 
#            elif t=='/':
#                 v=a/b
#            else:
#                v=a//b 

#            print("{0}{1}{2}={3}".format (a,t,b,v))


#        else:
#            print("Tundmatu märk")
#    except:
#        print("Vale b arvu andmetüüp")
#except:
#    print("Vale a arvu andmetüüp")

#    11 Juubel
#        Kasutaja sisestab oma sünnipäeva ja sinu programm ütleb, kas tegemist on juubeliga.
#        Plokkskeemi pole vaja!

from datetime import date
sp=date(int(input("Sünniaasta")), int(input("Sünnikuu")), int(input("Sünnipäeva")))
praegu=date.today().year 
if(praegu-sp.year)%10==0:
    print("Juubel")
else:
    print("ei ole juubel")

#    12 Müük
#        Kasutaja sisestab toote hinna. Kui see on hinnaga kuni 10€, saab ta allahindlust 10%. Üle 10€ tooted saavad soodukat 20%.
#        Kuva toote lõplik hind. Plokkskeemi pole vaja!
#    13 Jalgpalli meeskond
#        Sa pead looma programmi, mis kontrollib kas kandideerija sobib antud meeskonda.
#        Vanus peab jääma vahemikku 16-18 ning lubatud on ainult meessugu.
#        Täienda programmi nii, et kui kandideerija on naissoost, siis vanust üldse ei küsita
#    14
#    Busside logistika
