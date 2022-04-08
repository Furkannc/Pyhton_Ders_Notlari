import random
import time

tahmin_sayi=random.randint(1,50)
hak=8
print("""
************************25******
1-50 ArasındaSayı Tahmin Oyunu
******************************
""")

while True:
    tahmin=int(input("Tahmininiz Nedir? :  "))
    if tahmin < tahmin_sayi:
        print("Hmmmmmmmm")
        time.sleep(1)
        print("Daha Yuksek Bi Sayı")
        hak-=1
    elif tahmin > tahmin_sayi:
        print("Hmmmmmmmm")
        time.sleep(1)
        print("Daha Düşük Bi Sayı")
        hak -= 1
    else:
        print("Hmmmmmmmm")
        time.sleep(1)
        print("Tebrikler! Tahminiz Doğru.  ",tahmin_sayi)
        break
    if hak==0:
        print("Görünüşe Göre Tahmin Hakkınız Kalmamış")
        print("Tahmin Edilmesi Gereken Sayı:  ",tahmin_sayi)
        break