import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class InvestasiApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Penghitung Investasi")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        layout_investasi_awal = QHBoxLayout()
        self.label_investasi_awal = QLabel('Investasi Awal:')
        self.input_investasi_awal = QLineEdit(self)
        self.input_investasi_awal.setPlaceholderText('Masukkan jumlah investasi awal')
        layout_investasi_awal.addWidget(self.label_investasi_awal)
        layout_investasi_awal.addWidget(self.input_investasi_awal)

        layout_bunga = QHBoxLayout()
        self.label_bunga = QLabel('Bunga per Tahun (%):')
        self.input_bunga = QLineEdit(self)
        self.input_bunga.setPlaceholderText('Masukkan suku bunga per tahun (%)')
        layout_bunga.addWidget(self.label_bunga)
        layout_bunga.addWidget(self.input_bunga)

        layout_waktu = QHBoxLayout()
        self.label_waktu = QLabel('Jangka Waktu (tahun):')
        self.input_waktu = QLineEdit(self)
        self.input_waktu.setPlaceholderText('Masukkan jangka waktu dalam tahun')
        layout_waktu.addWidget(self.label_waktu)
        layout_waktu.addWidget(self.input_waktu)

        self.button_hitung = QPushButton('Hitung Total Investasi', self)
        self.button_hitung.clicked.connect(self.hitung_investasi)

        self.label_hasil = QLabel('Total Nilai Investasi: -')

        layout.addLayout(layout_investasi_awal)
        layout.addLayout(layout_bunga)
        layout.addLayout(layout_waktu)
        layout.addWidget(self.button_hitung)
        layout.addWidget(self.label_hasil)

        self.setLayout(layout)

    def hitung_investasi(self):
        try:
            investasi_awal = float(self.input_investasi_awal.text())
            bunga = float(self.input_bunga.text())
            waktu = int(self.input_waktu.text())

            total_investasi = investasi_awal * ((1 + (bunga / 100)) ** waktu)

            self.label_hasil.setText(f"Total Nilai Investasi: Rp {total_investasi:,.2f}")

        except ValueError:
            QMessageBox.warning(self, "Input Error", "Masukkan nilai yang valid untuk semua input!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InvestasiApp()
    window.show()
    sys.exit(app.exec_())
