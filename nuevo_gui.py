from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib
matplotlib.use('Qt5Agg')
import numpy as np
import math
import roboticstoolbox as rtb
from roboticstoolbox import RevoluteDH, SerialLink
import matplotlib.pyplot as plt #Para plotear
from scipy.io import loadmat #Cargar .mat
import cv2 #Para generar contornos imagenes
from adafruit_servokit import ServoKit 


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
        self.Boto_julian2.setText(_translate("MainWindow", "Arley"))
        self.boton_area_trabajo.setText(_translate("MainWindow", "Area de trabajo"))
        self.label_7.setText(_translate("MainWindow", "Integrantes\n"
"Julian Paez\n"
"Julian Zarate\n"
"Daniel Quiroga\n"
"Prof. Robotica 2024-1"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Dibujar Contorno"))
        self.boton_contorno.setText(_translate("MainWindow", "Contorno"))
#import logo_rc

    def mover_servos(self, theta1, theta2):
        # Convertir los �ngulos de radianes a grados (OPCIONAL)
        #theta1 = math.degrees(theta1)
        #theta2 = math.degrees(theta2)
        
        if theta1 == 0 :
            pca.servo[0].angle = (MIN_ANG[0])
        if theta2 == 0:
            pca.servo[1].angle = (MIN_ANG[0])



        # kit.servo[0].angle= (theta1) #Servo 1
        # kit.servo[1].angle= (theta2) #Servo 2
        pca.servo[0].angle = theta1
        pca.servo[1].angle = theta2

    def CD(self, theta1, theta2):
        l1 =8.5
        l2 =7.5
        q = np.array([theta1, theta2])

        robot = SerialLink([
            RevoluteDH(d=0, alpha=0, a=l1, offset=0),
            RevoluteDH(d=0, alpha=0, a=l2, offset=0)
        ], name= "mi_chimbo")   
        # Visualizar el robot, con sus limites
        #robot.plot(q, limits= [-25, 25, -25, 25, 0, 5])
        robot.plot(q, limits=[-30, 30, -30, 30, -30, 30])
        
        MTH = robot.fkine(q)
        return MTH
    
    #Cinematica Inversa (Coordenadas a Angulos)
    def CI(self, px, py):

        l1 = 8.5
        l2 = 7.5

        b = np.sqrt(px**2 + py**2)
        cos_theta2 = (b**2-l2**2-l1**2)/(2*l2*l1)
        sen_theta2 = np.sqrt(1 - cos_theta2**2)
        theta2 = np.arctan2(sen_theta2, cos_theta2)
        print(f'Theta2 inicial = {np.degrees(theta2):.3f} grados')
        # Calcular alpha y phi para theta1
        alpha = np.arctan2(py,px)
        phi = np.arctan2(l2 * sen_theta2, l1 + l2 * cos_theta2)
        # Calcular theta1
        theta1 = alpha - phi
        theta1 = theta1 + 2 * np.pi if theta1 <= -np.pi else theta1 #Otra forma de hacer el if
        print(f'Theta1  inicial= {np.degrees(theta1):.3f} grados')
        theta1 = math.degrees(theta1)
        theta2 = math.degrees(theta2)
        print(f'Theta1 final= {theta1} grados')
        print(f'Theta2 final= {theta2} grados')

        #Retorno
        return theta1,theta2
    

    def esp_trabajo(self):
        #Cantidad de linspace y de iteraciones en los for
        can_puntos = 5

        theta1P1_P2 = 0
        theta2P1_P2 = np.linspace(150, 0, can_puntos)
        for i in range(can_puntos):
            MTH = self.CD(theta1P1_P2, theta2P1_P2[i]) 
            self.mover_servos(theta1P1_P2 , theta2P1_P2[i])
            
        theta1P2_P3 = np.linspace(0, 90, can_puntos)
        theta2P2_P3 = 0
        for i in range(can_puntos):
            MTH = self.CD(theta1P2_P3[i], theta2P2_P3) 
            self.mover_servos(theta1P2_P3[i] , theta2P2_P3)

        theta1P3_P4 = np.linspace(90, 180, can_puntos)
        theta2P3_P4 = 0
        for i in range(can_puntos):
            MTH = self.CD(theta1P3_P4[i], theta2P3_P4) 
            self.mover_servos(theta1P3_P4[i] , theta2P3_P4)

        theta1P4_P5 = 180
        theta2P4_P5 = np.linspace(0, 150, can_puntos)
        for i in range(can_puntos):
            MTH = self.CD(theta1P4_P5, theta2P4_P5[i]) 
            self.mover_servos(theta1P4_P5 , theta2P4_P5[i])
            # Realizar accion para la ultima iteracion
            if i == can_puntos - 1: #Ultima Iteracion
                self.pxInicial = MTH.t[0]
                self.pyInicial = MTH.t[1]

    def imagenes(self):
        puntos = 5 #De a cada cuantos puntos se guarda
         
        #FIGURA 2 Chevrolet
        #if opcion == 2:
            #Leer la imagen en formato cv2
        imagen = cv2.imread('/home/juliapaez1227/Documents/taller2corte/chevrolet.png')

            # Convertir la imagen a escala de grises
        img_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

            # Aplicar suavizado Gaussiano (filtro) Imagen Filtrada
        img_fil = cv2.GaussianBlur(img_gris, (5,5), 0) #El 0 calcula la Desviacion Estandar automaticamente

            # Encontrar los contornos en la imagen (imagen, metodo, para que se almacenen todos los puntos)
        contornos, _ = cv2.findContours(img_fil, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            #print(len(contornos)) #Corroborar numero de contornos
        print(contornos)

        ofset=500
            # COMTORMO #1
            # Ajustar espejo, coordenadas y convertirlas en un array numpy
        contorno1 = np.array([[(punto[0][0]/100)-10, ((punto[0][1]*-1+ofset)/100)+10.5] for punto in contornos[0]])
            # Seleccionar cada n elemento y agregar el ultimo punto
        contorno1 = np.vstack([contorno1[0::puntos], contorno1[-1]])

            # COMTORMO #2
            # Ajustar espejo, coordenadas y convertirlas en un array numpy
        contorno2 = np.array([[(punto[0][0]/100)-10, ((punto[0][1]*-1+ofset)/100)+10.5] for punto in contornos[1]])
            # Seleccionar cada n elemento y agregar el ultimo punto
        contorno2 = np.vstack([contorno2[0::puntos], contorno2[-1]])

            #AHORA SI DIBUJAR CONTORNOS
            #CONTORNO 1
        for i in range(len(contorno1)):
            theta1, theta2 = self.CI(contorno1[i][0],contorno1[i][1])
            MTH = self.CD(theta1, theta2) 
            self.mover_servos(theta1, theta2)

            #CONTORNO 2
        for i in range(len(contorno2)):
            theta1, theta2 = self.CI(contorno2[i][0],contorno2[i][1])
            MTH = self.CD(theta1, theta2) 
            self.mover_servos(theta1, theta2)
                #Ultima Iteracion
            if i == len(contorno2) - 1: 
                    #Guardar ultimas coordenadas, para el siguiente metodo
                self.pxInicial = MTH.t[0]
                self.pyInicial = MTH.t[1]
         

#/home/juliapaez1227/Documents/taller2corte/imagenes
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.boton_area_trabajo.clicked.connect(ui.esp_trabajo)
    ui.boton_coordenadas.clicked.connect(ui.imagenes)
    MainWindow.show()
    sys.exit(app.exec_())
