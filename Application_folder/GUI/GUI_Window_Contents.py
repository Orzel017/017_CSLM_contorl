"""
File name: "GUI_Window_Contents.py"

Contents: QMainWindow for overall application window -to hold contents. This is the background window

Dates:
Originally created: 01-14-2023
Last modifed: 01-17-2023
Original author: MDA
Last modified by: MDA

Notes: This file sets up the first set of child Widget contents of the main application window

TODO:
*
"""

######################################################################################## start package imports ########################################################################################

from PyQt5.QtWidgets import (QListWidget, QHBoxLayout, QWidget, QStackedWidget) # import submodules from PyQt5.QtWidgets

import page_1, page_2, page_3 # import subpages. More info for here to come

########################################################################################## end package imports ########################################################################################

##################### attempts for about window imports below ##################################################

import os
import sys  # import system-specific parameters and functions
import inspect
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
# print(root_folder)

sys.path.append("017_CLSM_Control/Application_folder")
# from Application_folder.Extra_Windows import Make_About_Window # import `Make_About_Window` from the "About_Window.py" file for displaying the About window accessed from the Help menu bar item

from GUI_Helper_Utilities import GUI_Helper_Functions

##################### attempts for about window imports above ##################################################

class Build_GUI_Constant_Contents(QWidget): # setup first GUI child object? Is `parent = None` required?

    """
    This class sets up the second-highest level Widgets of the application window. It builds the horizontal (QHBoxLayout) splitter and QStackedWidget for the lower-level widgets.
    """

    def display_index_page(self, i):

        self.Stack.setCurrentIndex(i)

    def __init__(self, parent = None): # inheritance?

        super(Build_GUI_Constant_Contents, self).__init__(parent)

        self.hbox = QHBoxLayout(self)
        self.setLayout(self.hbox)

        ################################################################################# start left half main GUI window #############################################################################

        self.leftlist = QListWidget()
        self.leftlist.insertItem (0, "Item 1")
        self.leftlist.insertItem (1, "Item 2")
        self.leftlist.insertItem (2, "Item 3")

        self.leftlist.currentRowChanged.connect(self.display_index_page)

        ############################################################################# end left half main GUI window ###################################################################################

        ############################################################################### start right half main GUI window ##############################################################################

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        page_1.stack1UI(self)
        page_2.stack2UI(self)
        page_3.stack3UI(self)

        self.Stack = QStackedWidget (self)
        self.Stack.addWidget (self.stack1)
        self.Stack.addWidget (self.stack2)
        self.Stack.addWidget (self.stack3)

        ########################################################################### end right half main GUI window ####################################################################################

        # self.hbox.addWidget(self.Stack)

        self.hbox.addWidget(self.leftlist)
        self.hbox.addWidget(self.Stack)
