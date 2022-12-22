"""
File name:

Contents: PyQt framework for building an error window (currently this corresponds to a resolution issue -this should be changed but is a very large issue pertaining to error handling across the app)

Dates:
Originally separated/organized: 12-21-2022
Last modifed: 12-22-2022
Original author: MDA
Last modified by: MDA

Notes:

TODO:
*Re-implement error-handling framework for the entire software package
"""

######################################################################################## start imports ################################################################################################

from PyQt5 import QtWidgets # import QtWidgets from PyQt5 for building the window

from PyQt5.QtWidgets import QLabel # import QLabel for displaying text on the window

########################################################################################## end imports ################################################################################################

################################################################################ start `Make_Error_Window` Class ######################################################################################
class Make_Error_Window(QtWidgets.QMainWindow): # create the `Make_Error_Window` class for displaying a new window with error content displayed

    def __init__(self, parent = None): # setup error window object?

        super().__init__(parent) # inheritance?

        ################################################################################### start window prelims ######################################################################################

        self.setStyleSheet("background-color: red;") # make backgound color red

        self.title = "Error" # define the title of the error window

        # location
        self.top = 350 # set the display location of the error window
        self.left = 675 # can this be set to the center of the screen regardles of the position of the main window?

        # dimensions
        self.error_window_width  = 205 # define the width of the error window
        self.error_window_height = 50 # define the height of the error window
        self.setGeometry(self.left, self.top, self.error_window_width, self.error_window_height) # set the geometry (size) of the displayed error window

        # scaling
        self.setMaximumSize(self.error_window_width, self.error_window_height) # set the maximum size of the error window
        self.setMinimumSize(self.error_window_width, self.error_window_height) # set the minimum size of the error window

        # labeling
        self.setWindowTitle(self.title) # set the title of the displayed error window

        ############################################################################### start content of the aobut window #############################################################################
        error_window_left_justify_adjust = 5 # optional adjustment parameter for the content of the error window (left justify)

        error_window_top_justify_adjust = 5 # optional adjustment parameter for the content of the error window (top justify)

        error_window_content_line_1 = QLabel("ERROR!", self)
        error_window_content_line_1.move(60 + error_window_left_justify_adjust, 0 + error_window_top_justify_adjust)
        error_window_content_line_1.resize(300, 15)

        error_window_content_line_2 = QLabel("Adjust resolution", self)
        error_window_content_line_2.move(45 + error_window_left_justify_adjust, 15 + error_window_top_justify_adjust)
        error_window_content_line_2.resize(300, 15)

        ################################################################################ end content of the aobut window ##############################################################################
