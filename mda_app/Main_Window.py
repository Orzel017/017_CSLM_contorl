"""
File name: "Main_Window.py"

Contents: QMainWindow for overall application window -to hold contents. This is the background window

Dates:
Originally separated/organized: 12-21-2022
Last modifed: 12-22-2022
Original author: MDA
Last modified by: MDA

Notes: this file uses the `QtWidgets.QMainWindow` to build the background window of the overall application. After this the contents of the application are build for user-interaction. Importantly, 
the geometry and scaling parameters of the whole application can be set here

TODO:
*Scaling issues- need to adjust from fixed maximum main window width to arbitrary user-defined window dimensions. This requries some kind of adjustment for all child widgets within the main app 
window
*
"""

########################################################################################## start imports ##############################################################################################

from PyQt5 import QtWidgets # import QtWidgets from PyQt5 for building the window

from PyQt5.QtWidgets import qApp # import qApp for inner-app functionality (used for quitting the application while it is running)

from About_Window import Make_About_Window # import `Make_About_Window` from the "About_Window.py" file for dispalying the About window accessed from the Help menu bar item

from Class_file import Child # import `Child` class from the file "Class_file.py" to setup and build the contents of the application

######################################################################################### end imports #################################################################################################

################################################################################ start `Setup_Main_Window_Background`` class ##########################################################################

class Setup_Main_Window_Background(QtWidgets.QMainWindow): # define class `Setup_Main_Window_Background` using QMainWindow 

    def __init__(self, parent = None): # setup main window object? Is `parent = None` required?

        super().__init__(parent) # inheritance?

        ################################################################################### start main window functions ###############################################################################

        def display_about_window(): # define `display_about_window` to be accessed from Help menu item

            self.Make_About_Window = Make_About_Window() # construct the about window from imported class Make_About_Window

            self.Make_About_Window.show() # show the about window
        
        # space for other main window functions here

        # more space here for the same
        
        ################################################################################### end main window functions #################################################################################

        ############################################################################## start GUI main window prelims ##################################################################################

        self.child_widget = Child(parent = self) # designate the child widget

        self.setCentralWidget(self.child_widget) # setting the central widget of the main window (Setup_Main_Window_Background class) to the Child class

        # overall application dimensions
        gui_window_height = 470 # define the main window height
        gui_window_width = 800 # define the main window width

        self.setGeometry(400, 200, gui_window_width, gui_window_height) # `.setgeometry()` function arguments run: x-coord, y-coord, width, height

        # scaling of the main app window
        self.setMinimumSize(gui_window_width, gui_window_height) # set the main window min size
        self.setMaximumSize(gui_window_width, gui_window_height) # set the main window max size

        # asthetics
        self.setWindowTitle("mda_017_gui") # set the title of the main app window

        ################################################################################ end GUI main window prelims ##################################################################################

        ########################################################################################## start menu bar #####################################################################################

        main_window_menu_bar = self.menuBar() # create the menu bar for the main app window
        
        # "File" menu item
        file_menu_bar_item = main_window_menu_bar.addMenu("File") # add the "File" item to the main window's menu bar

        exit_app_file_sub_item = QtWidgets.QAction("Exit", self) # adds the "Exit" sub_item to "File" menu item

        file_menu_bar_item.addAction(exit_app_file_sub_item) # adding an action to the "Exit" sub-item

        exit_app_file_sub_item.triggered.connect(qApp.quit) # setting the function of clicking "Exit" sub_option to quit application
        
        # "Help" menu item
        help_menu = main_window_menu_bar.addMenu("Help") # this adds the "Help" option to the main window's menu bar
        hep_menu_about = QtWidgets.QAction("About", self) # this adds an "About" sub_option to the "Help" option
        hep_menu_about.triggered.connect(display_about_window) # this connects clicking the "About" to "..."
        help_menu.addAction(hep_menu_about) # adding "About" sub_option to the "Help" menu option

        ############################################################################################ end menu bar #####################################################################################

################################################################################## end `Setup_Main_Window_Background` class ###########################################################################
