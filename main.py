import sys
from PySide6.QtWidgets import QApplication
from gui.ui import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
