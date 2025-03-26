plik = open("liczby.txt")
wiersze = plik.readlines()

wiersze = [int(x) for x in wiersze]

def czy_pierwsza(x):
    if x == 1:
        return False
    elif x == 2:
        return True

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
        
    return True

liczbaNajwiekszyRozklad = wiersze[0]
ileNajwiekszyRozklad = 0
liczbaNajmniejszyRozklad = wiersze[0]
ileNajmniejszyRozklad = 1000000

for liczba in wiersze:
    ile = 0
    for i in range(liczba - 1, liczba // 2, -2):
        if czy_pierwsza(i) == True and czy_pierwsza(liczba - i):
            ile += 1
    
    if czy_pierwsza(liczba - 2): #czy liczba 2 jest możliwa w rozkładzie?
        ile += 1

    if ile > ileNajwiekszyRozklad:
        ileNajwiekszyRozklad = ile
        liczbaNajwiekszyRozklad = liczba

    if ile < ileNajmniejszyRozklad:
        ileNajmniejszyRozklad = ile
        liczbaNajmniejszyRozklad = liczba

print(liczbaNajwiekszyRozklad, ileNajwiekszyRozklad, liczbaNajmniejszyRozklad, ileNajmniejszyRozklad)