import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

win = QWidget()
win.setWindowTitle("Hisoblagich (Counter)")
win.setFixedSize(300, 250)
win.setStyleSheet("background-color: #f4f4f9;")

counter = 0

label_num = QLabel("0")
label_num.setAlignment(Qt.AlignCenter)
label_num.setStyleSheet("font-size: 60px; font-weight: bold; color: #2c3e50;")

btn_plus = QPushButton("+1")
btn_minus = QPushButton("-1")

btn_style = """
    QPushButton {
        font-size: 20px; 
        font-weight: bold; 
        min-height: 50px; 
        min-width: 80px; 
        border-radius: 10px; 
        color: white;
    }
"""
btn_plus.setStyleSheet(btn_style + "background-color: #27ae60;") 
btn_minus.setStyleSheet(btn_style + "background-color: #e74c3c;") 

def increase():
    global counter
    counter += 1
    label_num.setText(str(counter))

def decrease():
    global counter
    counter -= 1
    label_num.setText(str(counter))

btn_plus.clicked.connect(increase)
btn_minus.clicked.connect(decrease)

main_layout = QVBoxLayout() 
main_layout.addStretch()
main_layout.addWidget(label_num)
main_layout.addSpacing(20)

buttons_row = QHBoxLayout()
buttons_row.addWidget(btn_minus) 
buttons_row.addWidget(btn_plus)  

main_layout.addLayout(buttons_row) 
main_layout.addStretch()

win.setLayout(main_layout)

win.show()
sys.exit(app.exec_())