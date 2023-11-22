#1
# print("Tervitan sind!")
# nimi=input("Mis su nimi on? ")
# print("Tervitan sind, ", nimi)

 #2
# arve = 3 + 8 / (4 - 2) * 4
# print(" Оригинальный Результат выражения 3 + 8 / (4 - 2) * 4 =", arve)
# arve = 3 + 8 / 4 - 2 * 4
# print(" Без скобок, Результат выражения 3 + 8 / 4 - 2 * 4 =", arve)
# arve = (3 + 8) / 4 - 2 * 4
# print(" С измененным положением, Результат выражения (3 + 8) / 4 - 2 * 4 =", arve)
# arve = (3 + 8) / (4 - 2) * 4
# print(" С добавленными скобками, Результат выражения (3 + 8) / (4 - 2) * 4 =", arve)
# При использование/неиспользование круглых скобок выражение меняется

#3
import math

# # radius kruga raven 3
# r=3
# #ploshad kruga
# S_krug= math.pi*r**2
# #perimetr kruga
# P_krug=2*math.pi*r
# #storona kvadrata a
# a=2*r
# #ploshad kvadrata
# S_kv=a**2
# #Perimetr kvadrata
# P_kv=4*a
# print(f"ploshad kvadrata: {S_kv}")
# print(f"Perimetr kvadrata: {P_kv}")
# print(f"ploshad kruga {S_krug}")
# print(f"perimetr kruga: {P_krug}")

#4

# #Найти радиус окружности Земли c=2pir
# r=6378
# C=2*math.pi*r
# #монета
# eur=2
# #сколько монет нужно
# vaja= C/eur
# print(f"Длина окружности Земли над экватором: {C:.2f} км")# 2f Форматирование строки с использованием :.
# # 2f означает, что мы хотим отформатировать число, чтобы оно было представлено с фиксированным количеством десятичных 
# # знаков после точки (две цифры после запятой в данном случае).
# print(f"Количество монет {eur} евро, чтобы покрыть длину окружности: {int(vaja)} монет") 

# #5 

# word1 = "kill"
# word2 = "koll"
# word3 = "killadi"

# words_list = [word1, word2, word3, word2, word1, word2, word3, word2, word1, word2, word3, word2, word1, word2]
# output = " ".join(words_list)
# print(output)

# # join - метод строки, который берет список строк и объединяет их в одну строку.
# # " ".join(words_list) - это вызов метода join для строки с разделителем, представленным пробелом. Это означает, что каждый элемент списка будет разделен пробелом при объединении.

#6

# def print_laul(): #Ключевое слово def в Python используется для определения функций. 
#     #Функции позволяют упростить код, разбивая его на более мелкие блоки, которые могут быть 
#     #многократно использованы.
#     print("Rong see sõitis tsuhh tsuhh tsuhh,")
#     print("piilupart oli rongijuht.")
#     print("attad tegid rat tat taa,")
#     print("rat tat taa ja tat tat taa.")
#     print("Aga seal rongi peal,")
#     print("kas sa tead, kes olid seal?")
# print_laul()

# # Вывод разделителя
# print("\n" + "=" * 40 + "\n") #Строка-разделитель, как в примере "\n" + "=" * 40 + "\n", 
# #часто используется для визуального разделения различных частей вывода в консоли или в файле. 
#  #Это может улучшить читаемость и восприятие информации.

# # В данном случае:

# # "\n" добавляет символ новой строки перед строкой-разделителем, чтобы он отобразился на новой строке.
# # "=" * 40 создает строку, состоящую из 40 символов "=".
# # "\n" добавляет еще один символ новой строки после строки-разделителя.

# # Изменение текста для второй песни
# def print_laul2():
#     print("Rong see sõitis tuut tuut tuut,")
#     print("piilupart oli rongijuht.")
#     print("Rattad tegid kill koll koll,")
#     print("kill koll koll ja kill koll kill.")

# print_laul2()

# #7 Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused ning 
# #väljastab ekraanile ristküliku ümbermõõdu ja pindala.

# a=float(input("Ristiküliku a= "))
# b=float(input("Ristiküliku b= "))
# c=float(input("Ristiküliku c= "))
       
# S=(a + b + c) / 2
# P= a + b + c

# print(f"Ristiküliku ümbermõõde on: {S} ja pindala on: {P}")

# #8Расчет расхода топлива
# # Пользователь вводит количество заправленного топлива в литрах
# #      Пользователь вводит пройденные километры
# #      Программа находит средний расход топлива на 100 км.

# toplivo=float(input("количество заправленного топлива в литрах: "))
# km=float(input("пройденные километры: "))
# rashod= (toplivo/km)*100
# print("средний расход топлива на 100 км : ",rashod)

#9 Rulluisutajad
    # Rulluisutaja keskmine kiirus on 29,9km/h
    # Kui kaugele jõuab M minutiga

# kmh= 29.9
# M=kmh/60
# print(f"Ta jõuab {M: .2f} minutiga")

#10Задача 8
# Преобразование времени

#      Пользователь вводит время в минутах
#      Ваша формула находит и выводит часы и минуты.
#      Например: ввод 72, ответ 1:12.

t=int(input("вводи время в минутах: "))
hours=t//60 #Оператор // в Python выполняет деление с округлением вниз (целочисленное деление). 
#Он возвращает целую часть результата деления.
minutes=t% 60
print(f"{hours}:{minutes}")















