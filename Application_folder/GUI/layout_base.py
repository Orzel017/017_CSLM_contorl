"""
Made: 01-14-2023
"""

import sys

from PyQt5.QtWidgets import (QApplication, QComboBox, QFormLayout, QLineEdit, QStackedLayout, QVBoxLayout, QWidget, )

class Window(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Example")

        # Create a top-level layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create and connect the combo box to switch between pages
        self.pageCombo = QComboBox()
        self.pageCombo.addItems(["Page 1", "Page 2"])
        self.pageCombo.activated.connect(self.switchPage)
        
        # Create the stacked layout
        self.stackedLayout = QStackedLayout()

        # add pages to the stacked layout
        self.stackedLayout.addWidget(self.page1)
        self.stackedLayout.addWidget(self.page2)

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
