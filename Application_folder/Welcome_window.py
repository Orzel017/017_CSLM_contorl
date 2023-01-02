"""
File name: "Welcome_window.py"

Contents: wlecome window content (and brief tutorial messages?)

Dates:
Originally created: 12-30-2022
Last modifed: 01-02-2023
Original author: MDA
Last modified by: MDA

Notes:

TODO:
*move main application window dimensions (width and height) to external accessible variable(?) file for access in multiple files
"""

############################################################################################## start imports ##########################################################################################

from PyQt5 import QtWidgets # QtWidgets module

from PyQt5.QtWidgets import QFrame, QLabel, QPushButton # submodules from QtWidgets

from PyQt5.QtGui import QFont # submodule from QtWidgets

import Helper_Functions # import 'Helper_Functions.py" file

############################################################################################# end imports #############################################################################################

class Setup_Welcome_Window(QtWidgets.QMainWindow):#, **kwargs): # kwargs needed?

    # setup welcome window object
    def __init__(self, parent = None):#, **kwargs): # kwargs needed?

        super().__init__(parent) # inheritance?

    ################################################################################## start welcome window functions #################################################################################

        def display_window_contents_function(): # define a small function to display the main window contents on the Main_window

            # remove welcome window widgets to clear main window area for main window contents (their likely is a better alternative to doing this -perhaps a `layout`?)
            self.welcome_frame.hide() # remove the welcome_frame

            self.welcome_title.hide() # remove the welcome_title

            self.transition_button.hide() # remove the transition_button

            self.image_area_locator_label.hide() # remove the image area locator label

            self.imaging_settings_locator_label.hide() # remove the imaging settings locator label

            self.imaging_mode_locator_label.hide() # remove the imaging mode locator label

            Helper_Functions.display_window_contents(self) # display the main window contents

    #################################################################################### end welcome window functions #################################################################################

    ################################################################################## start welcome window main code #################################################################################
        
        ##### setup window frame #####
        self.welcome_frame = QFrame(self)

        self.welcome_frame.setFrameShape(QFrame.StyledPanel)

        # welcome window frame dimensions        
        welcome_window_frame_width = 400 # define width
        welcome_window_frame_height = 300 # define height

        self.welcome_frame.setFixedSize(welcome_window_frame_width, welcome_window_frame_height) # set the dimensions of the frame

        self.welcome_frame.move(int(1000 / 2) - int(welcome_window_frame_width / 2), int(500 / 2) - int(welcome_window_frame_height / 2)) # set frame location on main window background

        self.welcome_frame.setStyleSheet("background-color: rgb(0, 0, 0)") # set background color

        ##### welcome window title label #####
        self.welcome_title = QLabel("Welcome to MDA_gui", self) # display title to the application

        self.welcome_title.setParent(self.welcome_frame) # designate parent widget

        self.welcome_title.move(int(welcome_window_frame_width / 2) - 160, 20) # position the title

        self.welcome_title.setStyleSheet("color : rgb(255, 255, 255)") # set text color

        self.welcome_title.setFont(QFont("Times", 25)) # designate font and text size

        ##### change window button (to main window contents) #####
        self.transition_button = QPushButton("Ready to image?", self) # setup transition button

        self.transition_button.setParent(self.welcome_frame) # designate parent widget

        # transition button dimensions
        transition_button_width = 100 # define width
        transition_button_height = 50 # define height

        self.transition_button.setFixedSize(transition_button_width, transition_button_height) # set the dimensions of the button

        # set button location
        self.transition_button.move(int(welcome_window_frame_width / 2) - int(transition_button_width / 2), int(welcome_window_frame_height / 2) - int(transition_button_height / 2))

        self.transition_button.setStyleSheet("background-color: rgb(255, 255, 255)") # set background color

        self.transition_button.clicked.connect(display_window_contents_function) # function call for transition to main window contents

        ##### image area locator #####

        self.image_area_locator_label = QLabel("Image area ->", self) # set label for image area

        self.image_area_locator_label.setParent(self) # designate parent widget (note this is outside of the welcome frame and thus has a different parent widget)

        self.image_area_locator_label.move(800, 200) # position the image area locator

        ##### imaging settings area locator #####

        self.imaging_settings_locator_label = QLabel("Set imaging\nsettings ->", self) # set label for imaging settings locator area

        self.imaging_settings_locator_label.setParent(self) # designate parent widget (note this is outside of the welcome frame and thus has a different parent widget)

        self.imaging_settings_locator_label.move(180, 200) # position the image area locator

        ##### imaging mode area locator #####

        self.imaging_mode_locator_label = QLabel("Designate imaging\nmode ->", self) # set label for imaging mode locator area

        self.imaging_mode_locator_label.setParent(self) # designate parent widget (note this is outside of the welcome frame and thus has a different parent widget)

        self.imaging_mode_locator_label.move(10, 200) # position the image area locator

    ################################################################################## end welcome window main code ###################################################################################
