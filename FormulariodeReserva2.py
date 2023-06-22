import sys
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QVBoxLayout,QGridLayout, QWidget, QLineEdit, QPushButton, QMessageBox, QLabel, QDateEdit, QCalendarWidget
from PyQt6.QtGui import QFont
from PyQt6 import QtCore
from datetime import date, timedelta


class Reserva(QWidget):

    def __init__(self):
        super().__init__()
        self.iniciarUI()
    
    def iniciarUI(self):
        self.setFixedSize(600, 500) #geometria de la ventana
        self.setWindowTitle("Formulario De Reserva de Excursion")
        self.reservar()
        self.show()

    def reservar(self):
        
        #titulo
        titulo = QLabel()
        titulo.setText("Inicio De Sesion")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        titulo.setFont(font)

        #nombre
        nombre_label = QLabel()
        nombre_label.setText("Nombre: ")

        self.nombre_input = QLineEdit()

        #apellido
        apellido_label = QLabel()
        apellido_label.setText("Apellidos: ")

        self.apellido_input = QLineEdit()

        #rut
        rut_label = QLabel()
        rut_label.setText("Rut: ")

        self.rut_input = QLineEdit()

        #fecha de nacimiento
        fecha_nacimiento = QLabel()
        fecha_nacimiento.setText("Fecha de Nacimiento: ")
        self.fecha_nacimiento = QDateEdit()

        #telefono
        telefono_label = QLabel()
        telefono_label.setText("Telefono: ")

        self.telefono_input = QLineEdit()
        
        #email
        email_label = QLabel()
        email_label.setText("E-mail: ")

        self.email_input = QLineEdit()

        #calendario para fecha de inicio de la excursion
        fecha_inicio = QLabel()
        fecha_inicio.setText("Fecha Inicio De la Excursion: ")
        self.fecha_inicio = QCalendarWidget()
        self.fecha_inicio.setFixedSize(350,200)
            #minimo y maximo
        self.fecha_inicio.setMinimumDate(date.today())
        self.fecha_inicio.setMaximumDate(date.today()+timedelta(days=60))

        #boton
        boton = QPushButton()
        boton.setText("Agregar Reserva")
        boton.clicked.connect(self.guardar_reserva)

        #layouts
        layout_main = QVBoxLayout()
    
        layout_labels1 = QVBoxLayout()
        layout_labels1.addWidget(nombre_label)
        layout_labels1.addWidget(apellido_label)
        layout_labels1.addWidget(rut_label)

        layout_input1 = QVBoxLayout()
        layout_input1.addWidget(self.nombre_input)
        layout_input1.addWidget(self.apellido_input)
        layout_input1.addWidget(self.rut_input)

        layout_labels2 = QVBoxLayout()
        layout_labels2.addWidget(fecha_nacimiento)
        layout_labels2.addWidget(telefono_label)
        layout_labels2.addWidget(email_label)

        layout_input2 = QVBoxLayout()
        layout_input2.addWidget(self.fecha_nacimiento)
        layout_input2.addWidget(self.telefono_input)
        layout_input2.addWidget(self.email_input)

        layouts = QHBoxLayout()
        layouts.addLayout(layout_labels1)
        layouts.addLayout(layout_input1)
        layouts.addLayout(layout_labels2)
        layouts.addLayout(layout_input2)

        layout_main.addWidget(titulo)
        layout_main.addLayout(layouts)
        layout_main.addWidget(fecha_inicio)
        layout_main.addWidget(self.fecha_inicio)
        layout_main.addWidget(boton)

        self.setLayout(layout_main)

    #guarda datos
    def guardar_reserva(self):
        pass

if __name__ == "__main__":    
    app = QApplication(sys.argv)
    iniciar = Reserva()
    sys.exit(app.exec())