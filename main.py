from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
                             QLineEdit, QComboBox, QVBoxLayout,QLabel)

app = QApplication([])
window = QWidget()
txt1 = QLabel('Сума:')
txt2 = QLabel('У Валюту:')
txt3 = QLabel('Резултат:')
txt4 = QLabel(' ')
line = QLineEdit()
b1 = QPushButton('конвертувати')

combo = QComboBox()
list1 = ['eur', 'usd', 'gbp']
combo.addItems(list1)




v1 = QVBoxLayout()
v1.addWidget(txt1)
v1.addWidget(line)
v1.addWidget(txt2)
v1.addWidget(combo)
v1.addWidget(txt3)
v1.addWidget(txt4)
v1.addWidget(b1)

def add_task():
    t = line.text()
    c = combo.currentText()
    if c == 'eur':
        result = int(t) * 40
        txt4.setText(str(result))
    elif c == 'usd':
        result = int(t) * 37
        txt4.setText(str(result))
    elif c == 'gbp':
        result = int(t) * 48
        txt4.setText(str(result))

b1.clicked.connect(add_task)
window.setLayout(v1)
window.show()
app.exec()
