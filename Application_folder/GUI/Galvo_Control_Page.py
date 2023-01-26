"""
File name: "Galvo_Control_Page.py"

Contents: UI elements for XY sanning

Dates:
Originally created: 01-14-2023
Last modifed: 01-26-2023
Original author: MDA
Last modified by: MDA

Notes:

TODO:

"""

######################################################################################## start package imports ########################################################################################

from PyQt5.QtWidgets import (QHBoxLayout, QFrame, QSplitter, QLabel) # import submodules from PyQt5.QtWidgets

from PyQt5.QtCore import Qt # Qt module from QtCore

########################################################################################## end package imports ########################################################################################

def build_galvo_control_page(self):

    self.background_layout = QHBoxLayout() # create highest-level background layout as QHBoxLayout

    self.background_layout.setSpacing(1) # control space between widgets

    self.background_layout.setContentsMargins(0, 0, 0, 0) # control margin between widgets(for on background widget spacing)

    # left window
    self.left_window = QFrame()
    self.left_window.setFrameShape(QFrame.StyledPanel)
    # self.left_window.setFixedSize(400, 400)

    # right window
    self.right_window = QFrame()
    self.right_window.setFrameShape(QFrame.StyledPanel)
    # self.right_window.setFixedSize(300, 500)

    self.splitter1 = QSplitter(Qt.Horizontal)
    self.splitter1.addWidget(self.left_window)
    self.splitter1.addWidget(self.right_window)
    self.background_layout.addWidget(self.splitter1) # set layout and show window
    self.splitter1.setHandleWidth(1)

    self.galvo_control_widget = QLabel("Galvo Control Page") # create label widget

    self.galvo_control_widget.setParent(self.left_window) # designate parent of label widget

    self.galvo_control_widget.move(300, 150) # position the label

    self.Galvo_control_page.setLayout(self.background_layout)