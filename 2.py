import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

app = QApplication([])

win = QWidget()
win.setWindowTitle("Ma'lumotlar oynasi")
win.setFixedSize(400, 350)
win.setStyleSheet("background-color: #ecf0f1;") 

label = QLabel("Tugmalardan birini bosing")
label.setAlignment(Qt.AlignCenter)
label.setStyleSheet("font-size: 22px; color: #2c3e50; font-weight: bold; margin-bottom: 20px;")

btn_ism = QPushButton("Ismni ko'rsatish")
btn_fam = QPushButton("Familiyani ko'rsatish")
btn_sana = QPushButton("Tug'ilgan sanani ko'rsatish")

button_style = """
    QPushButton {
        background-color: #34495e;
        color: white;
        border-radius: 8px;
        font-size: 16px;
        min-height: 45px;
    }
    QPushButton:hover {
        background-color: #1abc9c;
    }
"""
btn_ism.setStyleSheet(button_style)
btn_fam.setStyleSheet(button_style)
btn_sana.setStyleSheet(button_style)

def show_name():
    label.setText("Ismingiz: Aziz")
    label.setStyleSheet("font-size: 22px; color: #2980b9; font-weight: bold;")

def show_surname():
    label.setText("Familiyangiz: Karimov")
    label.setStyleSheet("font-size: 22px; color: #8e44ad; font-weight: bold;")

def show_birthdate():
    label.setText("Sana: 01.01.2000")
    label.setStyleSheet("font-size: 22px; color: #27ae60; font-weight: bold;")

btn_ism.clicked.connect(show_name)
btn_fam.clicked.connect(show_surname)
btn_sana.clicked.connect(show_birthdate)

layout = QVBoxLayout()
layout.addStretch()
layout.addWidget(label)
layout.addWidget(btn_ism)
layout.addWidget(btn_fam)
layout.addWidget(btn_sana)
layout.addStretch()

win.setLayout(layout)

win.show()
sys.exit(app.exec_())