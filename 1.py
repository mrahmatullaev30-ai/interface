import random 
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

app = QApplication([])

win = QWidget()
win.setWindowTitle("Random Son Generatori")
win.setFixedSize(400, 300)
win.setStyleSheet("background-color: #f0f0f0;") 

label = QLabel("Son kutilmoqda...")
label.setAlignment(Qt.AlignCenter)

label.setStyleSheet("""
    color: #2c3e50; 
    font-size: 35px; 
    font-weight: bold;
""")
button = QPushButton("Random son chiqarish")

button.setStyleSheet("""
    QPushButton {
        background-color: #3498db;
        color: white;
        border-radius: 10px;
        font-size: 18px;
        min-height: 50px;
    }
    QPushButton:hover {
        background-color: #2980b9;
    }
""")

def generate_number():
  
    random_num = random.randint(1, 100)

    label.setText(str(random_num))

    label.setStyleSheet("color: #e74c3c; font-size: 45px; font-weight: bold;")

button.clicked.connect(generate_number)

layout = QVBoxLayout()
layout.addStretch() 
layout.addWidget(label)
layout.addStretch() 
layout.addWidget(button)
layout.addStretch()  

win.setLayout(layout)

win.show()

sys.exit(app.exec_())