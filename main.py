import sys


from PyQt5.QtWidgets import QApplication,QWidget

class calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setWindowTitle('Calculator')
        self.resize(512,512)
        self.show()

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = calculator()
    sys.exit(app.exec_())
    