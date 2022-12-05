from PyQt5.QtWidgets import *
import sys

class Panel_DO(QWidget):

    list_DO = [False, False, False, False, False]
    # list_btn

    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.test()
        self.show()

    def initUI(self):

        for i in range(len(self.list_DO)):
            QPushButton('1')

        btn1 = QPushButton('1')
        btn2 = QPushButton('2')

        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)

        self.setLayout(hbox)

    def test(self):
        print(len(self.list_DO))
        for i in range(len(self.list_DO)):
            print(i)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Panel_DO()
    app.exec_()
