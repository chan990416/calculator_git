import sys


from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QMessageBox,QPlainTextEdit
from PyQt5.QtGui  import QIcon

class calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        self.btn1 = QPushButton('Massage',self)
        self.btn1.clicked.connect(self.activateMessage)

        vbox = QVBoxLayout()
        vbox.addWidget(self.te1)
        vbox.addStretch(1)
        vbox.addWidget(self.btn1)
        vbox.addStretch(1)
        self.setLayout(vbox)
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))

        self.resize(512,512)
        self.show()

    def activateMessage(self):
        #QMessageBox.information(self,"information","Button_clecked")
        self.te1.appendPlainText("Button Clicked")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = calculator()
    sys.exit(app.exec_())
    