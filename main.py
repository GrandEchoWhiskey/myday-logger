from PyQt5.QtWidgets import QApplication
import sys

from ui_main import Ui_MainWindow

app = QApplication(sys.argv)

window = Ui_MainWindow()
window.show()

app.exec()