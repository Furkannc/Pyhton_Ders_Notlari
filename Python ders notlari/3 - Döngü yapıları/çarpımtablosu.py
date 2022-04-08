liste=list()
say=int(input("Hangi Tabloyu İstersiniz: 'Sayı'  "))
kac=int(input("Tablo Boyu 'Sayı'  "))

for i in range(kac):
    liste.append(i+1)
for i in liste:
    print(i," x ",say,":",i*say)
