from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(30, 520, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(260, 540, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 440, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(200, 480, 80, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 450, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 450, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(340, 480, 80, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 771, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(490, 550, 241, 41))
        #self.label_4.setStyleSheet("border-image: url(:/cct/logo ECCI.jpg);")
        
        self.label_4.setStyleSheet("border-image: url(/home/juliapaez1227/Downloads/logo_ecci.png)")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(500, 430, 251, 111))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Crear una figura de Matplotlib como variable de instancia
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.verticalLayout.addWidget(self.canvas)  # Asegúrate de tener un QVBoxLayout en tu diseño

        
        #////////////////////////////////////
        #//////accion del boton graficar/////
        #////////////////////////////////////
        self.pushButton.clicked.connect(self.graficar)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Graficas"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Seno"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Coseno"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Tangente"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Cotangente"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Secante"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Cosecante"))
        self.pushButton.setText(_translate("MainWindow", "Graficar"))
        self.label.setText(_translate("MainWindow", "Funciones\n"
"Trigonometricas"))
        self.label_2.setText(_translate("MainWindow", "valor minimo"))
        self.label_3.setText(_translate("MainWindow", "valor maximo"))
        self.label_5.setText(_translate("MainWindow", "julian paez"))
    
    def graficar(self):
        opcion = self.comboBox.currentText()
        try:
            min = float(self.textEdit.toPlainText())
            max = float(self.textEdit_2.toPlainText())
        except ValueError:
            print(f'\nLos valores no son correctos\n')

        x = np.linspace(min,max,1000)
        if opcion == "Seno":
            y = np.sin(x)
            print(f'{y}')
        elif opcion == "Coseno":
            y = np.cos(x)
            print(f'{y}')
        elif opcion == "Tangente":
            y = np.tan(x)
        elif opcion == "Secante":
            y = 1 / np.cos(x)
            print(f'{y}')
        elif opcion == "Cosecante":
                y = 1 / np.sin(x)
                print(f'{y}')
        elif opcion == "Cotangente":
            y = 1 / np.tan(x)
            print(f'{y}')

             # Limpiar la figura
        self.figure.clear()
        axes = self.figure.add_subplot() #colocar 111 en parentesis
        axes.plot(x, y)
        axes.grid()
        axes.set_title(f'Gráfica de {opcion}')
        axes.set_xlabel('X')
        axes.set_ylabel('Y')
        self.canvas.draw()

        

#import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
