from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def add_lable():



def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Easy prog")
    window.setGeometry(300, 250, 350, 200)

    a1 = QtWidgets.QLabel(window)
    a1.setText("Hello")
    a1.move(100, 100)
    a1.adjustSize()
    btn = QtWidgets.QPushButton(window)
    btn.move(10, 20)
    btn.setText("Hello")
    btn.setFixedWidth(200)

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
