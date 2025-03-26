plik = open("liczby.txt")
wiersze = plik.readlines()

def hex(x):
    liczba = ""
    while x > 0:
        n = x % 16

        if n == 10:
            n = "A"
        elif n == 11:
            n = "B"
        elif n == 12:
            n = "C"
        elif n == 13:
            n = "D"
        elif n == 14:
            n = "E"
        elif n == 15:
            n = "F"

        liczba += str(n)

        x //= 16
    
    return liczba[::-1]

wiersze = [hex(int(x)) for x in wiersze]

wiersze = "".join(wiersze)

hexZnaki = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

for i in hexZnaki:
    print(i, ":", wiersze.count(i))