#update- yuzde alma
class HesapMakinesi:
    def __init__(self):
        pass
    
    def menu_goster(self):
        print("lutfen islem seciniz")
        print("1. toplama")
        print("2. çıkarma")
        print("3. çarpma")
        print("4. bölme")
        print("5. yüzde")
        print("6. çıkış")
    
    def toplama(self, s1, s2):
        
        return s1 + s2
    
    def cikarma(self, s1, s2):
        return s1 - s2
    
    def carpma(self, s1, s2):
        return s1 * s2
    
    def bolme(self, s1, s2):
        if s2 == 0:
            return "sıfıra bölünemez"
        else:
            
            return s1 / s2
    
    
    def yuzde(self, s1, yuzde):
        return s1 * (yuzde / 100)
    
    
    
    def hesapla(self):
        while True:
            self.menu_goster()
            
            secim = input("seçiminizi girin: ")
            
            if secim == '6':
                print("çıkış yapi")
                break
            
            if secim in ('1', '2', '3', '4', '5'):
                s1 = float(input("birinci sayıyı girin: "))
                #sıkıntı 
                if secim != '5':
                    s2 = float(input("ikinci sayıyı girin: "))
                
                if secim == '1':
                    
                    print("sonuc:", self.toplama(s1, s2))
                elif secim == '2':
                    
                    print("sonuc:", self.cikarma(s1, s2))
                elif secim == '3':
                    
                    print("sonuc:", self.carpma(s1, s2))
                elif secim == '4':
                    
                    print("sonuc:", self.bolme(s1, s2))
                elif secim == '5':
                    
                    yuzde_sayi = float(input("yüzdeyi girin: "))
                    print("sonuc:", self.yuzde(s1, yuzde_sayi))
            else:
                print("Hata:lutfen 1,23,4,5 içinden bir sayi girin.______hata_____")

hm = HesapMakinesi()
hm.hesapla()
