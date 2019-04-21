from PyQt5 import QtCore, QtWidgets, QtGui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, common):
        super(MainWindow, self).__init__()
        self.common = common

        self.setWindowTitle('Downloader')
        self.setWindowIcon(QtGui.QIcon(self.common.get_resource_path('logo.png')))

        self.show()
