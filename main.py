
#Coded By Sihab Sahariar
from PyQt5 import QtCore, QtGui, QtWidgets
import serial
s = serial.Serial('COM5',9600,timeout = 2) #My Bluetooth COM Port is 5
class Ui_MainWindow(object):
    #def setupUi(self, MainWindow):
    def __init__(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(838, 557)
        MainWindow.setStyleSheet("background-color: rgb(71, 80, 98);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 841, 51))
        self.frame.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(170, 0, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(130, 220, 281, 261))
        self.frame_2.setStyleSheet("background-color: rgb(255, 253, 238);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(40, 60, 201, 41))
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 120, 201, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 170, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setObjectName("label_2")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(430, 220, 281, 261))
        self.frame_3.setStyleSheet("background-color: rgb(255, 253, 238);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 60, 201, 41))
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 120, 201, 41))
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 170, 127);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 170, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 490, 581, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 127);")
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 90, 581, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 127);")
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setObjectName("label_5")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(350, 90, 91, 51))
        self.textEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 127);")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(570, 90, 141, 51))
        self.pushButton_5.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.led_on)
        self.pushButton_2.clicked.connect(self.led_off)
    def led_on(self):
        try:
            s.write(bytes("a",'utf-8'))
            #self.label_4.setText("<html><head/><body><p align=\"center\">LED ON</p></body></html>")

        except Exception as e:
            #self.label_4.setText("<html><head/><body><p align=\"center\">SOMETHING WRONG</p></body></html>")
            print(f'Something went wrong: {e}')   

    def led_off(self):
        try:
            
            s.write(bytes("b",'utf-8'))
        except Exception as e:
            #self.label_4.setText("<html><head/><body><p align=\"center\">SOMETHING WRONG</p></body></html>")
            print(f'Something went wrong: {e}')   
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyQt5-HC05"))
        self.label.setText(_translate("MainWindow", "BLUETOOTH - HC05 CONTROl PANEL"))
        self.pushButton.setText(_translate("MainWindow", "TURN ON LED"))
        self.pushButton.setShortcut(_translate("MainWindow", "W"))
        self.pushButton_2.setText(_translate("MainWindow", "TURN OFF LED"))
        self.pushButton_2.setShortcut(_translate("MainWindow", "E"))
        self.label_2.setText(_translate("MainWindow", "     LED CONTROL"))
        self.pushButton_3.setText(_translate("MainWindow", "TURN ON FAN"))
        self.pushButton_4.setText(_translate("MainWindow", "TURN OFF FAN"))
        self.label_3.setText(_translate("MainWindow", "     FAN CONTROL"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">STATUS</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">BLUETOOTH PORT :</span></p></body></html>"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#55ffff;\">COM5</span></p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "CONNECT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
