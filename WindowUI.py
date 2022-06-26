# -*- coding: utf-8 -*-
#
# Created by: PyQt5 UI code generator 5.15.7


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("三石背景V1.0.0")
        MainWindow.resize(482, 369)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(120, 20, 101, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 60, 101, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 60, 101, 31))
        self.pushButton_3.setAutoFillBackground(False)
        self.pushButton_3.setCheckable(False)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 21, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 71, 16))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 110, 351, 231))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "三石背景V1.0.0"))
        self.comboBox.setItemText(0, _translate("MainWindow", "标准-550"))
        self.comboBox.setItemText(1, _translate("MainWindow", "高清-1100"))
        self.comboBox.setItemText(2, _translate("MainWindow", "超清-2200"))
        self.comboBox.setItemText(3, _translate("MainWindow", "4K-4400"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "不自动更新"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "每10分钟"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "每30分钟"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "每1小时"))
        self.pushButton_3.setText(_translate("MainWindow", "设置为壁纸"))
        self.label.setText(_translate("MainWindow", "图像画质："))
        self.label_2.setText(_translate("MainWindow", "更新频次："))
