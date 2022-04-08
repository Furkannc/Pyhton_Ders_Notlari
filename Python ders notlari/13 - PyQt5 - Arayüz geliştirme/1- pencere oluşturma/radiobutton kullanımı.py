import  sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QRadioButton

class Pencere(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.rb_yaz=QLabel("Hangi dili daha çok seviyorsun")
        self.rb1=QRadioButton("C#")
        self.rb2=QRadioButton("Python")
        self.rb3=QRadioButton("Java")

        self.yazi=QLabel("")

        self.buton=QPushButton("Seç")

        self.v_box=QVBoxLayout()

        self.v_box.addWidget(self.rb_yaz)
        self.v_box.addWidget(self.rb1)
        self.v_box.addWidget(self.rb2)
        self.v_box.addWidget(self.rb3)
        self.v_box.addWidget(self.buton)
        self.v_box.addWidget(self.yazi)

        self.buton.clicked.connect(lambda : self.click(self.rb1.isChecked(),self.rb2.isChecked(),self.rb3.isChecked(),self.yazi))

        self.setLayout(self.v_box)
        self.setWindowTitle("radio button")
        self.show()

    def click(self,rb1,rb2,rb3,yazi):
        if rb1:
            yazi.setText("C# DİLİ İYİ BİR SEÇİM")
        if rb2:
            yazi.setText("Python sevdiğini biliyodum")
        if rb3:
            yazi.setText("ZOR AMA ZEVKLİ BİR DİL SEÇİMİ")



app=QApplication(sys.argv)

penc=Pencere()

sys.exit(app.exec())