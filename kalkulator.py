def get_info():
    print("Witaj to jest prosty kalkulator")

def dodaj(a,b):
    wynik = a + b
    return wynik

get_info()    
a = int(input())
b = int(input())
print(dodaj(a, b))

print("koniec programu")

def odejmij(a,b):
    wynik = a - b
    return wynik
