"""
Made: 01-14-2023

Last modifed: 01-17-2023

(Test) page 2
"""

from PyQt5.QtWidgets import (QHBoxLayout, QRadioButton, QLabel, QFormLayout, QLineEdit)

# Create the second page

# class page_2(QWidget):

#     def __init__(self, parent = None):

#         super(page_2, self).__init__(parent)

#         self.page2 = QWidget()
#         self.page2Layout = QFormLayout()
#         self.page2Layout.addRow("Job:", QLineEdit())
#         self.page2Layout.addRow("Department:", QLineEdit())
#         self.page2.setLayout(self.page2Layout)

def stack2UI(self):
    layout = QFormLayout()
    sex = QHBoxLayout()
    sex.addWidget(QRadioButton("Male"))
    sex.addWidget(QRadioButton("Female"))
    layout.addRow(QLabel("Sex"),sex)
    layout.addRow("Date of Birth",QLineEdit()) 
    self.stack2.setLayout(layout)