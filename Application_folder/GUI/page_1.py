"""
Made: 01-14-2023

Last modifed: 01-17-2023

(Test) page_1
"""

from PyQt5.QtWidgets import (QWidget, QFormLayout, QLineEdit)

# Create the first page

# class page_1(QWidget):

#     def __init__(self, parent = None):

#         super(page_1, self).__init__(parent)

#         self.page1 = QWidget()
#         self.page1Layout = QFormLayout()
#         self.page1Layout.addRow("Name:", QLineEdit())
#         self.page1Layout.addRow("Address:", QLineEdit())
#         self.page1.setLayout(self.page1Layout)
#         # self.page1.show()

def stack1UI(self):
    
    layout = QFormLayout()
    layout.addRow("Name",QLineEdit())
    layout.addRow("Address",QLineEdit())
    self.stack1.setLayout(layout)