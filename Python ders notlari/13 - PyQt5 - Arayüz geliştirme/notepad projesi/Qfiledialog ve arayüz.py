import sys
import os
from PyQt5.QtWidgets import QWidget,QLabel,QVBoxLayout,QApplication,QTextEdit,QPushButton,QFileDialog,QHBoxLayout


class notepad(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.yazialan=QTextEdit()
        self.temizle=QPushButton("Temizle")
        self.ac=QPushButton("Aç")
        self.kaydet=QPushButton("kaydet")

        self.h_box=QHBoxLayout()

        self.h_box.addWidget(self.temizle)
        self.h_box.addWidget(self.ac)
        self.h_box.addWidget(self.kaydet)

        self.v_box=QVBoxLayout()

        self.v_box.addWidget(self.yazialan)
        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)

        self.setWindowTitle("Notepad")

        self.temizle.clicked.connect(self.sil)
        self.ac.clicked.connect(self.dosyaac)
        self.kaydet.clicked.connect(self.dosyakaydet)

        self.show()

    def sil(self):##################
        self.yazialan.clear()

    def dosyaac(self):#######################
        dosyaad=QFileDialog.getOpenFileName(self,"Dosya ac",os.getenv("Desktop"))
        with open(dosyaad[0],"r") as file:
            self.yazialan.setText(file.read())
    def dosyakaydet(self):#######################
        dosyaad = QFileDialog.getSaveFileName(self, "Dosya kaydet", os.getenv("Desktop"))
        with open(dosyaad[0], "w") as file:
            file.write(self.yazialan.toPlainText())





app=QApplication(sys.argv)
note=notepad()
sys.exit(app.exec())