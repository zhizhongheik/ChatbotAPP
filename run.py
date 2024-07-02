from PyQt5.QtWidgets import QApplication
from ui import ChatUi


if __name__ == "__main__":
    app = QApplication([])
    screen = ChatUi()
    screen.show()
    app.exec_()