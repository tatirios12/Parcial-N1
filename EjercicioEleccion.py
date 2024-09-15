import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton, QComboBox, QSpinBox, QPushButton
from PyQt5.QtCore import Qt

class VentanaDatos(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana
        self.setWindowTitle('Datos Personales')
        self.setGeometry(100, 100, 300, 300)
        self.setStyleSheet('background-color:lightgray;')  # Fondo gris claro para la ventana(no se porque no lo refleja)
        
        # Creamos un layout vertical
        layout = QVBoxLayout()

        # Etiqueta y radiobox para seleccionar el género
        genero_label = QLabel('Seleccione su género:')
        self.genero_masculino = QRadioButton('Masculino')
        self.genero_femenino = QRadioButton('Femenino')

        # Combobox para seleccionar el país de residencia
        pais_label = QLabel('Seleccione su país de residencia:')
        self.pais_combobox = QComboBox()
        self.pais_combobox.addItems(['Elija su país', 'Brasil', 'El Salvador', 'Argentina', 'Colombia', 'Chile', 'Perú'])

        # Spinbox para seleccionar la edad
        edad_label = QLabel('Seleccione su edad:')
        self.edad_spinbox = QSpinBox()
        self.edad_spinbox.setRange(0, 120)  # Edad entre 0 y 120 años, si, creemos que hay gente de esa edad xd(broma)

        # Botón para enviar los datos
        submit_button = QPushButton('Enviar')
        submit_button.clicked.connect(self.mostrar_datos)

        # Usamos la misma solucion que con el ejercio del nombre y la edad
        self.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #333;
            }
            QRadioButton {
                font-size: 14px;
            }
            QComboBox {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px;
                background-color: #fff;
                font-size: 14px;
            }
            QComboBox::drop-down {
                border: 1px solid #ccc;
                border-radius: 5px;
                background-color: #fff;
                width: 20px;
            }
            QComboBox::down-arrow {
                image: url(https://img.icons8.com/material-outlined/24/000000/expand-arrow.png);
            }
            QSpinBox {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px;
                background-color: #fff;
                font-size: 14px;
            }
            QPushButton {
                background-color: #0078d4;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
        """)

        # Añadimos los widgets al layout
        layout.addWidget(genero_label)
        layout.addWidget(self.genero_masculino)
        layout.addWidget(self.genero_femenino)
        layout.addWidget(pais_label)
        layout.addWidget(self.pais_combobox)
        layout.addWidget(edad_label)
        layout.addWidget(self.edad_spinbox)
        layout.addWidget(submit_button)

        # Establecemos el layout de la ventana
        self.setLayout(layout)

    # Añadimos la Función para manejar la acción del botón
    def mostrar_datos(self):
        genero = 'Masculino' if self.genero_masculino.isChecked() else 'Femenino' if self.genero_femenino.isChecked() else 'No especificado'
        pais = self.pais_combobox.currentText()
        edad = self.edad_spinbox.value()

        print(f"Género: {genero}, País: {pais}, Edad: {edad}")

# Iniciamos la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaDatos()
    ventana.show()
    sys.exit(app.exec_())
