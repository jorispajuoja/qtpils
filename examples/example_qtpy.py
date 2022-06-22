import sys

from qtpy import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QtWidgets.QWidget()
        self.central_widget.setObjectName("CentralWidget")
        self.setCentralWidget(self.central_widget)

        self.central_layout = QtWidgets.QGridLayout()
        self.central_layout.setObjectName("CentralLayout")
        self.central_widget.setLayout(self.central_layout)

        self.button1 = QtWidgets.QPushButton()
        self.button1.setObjectName("Button 1")
        self.button1.setText("Button 1")
        self.central_layout.addWidget(self.button1, 0, 0)

        self.button2 = QtWidgets.QPushButton()
        self.button2.setObjectName("Button 2")
        self.button2.setText("Button 2")
        self.central_layout.addWidget(self.button2, 0, 1)

        self.button3 = QtWidgets.QPushButton()
        self.button3.setObjectName("Button 3")
        self.button3.setText("Button 3")
        self.central_layout.addWidget(self.button3, 0, 2)

        self.show()


def main():
    """run the app"""
    app = QtWidgets.QApplication(sys.argv)
    gui = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
