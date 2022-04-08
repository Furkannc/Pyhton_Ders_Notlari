import sqlite3 
con=sqlite3.connect("kütüphane.db") 
cursor=con.cursor()

def guncelle(isim):
    cursor.execute("delete from kitaplık where isim=?",(isim,))
    con.commit()

isim=input("silinmesini istediğini kitap adı: ")
guncelle(isim)
con.close()
print("Veri silindi")
