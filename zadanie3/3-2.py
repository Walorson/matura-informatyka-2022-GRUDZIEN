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

ile = 0
for liczba in wiersze:
    if czy_pierwsza(liczba - 1) == True:
        ile += 1

print(ile)