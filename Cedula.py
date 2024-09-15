import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class VentanaCedulaNombre(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana
        self.setWindowTitle('Ingreso de Cédula y Nombre')
        self.setGeometry(100, 100, 300, 200)
        # El mismo problemas que el ejercicio anterior y probablemente con los que le siguen 
        
        # Crear un layout vertical
        layout = QVBoxLayout()
        
        # Etiquetas y campos de entrada
        cedula_label = QLabel('Número de cédula:')
        self.cedula_input = QLineEdit()
        
        nombre_label = QLabel('Nombre completo:')
        self.nombre_input = QLineEdit()
        
        # Botón para enviar
        submit_button = QPushButton('Enviar')
        submit_button.clicked.connect(self.mostrar_datos)
        self.nombre_input.returnPressed.connect(self.mostrar_datos) # esta linea siempre es para poder usar la tecla enter
        
        # Añadir widgets al layout
        layout.addWidget(cedula_label)
        layout.addWidget(self.cedula_input)
        layout.addWidget(nombre_label)
        layout.addWidget(self.nombre_input)
        layout.addWidget(submit_button)
        
        # Establecer el layout de la ventana
        self.setLayout(layout)

    # Función para manejar la acción del botón
    def mostrar_datos(self):
        cedula = self.cedula_input.text()
        nombre = self.nombre_input.text()
        print(f"Cédula: {cedula}, Nombre: {nombre}")

# Iniciar la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaCedulaNombre()
    ventana.show()
    sys.exit(app.exec_())
