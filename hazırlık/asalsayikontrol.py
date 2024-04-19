from sympy import isprime

sayi = int(input("Lutfen bir sayi giriniz: "))

if isprime(sayi):
    print(sayi, "sayisi bir asal sayidir.")
else:
    print(sayi, "sayisi asal degildir.")

"""
def asal(s):
    if s <= 1:
        return False#oto asal degil
    
    for i in range(2, int(s**0.5) + 1):
        
        if s % i == 0:
            return False
    return True

sayi = int(input("Lutfen bir sayi giriniz: "))

if asal(num):
    print(sayi, "sayisi bir asal sayidir.")
else:
    print(sayi, "sayisi asal degildir.")
"""
