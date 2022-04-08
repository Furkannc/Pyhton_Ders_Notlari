import os
import sys

from PyQt5.QtWidgets import QApplication,QAction,qApp,QMainWindow

class menu(QMainWindow):
    def __init__(self):
        super().__init__()

        menubar=self.menuBar()
        dosya=menubar.addMenu("Dosya")
        duzenle=menubar.addMenu("duzenle")

        dosya_ac=QAction("Dosya aç",self)
        dosya_ac.setShortcut("Ctrl+O")

        dosya_kaydet=QAction("Dosyayı kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+s")

        cikis=QAction("Çıkış",self)
        cikis.setShortcut("Ctrl+Q")

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(cikis)

        aravedegistir=duzenle.addMenu("Ara ve Değiştir")

        ara=QAction("Ara",self)

        degistir=QAction("Değiştir",self)

        aravedegistir.addAction(ara)
        aravedegistir.addAction(degistir)
        duzen

        self.setWindowTitle("Menüler")



        self.show()





app=QApplication(sys.argv)
mn=menu()
sys.exit(app.exec())