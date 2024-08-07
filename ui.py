# -*- coding: utf-8 -*-
"""UI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wWeES3YmaySvvCnpLzuJ9Qkee5nbQY7p
"""

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QTextEdit
from PyQt5.QtCore import QThread, pyqtSignal
from chatbot_main import get_response, words, classes, data
from train import pred_class

class Worker(QThread):
    finished = pyqtSignal(str)

    def __init__(self, text, words, classes, data):
        super(Worker, self).__init__()
        self.text = text
        self.words = words
        self.classes = classes
        self.data = data

    def run(self):
        try:
            intents = pred_class(self.text, self.words, self.classes)
            result = get_response(intents, self.data)
            self.finished.emit(result)
        except Exception as e:
            print(f"Error in Worker thread: {e}")


class ChatUi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat Bot")

        # Set window size
        self.setFixedSize(800, 600)

        # Add an informative label
        self.app_description = QLabel()  
        self.app_description.setGeometry(10, 10, 300, 100)
        self.app_description.setText("You can enter information in the dialog box and then receive a reply below the dialog box.")
        self.app_description.setWordWrap(True)

        self.layout = QVBoxLayout()

        self.text = QTextEdit()
        self.button = QPushButton("Submit")
        self.quitButton = QPushButton("Quit")
        self.resultLabel = QLabel()
        self.resultLabel.setGeometry(10, 400, 780, 150) 

        self.layout.addWidget(self.app_description)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.quitButton)
        self.layout.addWidget(self.resultLabel)

        self.setLayout(self.layout)

        self.thread = None  # Initialize thread as None

        self.button.clicked.connect(self.start_worker)
        self.quitButton.clicked.connect(self.close)

    def start_worker(self):
        if self.thread is not None and self.thread.isRunning():
            return
        self.thread = Worker(self.text.toPlainText(), words, classes, data)
        self.thread.finished.connect(lambda result: [self.text.clear(), self.resultLabel.setText(result)])
        self.thread.start()