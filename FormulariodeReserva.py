from PyQt6 import QtCore, QtGui, QtWidgets
import pandas

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(636, 626)

        # Importar el dataset de los países
        self.ds = pandas.read_csv('Dataset/paises.csv')

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # horizontalLayoutWidget_2
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(300, 60, 371, 221))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        # widget_4
        self.widget_4 = QtWidgets.QWidget(parent=self.horizontalLayoutWidget_2)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.widget_4)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 131, 189))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        # Labels en verticalLayout_2
        self.label_7 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(parent=self.verticalLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        
        # widget_5
        self.widget_5 = QtWidgets.QWidget(parent=self.widget_4)
        self.widget_5.setGeometry(QtCore.QRect(70, 0, 241, 211))
        self.widget_5.setObjectName("widget_5")
        
        # LineEdits y ComboBox en widget_5
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.widget_5)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 170, 211, 21))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self.widget_5)
        self.lineEdit_7.setGeometry(QtCore.QRect(10, 120, 211, 21))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        
        self.comboBox = QtWidgets.QComboBox(parent=self.widget_5)
        self.comboBox.setGeometry(QtCore.QRect(10, 70, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Seleccione Género")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.widget_5)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 20, 121, 21))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        
        self.horizontalLayout_2.addWidget(self.widget_4)
        
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 330, 91, 16))
        self.label_6.setObjectName("label_6")
        
        self.comboBox_2 = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 330, 141, 22))
        self.comboBox_2.setMaximumSize(QtCore.QSize(16777215, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem('Seleccione País')
        self.ds['nombre'] = self.ds['nombre'].astype(str)
        self.comboBox_2.addItems(self.ds['nombre'].unique())
        
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 580, 131, 24))
        self.pushButton.setObjectName("pushButton")
        
        self.calendarWidget = QtWidgets.QCalendarWidget(parent=self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(350, 300, 272, 190))
        self.calendarWidget.setObjectName("calendarWidget")
        
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 371, 221))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        # widget
        self.widget = QtWidgets.QWidget(parent=self.horizontalLayoutWidget)
        self.widget.setObjectName("widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 131, 189))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Labels en verticalLayout
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        
        # widget_2
        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        self.widget_2.setGeometry(QtCore.QRect(120, 0, 151, 211))
        self.widget_2.setObjectName("widget_2")
        
        # LineEdits y DateEdit en widget_2
        self.dateEdit = QtWidgets.QDateEdit(parent=self.widget_2)
        self.dateEdit.setGeometry(QtCore.QRect(10, 120, 121, 21))
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 121, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.widget_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 70, 121, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.widget_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 170, 121, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        
        self.horizontalLayout.addWidget(self.widget)
        
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 370, 291, 16))
        self.label_11.setObjectName("label_11")
        
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 390, 321, 16))
        self.label_12.setObjectName("label_12")
        
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 500, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.treeView = QtWidgets.QTreeView(parent=self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(40, 420, 271, 71))
        self.treeView.setObjectName("treeView")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "Apellidos:"))
        self.label_8.setText(_translate("MainWindow", "Sexo:"))
        self.label_9.setText(_translate("MainWindow", "Domicilio:"))
        self.label_10.setText(_translate("MainWindow", "Email:"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Hombre"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Mujer"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Otro"))
        self.label_6.setText(_translate("MainWindow", "Nacionalidad:"))
        self.pushButton.setText(_translate("MainWindow", "Confirmar Reserva"))
        self.label.setText(_translate("MainWindow", " Informacion del usuario"))
        self.label_3.setText(_translate("MainWindow", "Nombre:"))
        self.label_2.setText(_translate("MainWindow", "Rut:"))
        self.label_4.setText(_translate("MainWindow", "Fecha de Nacimiento:"))
        self.label_5.setText(_translate("MainWindow", "Telefono de Contacto:"))
        self.label_11.setText(_translate("MainWindow", " Ingrese los documentos solicitados en esta bandeja"))
        self.label_12.setText(_translate("MainWindow", " (Constancia medica, declaración jurada, exámenes anexos)"))
        self.pushButton_2.setText(_translate("MainWindow", "Adjuntar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
