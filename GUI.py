import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class PitotCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sebességi osztály")
        self.setGeometry(200, 300, 1300, 450)

        self.label_sebesseg = QLabel("Sebesség:", self)
        self.label_sebesseg.move(50, 30)

        self.input_sebesseg = QLineEdit(self)
        self.input_sebesseg.move(170, 30)

        self.button_szamitas = QPushButton("Számítás", self)
        self.button_szamitas.move(170, 80)
        self.button_szamitas.clicked.connect(self.calculate_speed_category)

        self.label_result = QLabel("", self)
        self.label_result.setGeometry(40, 130, 300, 30)
        self.label_result.setAlignment(Qt.AlignCenter)

        self.label_darab = QLabel("", self)
        self.label_darab.setGeometry(350, 350, 400, 30)
        self.label_darab.setAlignment(Qt.AlignLeft)

        self.label_max_sebesseg = QLabel("", self)
        self.label_max_sebesseg.setGeometry(350, 370, 700, 30)
        self.label_max_sebesseg.setAlignment(Qt.AlignLeft)

        self.label_max_utas = QLabel("", self)
        self.label_max_utas.setGeometry(350, 390, 700, 30)
        self.label_max_utas.setAlignment(Qt.AlignLeft)

        self.label_image = QLabel(self)
        self.label_image.setGeometry(80, 180, 240, 150)
        self.label_image.setAlignment(Qt.AlignCenter)

        self.table = QTableWidget(self)
        self.table.setGeometry(350, 30, 240, 300)
        self.table.setSortingEnabled(True) # sorrendbe rendezés

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

        # A lista elemeinek darabszáma
        darabszam = len(lines) - 1
        self.label_darab.setText(f"A táblázatban található repülőgépek száma: {str(darabszam)} darab.")

        # Legnagyobb utazási sebességű gép adatai
        max_sebesseg = 0
        legnagyobb_gep_adatok = None
        for i in range(1, len(lines)):
            sor = lines[i].strip().split(';')
            try:
                sebesseg = float(sor[4])
                if sebesseg > max_sebesseg:
                    max_sebesseg = sebesseg
                    legnagyobb_gep_adatok = sor
            except ValueError:
                continue

        if legnagyobb_gep_adatok:
            legnagyobb_gep_nev = legnagyobb_gep_adatok[0]
            legnagyobb_gep_sebesseg = legnagyobb_gep_adatok[4]

            self.label_max_sebesseg.setText(
                f"Legnagyobb sebességű gép a {legnagyobb_gep_nev} melynek utazósebessége: {legnagyobb_gep_sebesseg} km/h")
        else:
            self.label_max_sebesseg.setText("Nincs elérhető adat a legnagyobb sebességű gépről.")

            # Legtöbb utast szállító gép adatai
        legtobb_utas = 0
        legtobb_tipus = ""
        for i in range(1, len(lines)):
            sor = lines[i].strip().split(';')
            if len(sor) >= 5:  # Ellenőrzés, hogy a sor tartalmazza-e a szükséges elemeket
                utasok = sor[2].split('-')
                if len(utasok) >= 2:  # Ellenőrzés, hogy a szöveg megfelelően osztható-e
                    try:
                        utasok = int(utasok[1])
                        if utasok > legtobb_utas:
                            legtobb_utas = utasok
                            legtobb_tipus = sor[0]
                    except ValueError:
                        continue

        if legtobb_tipus:
            self.label_max_utas.setText(f"Legtöbb utast szállító gép típusa: {legtobb_tipus}, amely  {legtobb_utas} utast is el tud szállítani.")
        else:
            self.label_max_utas.setText("Nincs elérhető adat a legtöbb utast szállító gépről.")

    def calculate_speed_category(self):
        speed_text = self.input_sebesseg.text()
        if not speed_text:
            # Ha a beviteli mező üres, hibaüzenetet jelenítünk meg
            self.label_result.setText("Kérem adjon meg egy sebességet!")
            self.label_result.setStyleSheet("color: red")  # Beállítjuk a piros színt
            self.label_image.clear()  # Töröljük a képet
            return

        try:
            speed = float(speed_text)

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
            self.label_result.setStyleSheet("color: blue")

            # Set the image
            pixmap = QPixmap(image_path)
            pixmap = pixmap.scaled(self.label_image.size(), Qt.AspectRatioMode.KeepAspectRatio)
            self.label_image.setPixmap(pixmap)

        except ValueError:
            # Ha a beviteli mező nem számot tartalmaz, hibaüzenetet jelenítünk meg
            self.label_result.setText("Érvénytelen sebességérték!")
            self.label_image.clear()  # Töröljük a képet


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PitotCalculator()
    window.show()
    sys.exit(app.exec_())