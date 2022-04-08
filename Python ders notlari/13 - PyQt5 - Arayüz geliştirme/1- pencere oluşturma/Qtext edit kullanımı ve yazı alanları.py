import sys
from PyQt5.QtWidgets import QWidget,QLabel,QPushButton,QApplication,QTextEdit,QVBoxLayout

class pencere(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.yazi_alan=QTextEdit()
        self.temizle=QPushButton("Temizle")
        self.v_box=QVBoxLayout()

        self.v_box.addWidget(self.yazi_alan)
        self.v_box.addWidget(self.temizle)
        self.setLayout(self.v_box)
        self.setWindowTitle("QTEXT EDİT")
        self.show()

        self.temizle.clicked.connect(self.click)#####################

    def click(self):##############
        self.yazi_alan.clear()


app=QApplication(sys.argv)
pnc=pencere()
sys.exit(app.exec())