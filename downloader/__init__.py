import sys
import signal
from PyQt5 import QtCore, QtWidgets

from .common import Common
from .main_window import MainWindow


def main():
    # Allow Ctrl-C to smoothly quit the program instead of throwing an exception
    # https://stackoverflow.com/questions/42814093/how-to-handle-ctrlc-in-python-app-with-pyqt
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    # Start the Qt app
    app = QtWidgets.QApplication(sys.argv)

    common = Common()
    window = MainWindow(common)

    # Execute
    sys.exit(app.exec_())
