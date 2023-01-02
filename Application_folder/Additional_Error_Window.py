"""
File name: `Additional_Error_Window`

Contents: framework for additional error window (this window corresponds to a saving address error when saving a `.npy` data array)

Dates:
Originally separated/organized: 12-22-2022
Last modifed: 12-22-2022
Original author: MDA
Last modified by: MDA

Notes:

TODO:
"""

########################################################################################### start imports #############################################################################################

from PyQt5 import QtWidgets # import QtWidgets from PyQt5 for building the window

from PyQt5.QtWidgets import QLabel # import QLabel for displaying text on the window

########################################################################################### start imports #############################################################################################

################################################################## "Make_Error_Window_2" Class ######################################################################
class Make_Error_Window_2(QtWidgets.QMainWindow): # create the "Make_Error_Window_2" for displaying a new window with error content

    # ?
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet("background-color: red;")

        self.title = "Error" # define the title of the error window

        self.top = 350 # set the display location of the error window
        self.left = 675 # can this be set to the center of the screen regardles of the position of the main window?

        self.error_window_width = 205 # define the width of the error window
        self.error_window_height = 50 # define the height of the error window

        self.setMaximumSize(self.error_window_width, self.error_window_height) # set the maximum size of the error window
        self.setMinimumSize(self.error_window_width, self.error_window_height) # set the minimum size of the error window

        # begin content of the error window
        error_window_left_justify_adjust = 5 # optional adjustment parameter for the content of the error window (left justify)

        error_window_top_justify_adjust = 5 # optional adjustment parameter for the content of the error window (top justify)

        error_window_content_line_1 = QLabel("ERROR!", self)
        error_window_content_line_1.move(60 + error_window_left_justify_adjust, 0 + error_window_top_justify_adjust)
        error_window_content_line_1.resize(300, 15)

        error_window_content_line_2 = QLabel("Adjust address to save", self)
        error_window_content_line_2.move(40 + error_window_left_justify_adjust, 15 + error_window_top_justify_adjust)
        error_window_content_line_2.resize(300, 15)

        # end content of the error window

        self.setWindowTitle(self.title) # set the title of the displayed error window
        self.setGeometry(self.left, self.top, self.error_window_width, self.error_window_height) # set the geometry (size) of the displayed error window