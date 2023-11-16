print("Tere tulemast!" .center(50))
kool=input("Mis koolis sa õpid?: ").capitalize() #str kool
kursus=int(input("\tMis kuursusel?: ")) # int kursus
print("Tere tulemast kooli "+kool+"!\nole hea "+str(kursus)+" .kursuse õpilaseks!")
print("Tere tulemast kooli" ,kool.upper(), "!\nole hea" ,kursus, " .kuursuse õpilaseks!")
print("Tere tulemast kooli {0}!\nole hea {1} .kuursuse õpetajaks!" .format(kool,kursus))  #koo="Tthk"
print(type(kool))
print(type(kursus))
arv1=float(input("Arv1: "))
arv2=float(input("Arv2: "))
print("Summa{0}+{1}={2}".format(arv1,arv2,arv1+arv2)) #summa
print("Summa{0}-{1}={2}".format(arv1,arv2,arv1-arv2)) #lahutamine
print("Summa{0}*{1}={2}".format(arv1,arv2,arv1*arv2)) #korrutis
print("Summa{0}/{1}={2}".format(arv1,arv2,arv1/arv2)) #jagamine
print("Summa{0}astmes{1}={2}".format(arv1,arv2,arv1**arv2)) #astendamine
print("Summa{0}ja{1}jääk={2}".format(arv1,arv2,arv1%arv2)) #jagamisjääk
print("Summa{0}ja{1}jagamise täis osa{2}".format(arv1,arv2,arv1//arv2)) #
tehe=input("Mida teha: ")
v=eval(str(arv1)+tehe+str(arv2))
print(v)