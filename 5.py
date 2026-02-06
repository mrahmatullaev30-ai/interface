import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
from PyQt5.QtCore import Qt

app = QApplication([])

win = QWidget()
win.setWindowTitle("Parol Tekshiruvchi")
win.setFixedSize(350, 250)

label = QLabel("Parolni kiriting:")
label.setAlignment(Qt.AlignCenter)
label.setStyleSheet("font-size: 18px; font-weight: bold;")

password_input = QLineEdit()
password_input.setPlaceholderText("Parol...")
password_input.setEchoMode(QLineEdit.Password) 
password_input.setStyleSheet("font-size: 16px; padding: 5px; border: 1px solid gray;")

btn = QPushButton("Tekshirish")
btn.setStyleSheet("background-color: #2ecc71; color: white; font-size: 16px; min-height: 40px;")

def check_password():

    user_input = password_input.text()
    
    if user_input == "12345":
        label.setText("Parol togri")
        label.setStyleSheet("font-size: 18px; font-weight: bold; color: green;")
    else:
        label.setText("Notogri parol")
        label.setStyleSheet("font-size: 18px; font-weight: bold; color: red;")

btn.clicked.connect(check_password)

layout = QVBoxLayout()
layout.addStretch()
layout.addWidget(label)
layout.addWidget(password_input)
layout.addWidget(btn)
layout.addStretch()

win.setLayout(layout)

win.show()
sys.exit(app.exec_())