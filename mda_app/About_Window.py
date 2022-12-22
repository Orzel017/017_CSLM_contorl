"""
File name: "About_Window.py"
Date Created: 12-21-2022

Contents: class 'Make_About_Window' to display "About" window accessed from "Help" menu
"""

########################################################################################## start imports ##############################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel
from datetime import date

############################################################################################ end imports ##############################################################################################

get_todays_date = date.today()
date = get_todays_date.strftime("%m%d%Y")

################################################################################## start "Make_About_Window" Class ####################################################################################

class Make_About_Window(QtWidgets.QMainWindow): # create the class "Make_About_Window" for displaying a new window with about content accessed from "Help" menu

    # ?
    def __init__(self, parent=None):
        super().__init__(parent)

        self.title = "About" # define the title of the about window

        self.top    = 350 # set the display location of the about window
        self.left   = 675 # can this be set to the center of the screen regardles of the position of the main window?

        self.about_window_width  = 205 # define the width of the about window
        self.about_window_height = 70 # define the height of the about window

        self.setMaximumSize(self.about_window_width, self.about_window_height) # set the maximum size of the about window
        self.setMinimumSize(self.about_window_width, self.about_window_height) # set the minimum size of the about window

        # begin content of the aobut window
        about_window_left_justify_adjust = 5 # optional adjustment parameter for the content of the about window (left justify)

        about_window_top_justify_adjust = 5 # optional adjustment parameter for the content of the about window (top justify)

        about_window_content_line_1 = QLabel("Application name: mda_017_gui", self)
        about_window_content_line_1.move(0 + about_window_left_justify_adjust, 0 + about_window_top_justify_adjust)
        about_window_content_line_1.resize(300, 15)

        about_window_content_line_2 = QLabel("Author: Miles D. Ackerman", self)
        about_window_content_line_2.move(0 + about_window_left_justify_adjust, 15 + about_window_top_justify_adjust)
        about_window_content_line_2.resize(300, 15)

        about_window_content_line_3 = QLabel("Last modified (ran): %s" % (date), self)
        about_window_content_line_3.move(0 + about_window_left_justify_adjust, 30 + about_window_top_justify_adjust)
        about_window_content_line_3.resize(300, 15)

        about_window_content_line_3 = QLabel("OS: access somehow from computer?", self)
        about_window_content_line_3.move(0 + about_window_left_justify_adjust, 45 + about_window_top_justify_adjust)
        about_window_content_line_3.resize(300, 15)
        # end content of the about window

        self.setWindowTitle(self.title) # set the title of the displayed about window
        self.setGeometry(self.left, self.top, self.about_window_width, self.about_window_height) # set the geometry (size) of the displayed about window

#################################################################################### end "Make_About_Window" Class ####################################################################################
