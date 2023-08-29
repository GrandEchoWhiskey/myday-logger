from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QWidget, QPushButton, QLabel, QStatusBar, QVBoxLayout, QGridLayout, QHBoxLayout, QScrollArea, QListWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QRect, pyqtSignal, QObject
from datetime import datetime

class ActionItem(QPushButton):

    logged = pyqtSignal(str, name="logged")

    def __init__(self, logMsg: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = args[0]
        self.logMsg = logMsg
        self.clicked.connect(lambda: self.log())

    def log(self, time: datetime = datetime.now()):
        d = time.strftime("%Y-%m-%d")
        t = time.strftime("%Y-%m-%d %H:%M")
        with open(f"log/{d}.log", "a") as f:
            f.write(f"[{t}] {self.logMsg}\n")
        self.logged.emit(f"[{t}] {self.logMsg}")

actionItems = []

class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.layout = QHBoxLayout()
        
        left = QListWidget()
        right = QScrollArea()

        rightGrid = QGridLayout()
        
        actionItems.extend([
            ActionItem("Was out for running.", "Running"),
            ActionItem("Was out for cycling.", "Cycling"),
            ActionItem("Was out for swimming.", "Swimming"),
            ActionItem("Was out for walking.", "Walking"),
            ActionItem("Was out for hiking.", "Hiking"),
            ActionItem("Was out for shopping.", "Shopping"),
            ActionItem("Was out for eating.", "Eating"),
            ActionItem("Was out for drinking.", "Drinking"),
            ActionItem("Was out for partying.", "Partying"),
            ActionItem("Was out for working.", "Working"),
        ])

        for i, item in enumerate(actionItems):
            item.logged.connect(lambda msg: left.addItem(msg))
            x = i // 3
            y = i % 3
            rightGrid.addWidget(item, x, y)

        right.setLayout(rightGrid)

        d = datetime.now().strftime("%Y-%m-%d")
        try:
            with open(f"log/{d}.log", "r") as f:
                for line in f.readlines():
                    left.addItem(line.strip())
        except FileNotFoundError:
            print("No log file found.")

        left.scrollToBottom()
        self.layout.addWidget(left)
        self.layout.addWidget(right)

        centalWidget = QWidget()
        centalWidget.setLayout(self.layout)
        self.setCentralWidget(centalWidget)