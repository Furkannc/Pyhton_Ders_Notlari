print(""""**********
Hesap makinesi Programı
1.Toplama işlemi
2.Çıkarma işlemi
3.Çarpma işlemi
4.Çarpma işlemi
**********""")

s1=int(input("1.SAYI:  "))
s2=int(input("2.SAYI:  "))
işlem=input("Lütfen seçim yapınız:  ")
if(işlem=="1"):
    print("{} İle {} Toplamı {}'dir".format(s1,s2,s1+s2))
elif(işlem=="2"):
    print("{} ile {} Kalanı {}'dir".format(s1,s2,s1-s2))
elif(işlem=="3"):
    print("{} ile {} Çarpımı {}'dir".format(s1,s2,s1*s2))
elif(işlem=="4"):
    print("{} ile {} Bölümü {}'dir".format(s1,s2,s1/s2))
else:
    print("Hatalı İşlem")
