import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class VentanaDatosPersonales(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configuración de la ventana
        self.setWindowTitle('Datos Característicos de una Persona')
        self.setGeometry(100, 100, 400, 400)
        
        # Crear un layout vertical
        layout = QVBoxLayout()
        
        # Crear etiquetas y campos de entrada para 10 datos, ya que como seran muchas entradas decidimos hacer mejor un ciclo for|
        self.datos = []
        for i in range(1, 11):
            etiqueta = QLabel(f'Dato {i}:')
            entrada = QLineEdit()
            self.datos.append(entrada)
            layout.addWidget(etiqueta)
            layout.addWidget(entrada)
        
        # Botón para enviar los datos
        submit_button = QPushButton('Enviar')
        submit_button.clicked.connect(self.mostrar_datos)
        
        layout.addWidget(submit_button)
        
        # Establecer el layout de la ventana
        self.setLayout(layout)

    # Función para manejar la acción del botón
    def mostrar_datos(self):
        datos = [entrada.text() for entrada in self.datos]
        print(f"Datos ingresados: {datos}")

# Iniciar la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaDatosPersonales()
    ventana.show()
    sys.exit(app.exec_())
