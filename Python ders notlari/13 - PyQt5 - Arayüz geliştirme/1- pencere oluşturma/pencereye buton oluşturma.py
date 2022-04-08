import  sys
from PyQt5 import QtWidgets

def PENCERE():
    app=QtWidgets.QApplication(sys.argv)
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("PyQt5 button oluşturma")
    pencere.setGeometry(100,100,500,500)

    buton=QtWidgets.QPushButton(pencere)#butonu oluştur ve pencereye ata
    buton.setText("Tıkla") #butonun uzerindeki yazı
    buton.move(0,50) #butonun konumu

    yazı=QtWidgets.QLabel(pencere)
    yazı.setText("İŞTE BUNA SJ DERİM")
    pencere.show()

    sys.exit(app.exec_())






PENCERE()