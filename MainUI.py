# Form implementation generated from reading ui file 'MainUI.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(875, 466)
        MainWindow.setMinimumSize(QtCore.QSize(875, 466))
        MainWindow.setMaximumSize(QtCore.QSize(875, 466))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonStartServe = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonStartServe.setGeometry(QtCore.QRect(780, 390, 71, 23))
        self.pushButtonStartServe.setObjectName("pushButtonStartServe")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(90, 0, 771, 381))
        self.stackedWidget.setObjectName("stackedWidget")
        self.servePage = QtWidgets.QWidget()
        self.servePage.setObjectName("servePage")
        self.tableWidgetToDo = QtWidgets.QTableWidget(parent=self.servePage)
        self.tableWidgetToDo.setGeometry(QtCore.QRect(10, 10, 751, 361))
        self.tableWidgetToDo.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidgetToDo.setObjectName("tableWidgetToDo")
        self.tableWidgetToDo.setColumnCount(0)
        self.tableWidgetToDo.setRowCount(0)
        self.stackedWidget.addWidget(self.servePage)
        self.jobPage = QtWidgets.QWidget()
        self.jobPage.setObjectName("jobPage")
        self.label = QtWidgets.QLabel(parent=self.jobPage)
        self.label.setGeometry(QtCore.QRect(180, 100, 101, 51))
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.jobPage)
        self.resumePage = QtWidgets.QWidget()
        self.resumePage.setObjectName("resumePage")
        self.label_2 = QtWidgets.QLabel(parent=self.resumePage)
        self.label_2.setGeometry(QtCore.QRect(150, 140, 71, 31))
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.resumePage)
        self.listWidgetFunc = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidgetFunc.setGeometry(QtCore.QRect(10, 10, 71, 361))
        self.listWidgetFunc.setObjectName("listWidgetFunc")
        item = QtWidgets.QListWidgetItem()
        self.listWidgetFunc.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetFunc.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetFunc.addItem(item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 875, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.listWidgetFunc.setCurrentRow(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonStartServe.setText(_translate("MainWindow", "启动服务"))
        self.label.setText(_translate("MainWindow", "岗位信息"))
        self.label_2.setText(_translate("MainWindow", "获取简历"))
        __sortingEnabled = self.listWidgetFunc.isSortingEnabled()
        self.listWidgetFunc.setSortingEnabled(False)
        item = self.listWidgetFunc.item(0)
        item.setText(_translate("MainWindow", "服务"))
        item = self.listWidgetFunc.item(1)
        item.setText(_translate("MainWindow", "岗位信息"))
        item = self.listWidgetFunc.item(2)
        item.setText(_translate("MainWindow", "获取简历"))
        self.listWidgetFunc.setSortingEnabled(__sortingEnabled)