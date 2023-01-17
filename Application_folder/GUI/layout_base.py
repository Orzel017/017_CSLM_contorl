"""
Made: 01-16-2023
"""

import sys

from PyQt5.QtWidgets import (QApplication, QComboBox, QStackedLayout, QVBoxLayout, QWidget)

import page_1, page_2
from page_1 import page_1
from page_2 import page_2

class Window(QWidget):

    def __init__(self, parent = None):

        super(Window, self).__init__(parent)

        self.setWindowTitle("Example")

        # Create a top-level layout
        layout = QVBoxLayout(self)
        self.setLayout(layout)

        # Create and connect the combo box to switch between pages
        self.pageCombo = QComboBox()
        self.pageCombo.addItems(["Page 1", "Page 2"])
        self.pageCombo.activated.connect(self.switchPage)
        
        # Create the stacked layout
        self.stackedLayout = QStackedLayout()

        page_1_widget = page_1(self)
        page_2_widget = page_2(self)

        # add pages to the stacked layout
        self.stackedLayout.addWidget(page_1_widget)
        self.stackedLayout.addWidget(page_2_widget)

        # Add the combo box and the stacked layout to the top-level layout
        layout.addWidget(self.pageCombo)
        layout.addLayout(self.stackedLayout)

    def switchPage(self):

        self.stackedLayout.setCurrentIndex(self.pageCombo.currentIndex())

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
