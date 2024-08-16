from gpiozero import LED
from time import sleep
import RPi.GPIO as GPIO


from PyQt5 import QtCore, QtGui, QtWidgets
GPIO.setmode(GPIO.BCM)
pin_servo = 12
pin_servo2 = 13
GPIO.setup(pin_servo, GPIO.OUT)
GPIO.setup(pin_servo2, GPIO.OUT)
pwm = GPIO.PWM(pin_servo, 50)
pwm2 = GPIO.PWM(pin_servo2, 50)
pwm.start(0)
pwm2.start(0)


class Ui_Dialog(object):
    

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(701, 395)
        Dialog.setStyleSheet("background-color: rgb(159, 5, 190);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(260, 40, 201, 41))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(350, 160, 111, 16))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(350, 210, 111, 16))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(500, 150, 121, 31))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(500, 200, 121, 31))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.horizontalSlider = QtWidgets.QSlider(Dialog)
        self.horizontalSlider.setGeometry(QtCore.QRect(260, 300, 191, 31))
        self.horizontalSlider.setMouseTracking(False)
        self.horizontalSlider.setStyleSheet("background-color: rgb(172, 172, 172);")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(210, 160, 41, 31))
        self.textEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 160, 151, 51))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        #self.pushButton = QtWidgets.QPushButton(Dialog)
        #self.pushButton.setGeometry(QtCore.QRect(30, 240, 111, 31))
        #self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        #self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">SERVOMOTORES</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">SERVO 1</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">SERVO 2</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">ELIJA EL SERVO</p><p align=\"center\">(en numero)</p></body></html>"))
        #self.pushButton.setText(_translate("Dialog", "EJECUTAR"))
    #def opcservo (self):
        #eleccion_servo = self.textEdit_3.toPlainText()

    def slider(self):
        eleccion_servo = self.textEdit_3.toPlainText()
        m = 0.10
        b = 2.4
        m2 = 1.84
        valor_slider = self.horizontalSlider.value()
        posicion = (valor_slider * m) + b
        grados = str(f'{valor_slider * m2:.2f}')
        #pwm.ChangeDutyCycle(posicion)
        self.textEdit.setText(grados + "º")
        
        if eleccion_servo == "1":
            pwm.ChangeDutyCycle(posicion)
            self.textEdit.setText(grados + "º")
        elif eleccion_servo == "2":
            pwm2.ChangeDutyCycle(posicion)
            self.textEdit_2.setText(grados + "º")


        
        
        print(valor_slider)
        print(posicion)
        print(grados)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    ui.horizontalSlider.sliderMoved.connect(ui.slider)
    #ui.pushButton.clicked.connect(ui.opcservo)
    sys.exit(app.exec_())
