def bolenbul(sayi):
    tam=[]
    for i in range(2,sayi):
    
        if sayi%i==0:
            tam.append(i)
    return tam


while True:
    sayi=int(input("SAYI:  "))
    print("Tam Bölenler",bolenbul(sayi))