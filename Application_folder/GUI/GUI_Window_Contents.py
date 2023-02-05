"""
File name: "GUI_Window_Contents.py"

Contents: QMainWindow for overall application window -to hold contents. This is the background window

Dates:
Originally created: 01-14-2023
Last modifed: 02-05-2023
Original author: MDA
Last modified by: MDA

Notes: This file sets up the first set of child Widget contents of the main application window

TODO:
*Fix about window import issue
"""

######################################################################################## start package imports ########################################################################################

from PyQt5.QtWidgets import (QListWidget, QHBoxLayout, QWidget, QStackedWidget, QMenu) # import submodules from PyQt5.QtWidgets

from PyQt5.QtCore import Qt # Qt module from QtCore

from Pages import Welcome_Page, Galvo_Control_Page, Camera_Control_Page, XY_Scan_Page # import subpages

########################################################################################## end package imports ########################################################################################

class Build_GUI_Constant_Contents(QWidget): # setup first GUI child object? Is `parent = None` required?

    """
    This class sets up the second-highest level Widgets of the application window. It builds the horizontal (QHBoxLayout) splitter and QStackedWidget for the lower-level widgets.
    """

    #################################################################################### start content functions ######################################################################################

    # function to change the displayed page
    def display_index_page(self, i): # define the function to switch pages within the `QStackedLayout`

        self.multi_item_display.setCurrentIndex(i) # switch to the new page index
    
    # function to create the context menu
    def contextMenuEvent(self, event): # create context (right-click) menu for access throughout application

        context_menu = QMenu(self) # create an instance of a context menu from `QMenu`
        
        context_menu_first_item = context_menu.addAction("One") # add the first item to the context menu

        context_menu_second_item = context_menu.addAction("Two") # add the second item to the context menu

        context_menu_third_item = context_menu.addAction("Three") # add the third item to the context menu

        activate_context_menu = context_menu.exec_(self.mapToGlobal(event.pos())) # allow teh context menu to be access by right-click from accros the application
    
    ###################################################################################### end content functions ######################################################################################

    def __init__(self, parent = None): # setup first child GUI window object? Is `parent = None` required?

        super(Build_GUI_Constant_Contents, self).__init__(parent) # inheritance?

        ############################################################################### start overal layout strucutre #################################################################################

        self.hbox = QHBoxLayout(self) # setup a `QHBoxLayout` object

        self.setLayout(self.hbox) # designate the layout widget of the `QWidget` class

        ################################################################################ end overal layout strucutre ##################################################################################

        ################################################################################# start left half main GUI window #############################################################################

        # setup a QListWidget to display the available imaging options

        self.left_items_list = QListWidget() # build a `QListWidget` for listing imaging options

        self.left_items_list.setFixedWidth(96) # control width of left list

        # adding items to the `QListWidget`
        self.left_items_list.insertItem (0, "Welcome") # item 1: welcome window
        self.left_items_list.insertItem (1, "Galvo Control") # item 2: XY-image (TODO: implemented but awaiting transition)
        self.left_items_list.insertItem (2, "Camera Control") # item 2: Camera Control (TODO: implement ThorCam API)
        self.left_items_list.insertItem (3, "XY-Image") # item 3: YZ-image (TODO: implemented but awaiting transition)
        # self.left_items_list.insertItem (4, "Item 4") # item 4: XZ-image (TODO: implemented but awaiting transition)
        # self.left_items_list.insertItem (5, "Item 5") # item 5: tiling image (TODO:)
        # self.left_items_list.insertItem (6, "Item 6") # item 6: Z-stack image (TODO:)

        # permanently remove scroll bars from QListWidget
        self.left_items_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff) # vertical scroll bar
        self.left_items_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff) # horizontal scroll bar

        self.left_items_list.currentRowChanged.connect(self.display_index_page) # connect the function to change the UI elements displayed based on QListWidget item selection

        ############################################################################# end left half main GUI window ###################################################################################

        ############################################################################### start right half main GUI window ##############################################################################

        # setup a QStackedWidget to display the selected imaging UI elements

        self.Welcome_page = QWidget()
        self.Galvo_control_page = QWidget()
        self.Camera_control_page = QWidget()
        self.XY_scan_page = QWidget()

        # initialize all displayed options UI elements
        Welcome_Page.build_welcome_page(self)
        Galvo_Control_Page.build_galvo_control_page(self)
        Camera_Control_Page.build_camera_control_page(self)
        XY_Scan_Page.build_xy_scan_page(self)

        self.multi_item_display = QStackedWidget(self) # create the QStackedWidget

        # add all displayed options UIwidgets
        self.multi_item_display.addWidget(self.Welcome_page)
        self.multi_item_display.addWidget(self.Galvo_control_page)
        self.multi_item_display.addWidget(self.Camera_control_page)
        self.multi_item_display.addWidget(self.XY_scan_page)

        ########################################################################### end right half main GUI window ####################################################################################

        ####################################################################### start to finalize the overall layout strucutre ########################################################################

        # complete the second-highest level GUI layout

        self.hbox.addWidget(self.left_items_list) # add the QListWidget

        self.hbox.addWidget(self.multi_item_display) # add the QStackWidget

        ###################################################################### end of finalizing the overall layout strucutre ########################################################################
