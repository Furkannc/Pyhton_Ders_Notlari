import sqlite3 
con=sqlite3.connect("kütüphane.db") 
cursor=con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (isim TEXT,yazar TEXT,yayinevi TEXT,sayfasayisi İNT)")
    con.commit()
def veri_ekle(isim,yazar,yayinevi,sayfasayisi):
    cursor.execute("insert into kitaplık values (?,?,?,?)",(isim,yazar,yayinevi,sayfasayisi))
    con.commit()

tablo_olustur()
isim=input("Kitap ismi giriniz: ")
yazar=input("Yazar ismi giriniz: ")
yayinevi=input("Yayınevi adı: ")
sayfasayisi=int(input("Sayfa sayısı: "))
veri_ekle(isim,yazar,yayinevi,sayfasayisi)
con.close()
print("Kitap Kayıt Edildi")
