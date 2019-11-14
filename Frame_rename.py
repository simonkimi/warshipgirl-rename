# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Frame_rename.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame_rename(object):
    def setupUi(self, Frame_rename):
        Frame_rename.setObjectName("Frame_rename")
        Frame_rename.resize(305, 370)
        self.centralwidget = QtWidgets.QWidget(Frame_rename)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 41, 21))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(158, 10, 41, 21))
        self.label_2.setPixmap(QtGui.QPixmap("../Auto_JR/icon/lock.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.ed_username = QtWidgets.QLineEdit(self.centralwidget)
        self.ed_username.setGeometry(QtCore.QRect(50, 10, 101, 21))
        self.ed_username.setObjectName("ed_username")
        self.ed_password = QtWidgets.QLineEdit(self.centralwidget)
        self.ed_password.setGeometry(QtCore.QRect(200, 10, 101, 21))
        self.ed_password.setObjectName("ed_password")
        self.cb_server = QtWidgets.QComboBox(self.centralwidget)
        self.cb_server.setGeometry(QtCore.QRect(70, 40, 81, 21))
        self.cb_server.setObjectName("cb_server")
        self.cb_server.addItem("")
        self.cb_server.addItem("")
        self.cb_server.addItem("")
        self.cb_server.addItem("")
        self.cb_server.addItem("")
        self.cb_server.addItem("")
        self.cb_server.addItem("")
        self.cb_server.addItem("")
        self.cb_server.addItem("")
        self.cb_server.addItem("")
        self.cb_server.addItem("")
        self.cb_server.addItem("")
        self.cb_server.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 51, 21))
        self.label_3.setPixmap(QtGui.QPixmap("../Auto_JR/icon/aa0f9c8338db3e8925056220c29445e0.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.bt_login = QtWidgets.QPushButton(self.centralwidget)
        self.bt_login.setGeometry(QtCore.QRect(160, 40, 141, 21))
        self.bt_login.setObjectName("bt_login")
        self.list_log = QtWidgets.QListWidget(self.centralwidget)
        self.list_log.setGeometry(QtCore.QRect(10, 70, 291, 261))
        self.list_log.setObjectName("list_log")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 340, 301, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        Frame_rename.setCentralWidget(self.centralwidget)

        self.retranslateUi(Frame_rename)
        QtCore.QMetaObject.connectSlotsByName(Frame_rename)

    def retranslateUi(self, Frame_rename):
        _translate = QtCore.QCoreApplication.translate
        Frame_rename.setWindowTitle(_translate("Frame_rename", "Rename"))
        self.label.setText(_translate("Frame_rename", "帐号:"))
        self.label_2.setText(_translate("Frame_rename", "密码："))
        self.cb_server.setItemText(0, _translate("Frame_rename", "胡德"))
        self.cb_server.setItemText(1, _translate("Frame_rename", "萨拉托加"))
        self.cb_server.setItemText(2, _translate("Frame_rename", "俾斯麦"))
        self.cb_server.setItemText(3, _translate("Frame_rename", "声望"))
        self.cb_server.setItemText(4, _translate("Frame_rename", "纳尔逊"))
        self.cb_server.setItemText(5, _translate("Frame_rename", "空想"))
        self.cb_server.setItemText(6, _translate("Frame_rename", "海伦娜"))
        self.cb_server.setItemText(7, _translate("Frame_rename", "突击者"))
        self.cb_server.setItemText(8, _translate("Frame_rename", "黎塞留"))
        self.cb_server.setItemText(9, _translate("Frame_rename", "贝尔法斯特"))
        self.cb_server.setItemText(10, _translate("Frame_rename", "埃塞克斯"))
        self.cb_server.setItemText(11, _translate("Frame_rename", "昆西"))
        self.cb_server.setItemText(12, _translate("Frame_rename", "长春"))
        self.label_3.setText(_translate("Frame_rename", "服务器："))
        self.bt_login.setText(_translate("Frame_rename", "登录并改名"))

