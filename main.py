from PyQt5.QtWidgets import QApplication
from util import open_qt_resource
from app import MainWindow
from res import *
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(open_qt_resource(":style/style.qss"))
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
