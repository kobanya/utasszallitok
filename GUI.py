import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class PitotCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sebességi osztály")
        self.setGeometry(200, 300, 1300, 400)

        self.label_pressure = QLabel("Sebesség:", self)
        self.label_pressure.move(50, 30)

        self.input_pressure = QLineEdit(self)
        self.input_pressure.move(170, 30)

        self.button_calculate = QPushButton("Számítás", self)
        self.button_calculate.move(170, 80)
        self.button_calculate.clicked.connect(self.calculate_speed_category)

        self.label_result = QLabel("", self)
        self.label_result.setGeometry(40, 130, 300, 30)
        self.label_result.setAlignment(Qt.AlignCenter)

        self.label_darab = QLabel("", self)
        self.label_darab.setGeometry(350, 340, 400, 30)
        self.label_darab.setAlignment(Qt.AlignLeft)

        self.label_image = QLabel(self)
        self.label_image.setGeometry(80, 180, 240, 150)
        self.label_image.setAlignment(Qt.AlignCenter)

        self.table = QTableWidget(self)
        self.table.setGeometry(350, 30, 240, 300)

        self.load_data()

    def load_data(self):
        with open('utasszallitok.txt', 'r') as file:
            lines = file.readlines()

            # Felbontás és adatok hozzáadása a táblázathoz
            header = lines[0].strip().split(';')
            self.table.setColumnCount(len(header))
            self.table.setHorizontalHeaderLabels(header)
            self.table.setGeometry(350, 30, 900, 300)
            self.table.setColumnWidth(0, 215)
            self.table.setColumnWidth(4, 120)
            self.table.setColumnWidth(5, 120)

            data = [line.strip().split(';') for line in lines[1:]]
            self.table.setRowCount(len(data))
            for i, row in enumerate(data):
                for j, item in enumerate(row):
                    self.table.setItem(i, j, QTableWidgetItem(item))

        #A lista elemeinek darabszáma
        darabszam = len(lines)-1
        self.label_darab.setText(f"A táblázatban található repülőgépek száma: {str(darabszam)} darab.")

    def calculate_speed_category(self):
        speed = float(self.input_pressure.text())

        if speed < 500:
            speed_category = "Alacsony sebességű repülőgép"
            image_path = "dulpafedele.png"
        elif speed < 1000:
            speed_category = "Szubszónikus sebességű repülőgép"
            image_path = "szub.png"
        elif speed < 1200:
            speed_category = "Transzszónikus sebességű repülőgép"
            image_path = "concorde.png"
        else:
            speed_category = "Hiperszónikus sebességű repülőgép"
            image_path = "mig.jpg"

        self.label_result.setText(speed_category)

        # Set the image
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(self.label_image.size(), Qt.AspectRatioMode.KeepAspectRatio)
        self.label_image.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PitotCalculator()
    window.show()
    sys.exit(app.exec_())
