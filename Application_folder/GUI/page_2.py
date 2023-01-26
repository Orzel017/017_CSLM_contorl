"""
Made: 01-14-2023

Last modifed: 01-26-2023

(Test) page 2
"""

from PyQt5.QtWidgets import (QHBoxLayout, QFrame, QSplitter, QLabel, QFormLayout)

from PyQt5.QtCore import Qt # Qt module from QtCore

def stack2UI(self):

    # layout = QFormLayout()
    self.layout = QHBoxLayout()
    # layout.addRow("Name",QLineEdit())
    # layout.addRow("Address",QLineEdit())

    self.left_window = QFrame(self)
    self.left_window.setFrameShape(QFrame.StyledPanel)
    self.left_window.setFixedSize(400, 400)

    self.right_window = QFrame(self)
    self.right_window.setFrameShape(QFrame.StyledPanel)
    self.right_window.setFixedSize(300, 500)

    self.splitter1 = QSplitter(Qt.Horizontal)
    self.splitter1.addWidget(self.left_window)
    self.splitter1.addWidget(self.right_window)
    self.layout.addWidget(self.splitter1) # set layout and show window

    self.XY_image_UI.setLayout(self.layout)