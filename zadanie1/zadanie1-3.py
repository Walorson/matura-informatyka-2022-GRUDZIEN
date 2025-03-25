plik = open("mecz_przyklad.txt")
wiersz = plik.readline()

passaA = 0
passaB = 0
najPassaA = 0
najPassaB = 0
ilePassA = 0
ilePassB = 0
nieLiczA = 0
nieLiczB = 0

for i in wiersz:
    if i == 'A':
        passaA += 1
        if passaB > najPassaB:
            najPassaB = passaB

        if passaA >= 10 and nieLiczA == False:
            ilePassA += 1
            nieLiczA = True

        nieLiczB = False
        passaB = 0

    elif i == 'B':
        passaB += 1
        if passaA > najPassaA:
            najPassaA = passaA
            
        if passaB >= 10 and nieLiczB == False:
            ilePassB += 1
            nieLiczB = True
            
        nieLiczA = False
        passaA = 0

print("LICZNIK DOBRYCH PASS: ", ilePassA, ilePassB)
print("NAJWIEKSZA PASSA:", najPassaA, najPassaB)