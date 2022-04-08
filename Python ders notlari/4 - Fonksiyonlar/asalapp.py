def asalmi(sayi):
    if sayi==1:
        return False
    elif sayi==2:
        return  True
    else:
        for i in range(2,sayi):
            if sayi%i==0:
                return False
        return True
while True:
    sayi=int(input("Asal olup olmadığını Bulmak istediğiniz sayı:  "))
    
    if asalmi(sayi):
        print(sayi," Asal bir sayıdır")
        
    else :
        print(sayi,"asal bir sayı değildir")
        
