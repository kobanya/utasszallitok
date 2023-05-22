import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt, QSize


class PassengerCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Utasszállítók")
        self.setGeometry(200, 300, 1150, 400)

        self.details_label = QLabel("", self)
        self.details_label.setGeometry(10, 200, 300, 180)
        self.details_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.details_label.setStyleSheet("border: 1px solid black;")

        self.table = QTableWidget(self)
        self.table.setGeometry(320, 10, 800, 380)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.table.itemSelectionChanged.connect(self.display_selected_row_data)

        self.load_data()

    def load_data(self):
        with open('utasszallitok.txt', 'r') as file:
            lines = file.readlines()

            header = lines[0].strip().split(';')
            self.table.setColumnCount(len(header))
            self.table.setHorizontalHeaderLabels(header)

            data = [line.strip().split(';') for line in lines[1:]]
            self.table.setRowCount(len(data))

            for i, row in enumerate(data):
                for j, item in enumerate(row):
                    table_item = QTableWidgetItem(item)
                    table_item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                    self.table.setItem(i, j, table_item)

            self.table.setEditTriggers(QTableWidget.NoEditTriggers)
            self.table.setSelectionBehavior(QTableWidget.SelectRows)
            self.table.setSelectionMode(QTableWidget.SingleSelection)

            self.table.setSortingEnabled(True)

    def display_selected_row_data(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            selected_data = []
            for column in range(self.table.columnCount()):
                header_item = self.table.horizontalHeaderItem(column)
                data_item = self.table.item(selected_row, column)
                selected_data.append(f"{header_item.text().upper()}: \t{data_item.text()}")

            details_text = "<br>".join(selected_data)
            self.details_label.setText(f'\t{details_text}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PassengerCalculator()
    window.show()
    sys.exit(app.exec_())
