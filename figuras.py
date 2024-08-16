from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import cv2
from PyQt5.QtGui import QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(809, 567)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 460, 311, 71))
        self.label.setStyleSheet("border-image: url(:/cct/logo ECCI.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 430, 271, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 170, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 40, 461, 361))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 400, 611, 31))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 400, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(450, 10, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

  
        #-------------------------------------
        #--------acciones de boton------------
        #-------------------------------------
        self.pushButton.clicked.connect(self.cargar_imagen)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Analisis Imagen"))
        self.label_2.setText(_translate("MainWindow", "Daniel ricardo quiroga"))
        self.pushButton.setText(_translate("MainWindow", "Analizar Img"))
        self.label_5.setText(_translate("MainWindow", "Directorio"))
        self.label_6.setText(_translate("MainWindow", "Imagen original"))

    def cargar_imagen (self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Imagenes (*.png *.jpg *.jpeg *.bmp)")
        file_dialog.setViewMode(QFileDialog.Detail)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        
        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]  #aloja direccion de archivo
           
              #
            self.label_4.setText(file_path)             #aca imprimo la direccion del archivo
            
            img=cv2.imread(file_path)                   #creo objeto cv para la imagen leida
            img_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
            imgbinary = cv2.Canny(img,20,60)            #cambio a imagne binaria
            contornos, _ =cv2.findContours(imgbinary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)   #creo cortornos
            print(contornos)                            #imprimo contornos
            cv2.drawContours(img,contornos,-1,(0,255,0),3)
        
            self.label_3.setPixmap(QPixmap(cv2.imshow("Imagen analizada",img)))
            

#import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



