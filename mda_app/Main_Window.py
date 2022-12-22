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
*Implement "View" menu bar item actions -should be to change the UI for the user
*Implement "Actions" menu bar functionality -could be to re-arrange the child windows on the GUI
*Implement "Devices" meny bar actions -should be to list avaialble devices (info. about the DAQ, the ITC4001, and more)
"""

########################################################################################## start imports ##############################################################################################

from PyQt5 import QtWidgets # import QtWidgets from PyQt5 for building the window

from PyQt5.QtWidgets import qApp # import qApp for inner-app functionality (used for quitting the application while it is running)

from About_Window import Make_About_Window # import `Make_About_Window` from the "About_Window.py" file for dispalying the About window accessed from the Help menu bar item

from Window_Contents import Setup_Main_Window_Contents # import `Setup_Main_Window_Contents` class from the file "Class_file.py" to setup and build the contents of the application

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

        self.child_widget = Setup_Main_Window_Contents(parent = self) # designate the child widget

        self.setCentralWidget(self.child_widget) # setting the central widget of the main window (Setup_Main_Window_Background class) to the Child class

        # overall application dimensions
        gui_window_height = 470 # define the main window height
        gui_window_width = 800 # define the main window width

        self.setGeometry(400, 200, gui_window_width, gui_window_height) # `.setgeometry()` function arguments run: x-coord, y-coord, width, height

        # scaling of the main app window
        self.setMinimumSize(gui_window_width, gui_window_height) # set the main window min size
        self.setMaximumSize(gui_window_width, gui_window_height) # set the main window max size

        # asthetics
        self.setWindowTitle("unique_app_name") # set the title of the main app window

        ################################################################################ end GUI main window prelims ##################################################################################

        ########################################################################################## start menu bar #####################################################################################

        main_window_menu_bar = self.menuBar() # create the menu bar for the main app window
        
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

        hep_menu_bar_about_sub_item.triggered.connect(display_about_window) # this connects clicking the "About" sub-item to display the about window

        ############################################################################################ end menu bar #####################################################################################

################################################################################## end `Setup_Main_Window_Background` class ###########################################################################
