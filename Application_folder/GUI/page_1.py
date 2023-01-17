"""
Made: 01-14-2023

Last modifed: 01-17-2023

(Test) page_1
"""

from PyQt5.QtWidgets import (QWidget, QFormLayout, QLineEdit)

# Create the first page

def stack1UI(self):

    layout = QFormLayout()
    layout.addRow("Name",QLineEdit())
    layout.addRow("Address",QLineEdit())
    self.stack1.setLayout(layout)