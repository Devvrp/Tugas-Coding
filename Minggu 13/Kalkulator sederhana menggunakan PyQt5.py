import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QMessageBox

class Kalkulator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Kalkulator Sederhana')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.input = QLineEdit(self)
        self.input.setPlaceholderText('Masukkan operasi matematika')
        layout.addWidget(self.input)

        button_layout = QHBoxLayout()

        self.button_tambah = QPushButton('+', self)
        self.button_tambah.clicked.connect(lambda: self.hitung('+'))
        button_layout.addWidget(self.button_tambah)

        self.button_kurang = QPushButton('-', self)
        self.button_kurang.clicked.connect(lambda: self.hitung('-'))
        button_layout.addWidget(self.button_kurang)

        self.button_kali = QPushButton('*', self)
        self.button_kali.clicked.connect(lambda: self.hitung('*'))
        button_layout.addWidget(self.button_kali)

        self.button_bagi = QPushButton('/', self)
        self.button_bagi.clicked.connect(lambda: self.hitung('/'))
        button_layout.addWidget(self.button_bagi)

        self.button_pangkat = QPushButton('^', self)
        self.button_pangkat.clicked.connect(lambda: self.hitung('^'))
        button_layout.addWidget(self.button_pangkat)

        self.button_modulus = QPushButton('%', self)
        self.button_modulus.clicked.connect(lambda: self.hitung('%'))
        button_layout.addWidget(self.button_modulus)

        layout.addLayout(button_layout)

        self.button_clear = QPushButton('Clear', self)
        self.button_clear.clicked.connect(self.clear_input)
        layout.addWidget(self.button_clear)

        self.setLayout(layout)

    def hitung(self, operasi):
        try:
            input_text = self.input.text()
            angka1, angka2 = map(float, input_text.split(operasi))

            if operasi == '+':
                hasil = angka1 + angka2
            elif operasi == '-':
                hasil = angka1 - angka2
            elif operasi == '*':
                hasil = angka1 * angka2
            elif operasi == '/':
                if angka2 == 0:
                    raise ValueError("Tidak dapat membagi dengan nol.")
                hasil = angka1 / angka2
            elif operasi == '^':
                hasil = angka1 ** angka2
            elif operasi == '%':
                hasil = angka1 % angka2

            self.input.setText(str(hasil))

        except ValueError:
            QMessageBox.warning(self, 'Error', 'Masukkan format angka yang valid!')

    def clear_input(self):
        self.input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Kalkulator()
    window.show()
    sys.exit(app.exec_())
