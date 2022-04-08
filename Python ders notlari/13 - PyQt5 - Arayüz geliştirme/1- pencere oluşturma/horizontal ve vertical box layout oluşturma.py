import sys
from PyQt5 import QtWidgets

def PENCERE():
    app=QtWidgets.QApplication(sys.argv)

    #PENCERE OLUŞTURULUR
    pencere=QtWidgets.QWidget()
    pencere.setWindowTitle("ders 4")
    pencere.setGeometry(100,100,1000,600)
    #BUTONLAR OLUŞTURULUR
    okay=QtWidgets.QPushButton("OK")
    cancel=QtWidgets.QPushButton("CNC")

    #VERTİCAL LAYOUT OLUŞTURMA
    v_box=QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addWidget(okay)
    v_box.addWidget(cancel)

    #HORİZONTAL LAYOUT OLUŞTURMA
    H_BOX=QtWidgets.QHBoxLayout()#H box adında horizontal layout oluşturulur
    H_BOX.addStretch()  # addstretch fonksiyonu boşluk bırakır nereye yazılırsa oraya bırakır boşlugu
    #iki butonda layouta eklenir
    H_BOX.addWidget(okay)
    H_BOX.addWidget(cancel)



    #İKİSİNİ AYNI ANDA KULLANMA
    v_box.addLayout(H_BOX)
    pencere.setLayout(v_box)#en sonra ise pencere atanır layoutlar


    pencere.show()
    sys.exit(app.exec_())

PENCERE()