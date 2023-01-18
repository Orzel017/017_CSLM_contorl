"""

Made: 01-17-2023

Last modified: 01-18-2023
"""

# page 3 code for mock GUI re-work

from PyQt5.QtWidgets import (QHBoxLayout, QLabel, QCheckBox)

def stack3UI(self):
    layout = QHBoxLayout()
    layout.addWidget(QLabel("subjects"))
    layout.addWidget(QCheckBox("Physics"))
    layout.addWidget(QCheckBox("Maths"))
    self.YZ_image_UI.setLayout(layout)
