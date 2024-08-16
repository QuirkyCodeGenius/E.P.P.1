
import matplotlib
matplotlib.use('Qt5Agg')  # Asegúrate de que esto está antes de importar matplotlib.pyplot
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
import time
from adafruit_servokit import ServoKit    #https://circuitpython.readthedocs.io/projects/servokit/en/latest/
from roboticstoolbox import *
from spatialmath.base import *
import math
import numpy


from roboticstoolbox import DHRobot, RevoluteDH

#Constants
nbPCAServo=2

ServoKit.frequency = 50
#Parameters
MIN_IMP  =[500] * 16
MAX_IMP  =[2500] * 16
MIN_ANG  =[0] 
MAX_ANG  =[180]

#Objects
pca = ServoKit(channels=16)

l1 =8.5
l2 =7.5

for i in range(nbPCAServo):
        pca.servo[i].set_pulse_width_range(MIN_IMP[i] , MAX_IMP[i])

px_inicial = -13
py_inicial = 11

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
        self.groupBox_3.setGeometry(QtCore.QRect(480, 240, 341, 161))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.btn_escribir = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_escribir.setGeometry(QtCore.QRect(190, 50, 93, 28))
        self.btn_escribir.setObjectName("btn_escribir")
        self.palabra_escribir = QtWidgets.QTextEdit(self.groupBox_3)
        self.palabra_escribir.setGeometry(QtCore.QRect(20, 50, 121, 31))
        self.palabra_escribir.setObjectName("palabra_escribir")
        self.chevrolet = QtWidgets.QPushButton(self.groupBox_3)
        self.chevrolet.setGeometry(QtCore.QRect(10, 100, 80, 25))
        self.chevrolet.setObjectName("chevrolet")
        self.renault = QtWidgets.QPushButton(self.groupBox_3)
        self.renault.setGeometry(QtCore.QRect(120, 100, 80, 25))
        self.renault.setObjectName("renault")
        self.kia = QtWidgets.QPushButton(self.groupBox_3)
        self.kia.setGeometry(QtCore.QRect(240, 100, 80, 25))
        self.kia.setObjectName("kia")
        self.mercedez = QtWidgets.QPushButton(self.groupBox_3)
        self.mercedez.setGeometry(QtCore.QRect(110, 130, 101, 25))
        self.mercedez.setObjectName("mercedez")
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
        self.btn_escribir.setText(_translate("MainWindow", "escibir"))
        self.chevrolet.setText(_translate("MainWindow", "chevrolet"))
        self.renault.setText(_translate("MainWindow", "renault"))
        self.kia.setText(_translate("MainWindow", "kia"))
        self.mercedez.setText(_translate("MainWindow", "mercedez"))
#import logo_rc


    def ubicar_puntos(self):
       
        Px = float(self.coordenada_x.toPlainText())
        Py = float(self.coordenada_y.toPlainText())
        #Px = 20
        #Py = 0
        b = math.sqrt(Px**2+Py**2)
        # Theta 2
        cos_theta2 = (b**2-l2**2-l1**2)/(2*l1*l2)
        sen_theta2 = math.sqrt(1-(cos_theta2)**2)#(+)codo abajo y (-)codo arriba
        theta2 = math.atan2(sen_theta2, cos_theta2)
        print(f'theta 2 = {numpy.rad2deg(theta2):.4f}')
        # Theta 1
        alpha = math.atan2(Py,Px)
        phi = math.atan2(l2*sen_theta2, l1+l2*cos_theta2)
        theta1_x = alpha - phi
        theta1 = round(theta1_x, 4)
        #no esta entrando al if cuando seleccionamos el cuadrante negativo
        x = -3.1416
        if theta1 <= (x) :
            theta1 = ((2*math.pi) + theta1)


        print(f'theta 1 = {numpy.rad2deg(theta1):.4f}')
        #-------------
        #convertir de radianes a grados
        grado_servo1 = theta1 * (180/3.1416)
        grado_servo2 = theta2 * (180/3.1416)
        valorth1 = str(grado_servo1)
        valorth2 = str(grado_servo2)
        self.th1.setText(valorth1)
        self.th2.setText(valorth2)

        angulo_deseado1 = grado_servo1
        angulo_deseado2 = grado_servo2

        if grado_servo1 == 0:
            angulo_deseado1 = 1
            
        if grado_servo2 == 0:
            angulo_deseado2 = 1
        if grado_servo1 == 0 and grado_servo2 == 0:
            angulo_deseado1 = 1
            angulo_deseado2 = 1

        
        
        angulo_final1 = (180 / angulo_deseado1) 
        angulo_final2 = (180 / angulo_deseado2) 
        
            
        pca.servo[0].angle = (MAX_ANG[0] / angulo_final1)
        pca.servo[1].angle = (MAX_ANG[0] / angulo_final2)

        q1 = theta1
        q2 = theta2

        R = []
        R.append(RevoluteDH(d=0, alpha=0, a=l1, offset=0))
        R.append(RevoluteDH(d=0, alpha=0, a=l2, offset=0))
        Robot = DHRobot(R, name='Bender')
        print(Robot)

        Robot.plot([q1, q2], limits=[-30,30,-30,30,-30,30])


        #Robot.plot([q1, q2], limits=[-30,30,-30,30])

        MTH = Robot.fkine([q1,q2])
        print(MTH)
        resultado = tr2rpy(MTH.R, 'deg', 'zyx')
        print(f'Roll, Pitch, Yaw = {resultado}')

        #plt.show(block=True)



    def espacio_trabajo(self):
            # Crear los eslabones del robot utilizando la convención DH
        R1 = RevoluteDH(a=l1, alpha=0, d=0, offset=0)
        R2 = RevoluteDH(a=l2, alpha=0, d=0, offset=0)

        # Crear el robot serial con los eslabones definidos
        robot = DHRobot([R1, R2], name='Robot 2R')

        MTHs = []

        # Número de pasos intermedios entre posiciones
        steps = 5

        position = [(0, 2.618),(0, 0),(numpy.pi/2, 0),(numpy.pi, 0),(numpy.pi, 2.618)]

        for i in range(len(position) - 1):
            start = numpy.array(position[i])
            end = numpy.array(position[i + 1])

            # Generar pasos intermedios
            for step in range(steps):
                # Interpolación lineal entre las posiciones
                q = start + (end - start) * step / steps

                # Calcular la matriz de transformación homogénea
                MTH = robot.fkine(q)
                MTHs.append(MTH)
                #print(MTH)

                # Convertir ángulos a grados
                degrees1 = math.degrees(q[0])
                degrees2 = math.degrees(q[1])

                # Controlar los servos con los ángulos calculados
                pca.servo[0].angle = degrees1
                pca.servo[1].angle = degrees2

                # Visualizar el robot
                robot.plot(q, limits=[-30, 30, -30, 30, -30, 30])

                # Añadir un pequeño retraso para la visualización
                time.sleep(0.005)

        # Retornar la úlima matriz de transformación homogénea calculada
        return MTHs[-1]
    
    def nombres(self):



        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.boton_coordenadas.clicked.connect(ui.ubicar_puntos)
    ui.boton_area_trabajo.clicked.connect(ui.espacio_trabajo)
    MainWindow.show()
    sys.exit(app.exec_())
