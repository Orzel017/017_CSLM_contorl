"""
File name: "GUI_Window_Contents.py"

Contents: QMainWindow for overall application window -to hold contents. This is the background window

Dates:
Originally created: 01-14-2023
Last modifed: 01-26-2023
Original author: MDA
Last modified by: MDA

Notes: This file sets up the first set of child Widget contents of the main application window

TODO:
*Fix about window import issue
"""

######################################################################################## start package imports ########################################################################################

from PyQt5.QtWidgets import (QListWidget, QHBoxLayout, QWidget, QStackedWidget) # import submodules from PyQt5.QtWidgets

from PyQt5.QtCore import Qt # Qt module from QtCore

import Welcome_page, page_2, page_3 # import subpages. More info for here to come

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

    ######################################### !!! ##################################### start temporary functions ################################################ !!! ################################

    def display_index_page(self, i): # define the function to switch pages within the `QStackedLayout`

        self.multi_item_display.setCurrentIndex(i) # switch to the new page index
    
    ################################## !!! ############################################# end temporary functions ################################################# !!! ################################

    def __init__(self, parent = None): # setup first child GUI window object? Is `parent = None` required?

        super(Build_GUI_Constant_Contents, self).__init__(parent) # inheritance?

        ############################################################################### start overal layout strucutre #################################################################################

        self.hbox = QHBoxLayout(self) # setup a `QHBoxLayout` object

        self.setLayout(self.hbox) # designate the layout widget of the `QWidget` class

        ################################################################################ end overal layout strucutre ##################################################################################

        ################################################################################# start left half main GUI window #############################################################################

        # setup a QListWidget to display the available imaging options

        self.left_items_list = QListWidget() # build a `QListWidget` for listing imaging options

        self.left_items_list.setFixedWidth(84) # control width of lest list

        # print(self.left_items_list.size())
        # print(self.left_items_list.pos().x())

        # adding items to the `QListWidget`
        self.left_items_list.insertItem (0, "Welcome") # item 1: welcome window
        self.left_items_list.insertItem (1, "Galvo Control") # item 2: XY-image (TODO: implemented but awaiting transition)
        self.left_items_list.insertItem (2, "XY-Image") # item 3: YZ-image (TODO: implemented but awaiting transition)
        self.left_items_list.insertItem (3, "Item 4") # item 4: XZ-image (TODO: implemented but awaiting transition)
        self.left_items_list.insertItem (4, "Item 5") # item 5: tiling image (TODO:)
        self.left_items_list.insertItem (6, "Item 6") # item 6: Z-stack image (TODO:)

        # permanently remove scroll bars from QListWidget
        self.left_items_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff) # vertical scroll bar
        self.left_items_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) # horizontal scroll bar

        self.left_items_list.currentRowChanged.connect(self.display_index_page) # connect the function to change the UI elements displayed based on QListWidget item selection

        ############################################################################# end left half main GUI window ###################################################################################

        ############################################################################### start right half main GUI window ##############################################################################

        # setup a QStackedWidget to display the selected imaging UI elements

        self.Welcome_page = QWidget()
        self.XY_image_UI = QWidget()
        self.YZ_image_UI = QWidget()

        # initialize all displayed options UI elements
        Welcome_page.build_welcome_page(self)
        page_2.stack2UI(self)
        page_3.stack3UI(self)

        self.multi_item_display = QStackedWidget(self) # create the QStackedWidget

        # add all displayed options UIwidgets
        self.multi_item_display.addWidget(self.Welcome_page)
        self.multi_item_display.addWidget(self.XY_image_UI)
        self.multi_item_display.addWidget(self.YZ_image_UI)

        ########################################################################### end right half main GUI window ####################################################################################

        ####################################################################### start to finalize the overall layout strucutre ########################################################################

        # complete the second-highest level GUI layout

        self.hbox.addWidget(self.left_items_list) # add the QListWidget

        self.hbox.addWidget(self.multi_item_display) # add the QStackWidget

        ###################################################################### end of finalizing the overall layout strucutre ########################################################################
