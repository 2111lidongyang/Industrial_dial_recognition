# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\login.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(942, 590)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet(".QFrame#frame{border-image: url(:/img/login.png);}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.loginBtn = QtWidgets.QPushButton(self.frame)
        self.loginBtn.setGeometry(QtCore.QRect(512, 410, 251, 28))
        self.loginBtn.setStyleSheet("font: 20 10pt \"阿里妈妈方圆体 VF Light\";\n"
"color:#000000;\n"
"border:none;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.loginBtn.setText("")
        self.loginBtn.setObjectName("loginBtn")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(610, 450, 41, 20))
        self.pushButton.setStyleSheet("font: 20 10pt \"阿里妈妈方圆体 VF Light\";\n"
"color:#000000;\n"
"border:none;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.idlineEdit = QtWidgets.QLineEdit(self.frame)
        self.idlineEdit.setGeometry(QtCore.QRect(520, 290, 241, 31))
        self.idlineEdit.setStyleSheet("font: 20 10pt \"阿里妈妈方圆体 VF Light\";\n"
"color:#000000;\n"
"border:none;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.idlineEdit.setObjectName("idlineEdit")
        self.pwdlineEdit = QtWidgets.QLineEdit(self.frame)
        self.pwdlineEdit.setGeometry(QtCore.QRect(520, 350, 241, 31))
        self.pwdlineEdit.setStyleSheet("font: 20 10pt \"阿里妈妈方圆体 VF Light\";\n"
"color:#000000;\n"
"border-bottom: 2px solid black;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.pwdlineEdit.setObjectName("pwdlineEdit")
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
import ui.img.image