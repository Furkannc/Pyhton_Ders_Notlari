import dortislem

print("""
**************
Hesap Makinesi
1- Toplama
2- Çıkarma
3- Çarpma
4- Bölme
**************
""")
while True:
    a = int(input("İlk Sayı:  "))
    b = int(input("İkinci Sayı  "))
    sec=input("Seçim Yapınız")
    if sec=="1":
        print("İlk Sayı ile İkinci Sayının Toplamı: ",dortislem.topla(a,b))
    elif sec=="2":
        print("İlk Sayı ile İkinci Sayının Toplamı: ",dortislem.cikar(a,b))
    elif sec=="3":
        print("İlk Sayı ile İkinci Sayının Toplamı: ",dortislem.carp(a,b))
    elif sec=="4":
        print("İlk Sayı ile İkinci Sayının Toplamı: ",dortislem.bol(a,b))
        
    
