
print("""
*******************************
Not hesaplayıcı app
*******************************
""")
s1=float(input("1.Vize Notu: "))*30/100
s2=float(input("2.Vize Notu: "))*30/100
s3=float(input("Final Notu: "))*40/100
ort=s1+s2+s3
if(ort>=90):
    print("Notunuzun Harf Notu AA")
elif(ort>=80):
    print("Notunuzun Harf Notu BB")
elif(ort>=70):
    print("Notunuzun Harf Notu BC")
elif(ort>=60):
    print("Notunuzun Harf Notu CC")
elif(ort>=50):
    print("Notunuzun Harf Notu DD")
else:
    print("Kaldınız")
