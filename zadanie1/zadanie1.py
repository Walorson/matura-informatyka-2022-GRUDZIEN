plik = open("mecz.txt")
wiersz = plik.readline()

ile = 0
druzyna = "B"
for i in wiersz:
    if i != druzyna:
        ile += 1
        druzyna = i

print(ile)