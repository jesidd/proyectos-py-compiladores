from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from pygame import mixer


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,600,300)
    win.setWindowTitle("Music Player")

    win.show()
    sys.exit(app.exec_())


#Ventana principal

window()
