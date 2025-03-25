plik = open("pary.txt")
wiersze = plik.readlines()

wiersze = [x.strip() for x in wiersze if x.strip() != ""]

N = 100000

def rysuj(x):
    if 2*x == b or 2*x + 1 == b:
        print(a, b)

    if 2*x <= N:
        rysuj(2*x)
    if 2*x + 1 <= N:
        rysuj(2*x + 1)

for wiersz in wiersze:
    wiersz = wiersz.split(" ")
    a = int(wiersz[0])
    b = int(wiersz[1])

    rysuj(a)