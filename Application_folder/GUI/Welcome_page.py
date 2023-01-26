"""
File name: "Welcome_page.py"

Made: 01-14-2023

Last modifed: 01-26-2023

"""

from PyQt5.QtWidgets import (QFrame, QVBoxLayout) # submodules from PyQt5.QtWidgets

from PyQt5.QtCore import Qt # Qt module from QtCore

# Create the first page

def build_welcome_page(self):

    ### create layout ###

    self.layout = QVBoxLayout()

    self.layout.setSpacing(0)

    self.layout.setContentsMargins(0, 0, 0, 0)

    ### end layout ###

    self.welcome_background_frame = QFrame()

    self.layout.addWidget(self.welcome_background_frame)

    self.welcome_background_frame.setStyleSheet("background-color: black") # temp set background color

    # self.welcome_background_frame.setParent(self) # designate the parent to higher level background widget

    self.Welcome_page.setLayout(self.layout)
