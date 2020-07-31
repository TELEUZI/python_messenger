# This Python file uses the following encoding: utf-8
import sys
from PySide2 import QtCore
from model import Model
from view import LoginForm, MainWindow
from PySide2.QtWidgets import QApplication


class Ctrl:
    def __init__(self):
        self.view = LoginForm(self)
        self.model = Model(self)
        self.view.show()
        self.view.ui.buttonBox.accepted.connect(self.model.show_main_window)
        self.view.ui.buttonBox.rejected.connect(self.model.exit)

    def show_main(self):
        self.view = MainWindow(self)
        self.view.show()
        self.model.receiver()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.model.launch_receiving_thread)
        self.timer.start(5000)
        self.view.ui.push_button.clicked.connect(self.model.launch_sending_thread)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = Ctrl()

    sys.exit(app.exec_())
