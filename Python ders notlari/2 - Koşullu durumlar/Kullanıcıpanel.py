sys_kad="admin"
sys_sifre="admin"
print("kullanıcı giris paneline hoşgeldiniz")
kad=input("Kullanıcı adınızı giriniz:  ")
sifre=input("Şifrenizi giriniz:  ")
if sys_kad==kad and sys_sifre==sifre:
    print("Giriş başarılı")
elif sys_kad==kad and sys_sifre!=sifre:
    print("Şifre Hatalı")
elif sys_kad!=kad and sys_sifre==sifre:
    print("Hatalı Kullanıcı adı")
else:
    print("Hatalı kullanıcı adı ve Şifre")
    
