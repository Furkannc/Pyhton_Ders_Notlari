#   Tablodaki veriler çekme   #

import sqlite3 
con=sqlite3.connect("kütüphane.db") 
cursor=con.cursor()

def verileri_al():
    cursor.execute("select * from kitaplık")
    liste=cursor.fetchall()
    #imleçdeki fetchall() metodu ile  butun verileri bize verir bizde bunu listeye atıyoruz
    #herhangi bi deger ataması olmadıgı için bizim commit() metoduna ihtiyacımız yok
    print("Kitaplık tablosu bilgileri...")
    for i in liste:
        print(i)
    #istenirse direk olarak print(liste) şeklinde kullanılabilir
def yayinevinegore(yayinevi):
    cursor.execute("select * from kitaplık where yayinevi=?",(yayinevi,))
    liste=cursor.fetchall()
    print("Yayınevine gore arama")
    for i in liste:
        print(i)
    
def isimegore(isim):
    cursor.execute("select * from kitaplık where isim=?",(isim,))
    liste=cursor.fetchall()
    print("İsime gore arama")
    for i in liste:
        print(i)
    
    
def yazaragore(yazar):
    cursor.execute("select * from kitaplık where yazar=?",(yazar,))
    liste=cursor.fetchall()
    print("yazaragore gore arama")
    for i in liste:
        print(i)

def sayfasayısına(ss):
    cursor.execute("select * from kitaplık where sayfasayisi>?",(ss,))
    liste=cursor.fetchall()
    print("Sayfa sayısına gore arama")
    for i in liste:
        print(i)

print("""Yayınevine gore aramak için ---------1
Kitap ismine gore aramak için --------2
Yazara gore aramak için --------3
Sayfa sayısına gore aramak için --------4
Çıkış için ---------x>5
          """)
while True:
    a=input("Seçiminiz: ")
    if a=="1":
        yayinevi=input("Yayınevi adı giriniz: ")
        yayinevinegore(yayinevi)
    elif a=="2":
        isim=input("Kitap ismi giriniz: ")
        isimegore(isim)
    elif a=="3":
        yazar=input("Yazar adı giriniz: ")
        yazaragore(yazar)
    elif a=="4":
        ss=int(input("Kaç sayfadan fazla olanları aramak isterseniz: "))
        sayfasayısına(ss)
    else:
        break

con.close()
