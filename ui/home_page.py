# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\home.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1058, 674)
        Form.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("QWidget#From{border-image: url(:/img/home.png);}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("QWidget#tab{border-image: url(:/img/home.png);}")
        self.tab.setObjectName("tab")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.tab)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox.setStyleSheet("font: 63 12pt \"阿里妈妈方圆体 VF SemiBold\";")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.chooseBtn = QtWidgets.QPushButton(self.groupBox)
        self.chooseBtn.setMinimumSize(QtCore.QSize(100, 50))
        self.chooseBtn.setStyleSheet("font: 63 10pt \"阿里妈妈方圆体 VF SemiBold\";")
        self.chooseBtn.setObjectName("chooseBtn")
        self.horizontalLayout_4.addWidget(self.chooseBtn)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.higspinBox = QtWidgets.QSpinBox(self.groupBox)
        self.higspinBox.setObjectName("higspinBox")
        self.horizontalLayout_4.addWidget(self.higspinBox)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lowspinBox = QtWidgets.QSpinBox(self.groupBox)
        self.lowspinBox.setObjectName("lowspinBox")
        self.horizontalLayout_4.addWidget(self.lowspinBox)
        self.detectBtn = QtWidgets.QPushButton(self.groupBox)
        self.detectBtn.setMinimumSize(QtCore.QSize(100, 50))
        self.detectBtn.setStyleSheet("font: 63 10pt \"阿里妈妈方圆体 VF SemiBold\";")
        self.detectBtn.setObjectName("detectBtn")
        self.horizontalLayout_4.addWidget(self.detectBtn)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox_2.setStyleSheet("font: 63 12pt \"阿里妈妈方圆体 VF SemiBold\";")
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setStyleSheet("font: 63 10pt \"阿里妈妈方圆体 VF SemiBold\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.numlineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.numlineEdit.setStyleSheet("font: 63 10pt \"阿里妈妈方圆体 VF SemiBold\";")
        self.numlineEdit.setObjectName("numlineEdit")
        self.horizontalLayout_6.addWidget(self.numlineEdit)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setStyleSheet("font: 63 10pt \"阿里妈妈方圆体 VF SemiBold\";")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.numlineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.numlineEdit_2.setMinimumSize(QtCore.QSize(150, 30))
        self.numlineEdit_2.setStyleSheet("font: 63 10pt \"阿里妈妈方圆体 VF SemiBold\";")
        self.numlineEdit_2.setObjectName("numlineEdit_2")
        self.horizontalLayout_6.addWidget(self.numlineEdit_2)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setStyleSheet("font: 63 10pt \"阿里妈妈方圆体 VF SemiBold\";")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setMinimumSize(QtCore.QSize(40, 40))
        self.label_7.setMaximumSize(QtCore.QSize(40, 40))
        self.label_7.setStyleSheet(" border-radius: 20px;      \n"
"background-color: rgb(255, 255, 0);\n"
"")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(60, 30))
        self.pushButton.setStyleSheet("font: 63 10pt \"阿里妈妈方圆体 VF SemiBold\";")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout_3.setStretch(0, 7)
        self.horizontalLayout_3.setStretch(1, 6)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableView_2 = QtWidgets.QTableView(self.tab_3)
        self.tableView_2.setObjectName("tableView_2")
        self.verticalLayout_3.addWidget(self.tableView_2)
        self.frame_5 = QtWidgets.QFrame(self.tab_3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(201, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.deluserBtn = QtWidgets.QPushButton(self.frame_5)
        self.deluserBtn.setMinimumSize(QtCore.QSize(200, 60))
        self.deluserBtn.setStyleSheet("font: 63 12pt \"阿里妈妈方圆体 VF SemiBold\";")
        self.deluserBtn.setObjectName("deluserBtn")
        self.horizontalLayout.addWidget(self.deluserBtn)
        spacerItem1 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.upuserBtn = QtWidgets.QPushButton(self.frame_5)
        self.upuserBtn.setMinimumSize(QtCore.QSize(200, 60))
        self.upuserBtn.setStyleSheet("font: 63 12pt \"阿里妈妈方圆体 VF SemiBold\";")
        self.upuserBtn.setObjectName("upuserBtn")
        self.horizontalLayout.addWidget(self.upuserBtn)
        spacerItem2 = QtWidgets.QSpacerItem(201, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.verticalLayout_3.setStretch(0, 4)
        self.verticalLayout_3.setStretch(1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableView = QtWidgets.QTableView(self.tab_2)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)
        self.frame_4 = QtWidgets.QFrame(self.tab_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.delBtn = QtWidgets.QPushButton(self.frame_4)
        self.delBtn.setGeometry(QtCore.QRect(430, 50, 200, 60))
        self.delBtn.setMinimumSize(QtCore.QSize(200, 60))
        self.delBtn.setStyleSheet("font: 63 12pt \"阿里妈妈方圆体 VF SemiBold\";")
        self.delBtn.setObjectName("delBtn")
        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout_2.setStretch(0, 4)
        self.verticalLayout_2.setStretch(1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_2.addWidget(self.tabWidget)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "选择操作"))
        self.chooseBtn.setText(_translate("Form", "选择图片"))
        self.label_2.setText(_translate("Form", "低阈值"))
        self.label_3.setText(_translate("Form", "高阈值"))
        self.detectBtn.setText(_translate("Form", "开始检测"))
        self.groupBox_2.setTitle(_translate("Form", "检测结果"))
        self.label_4.setText(_translate("Form", "表盘数："))
        self.label_5.setText(_translate("Form", "检测结果："))
        self.label_6.setText(_translate("Form", "检测状态"))
        self.pushButton.setText(_translate("Form", "退出"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "主页"))
        self.deluserBtn.setText(_translate("Form", "删除该用户"))
        self.upuserBtn.setText(_translate("Form", "提升该用户权限"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "用户管理"))
        self.delBtn.setText(_translate("Form", "删除该记录"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "查看数据"))
import ui.img.image
