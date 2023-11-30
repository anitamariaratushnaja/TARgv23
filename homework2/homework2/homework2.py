print("Tere! olen sinu uus sober - Phyton!")
nimi=input("Mis su nimi on?")
print(f"{nimi}, oi kui ilus nimi!")
soov=input(f"{nimi}!Kas leian Sinu keha indeksi? 0-ei, 1-jah ")
try: 
    if soov=="1":
      pikkus=int(input("Mis pikkus sul on?"))
      mass=float(input("Kui palju sa kaalud?"))
      indeks=mass/(0.01*pikkus)**2
      print(f"Sinu keha indeks on: {indeks: .1f} ")
      if indeks<16: 
        print("Tervisele ohtlik alakaal")
      elif 16<=indeks<19:
        print("Alakaal")
      elif 19<=indeks<25:
        print("Normaalkaal")
      elif 25<=indeks<30:
        print("Ulekaal")
      elif 30<=indeks<35:
        print("Rasvumine")
      elif 35<=indeks<40:
        print("Tugev rasvumine")
      elif indeks>=40:
        print("Tervisele ohtlik rasvumine")
    else :
     print("Kahju! See on vaga kasulik info!")
     print()
  
   
except ValueError:
    print("Vigane sisend! Palun sisestage oiged andmed.")
   
print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")

