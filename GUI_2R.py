# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_2R.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 10, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 70, 391, 231))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.coordenada_x = QtWidgets.QTextEdit(self.groupBox)
        self.coordenada_x.setGeometry(QtCore.QRect(130, 40, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.coordenada_x.setFont(font)
        self.coordenada_x.setObjectName("coordenada_x")
        self.coordenada_y = QtWidgets.QTextEdit(self.groupBox)
        self.coordenada_y.setGeometry(QtCore.QRect(130, 90, 51, 41))
        self.coordenada_y.setObjectName("coordenada_y")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(200, 40, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(200, 100, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.th1 = QtWidgets.QTextEdit(self.groupBox)
        self.th1.setGeometry(QtCore.QRect(290, 40, 51, 41))
        self.th1.setObjectName("th1")
        self.th2 = QtWidgets.QTextEdit(self.groupBox)
        self.th2.setGeometry(QtCore.QRect(290, 90, 51, 41))
        self.th2.setObjectName("th2")
        self.boton_coordenadas = QtWidgets.QPushButton(self.groupBox)
        self.boton_coordenadas.setGeometry(QtCore.QRect(140, 160, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.boton_coordenadas.setFont(font)
        self.boton_coordenadas.setObjectName("boton_coordenadas")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(490, 70, 331, 141))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.boton_julian1 = QtWidgets.QPushButton(self.groupBox_2)
        self.boton_julian1.setGeometry(QtCore.QRect(10, 90, 93, 28))
        self.boton_julian1.setObjectName("boton_julian1")
        self.boton_dani = QtWidgets.QPushButton(self.groupBox_2)
        self.boton_dani.setGeometry(QtCore.QRect(110, 90, 93, 28))
        self.boton_dani.setObjectName("boton_dani")
        self.Boto_julian2 = QtWidgets.QPushButton(self.groupBox_2)
        self.Boto_julian2.setGeometry(QtCore.QRect(210, 90, 93, 28))
        self.Boto_julian2.setObjectName("Boto_julian2")
        self.boton_area_trabajo = QtWidgets.QPushButton(self.groupBox_2)
        self.boton_area_trabajo.setGeometry(QtCore.QRect(80, 40, 161, 31))
        self.boton_area_trabajo.setObjectName("boton_area_trabajo")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(330, 420, 371, 71))
        self.label_6.setStyleSheet("border-image: url(:/cct/logo ECCI.jpg);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 340, 211, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setObjectName("label_7")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(480, 240, 341, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.boton_contorno = QtWidgets.QPushButton(self.groupBox_3)
        self.boton_contorno.setGeometry(QtCore.QRect(120, 50, 93, 28))
        self.boton_contorno.setObjectName("boton_contorno")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Robot 2R"))
        self.label.setText(_translate("MainWindow", "Robot planar 2R"))
        self.groupBox.setTitle(_translate("MainWindow", "Coordenadas"))
        self.label_2.setText(_translate("MainWindow", "Posicion X"))
        self.label_3.setText(_translate("MainWindow", "Posicion Y "))
        self.label_4.setText(_translate("MainWindow", "Theta 1"))
        self.label_5.setText(_translate("MainWindow", "Theta 2"))
        self.boton_coordenadas.setText(_translate("MainWindow", "Ubicar"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Escritura"))
        self.boton_julian1.setText(_translate("MainWindow", "Julian"))
        self.boton_dani.setText(_translate("MainWindow", "Dani"))
        self.Boto_julian2.setText(_translate("MainWindow", "Julian"))
        self.boton_area_trabajo.setText(_translate("MainWindow", "Area de trabajo"))
        self.label_7.setText(_translate("MainWindow", "Integrantes\n"
"Julian Paez\n"
"Julian Zarate\n"
"Daniel Quiroga\n"
"Prof. Robotica 2024-1"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Dibujar Contorno"))
        self.boton_contorno.setText(_translate("MainWindow", "Contorno"))
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
