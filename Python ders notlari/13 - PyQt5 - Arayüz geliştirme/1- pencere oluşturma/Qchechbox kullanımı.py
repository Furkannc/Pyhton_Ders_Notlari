import sys
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QLabel,QCheckBox,QVBoxLayout

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
#Qvidgetin fonksyonionlarını miras olarak alamasını istiyoruz


    def init_ui(self):
        self.chcbox=QCheckBox("Python seviyor  musunuz?")
        self.yazzialan=QLabel("")
        self.buton=QPushButton("Bana tıkla")
        self.v_box=QVBoxLayout()
        self.v_box.addWidget(self.chcbox)
        self.v_box.addWidget(self.yazzialan)
        self.v_box.addWidget(self.buton)
#kendi fonksyionlarımızı ekliyoruz


        self.setLayout(self.v_box)

        self.setWindowTitle("Chceck box")

        self.buton.clicked.connect(lambda : self.click(self.chcbox.isChecked(),self.yazzialan))
    #buton bagla (fonk:clcik fonksyionuna tiklenme durumunu gonder,yazzialanano paylaş

        self.show()

    def click(self,chcbox,yazzialan):
        #eğerk deger true ise
        if chcbox:
            yazzialan.setText("Python hayattır")

        else:#false ise
            yazzialan.setText("Bruhhhhhhhhh")

app=QApplication(sys.argv)

pncr=Pencere()

sys.exit(app.exec())