import  sys
from PyQt5 import QtWidgets

class pencere(QtWidgets.QWidget):#miras alma işlemini kullancaz pencere için
    def __init__(self):
        super().__init__() #Qwidget içindeki butun fonksiyonları miras alıyoruz

        self.init_ui()

    def init_ui(self):#kendi fonksiyonumzuu ekliyoruz
        self.yazı_alanı=QtWidgets.QLineEdit() #yazı alanı
        self.temizle=QtWidgets.QPushButton("Temizle") #temizle butonu
        self.yazdır=QtWidgets.QPushButton("Yazdır") #yazdır butonu


        v_box=QtWidgets.QVBoxLayout() #vertical box oluşturma

        v_box.addWidget(self.yazı_alanı)
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.yazdır)
        v_box.addStretch()
        #vertical boxa degerleri ekleme
        self.setLayout(v_box)
        #pencereye vertical boxı atamak

        self.temizle.clicked.connect(self.click)#temizlye basılırsa self click fonksiyonuna bağlıyoruz
        self.yazdır.clicked.connect(self.click)#yazdıra basılırsa self click fonksiyonuna bağlıyoryz

        self.show()#pencereyi goster diyoruz

    def click(self): #click fonksiyonunu oluştur
        sender=self.sender()#sender komutu ile click olayında buton uzerindeki yazıyı alıyoruz

        if sender.text()=="Temizle": #sender komutuna aldığımız yazıya eşit olura
            self.yazı_alanı.clear() #yazı alanını siler
        else:
            print(self.yazı_alanı.text()) #komut satırına yazı alananı yazar





app=QtWidgets.QApplication(sys.argv) #uygulama oldugunu belirtiyoruz
pncr=pencere() #pencere oluştururken class sınıfından alıyoruyz
sys.exit(app.exec_()) #çıkış yapmak için app uzerinden çıkış veriyyoruz
