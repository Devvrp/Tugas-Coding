import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox

class BarangApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Tambah Barang dan Harga")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        form_layout = QHBoxLayout()
        self.label_barang = QLabel('Nama Barang:')
        self.input_barang = QLineEdit(self)
        self.label_harga = QLabel('Harga:')
        self.input_harga = QLineEdit(self)
        self.input_harga.setPlaceholderText('0')

        form_layout.addWidget(self.label_barang)
        form_layout.addWidget(self.input_barang)
        form_layout.addWidget(self.label_harga)
        form_layout.addWidget(self.input_harga)

        self.button_tambah = QPushButton('Tambah Barang', self)
        self.button_tambah.clicked.connect(self.tambah_barang)

        self.tabel_barang = QTableWidget(self)
        self.tabel_barang.setColumnCount(2)
        self.tabel_barang.setHorizontalHeaderLabels(['Nama Barang', 'Harga'])

        layout.addLayout(form_layout)
        layout.addWidget(self.button_tambah)
        layout.addWidget(self.tabel_barang)

        self.setLayout(layout)

    def tambah_barang(self):
        nama_barang = self.input_barang.text()
        harga = self.input_harga.text()

        if not nama_barang or not harga.isdigit():
            QMessageBox.warning(self, "Input Error", "Masukkan nama barang dan harga yang valid!")
            return

        row_position = self.tabel_barang.rowCount()
        self.tabel_barang.insertRow(row_position)
        self.tabel_barang.setItem(row_position, 0, QTableWidgetItem(nama_barang))
        self.tabel_barang.setItem(row_position, 1, QTableWidgetItem(f"Rp {int(harga):,}"))

        self.input_barang.clear()
        self.input_harga.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BarangApp()
    window.show()
    sys.exit(app.exec_())