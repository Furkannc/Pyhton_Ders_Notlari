import sys
import sqlite3
from PyQt5 import QtWidgets

class pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.baglanti_olustur()
        self.init_ui()

    def baglanti_olustur(self):
        baglanti=sqlite3.connect("database.db")
        self.cursor=baglanti.cursor()
        self.cursor.execute("Create Table If not exists uyeler (kullanici_ad TEXT,parola TEXT)")
        baglanti.commit()
    def init_ui(self):

        self.kullanici_ad=QtWidgets.QLineEdit()
        self.parola=QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris=QtWidgets.QPushButton("Giriş yap")
        self.yazi_alani=QtWidgets.QLabel("")

        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanici_ad)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)

        h_box=QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.setWindowTitle("Kullanıcı Giriş Paneli ")

        self.giris.clicked.connect(self.login)


        self.show()

    def login(self):

        kul =self.kullanici_ad.text()
        par =self.parola.text()

        self.cursor.execute("select * from uyeler where kullanici_ad=? and parola=?",(kul,par))

        data=self.cursor.fetchall()

        if len(data)==0:
            self.yazi_alani.setText("Giriş başarısız")
        else:
            self.yazi_alani.setText("Giriş başarılı")







app=QtWidgets.QApplication(sys.argv)

pncr=pencere()

sys.exit(app.exec())