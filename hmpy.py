while True:
    print("İslem")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    print("5. exit")
    s = input("Seciminizi girin (1/2/3/4/5): ")
    if s in ('1', '2', '3', '4'):
        sayi1 = float(input("Birinci sayıyı gir: "))    
        sayi2 = float(input("İkinci sayıyı gir: "))
        if s == '1':
            print("sonuc:", sayi1 + sayi2)
        elif s == '2':
            print("sonuc:", sayi1 - sayi2)
        elif s == '3':
            print("sonuc:", sayi1 * sayi2)
        elif s == '4':
            if sayi2 == 0:
                print("sıfıra bolunmuyor")
            else:
                print("Sonuc:", sayi1 / sayi2)
    elif s == '5':
        print("cıkıs yapılıyor")
        break
    else:
        print("lutfen aralıkta bir rakam secin")