import sys
from PySide6.QtWidgets import QApplication
from gui.ui import MainWindow

from PySide6 import QtGui

app = QApplication(sys.argv)
window = MainWindow()
app.setWindowIcon(QtGui.QIcon('gui/icons/24x24/cil-speech.png'))
window.show()
sys.exit(app.exec_())
