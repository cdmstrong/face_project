import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Thread_num(QThread):
    # 创建信号，发送str类型数据
    num_signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()

    def run(self):
        for num in '12345':
            # 线程自带休眠方法
            self.sleep(1)
            print(num)
            # 发送信号，num是str类型数据
            self.num_signal.emit(num)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.move(500, 400)
        self.setFixedSize(300, 300)
        vlayout = QVBoxLayout()
        self.setLayout(vlayout)
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        vlayout.addWidget(text_edit)
        vlayout.addSpacing(10)
        num_button = QPushButton('12345')
        num_button.clicked.connect(lambda: self.numPrint(text_edit))
        vlayout.addWidget(num_button)

    def numPrint(self, text_edit):
        # 创建线程
        self.thread = Thread_num()
        self.text_edit = text_edit
        # 连接信号
        self.thread.num_signal.connect(self.showEdit)
        # 线程启动
        self.thread.start()

    def showEdit(self, num):
        self.text_edit.append(num)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
