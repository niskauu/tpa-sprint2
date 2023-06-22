from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QPushButton, QMessageBox, QLabel, QDateEdit

class Reserva(QWidget):
    def __init__(self):
        super().__init__()
        self.iniciarUI()
    
    def iniciarUI(self):
        self.setFixedSize(600, 700) #geometria de la ventana
        self.setWindowTitle("Formulario De Reserva de Excursion")
        self.reservar()
        self.show()

    def reservar(self):
        pass