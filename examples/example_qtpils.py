import sys

from qtpy import QtWidgets

import qtpils as qtpils


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = qtpils.CentralWidget(self)
        self.central_layout = qtpils.GridLayout("central", self.central_widget)

        self.button1 = qtpils.Button("Button 1", self.central_layout, [0, 0])
        self.button2 = qtpils.Button("Button 2", self.central_layout, [0, 1])
        self.button3 = qtpils.Button("Button 3", self.central_layout, [0, 3])

        self.show()


def main():
    """run the app"""
    app = QtWidgets.QApplication(sys.argv)
    gui = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
