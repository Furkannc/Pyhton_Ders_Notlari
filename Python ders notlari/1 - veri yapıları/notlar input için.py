input() #ile alınır
input("bir sayı giriniz") #print yerine kullanılabilir 
a = input("bir sayı giriniz") #şeklinde kullanılması gerekir
print(a) #girilen deger STRİNG şeklinde alınır
a = int(input("sayı giriniz"))#şeklinde kullması gerekir
#girilen degerler bi rakam veya sayı değilse hata verir

try:
    a=a=int(input("a:"))
    print(a)
except ValueError:
print("lutfen bir sayı giriniz") #şeklinde hata engellenebilir
