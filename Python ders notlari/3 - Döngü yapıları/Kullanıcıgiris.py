sys_kad="admin"
sys_parola="admin1"
hak=3
print("""
*******************
Giriş Paneli
*******************
""")
while True:
    kadi=input("Kullanıcı adı: ")
    parola=input("Parola: ")
    if kadi==sys_kad and parola!=sys_parola:
        print("Parola Hatalı")
        hak-=1
    elif kadi!=sys_kad and parola==sys_parola:
        print("Kullanıcı adi Hatalı")
        hak-=1
    elif kadi!=sys_kad and parola!=sys_parola:
        print("Hatalı Kullanıcı adı ve Parola")
        hak-=1
    else:
        print("Başarıyla Giriş Yaptınız")
        break
    if hak==0:
        print("Giriş Hakkınız Bulunmamaktadır")
        break
