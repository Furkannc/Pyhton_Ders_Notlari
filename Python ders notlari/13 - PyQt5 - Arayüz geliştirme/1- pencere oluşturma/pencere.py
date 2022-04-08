import sys
from PyQt5 import QtWidgets

def Pencere():
    app=QtWidgets.QApplication(sys.argv) #oluşturulan objeye qwidgetsin içiden
                                        # qapplication classını atadık  uygulamayı gorebilmek için gereklidir!
    pencere= QtWidgets.QWidget()#qwidget classının içinden pencere oluşturulur

    pencere.setWindowTitle("PyQt5 HII!")#başlık atandı
    pencere.show()#uyguamayı göster dedik
    sys.exit(app.exec_())#.exec_() fonksiyonu uygulamayı dönguye sokarak
                        #gormemizi sağlar

Pencere()#oluştuyrulan fonksyonu çağırıyorz