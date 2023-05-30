import sys, json, moment, datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()


        self.setWindowTitle("ITK's Library") # atur judul window
        self.setWindowIcon(QIcon('books.png')) # atur icon window
        self.setGeometry(300, 150, 820, 480) # atur lokasi sama ukuran window

        # self.title = QLabel('Library')
        # self.profileLabel = QLabel('Azhar Rizqullah')

        self.table = QTableWidget() # inisialisasi widget QTableWidget
        header = self.table.horizontalHeader() # inisialisasi objek horizontal header    
        header.setSectionResizeMode(QHeaderView.Stretch) # atur properti resizenya ke stretch
        self.table.setFont(QFont('Helvetica', 12)) # atur font
        self.table.setEditTriggers(self.table.NoEditTriggers) # atur supaya gak bisa diedit

        # Table Title
        self.tableTitle = QLabel() # inisialisasi widget QLabel
        self.tableTitle.setFont(QFont('Helvetica', 14 )) # atur font
        self.tableTitle.setMinimumWidth(150) # atur lebar minimumnya jadi 150
        self.tableTitle.setAlignment(Qt.AlignCenter) # atur alignment

        self.showPatronsButton = QPushButton('Daftar Peminjam') # inisialisasi widget QPushButton
        self.showPatronsButton.setStyleSheet('background: orange; color: white') # atur css
        self.showPatronsButton.setFont(QFont('helvetica', 12)) # atur font
        self.showPatronsButton.clicked.connect(self.loadPatrons) # ngehubungin ke fungsi loadPatrons ketika diklik

        self.showCatalogButton = QPushButton('Katalog Buku') # inisialisasi widget QPushButton
        self.showCatalogButton.setStyleSheet('background: red; color: white') # atur css
        self.showCatalogButton.setFont(QFont('helvetica', 12)) # atur font
        self.showCatalogButton.clicked.connect(self.loadCatalog) # ngehubungin ke fungsi loadCatalog ketika diklik

        # form content
        self.inputJudul = QLineEdit()
        self.inputNama = QLineEdit()
        self.inputNim = QLineEdit()

        # atur tinggi minimum input
        inputHeight = 30
        self.inputJudul.setMinimumHeight(inputHeight)
        self.inputNama.setMinimumHeight(inputHeight)
        self.inputNim.setMinimumHeight(inputHeight)

        # atur placeholder
        self.inputJudul.setPlaceholderText('Judul')
        self.inputNama.setPlaceholderText('Nama')
        self.inputNim.setPlaceholderText('NIM')

        # atur font
        inputFont = QFont('Helvetica', 12)
        self.inputJudul.setFont(inputFont)
        self.inputNama.setFont(inputFont)
        self.inputNim.setFont(inputFont)

        self.inputNim.setMaxLength(8) # atur maksimum karakter yang bisa diinput
        self.inputNim.setValidator(QIntValidator()) # atur supaya cuma bisa masukkin angka


        self.resetButton = QPushButton('RESET') # inisialisasi widget QPushButton
        self.resetButton.setStyleSheet('background: red; color: white') # atur css
        self.resetButton.setFont(QFont('helvetica', 12)) # atur font
        self.resetButton.clicked.connect(self.reset) # dihubungin ke fungsi reset

        self.button = QPushButton('PINJAM') # inisialisasi widget QPushButton
        self.button.setStyleSheet('background: green; color: white') # atur css
        self.button.setFont(QFont('helvetica', 12)) # atur font
        self.button.clicked.connect(self.borrow) # dihubungin ke fungsi borrow

        # warning window
        self.msg = MessageBox() # inisialisasi window warning
        self.msg.setWindowTitle("Warning") # atur judul window
        self.msg.setStyleSheet("QLabel{font-size: 18px;}") # atur css

        # layouts
        self.tableTitleFrame = QFrame()
        # self.tableTitleFrame.setStyleSheet('border: 2px solid black')
        self.tableContent = QFrame()
        self.formContent = QFrame()
        self.formContent.setMaximumWidth(300)
        self.formButtons = QFrame() # frame sebelah kanan

        outerLayout = QHBoxLayout()
        tableLayout = QVBoxLayout()
        formLayout = QVBoxLayout()
        horizontalFormLayout = QHBoxLayout()
        horizontalFormLayout.setContentsMargins(0, 0, 0, 0)
        horizontalTitleLayout = QHBoxLayout()
        horizontalTitleLayout.setContentsMargins(0, 0, 0, 0)


        self.setLayout(outerLayout)
        outerLayout.setContentsMargins(0,0,0,0)
        outerLayout.addWidget(self.tableContent)
        outerLayout.addWidget(self.formContent)
        self.tableContent.setLayout(tableLayout)
        self.formContent.setLayout(formLayout)
        tableLayout.addWidget(self.tableTitleFrame)
        tableLayout.addWidget(self.table)
        self.tableTitleFrame.setLayout(horizontalTitleLayout)
        horizontalTitleLayout.addWidget(self.tableTitle)
        horizontalTitleLayout.addStretch()
        
        formLayout.addWidget(self.inputJudul)
        formLayout.addWidget(self.inputNama)
        formLayout.addWidget(self.inputNim)
        formLayout.addWidget(self.formButtons)
        self.formButtons.setLayout(horizontalFormLayout)
        horizontalFormLayout.addWidget(self.resetButton)
        horizontalFormLayout.addStretch()
        horizontalFormLayout.addWidget(self.button)
        formLayout.addStretch()
        formLayout.addWidget(self.showPatronsButton)
        formLayout.addWidget(self.showCatalogButton)

        self.loadCatalog()


    def loadCatalog(self):

        # change table title
        self.tableTitle.setText('List of Catalog')

        try:
            with open('database.json') as f:
                databaseContent = json.load(f) # ngambil data dari file
                catalog = databaseContent['catalog'] # ngambil key catalog
        except json.decoder.JSONDecodeError:
            return None

        keys = ['Judul', 'Status'] # judul table

        self.table.setRowCount(len(catalog)) # atur jumlah baris
        self.table.setColumnCount(len(keys)) # atur jumlah kolom
        self.table.setHorizontalHeaderLabels(keys) # atur judul table

        # ngeload data yang ada di file json ke table
        for row, patron in enumerate(catalog):
            for column, key in enumerate(keys):
                item = QTableWidgetItem(patron[key])
                self.table.setItem(row, column, item)

        self.tableState = 'catalog'
        self.showCatalogButton.setDisabled(True)
        self.showPatronsButton.setDisabled(False)
        

    def loadPatrons(self):

        # change table title
        self.tableTitle.setText('List of Patrons')

        try:
            with open('database.json') as f:
                databaseContent = json.load(f)
                patrons = databaseContent['patrons']
        except json.decoder.JSONDecodeError:
            return None

        keys = ['Nama', 'NIM', 'Judul', 'Tenggat']

        self.table.setRowCount(len(patrons))
        self.table.setColumnCount(len(keys))
        self.table.setHorizontalHeaderLabels(keys)

        for row, patron in enumerate(patrons):
            for column, key in enumerate(keys):
                item = QTableWidgetItem(patron[key])
                self.table.setItem(row, column, item)

        self.tableState = 'patrons'
        self.showPatronsButton.setDisabled(True)
        self.showCatalogButton.setDisabled(False)
    
    def reset(self):
        self.inputJudul.setText('')
        self.inputNama.setText('')
        self.inputNim.setText('')

    def borrow(self):
        judul = self.inputJudul.text().lower() # ambil text dari input
        nama = self.inputNama.text()
        nim = self.inputNim.text()
        bookFound = False
        nimExist = False

        if judul != '' and nama != '' and nim != '':
            with open('database.json') as f:
                databaseContent = json.load(f)

            # ubah status
            for catalog in databaseContent['catalog']:
                if judul in catalog['Judul'].lower():
                    catalog['Status'] = 'tidak tersedia'
                    bookFound = True
            
            for patrons in databaseContent['patrons']:
                if nim in patrons['NIM']:
                    self.msg.setText("NIM ini telah meminjam buku!")
                    self.msg.exec_()
                    self.reset()
                    return None

            if bookFound:
                # atur tenggat waktu peminjaman jadi 1 minggu
                date = datetime.datetime.now().strftime('%x')
                tenggat = moment.date(date).add(weeks=1).format('DD/MM/YY')

                # atur format untuk diinput ke file database
                newPatron = {
                    "Nama": nama,
                    "NIM": nim,
                    "Judul": judul.capitalize(),
                    "Tenggat": tenggat
                }

                # input data ke file database
                with open('database.json', 'w') as f:
                    databaseContent['patrons'].append(newPatron)
                    json.dump(databaseContent, f, indent=4)

                self.reset()
                
                self.loadCatalog() if self.tableState == 'catalog' else self.loadPatrons()
            else:
                self.msg.setText("Buku tidak ditemukan!")
                self.msg.exec_()
                self.reset()

        else:
            self.msg.setText("Input tidak boleh kosong!")
            self.msg.exec_()

class MessageBox(QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        grid_layout = self.layout()

        qt_msgboxex_icon_label = self.findChild(QLabel, "qt_msgboxex_icon_label")
        qt_msgboxex_icon_label.deleteLater()

        qt_msgbox_label = self.findChild(QLabel, "qt_msgbox_label")
        qt_msgbox_label.setAlignment(Qt.AlignCenter)
        grid_layout.removeWidget(qt_msgbox_label)

        qt_msgbox_buttonbox = self.findChild(QDialogButtonBox, "qt_msgbox_buttonbox")
        grid_layout.removeWidget(qt_msgbox_buttonbox)

        grid_layout.addWidget(qt_msgbox_label, 0, 0)
        grid_layout.addWidget(qt_msgbox_buttonbox, 1, 0)


app = QApplication([])
window = MainWindow()
window.show()
app.exec_()