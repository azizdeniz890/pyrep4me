def faktoriyel(s):
    
    if s == 0: #s 0 sa 1 degeri dondur
        return 1
    
    else:
        return s * faktoriyel(s-1)#faktoriyel islemi

sayi = int(input("Sayi giriniz: "))

print(sayi, "sayisinin faktoriyeli:", faktoriyel(sayi))