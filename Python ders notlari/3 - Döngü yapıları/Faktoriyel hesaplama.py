while True:
    print("Çıkmak isterseniz 0")
    fak=int(input("Faktöriyel'ini bulmak istediğiniz sayıyı giriniz:  "))
    if fak==0:
        break
    for i in range(2,fak):
        fak*=i
        print(fak)