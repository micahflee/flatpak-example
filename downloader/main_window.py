from PyQt5 import QtCore, QtWidgets, QtGui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, common):
        super(MainWindow, self).__init__()
        self.common = common

        self.setWindowTitle('Downloader')
        self.setWindowIcon(QtGui.QIcon(self.common.get_resource_path('logo.png')))

        label = QtWidgets.QLabel("Type a URL to download:")
        self.lineedit = QtWidgets.QLineEdit()
        button = QtWidgets.QPushButton("Download")
        button.clicked.connect(self.download_clicked)

        self.status_bar = QtWidgets.QStatusBar()
        self.setStatusBar(self.status_bar)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.lineedit)
        layout.addWidget(button)
        layout.addStretch()

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.show()

    def download_clicked(self):
        self.status_bar.showMessage("Download button clicked")
