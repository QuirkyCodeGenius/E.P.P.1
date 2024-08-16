import RPi.GPIO as GPIO
import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets

# Configurar los pines GPIO
GPIO.setmode(GPIO.BCM)
pin = 18
GPIO.setup(pin, GPIO.IN)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(604, 318)
        Dialog.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 30, 321, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 110, 111, 31))
        self.label_2.setObjectName("label_2")
        self.estado = QtWidgets.QLabel(Dialog)
        self.estado.setGeometry(QtCore.QRect(250, 110, 111, 31))
        self.estado.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.estado.setObjectName("estado")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">lectura de puertos digitales</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">estado del pin</span></p></body></html>"))
        self.estado.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:700;\">bajo</span></p></body></html>"))
        self.estado.setStyleSheet("background-color: rgb(0, 85, 255);")

class GPIOThread(QtCore.QThread):
    estado_changed = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super(GPIOThread, self).__init__(parent)
        self.running = True

    def run(self):
        while self.running:
            estado = GPIO.input(pin)
            self.estado_changed.emit(estado)
            time.sleep(0.1)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()

    gpio_thread = GPIOThread()
    gpio_thread.estado_changed.connect(lambda estado: ui.estado.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:700;\">ALTO</span></p></body></html>") if estado == GPIO.HIGH else ui.estado.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:700;\">bajo</span></p></body></html>"))
    gpio_thread.estado_changed.connect(lambda estado: ui.estado.setStyleSheet("background-color: rgb(255, 0, 0);") if estado == GPIO.HIGH else ui.estado.setStyleSheet("background-color: rgb(0, 85, 255);"))
    gpio_thread.start()

    sys.exit(app.exec_())
