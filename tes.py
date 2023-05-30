import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication([])
window = QMainWindow()
window.setGeometry(450, 300, 500, 300)
window.setWindowTitle("Investasi anda")

labelKeluar = QLabel(window)
labelKeluar.setText("Jumlah Pengeluaran : ")
labelKeluar.setFixedWidth(150)
labelKeluar.move(20, 20)
leditKeluar = QLineEdit(window)
leditKeluar.setText('')
leditKeluar.setPlaceholderText('masukan')
leditKeluar.setToolTip('Silhkan masukkan jumlah pengeluaran')
leditKeluar.move(150, 20)
leditKeluar.setFixedWidth(300)

labelBunga = QLabel(window)
labelBunga.setText("Bunga(%) : ")
labelBunga.setFixedWidth(150)
labelBunga.move(20, 60)
leditBunga = QLineEdit(window)
leditBunga.setText('')
leditBunga.setPlaceholderText('Silahkan masukan jumlah bunga pertahun')
leditBunga.move(150, 60)
leditBunga.setFixedWidth(300)

labelTahun = QLabel(window)
labelTahun.setText("Tahun ke- : ")
labelTahun.setFixedWidth(150)
labelTahun.move(20, 100)
leditTahun = QLineEdit(window)
leditTahun.setText('')
leditTahun.setPlaceholderText('Silahkan Masukkan Tahun')
leditTahun.move(150, 100)
leditTahun.setFixedWidth(300)

btn_calculate = QPushButton(window)
btn_calculate.setText('Calculate')
btn_calculate.setFixedWidth(60)
btn_calculate.move(230, 160)

labelResult = QLabel(window)
labelResult.move(130, 200)
labelResult.setFixedWidth(400)


def calculate():
    isiKeluar = leditKeluar.text()
    isiKeluar = int(isiKeluar)
    isiBunga = leditBunga.text()
    isiBunga = int(isiBunga)
    isiTahun = leditTahun.text()
    isiTahun = int(isiTahun)
    if (isiTahun != 0 and isiKeluar != 0 and isiBunga != 0):
        isiResult = (isiKeluar*isiBunga/100+isiKeluar)*isiTahun
        isiResult = int(isiResult)
        labelResult.setText(f"Investasi anda selama {isiTahun}tahun menjadi RP. {isiResult}")


btn_calculate.clicked.connect(calculate)
window.show()
sys.exit(app.exec_())
