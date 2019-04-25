import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QSlider, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QMainWindow, QAction, qApp
from PyQt5.QtCore import Qt


class Window(QtWidgets.QWidget):
    count = 0
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.le = QtWidgets.QLineEdit()
        self.b = QtWidgets.QPushButton("Push me")
        self.l = QtWidgets.QLabel("Never click here")
        self.bReset = QtWidgets.QPushButton("Reset")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(1)
        self.slider.setMaximum(100)
        self.slider.setValue(50)
        self.slider.setTickInterval(2)
        self.slider.setTickPosition(QSlider.TicksBelow)
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.b)
        h_box.addStretch()
        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addStretch()
        h_box2.addWidget(self.l)
        h_box2.addStretch()
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.bReset)
        v_box.addLayout(h_box)
        v_box.addLayout(h_box2)
        v_box.addWidget(self.slider)

        self.setLayout(v_box)
        self.setWindowTitle("pyQt5")
        self.b.clicked.connect(self.btn_click)
        self.bReset.clicked.connect(self.btn_reset)
        self.slider.valueChanged.connect(self.v_change)
        self.show()

    def btn_click(self):
        self.count+= 1
        self.l.setText(str(self.count))
    def btn_reset(self):
        self.count = 0
        self.l.setText(str(self.count))
    def v_change(self):
        self.b.setText(str(self.slider.value()))


class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.text = QTextEdit(self)
        self.save_btn = QPushButton('Save')
        self.open_btn = QPushButton('Open')
        self.clear_btn = QPushButton('Clear')
        self.init_ui()



    def init_ui(self):
        layout = QVBoxLayout()
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.clear_btn)
        h_layout.addWidget(self.save_btn)
        h_layout.addWidget(self.open_btn)
        layout.addLayout(h_layout)
        layout.addWidget(self.text)
        self.save_btn.clicked.connect(self.save_text)
        self.open_btn.clicked.connect(self.open_text)
        self.clear_btn.clicked.connect(self.clear_text)
        self.setLayout(layout)
        self.setWindowTitle("PyQt Notepad")

        self.show()

    def save_text(self):
        filename = QFileDialog.getSaveFileName(self, "Save File", os.getenv("HOME"))
        with open(filename[0], 'w') as f:
            my_text = self.text.toPlainText()
            f.write(my_text)

    def clear_text(self):
        self.text.clear()

    def open_text(self):
        filename = QFileDialog.getOpenFileName(self, "Open File", os.getenv("HOME"))
        with open(filename[0], 'r') as f:
            file_text = f.read()
            self.text.setText(file_text)

class Writer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.form_widget = Notepad()
        self.setCentralWidget(self.form_widget)
        self.init_ui()
        self.show()
    def init_ui(self):
        bar = self.menuBar()
        file = bar.addMenu('File')

        new_action = QAction('New', self)
        new_action.setShortcut('Ctrl+N')
        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        open_action = QAction('Open', self)
        open_action.setShortcut('Ctrl+O')

        quit_action = QAction('Quit', self)
        quit_action.setShortcut('Ctrl+Q')
        file.addAction(new_action)
        file.addAction(save_action)
        file.addAction(open_action)
        file.addAction(quit_action)

        quit_action.triggered.connect(self.quit_trigger)
        file.triggered.connect(self.respond)
    def quit_trigger(self):
        qApp.quit
    def respond(self,q):
        signal = q.text()
        if signal == "New":
            self.form_widget.clear_text()
        if signal == "Save":
            self.form_widget.save_text()
        if signal == "Open":
            self.form_widget.open_text()

app = QtWidgets.QApplication(sys.argv)

b_window = Writer()
sys.exit(app.exec_())
