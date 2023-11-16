import math #import * from math
print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => ")) #float "
S=a**2 #*
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P) #"
di=a*math.sqrt(2) #sqrt
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #()
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #float
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) #float
S=b*c
print("Ristküliku pindala", S) #"
P=2*(b+c) #*
print("Ristküliku ümbermõõt", P)
di=math.sqrt(b**2+c**2) #*
print("Ristküliku diagonaal", round(di,2)) #roun(di,2)
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => ")) #float ""
d=2*r #*
print("Ringi läbimõõt", d) #,
S=math.pi*r**2 #S=math.pi*r**2
print("Ringi pindala", round(S,2)) #round(S,2)
C=2*math.pi*r #C=2*math.pi*r
print("Ringjoone pikkus", round(C,2)) #round(C,2))
