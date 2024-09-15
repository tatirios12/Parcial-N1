import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class VentanaMascotas(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana
        self.setWindowTitle('Datos de Mascotas')
        self.setGeometry(100, 100, 400, 300)
        
        # Creamos un layout vertical
        layout = QVBoxLayout()
        
       # En los siguientes 3 bloques de codigo lo que haremos sera configurar los label para ingresar los datos de las mascotas    
    
        # Datos de la primera mascota
        mascota1_label = QLabel('Mascota 1 - Nombre:')
        self.mascota1_nombre = QLineEdit()
        mascota1_tipo = QLabel('Mascota 1 - Tipo:')
        self.mascota1_tipo_input = QLineEdit()
        mascota1_edad = QLabel('Mascota 1 - Edad:')
        self.mascota1_edad_input = QLineEdit()
        
        # Datos de la segunda mascota
        mascota2_label = QLabel('Mascota 2 - Nombre:')
        self.mascota2_nombre = QLineEdit()
        mascota2_tipo = QLabel('Mascota 2 - Tipo:')
        self.mascota2_tipo_input = QLineEdit()
        mascota2_edad = QLabel('Mascota 2 - Edad:')
        self.mascota2_edad_input = QLineEdit()
        
        # Datos de la tercera mascota
        mascota3_label = QLabel('Mascota 3 - Nombre:')
        self.mascota3_nombre = QLineEdit()
        mascota3_tipo = QLabel('Mascota 3 - Tipo:')
        self.mascota3_tipo_input = QLineEdit()
        mascota3_edad = QLabel('Mascota 3 - Edad:')
        self.mascota3_edad_input = QLineEdit()
        
        # Botón para enviar los datos
        submit_button = QPushButton('Enviar')
        submit_button.clicked.connect(self.mostrar_mascotas)
        self.mascota3_edad_input.returnPressed.connect(self.mostrar_mascotas) # esta linea siempre es para poder usar la tecla enter
        
        # Añadimos los widgets al layout
        layout.addWidget(mascota1_label)
        layout.addWidget(self.mascota1_nombre)
        layout.addWidget(mascota1_tipo)
        layout.addWidget(self.mascota1_tipo_input)
        layout.addWidget(mascota1_edad)
        layout.addWidget(self.mascota1_edad_input)
        
        layout.addWidget(mascota2_label)
        layout.addWidget(self.mascota2_nombre)
        layout.addWidget(mascota2_tipo)
        layout.addWidget(self.mascota2_tipo_input)
        layout.addWidget(mascota2_edad)
        layout.addWidget(self.mascota2_edad_input)
        
        layout.addWidget(mascota3_label)
        layout.addWidget(self.mascota3_nombre)
        layout.addWidget(mascota3_tipo)
        layout.addWidget(self.mascota3_tipo_input)
        layout.addWidget(mascota3_edad)
        layout.addWidget(self.mascota3_edad_input)
        
        layout.addWidget(submit_button)
        
        # Establecemos el layout de la ventana
        self.setLayout(layout)

    # Función para manejar la acción del botón
    def mostrar_mascotas(self):
        mascota1 = f"Nombre: {self.mascota1_nombre.text()}, Tipo: {self.mascota1_tipo_input.text()}, Edad: {self.mascota1_edad_input.text()}"
        mascota2 = f"Nombre: {self.mascota2_nombre.text()}, Tipo: {self.mascota2_tipo_input.text()}, Edad: {self.mascota2_edad_input.text()}"
        mascota3 = f"Nombre: {self.mascota3_nombre.text()}, Tipo: {self.mascota3_tipo_input.text()}, Edad: {self.mascota3_edad_input.text()}"
        
        print(f"Mascota 1: {mascota1}")
        print(f"Mascota 2: {mascota2}")
        print(f"Mascota 3: {mascota3}")

# Iniciamos la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaMascotas()
    ventana.show()
    sys.exit(app.exec_())
