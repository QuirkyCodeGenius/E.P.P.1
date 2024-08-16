import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QTextEdit, QPushButton, QVBoxLayout, QFrame, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(579, 389)
        Dialog.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.valor1 = QTextEdit(Dialog)
        self.valor1.setGeometry(QtCore.QRect(400, 50, 141, 41))
        self.valor1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.valor1.setObjectName("valor1")
        self.valor2 = QTextEdit(Dialog)
        self.valor2.setGeometry(QtCore.QRect(400, 130, 141, 41))
        self.valor2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.valor2.setObjectName("valor2")
        self.bejecutar = QPushButton(Dialog)
        self.bejecutar.setGeometry(QtCore.QRect(400, 190, 141, 41))
        self.bejecutar.setObjectName("bejecutar")
        self.frame = QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(30, 20, 321, 291))
        self.frame.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.opcion = QtWidgets.QComboBox(Dialog)
        self.opcion.setGeometry(QtCore.QRect(400, 260, 141, 31))
        self.opcion.setObjectName("opcion")
        self.opcion.addItem("")
        self.opcion.addItem("")
        self.opcion.addItem("")
        self.opcion.addItem("")
        self.opcion.addItem("")
        self.opcion.addItem("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(440, 17, 71, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(440, 97, 81, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 330, 201, 31))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
            _translate = QtCore.QCoreApplication.translate
            Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
            self.bejecutar.setText(_translate("Dialog", "ejecutar"))
            self.opcion.setItemText(0, _translate("Dialog", "seno"))
            self.opcion.setItemText(1, _translate("Dialog", "coseno"))
            self.opcion.setItemText(2, _translate("Dialog", "tangente"))
            self.opcion.setItemText(3, _translate("Dialog", "cotangente"))
            self.opcion.setItemText(4, _translate("Dialog", "secante"))
            self.opcion.setItemText(5, _translate("Dialog", "cosecante"))
            self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">valor min</p></body></html>"))
            self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">valor max</p></body></html>"))
            self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">julian arley paez silva</p></body></html>"))
    def graficar(self):
        opcion = self.opcion.currentText()
        valor_min = float(self.valor1.toPlainText())
        valor_max = float(self.valor2.toPlainText())

        x = np.linspace(valor_min, valor_max, 1000)

        # Limpiar cualquier widget anterior en el frame
        for i in reversed(range(self.layout_frame.count())):
            widget = self.layout_frame.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        # Crear una figura y ejes
        fig, ax = plt.subplots()

        if opcion == "seno":
            y = np.sin(x)
            titulo = 'Gráfico de la función seno'
        elif opcion == "coseno":
            y = np.cos(x)
            titulo = 'Gráfico de la función coseno'
        elif opcion == "tangente":
            y = np.tan(x)
            titulo = 'Gráfico de la función tangente'
        elif opcion == "cotangente":
            y = 1 / np.tan(x)
            titulo = 'Gráfico de la función cotangente'
        elif opcion == "secante":
            y = 1 / np.cos(x)
            titulo = 'Gráfico de la función secante'
        elif opcion == "cosecante":
            y = 1 / np.sin(x)
            titulo = 'Gráfico de la función cosecante'

        # Trazar la función en los ejes
        ax.plot(x, y)

        # Personalizar los ejes
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title(titulo)

        # Crear un canvas para la figura
        canvas = FigureCanvas(fig)
        self.layout_frame.addWidget(canvas)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.bejecutar.clicked.connect(ui.graficar)
    Dialog.show()
    sys.exit(app.exec_())