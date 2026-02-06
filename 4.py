import sys
import random 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

app = QApplication([])

win = QWidget()
win.setWindowTitle("Ranglar jilosi")
win.setFixedSize(400, 300)
win.setStyleSheet("background-color: white;")

label = QLabel("Mening rangim o'zgaradi!")
label.setAlignment(Qt.AlignCenter)

label.setStyleSheet("font-size: 25px; font-weight: bold; color: black;")

btn = QPushButton("Rangni o'zgartirish")
btn.setCursor(Qt.PointingHandCursor) 
btn.setStyleSheet("""
    QPushButton {
        background-color: #34495e;
        color: white;
        font-size: 18px;
        border-radius: 12px;
        min-height: 50px;
    }
    QPushButton:hover {
        background-color: #2c3e50;
    }
""")

def change_label_color():

    colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown"]
    
    random_color = random.choice(colors)
    
    label.setStyleSheet(f"font-size: 25px; font-weight: bold; color: {random_color};")

btn.clicked.connect(change_label_color)

layout = QVBoxLayout()
layout.addStretch()
layout.addWidget(label)
layout.addSpacing(20) 
layout.addWidget(btn)
layout.addStretch()

win.setLayout(layout)

win.show()
sys.exit(app.exec_())