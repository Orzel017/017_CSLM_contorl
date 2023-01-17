"""
File name: "?.py"

Contents: QMainWindow for overall application window -to hold contents. This is the background window

Dates:
Originally created: 01-14-2023
Last modifed: 01-17-2023
Original author: MDA
Last modified by: MDA

Notes: this file uses the `QtWidgets.QMainWindow` to build the background window of the overall application. After this the contents of the application are build for user-interaction. Importantly, 
the geometry and scaling parameters of the whole application can be set here

TODO:
*Scaling issues- need to adjust from fixed maximum main window width to arbitrary user-defined window dimensions. This requries some kind of adjustment for all child widgets within the main app 
window
*Implement "View" menu bar item actions -should be to change the UI for the user
*Implement "Actions" menu bar functionality -could be to re-arrange the child windows on the GUI
*Implement "Devices" meny bar actions -should be to list avaialble devices (info. about the DAQ, the ITC4001, and more)
"""

######################################################################################## start package imports ########################################################################################

import sys # import system-specific parameters and functions

from PyQt5 import QtWidgets # import QtWidgets from PyQt5 for building the window

from PyQt5.QtWidgets import (QApplication, QListWidget, QHBoxLayout, QWidget, QStackedWidget, qApp, QMenuBar) # import submodules from PyQt5.QtWidgets

from PyQt5 import QtCore # import QtCore for viewing on high-dpi resolution monitors

from GUI_Window_Contents import Build_GUI_Constant_Contents








import os
import inspect
root_folder = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_folder)
print(root_folder)


sys.path.append("017_CLSM_Control/Application_folder")
# from Application_folder.Extra_Windows import Make_About_Window # import `Make_About_Window` from the "About_Window.py" file for displaying the About window accessed from the Help menu bar item

from GUI_Helper_Utilities import GUI_Helper_Functions

########################################################################################## end package imports ########################################################################################

# scaling issue
"""
# this short section servces to remedy high-dpi scaling issue (on high-resolution monitors the appearance of the GUI displayed differently)
# the below two lines are from https://leomoon.com/journal/python/high-dpi-scaling-in-pyqt5/
"""

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) # enable highdpi scaling for applicaiton

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) # use high-dpi icons across GUI

class GUI_Window_Background(QtWidgets.QMainWindow):

    ################################################################################# start GUI_Window_Background functions ###########################################################################

    # function one goes here

    # ...
    
    ################################################################################# end GUI_Window_Background functions #############################################################################

    def __init__(self): # setup main GUI window object? Is `parent = None` required?

        super(GUI_Window_Background, self).__init__() # inheritance?

        ################################################################################## start main GUI window UI elements ##########################################################################

        # overall application dimensions
        gui_window_height = 650 # define the main window height. Old was 470
        gui_window_width = 1000 # define the main window width. Old was 800

        self.setGeometry(400, 200, gui_window_width, gui_window_height) # `.setgeometry()` function arguments run: x-coord, y-coord, width, height

        # scaling of the main app window
        self.setMinimumSize(gui_window_width, gui_window_height) # set the main window min size
        self.setMaximumSize(gui_window_width, gui_window_height) # set the main window max size

        # asthetics
        self.setWindowTitle("mda_b017_gui") # set the title of the main app window

        ################################################################################ end main GUI window UI elements ##############################################################################

        ########################################################################################## start menu bar #####################################################################################

        main_window_menu_bar = self.menuBar() # create the menu bar for the main app window

        self.setMenuBar(main_window_menu_bar) # force set the menu bar for the background GUI window
        
        ####################################################################################### "File" menu bar item ##################################################################################
        file_menu_bar_item = main_window_menu_bar.addMenu("File") # add the "File" item to the main window's menu bar

        exit_app_file_sub_item = QtWidgets.QAction("Exit", self) # adds the "Exit" sub-item to "File" menu item

        file_menu_bar_item.addAction(exit_app_file_sub_item) # adding an action to the "Exit" sub-item

        exit_app_file_sub_item.triggered.connect(qApp.quit) # setting the function of clicking "Exit" sub_option to quit application

        ######################################################################################### "Edit" menu bar item ################################################################################
        edit_menu_bar_item = main_window_menu_bar.addMenu("Edit") # add the "Edit" item to the main window's menu bar
        
        temp_edit_one_edit_sub_item = QtWidgets.QAction("temp_1", self) #

        edit_menu_bar_item.addAction(temp_edit_one_edit_sub_item) #

        ############################################################################################ "View" menu bar item #############################################################################
        view_menu_bar_item = main_window_menu_bar.addMenu("View") # add the "View" item to the main window's menu bar
        
        temp_view_one_view_sub_item = QtWidgets.QAction("temp_1", self) #

        view_menu_bar_item.addAction(temp_view_one_view_sub_item) #

        ########################################################################################### "Actions" menu bar item ###########################################################################
        actions_menu_bar_item = main_window_menu_bar.addMenu("Actions") # add the "Actions" item to the main window's menu bar
        
        temp_actions_one_actions_sub_item = QtWidgets.QAction("temp_1", self) #

        actions_menu_bar_item.addAction(temp_actions_one_actions_sub_item) #

        ########################################################################################### "Devices" menu bar item ###########################################################################
        devices_menu_bar_item = main_window_menu_bar.addMenu("Devices") # add the "Devices" item to the main window's menu bar
        
        temp_devices_one_devices_sub_item = QtWidgets.QAction("temp_1", self) #

        devices_menu_bar_item.addAction(temp_devices_one_devices_sub_item) #
        
        ######################################################################################## "Help" menu bar item #################################################################################
        help_menu_bar_item = main_window_menu_bar.addMenu("Help") # this adds the "Help" item to the main window's menu bar

        hep_menu_bar_about_sub_item = QtWidgets.QAction("About", self) # this adds an "About" sub-item to the "Help" item

        help_menu_bar_item.addAction(hep_menu_bar_about_sub_item) # add "About" action to the "Help" menu item

        # hep_menu_bar_about_sub_item.triggered.connect(display_about_window) # this connects clicking the "About" sub-item to display the about window

        ############################################################################################ end menu bar #####################################################################################

        ############################################################################################ end menu bar #####################################################################################

        #################################################################################### start finalize GUI main window ###########################################################################

        self.main_widget = Build_GUI_Constant_Contents() # initialize `Build_GUI_Constant_Contents()` object from "GUI_Window_Cotents.py"

        self.setCentralWidget(self.main_widget) # designate central widget of GUI_Window_Background object

        self.show() # show the main GUI window

        ################################################################################### end finalize GUI main window ##############################################################################
