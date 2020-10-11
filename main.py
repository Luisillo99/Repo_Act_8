from PySide2.QtWidgets import QApplication
from mainwindow import MainWindow
import sys

# Aplicación de Qt
app = QApplication()

window = MainWindow()

window.show()

sys.exit(app.exec_())