import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt  

class VentanaContra(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana
        self.setWindowTitle('Ingresar la contraseña super Secreta')
        self.setGeometry(100, 100, 300, 150)
         # Aqui iria el cambio de color de la ventana pero nos dio demasiado errores, incluso con la solucion encontrada en internet
         # del anterior ejercicio asi que decidimos no agregarla :(
        
        # Creamos un layout vertical
        layout = QVBoxLayout()
        
        # Etiqueta y campo de entrada para la contraseña secreta
        contra_label = QLabel('Ingrese su contraseña super secreta:')
        self.contra_input = QLineEdit()
        
        # Configuraramos el campo de texto como entrada de contraseña
        self.contra_input.setEchoMode(QLineEdit.Password)
        

        # Botón para leer la contraseña
        submit_button = QPushButton('Enviar contraseña')
        submit_button.clicked.connect(self.mostrar_contra)  # Esta sera la accion que realice el boton
        
        # Esta linea de aqui lo que hara es que al apretar la tecla enter la contraseña sera ingresada
        #como si estuvieramos apretando el boton con el cursor
        self.contra_input.returnPressed.connect(self.mostrar_contra) 
        
        
        # Añadimos los widgets al layout
        layout.addWidget(contra_label)
        layout.addWidget(self.contra_input)
        layout.addWidget(submit_button)
        
        # Establecemos el layout de la ventana
        self.setLayout(layout)

    # Función para manejar la acción del botón
    def mostrar_contra(self):
        contra = self.contra_input.text()
        print(f"Contraseña ingresada: {contra}")

# Iniciamos la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaContra()
    ventana.show()
    sys.exit(app.exec_())
