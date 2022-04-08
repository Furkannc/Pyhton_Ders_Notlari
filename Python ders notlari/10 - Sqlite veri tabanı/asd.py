import sqlite3 

con=sqlite3.connect("manitaiti.db") 
cursor=con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE furkan (isim TEXT,yas int)")
    con.commit()

tablo_olustur() #şeklinde de fonkisyonu kullanıyoruz
con.close()