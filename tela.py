# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 60, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 130, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 190, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_apagar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_apagar.setGeometry(QtCore.QRect(260, 310, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_apagar.setFont(font)
        self.pushButton_apagar.setObjectName("pushButton_apagar")
        self.pushButton_enviar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_enviar.setGeometry(QtCore.QRect(440, 310, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_enviar.setFont(font)
        self.pushButton_enviar.setObjectName("pushButton_enviar")
        self.radioButton_masculino = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_masculino.setGeometry(QtCore.QRect(320, 190, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_masculino.setFont(font)
        self.radioButton_masculino.setObjectName("radioButton_masculino")
        self.radioButton_feminino = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_feminino.setGeometry(QtCore.QRect(440, 190, 95, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_feminino.setFont(font)
        self.radioButton_feminino.setObjectName("radioButton_feminino")
        self.checkBox_aceite = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_aceite.setGeometry(QtCore.QRect(260, 250, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_aceite.setFont(font)
        self.checkBox_aceite.setObjectName("checkBox_aceite")
        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setGeometry(QtCore.QRect(320, 130, 211, 22))
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Tela de Cadastro"))
        self.label_2.setText(_translate("MainWindow", "Nome:"))
        self.label_3.setText(_translate("MainWindow", "Sexo:"))
        self.pushButton_apagar.setText(_translate("MainWindow", "Apagar"))
        self.pushButton_enviar.setText(_translate("MainWindow", "Enviar"))
        self.radioButton_masculino.setText(_translate("MainWindow", "Masculino"))
        self.radioButton_feminino.setText(_translate("MainWindow", "Feminino"))
        self.checkBox_aceite.setText(_translate("MainWindow", "Aceito os termos"))
