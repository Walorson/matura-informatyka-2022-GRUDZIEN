plik = open("mecz.txt")
wiersz = plik.readline()

wynikA = 0
wynikB = 0

for i in wiersz:
    if i == 'A':
        wynikA += 1
    elif i == 'B':
        wynikB += 1

    if (wynikA >= 1000 or wynikB >= 1000) and abs(wynikA - wynikB) >= 3:
        break

print(wynikA, wynikB)