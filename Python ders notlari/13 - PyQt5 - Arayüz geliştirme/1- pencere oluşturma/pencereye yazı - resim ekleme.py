import sys
from PyQt5 import QtWidgets,QtGui#QtGui resim eklemye yarayan kutuphane

def Pencere():
    app=QtWidgets.QApplication(sys.argv)

    pencere=QtWidgets.QWidget()

    pencere.setWindowTitle("zarrrrrrrrrr")

    etiket=QtWidgets.QLabel(pencere)#yazı yazmak için oluşturulur ve nerde gorunecegi atanır

    etiket.setText("Bu bir label")#yazının ne olcagı belirlenir

    etiket.move(250,30)#yazyıyı istenilen konuma hareket ettirir

    resim=QtWidgets.QLabel(pencere)#resim eklemek içinde label objesi diye atanır

    resim.setPixmap(QtGui.QPixmap("indir.png"))#kutuphane yardımı ile istenilen resim atanır

    resim.move(50,50)#resmin hareket edecegi nokta

    pencere.setGeometry(300,300,600,600) #300*300 = uygulamanın konumu / 600*600 = uygulamanın boyutu

    pencere.show()

    sys.exit(app.exec_())
Pencere()