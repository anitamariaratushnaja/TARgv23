##Võileb
#soov=input("Kas tahad süüa?: ") .lower()
#if soov=="jah" or sov=="yes":
#   valik=int(input("1-juustuga võileb\n2-vorstiga võileb"))
#   if valik in[1,2]:
#       if valik==1:
#        print("Palun juustuga võileib")
#       else:
#           print("Palun vorstiga")
#   else:
#       print("vale valik")
#else:
#    print("Ei taha siis ei taha")




#Имеется кусок ткани длиной М метров. От него последовательно отрезаются куски разной длины. Все данные по использованию ткани заносятся в компьютер. Компьютер должен выдать сообщение о том, что материала не хватает, если будет затребован кусок ткани, большей длины, чем имеется. 
from hashlib import md5


m=1000
print(f"Meil on {m} meetri tekstiili")
m1=input("Kas ostate kõik?: ")
if m1=="jah":
    print("Müüdut")
else: 
    print(f"Jäänud {m} meetri tekstiili")
    m2=int(input("Kui palju soovite?: "))
    m3=m-m2 
    print(f"Meil on {m3} meetri tekstiili")
    m4=input("Kas soovite veel?: ")
    if m4=="jah":
        m5=int(input("Kui palju soovite?: ")) 
        m6=m3-m5 

    else:
     print("Aitäh")
    







#Toetus
#x=input("Mis gruppis sa õppid?: ") #sprashivaem
#if x=="TARgv23": #esli budet TARgv23 to perehodim k sledujushemu voprosu, esli net to stroka 14
#   y=int(input("Mittu puudumised?: "))
#   if y<15:
#    z=float(input("Mis on keskmine hinne?: "))
#    if z>3.8:
#        print("Toetus!")
#    else:
#        print("Liiga madal keskmine hind, toetus ei anna!")
#   else:
#       print("Toetus ei saa")

#else:
#    print("Rühma nimetus ei sobi")

#x=input("Mis gruppis sa õppid?: ")
#y=int(input("Mittu puudumised?: "))
#z=float(input("Mis on keskmine hinne?: "))
#if x=="TARgv23" and y<15 and z>3.8:
#    print("Toetus!")
#else:
#    print("Toetus ei saa")


## Kalkulaator
#try:
#    a=float(input("Esimine arv:"))
#    try:
#        b=float(input("Teine arv:"))
#        t=input("Tehe:")
#        if t in['+','-','/','*','**','%','//']: #""=''
#            if t=='+':
#                v=a+b
#            elif t=='-':
#                v=a-b 
#            elif t=='*' :
#                v=a*b 
#            elif t=='**':
#                v=a**b 
#            elif t=='%':
#                v=a%b 
#            elif t=='/':
#                if b==0:
#                 v="DIV/0"
#            else:
#                v=a//b 

#            print("{0}{1}{2}={3}".format (a,t,b,v))


#        else:
#            print("Tundmatu märk")
#    except:
#        print("Vale b arvu andmetüüp")
#except:
#    print("Vale a arvu andmetüüp")






##Kolmnurk 

#a=float(input("Alpha:"))
#b=float(input("Betta:"))
#c=float(input("Gamma:"))
#if a>0 and b>0 and c>0:
#    if a+b+c==180:
#       print("Kolmnurk")
#    else:
#        print("Nurgad")
#else: 
#    print("Andmed ei ole õiged")


