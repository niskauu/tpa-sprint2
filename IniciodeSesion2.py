import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QLineEdit, QPushButton, QMessageBox, QLabel
from PyQt6.QtGui import QFont
from FormulariodeReserva2 import Reserva

class IniciarSesion(QWidget):

    #init + iniciar ui
    def __init__(self):
        super().__init__()
        self.iniciarUI()

    def iniciarUI(self):
        self.setFixedSize(400,200) #geometria de la ventana
        self.setWindowTitle("Inicio de Sesion")
        self.iniciar_sesion()
        self.show()
    
    def iniciar_sesion(self): #establecer diseño de la ventana
        self.estaloggeado = False #la persona no ha iniciado sesion

        #titulo
        titulo = QLabel()
        titulo.setText("Inicio De Sesion")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        titulo.setFont(font)

        #correo
        correo_label = QLabel()
        correo_label.setText("Correo: ")

        self.correo_input = QLineEdit()

        #contraseña
        contrasenia_label = QLabel()
        contrasenia_label
        contrasenia_label.setText("Contraseña: ")

        self.contrasenia_input = QLineEdit()
        self.contrasenia_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )

        #boton iniciar sesion
        iniciar_boton = QPushButton()
        iniciar_boton.setText("Ingresar")
            #conectar la interaccion con ingresar a la ventana principar
        iniciar_boton.clicked.connect(self.ingresar)

        layout = QVBoxLayout()
        layout.addWidget(titulo)
        layout.addWidget(correo_label)
        layout.addWidget(self.correo_input)
        layout.addWidget(contrasenia_label)
        layout.addWidget(self.contrasenia_input)
        layout.addWidget(iniciar_boton)

        self.setLayout(layout)

    #manejo de usuario si existe o no
    def ingresar(self):
        usuarios =[]
        datos = f"{self.correo_input.text()},{self.contrasenia_input.text()}"

        try:
            archivo= open("Dataset/usuarios.csv","r")
            lineas = archivo.readlines()

            for linea in lineas:
                usuarios.append(linea.strip("\n"))
            
            if datos in usuarios:
                QMessageBox.information(self,"Inicio Sesion",
                "Se ha iniciado sesion",
                QMessageBox.StandardButton.Ok,
                QMessageBox.StandardButton.Ok)
                self.estaloggeado = True
                self.close()
                self.abrir_reserva()

        except FileNotFoundError as x:
            QMessageBox.warning(self, "Error Message",
            f"Datos de inicio de sesion no encontrados: {x}",
            QMessageBox.StandardButton.Close,
            QMessageBox.StandardButton.Close)

        except Exception as x:
            QMessageBox.warning(self, "Error Message",
            f"Error en la ejecucion: {x}",
            QMessageBox.StandardButton.Close,
            QMessageBox.StandardButton.Close)    
    
    #se abre ventana de registro de reserva
    def abrir_reserva(self):
        self.abrir_ventana = Reserva()
        self.abrir_ventana.show()

if __name__ == "__main__":    
    app = QApplication(sys.argv)
    iniciar = IniciarSesion()
    sys.exit(app.exec())
