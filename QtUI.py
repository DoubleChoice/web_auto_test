import sys
import threading

from PyQt6.QtWidgets import QApplication, QMainWindow, QHeaderView

import MyUtils
import recv
from MainUI import Ui_MainWindow


class MyWindow(Ui_MainWindow):
    def __init__(self, mainWindow):
        super().__init__()
        self.setupUi(mainWindow)
        self.initUI()

    def initUI(self):
        self.pushButtonStartServe.clicked.connect(self.startServe)
        self.tableWidgetToDo.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        self.tableWidgetToDo.setColumnCount(6)
        self.tableWidgetToDo.setHorizontalHeaderLabels(['岗位', '平台', '发布时间', '完成状态'])
        self.jobcontrol = MyUtils.JobControl(self)
        self.uicontrol = MyUtils.UIControl(self)
        self.listWidgetFunc.setCurrentRow(0)
        self.uicontrol.showServePage()
        self.listWidgetFunc.currentItemChanged.connect(self.uicontrol.onItemChanged)

    def startServe(self):
        self.p1 = threading.Thread(target=recv.main, args=(self.uicontrol, self.jobcontrol))
        self.p1.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    myform = MyWindow(window)
    window.show()
    sys.exit(app.exec())
