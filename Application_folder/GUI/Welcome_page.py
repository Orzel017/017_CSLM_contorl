"""
File name: "Welcome_page.py"

Contents: welcome page UI elements

Dates:
Originally created: 01-14-202
Last modifed: 01-26-2023
Original author: MDA
Last modified by: MDA

Notes:

TODO:

"""

######################################################################################## start package imports ########################################################################################

from PyQt5.QtWidgets import (QVBoxLayout, QFrame, QLabel) # submodules from PyQt5.QtWidgets

from PyQt5.QtCore import Qt # Qt module from QtCore

########################################################################################## end package imports ########################################################################################

def build_welcome_page(self): # define build_welcome_page to setup the welcome UI elements

    ##################################################################################### start create layout #########################################################################################

    self.behind_layout = QVBoxLayout() # create a VBoxLayout

    self.behind_layout.setSpacing(1) # control space between widgets

    self.behind_layout.setContentsMargins(0, 0, 0, 0) # control margin between widgets(for on background widget spacing)

    ##################################################################################### end create layout ###########################################################################################

    # creating two QFrames
    self.welcome_background_frame_top = QFrame() # create top
    self.welcome_background_frame_bottom = QFrame() # create bottom

    self.welcome_background_frame_top.setFixedHeight(500) # adjust height of top frame

    # adding widgets to background QFrames
    self.behind_layout.addWidget(self.welcome_background_frame_top) # top
    self.behind_layout.addWidget(self.welcome_background_frame_bottom) # bottom

    # frame edge styling
    self.welcome_background_frame_top.setFrameShape(QFrame.StyledPanel) # top
    self.welcome_background_frame_bottom.setFrameShape(QFrame.StyledPanel) # bottom

    self.welcome_title_widget = QLabel("Welcome Page") # create title widget

    self.welcome_title_widget.setParent(self.welcome_background_frame_top) # designate parent of title widget

    self.welcome_title_widget.move(200, 100) # position the title

    # self.welcome_background_frame_top.setStyleSheet("background-color: black") # temp set background color
    # self.welcome_background_frame_bottom.setStyleSheet("background-color: red") # temp set background color

    self.Welcome_page.setLayout(self.behind_layout) # display welcome page UI elements
