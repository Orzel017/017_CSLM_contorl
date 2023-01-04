"""
File name: "About_Window.py"

Dates:
Originally separated/organized: 12-21-2022
Last modifed: 01-02-2023
Original author: MDA
Last modified by: MDA

Contents: class 'Make_About_Window' to display "About" window accessed from "Help" menu. This is imported in "Main_Window.py"

Notes:

TODO:
*Adjust the position of the about window to display at the center of the screen regardless of the main app window's on-screen location
*Display current computer's OS in about window line 4
*Format the about widnow so all of the lines of text are center aligned and the window is slightly bigger
*Add info./a link to the license associated with this software
"""

########################################################################################## start imports ##############################################################################################

from PyQt5 import QtWidgets # import QtWidgets from PyQt5 for building the whole pop-up about window

from PyQt5.QtWidgets import QLabel # import QLabel for displaying text on the about window

from datetime import date # import date package (THIS IS TEMPORARAY) because of frequent updates being made to this software. This is used for designating the date of last updates made in this app

############################################################################################ end imports ##############################################################################################

################################################################################################# start preliminaries #################################################################################

# getting the current date
get_todays_date = date.today() # access today's date from date package import

formatted_date_string = get_todays_date.strftime("%m-%d-%Y") # format date string to display

# display adjustment variables
about_window_left_justify_adjust = 5 # optional adjustment parameter for the content of the about window (left justify)

about_window_top_justify_adjust = 5 # optional adjustment parameter for the content of the about window (top justify)

################################################################################################## end preliminaries ##################################################################################

################################################################################## start "Make_About_Window" Class ####################################################################################

class Make_About_Window(QtWidgets.QMainWindow): # create the class `Make_About_Window` for displaying a new window with about content accessed from "Help" menu

    def __init__(self, parent = None): # setup about window object?

        super().__init__(parent) # inheritance?

        self.title = "About" # set the title of the about window

        # location
        self.top = 350 # define the display location of the about window
        self.left = 675 # can this be set to the center of the screen regardles of the position of the main window?

        # dimensions
        self.about_window_width  = 205 # define the width of the about window
        self.about_window_height = 70 # define the height of the about window

        # scaling
        self.setMaximumSize(self.about_window_width, self.about_window_height) # set the maximum size of the about window
        self.setMinimumSize(self.about_window_width, self.about_window_height) # set the minimum size of the about window

        ################################################################################## start content of the aobut window ##########################################################################

        # line 1
        about_window_content_line_1 = QLabel("Application name: MDA_gui", self) # set line 1 text label
        about_window_content_line_1.move(0 + about_window_left_justify_adjust, 0 + about_window_top_justify_adjust) # position line 1 text
        about_window_content_line_1.resize(300, 15) # set size of text label (the effect of this is no completely clear)

        # line 2
        about_window_content_line_2 = QLabel("Author: Miles D. Ackerman", self) # set line 2 text label
        about_window_content_line_2.move(0 + about_window_left_justify_adjust, 15 + about_window_top_justify_adjust) # position line 2 text
        about_window_content_line_2.resize(300, 15) #

        # line 3
        about_window_content_line_3 = QLabel("Last modified (ran): %s" % (formatted_date_string), self) # set line 3 text label
        about_window_content_line_3.move(0 + about_window_left_justify_adjust, 30 + about_window_top_justify_adjust) # position line 3 text
        about_window_content_line_3.resize(300, 15)

        # line 4
        about_window_content_line_3 = QLabel("OS: access somehow from computer?", self) # set line 4 text label
        about_window_content_line_3.move(0 + about_window_left_justify_adjust, 45 + about_window_top_justify_adjust) # position line 4 text
        about_window_content_line_3.resize(300, 15) #
        ################################################################################### end content of the aobut window ###########################################################################

        self.setWindowTitle(self.title) # display the title of the displayed about window

        self.setGeometry(self.left, self.top, self.about_window_width, self.about_window_height) # set the geometry (size) of the displayed about window

#################################################################################### end "Make_About_Window" class ####################################################################################
