# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'face.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1031, 820)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/Users/4399-5080/Desktop/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 0, 181, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(3, 1, 1021, 791))
        self.label_2.setStyleSheet("border-image: url(D:/Users/4399-5080/Desktop/bg.jpg)\n"
"")
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.init = QtWidgets.QPushButton(self.centralwidget)
        self.init.setGeometry(QtCore.QRect(50, 120, 151, 51))
        self.init.setStyleSheet("background-color: rgb(186, 255, 143);\n"
"font: 16pt \"Microsoft YaHei UI\";\n"
"\n"
"")
        self.init.setObjectName("init")
        self.cameraCap = QtWidgets.QPushButton(self.centralwidget)
        self.cameraCap.setGeometry(QtCore.QRect(50, 210, 151, 51))
        self.cameraCap.setStyleSheet("background-color: rgb(186, 255, 143);\n"
"font: 16pt \"Microsoft YaHei UI\";\n"
"\n"
"")
        self.cameraCap.setObjectName("cameraCap")
        self.videoCap = QtWidgets.QPushButton(self.centralwidget)
        self.videoCap.setGeometry(QtCore.QRect(50, 310, 151, 51))
        self.videoCap.setStyleSheet("background-color: rgb(186, 255, 143);\n"
"font: 16pt \"Microsoft YaHei UI\";\n"
"\n"
"")
        self.videoCap.setObjectName("videoCap")
        self.videoTest = QtWidgets.QPushButton(self.centralwidget)
        self.videoTest.setGeometry(QtCore.QRect(50, 400, 151, 51))
        self.videoTest.setStyleSheet("background-color: rgb(186, 255, 143);\n"
"font: 16pt \"Microsoft YaHei UI\";\n"
"\n"
"")
        self.videoTest.setObjectName("videoTest")
        self.cameraTest = QtWidgets.QPushButton(self.centralwidget)
        self.cameraTest.setGeometry(QtCore.QRect(50, 500, 151, 51))
        self.cameraTest.setStyleSheet("background-color: rgb(186, 255, 143);\n"
"font: 16pt \"Microsoft YaHei UI\";\n"
"\n"
"")
        self.cameraTest.setObjectName("cameraTest")
        self.log = QtWidgets.QTextEdit(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(40, 620, 941, 151))
        self.log.setStyleSheet("background-color: rgba(253, 255, 255, 100);\n"
"font: 14pt \"Arial\";")
        self.log.setObjectName("log")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 580, 101, 31))
        self.label_3.setStyleSheet("color: rgb(255, 158, 133);\n"
"font: 12pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.show = QtWidgets.QLabel(self.centralwidget)
        self.show.setGeometry(QtCore.QRect(270, 90, 701, 501))
        self.show.setStyleSheet("background-color: rgba(255, 255, 255, 100);")
        self.show.setText("")
        self.show.setObjectName("show")
        self.weight = QtWidgets.QPushButton(self.centralwidget)
        self.weight.setGeometry(QtCore.QRect(50, 30, 151, 51))
        self.weight.setStyleSheet("background-color: rgb(186, 255, 143);\n"
"font: 16pt \"Microsoft YaHei UI\";\n"
"\n"
"")
        self.weight.setObjectName("weight")
        self.face_name = QtWidgets.QTextEdit(self.centralwidget)
        self.face_name.setGeometry(QtCore.QRect(370, 30, 411, 41))
        self.face_name.setStyleSheet("background-color: rgba(253, 255, 255, 100);\n"
"font: 14pt \"Arial\";")
        self.face_name.setObjectName("face_name")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(270, 30, 101, 31))
        self.label_4.setStyleSheet("color: rgb(255, 158, 133);\n"
"font: 12pt \"Arial\";")
        self.label_4.setObjectName("label_4")
        self.set_face = QtWidgets.QPushButton(self.centralwidget)
        self.set_face.setGeometry(QtCore.QRect(810, 30, 151, 51))
        self.set_face.setStyleSheet("background-color: rgb(186, 255, 143);\n"
"font: 16pt \"Microsoft YaHei UI\";\n"
"\n"
"")
        self.set_face.setObjectName("set_face")
        self.label_2.raise_()
        self.label.raise_()
        self.init.raise_()
        self.cameraCap.raise_()
        self.videoCap.raise_()
        self.videoTest.raise_()
        self.cameraTest.raise_()
        self.log.raise_()
        self.label_3.raise_()
        self.show.raise_()
        self.weight.raise_()
        self.face_name.raise_()
        self.label_4.raise_()
        self.set_face.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1031, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "东华集团人脸录入系统"))
        self.label.setText(_translate("MainWindow", "最安全的系统"))
        self.init.setText(_translate("MainWindow", "初始化模型"))
        self.cameraCap.setText(_translate("MainWindow", "人脸录入"))
        self.videoCap.setText(_translate("MainWindow", "视频录入"))
        self.videoTest.setText(_translate("MainWindow", "视频测试"))
        self.cameraTest.setText(_translate("MainWindow", "摄像头测试"))
        self.log.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">logging</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "系统日志："))
        self.weight.setText(_translate("MainWindow", "模型文件选择"))
        self.face_name.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.face_name.setPlaceholderText(_translate("MainWindow", "please input face_name with English", "d"))
        self.label_4.setText(_translate("MainWindow", "人脸名称："))
        self.set_face.setText(_translate("MainWindow", "设置名称"))

# import bg_rc
