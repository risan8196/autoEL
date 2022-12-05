from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import time

class Worker(QThread):
    timeout = pyqtSignal(bool)    # 사용자 정의 시그널

    def __init__(self):
        super().__init__()
        self.bb = False           # 초깃값 설정

    def run(self):
        while True:
            self.bb = not self.bb
            self.timeout.emit(self.bb)     # 방출
            # self.num += 1
            self.sleep(2)

class Panel_DO(QWidget):

    list_DO = [False, False, False, False, False]
    list_btn =[]

    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        # self.test()
        self.show()
        
        self.worker = Worker()
        self.worker.start()
        self.worker.timeout.connect(self.timeout)   # 시그널 슬롯 등록

    @pyqtSlot(bool)
    def timeout(self, bb):
        self.list_DO[2] = bb
        self.update()

    def change(self):
        time.sleep(3)
        self.list_DO[1] = True
        self.update()

        time.sleep(10)
        self.list_DO[2] = True
        self.update()


    def initUI(self):

        for i in range(len(self.list_DO)):
            self.list_btn.append(QPushButton(str(i)))

        # btn1 = QPushButton('1')
        # btn2 = QPushButton('2')

        hbox = QHBoxLayout()

        for btn in self.list_btn:
            hbox.addWidget(btn)

        # hbox.addWidget(btn1)
        # hbox.addWidget(btn2)

        self.setLayout(hbox)

    def paintEvent(self, QPaintEvent):
        for i in range(len(self.list_DO)):
            if self.list_DO[i] == True:
                self.list_btn[i].setStyleSheet("background-color : yellow")
            else:
                self.list_btn[i].setStyleSheet("background-color : green")

    def test(self):
        print(len(self.list_DO))
        for i in range(len(self.list_DO)):
            print(i)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Panel_DO()
    app.exec_()
