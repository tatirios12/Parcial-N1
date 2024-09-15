import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QComboBox
from PyQt5.QtCore import Qt

class VentanaNombreEdad(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana, en esta parte de aqui hacemos las configuraciones basicamente de la ventana que son el color
        # Tamaño y el nombre que esta ventana va a tener al momento de ejecutarla
        self.setWindowTitle('Nombre y Edad')
        self.setGeometry(100, 100, 300, 200)
        self.setStyleSheet('background-color:beige;')

        # Creamos un layout vertical
        layout = QVBoxLayout()

        # Etiquetas para el nombre completo y la edad, sera la plantilla de lo que se mostrara en la ventana
        # con el if que realizamos en la parte de abajo, el nombre y la edad cambiara en base a la opcion que se elija 
        self.nombre_label = QLabel('Nombre: Alexander Chicas')
        self.edad_label = QLabel('Edad: 21 años')

        # Creamos un combo box para seleccionar el nombre, creamos este combo box para mostrar ambos nombres 
        self.combo_box = QComboBox()
        self.combo_box.addItem('Alexander Chicas')
        self.combo_box.addItem('Tatiana Rios')
        self.combo_box.currentIndexChanged.connect(self.cambiar_datos)

        # Estilo moderno para el QComboBox, esto lo anduvimos buscando por internet porque
        # no nos gusto el estilo xp que tenia por defecto
        self.combo_box.setStyleSheet("""
            QComboBox {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px 10px;
                background-color: lightgray;
                font-size: 14px;
            }
            QComboBox::drop-down {
                border: 1px solid #ccc;
                border-radius: 5px;
                background-color: lightgray;
            }
            QComboBox QAbstractItemView {
                background-color: lightgray;
                selection-background-color: white;
                selection-color: black;
            }
        """)

        # Centrar el texto
        self.nombre_label.setAlignment(Qt.AlignCenter)
        self.edad_label.setAlignment(Qt.AlignCenter)

        # Añadimos los widgets al layout
        layout.addWidget(self.combo_box)
        layout.addWidget(self.nombre_label)
        layout.addWidget(self.edad_label)

        # Establecemos el layout de la ventana
        self.setLayout(layout)

    def cambiar_datos(self):
        # Obtener el texto seleccionado en el combo box
        nombre_seleccionado = self.combo_box.currentText()

        # Actualizar el nombre y la edad en función de la selección, hicimos esto con la intecion de poder mostar ambos
        # nombres de los integrantes
        if nombre_seleccionado == 'Alexander Chicas':
            self.nombre_label.setText('Nombre: Alexander Chicas')
            self.edad_label.setText('Edad: 21 años')
        elif nombre_seleccionado == 'Tatiana Rios':
            self.nombre_label.setText('Nombre: Tatiana Rios')
            self.edad_label.setText('Edad: 23 años')

# Iniciamos la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaNombreEdad()
    ventana.show()
    sys.exit(app.exec_())
