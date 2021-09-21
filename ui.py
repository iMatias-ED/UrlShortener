from PySide2.QtWidgets import *
from PySide2.QtCore import *

import pyshorteners

class Ui_MainWindow(QMainWindow):
    short = pyshorteners.Shortener()

    def setupUi(self):
        self.setFixedSize(500, 500)
        self.setStyleSheet('''
            QFrame{
                background: #2ECC71;
                border-radius: 10px;
            }
            QMainWindow{
                background: #242526;
            }
        ''')

        self.title_frame = QFrame(self)
        self.title_frame.setGeometry(10, 10, 480, 180)
        self.title_frame.setStyleSheet('''

        ''')

        self.input_frame = QFrame(self)
        self.input_frame.setGeometry(10, 200, 480, 290)

        self.title = QLabel(self.title_frame)
        self.title.setText("Url Shortener")
        self.title.setGeometry(0, 20, 480, 50)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet('''
            font-size: 40px;
            color: #212121;
            font-family: Comic Sans;
            font-weight: bold;
        ''')

        self.input = QLineEdit(self.input_frame)
        self.input.setGeometry(10, 20, 460, 40)
        self.input.setStyleSheet('''
            background: white;
            font-size: 14px;
            padding-left: 10px;
            padding-right: 10px;
            border-radius: 5px
        ''') 

        self.button = QPushButton(self.input_frame)
        self.button.setText('Convertir Url')
        self.button.setGeometry(190, 230, 100, 35)
        self.button.setStyleSheet('''
            QPushButton{
                border: 2px solid #212121;
                font-size: 12px;
                padding: 2px;
                font-family: Comic Sans;
                background: #58D68D;
                border-radius: 5px;
            }
            QPushButton:hover{
                background:#82E0AA;
                color: #212121;
                border: 2px solid white;
            }
        ''')
        self.button.clicked.connect(self.printShortedUrl)

    def printShortedUrl(self):
        url = self.input.text()

        shortedUrl = self.short.tinyurl.short(url)
        print(shortedUrl)

## Ejecutar la aplicacion
import sys

app = QApplication(sys.argv)

window = Ui_MainWindow()
window.setupUi()
window.show()

sys.exit(app.exec_())