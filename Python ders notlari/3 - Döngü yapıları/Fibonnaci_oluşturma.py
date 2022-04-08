a=1
b=1
fib=[a,b]
for i in range(10):#seri sayısı
    print("A: ",a,"B: ",b)
    a,b=b,a+b#a'ya b'nin eski değeri b'ye de a+b'yi veriyoruz
    fib.append(b)
print("Liste: ",fib)
