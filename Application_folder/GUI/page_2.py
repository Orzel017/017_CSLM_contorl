"""
Made: 01-14-2023

Last modifed: 01-17-2023

(Test) page 2
"""

from PyQt5.QtWidgets import (QHBoxLayout, QRadioButton, QLabel, QFormLayout, QLineEdit)

def stack2UI(self):
    layout = QFormLayout()
    sex = QHBoxLayout()
    sex.addWidget(QRadioButton("Male"))
    sex.addWidget(QRadioButton("Female"))
    layout.addRow(QLabel("Sex"),sex)
    layout.addRow("Date of Birth",QLineEdit()) 
    self.stack2.setLayout(layout)