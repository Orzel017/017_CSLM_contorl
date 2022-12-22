"""
File name: "Parent.py"

"""

########################################################################################## start imports ##############################################################################################

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import qApp
from About_Window import Make_About_Window
from Class_file import Child

############################################################################################ end imports ##############################################################################################

########################################################################## "Parent" class #####################################################################
class Parent(QtWidgets.QMainWindow):

    # ?
    def __init__(self, parent = None):
        super().__init__(parent)

        def display_about_window():

            self.Make_About_Window = Make_About_Window()
            self.Make_About_Window.show()

        ######################################################################### GUI prelims ##############################################################################

        # setting up main GUI window
        self.child_widget = Child(parent = self)
        self.setCentralWidget(self.child_widget) # setting the central widget of the main window (Parent class) to the Child class
        gui_window_height = 470 # define the main window height
        gui_window_width = 800 # define the main window width
        self.setGeometry(400, 200, gui_window_width, gui_window_height) # x-coord, y-coord, width, height
        self.setMinimumSize(gui_window_width, gui_window_height) # set the main window min size
        self.setMaximumSize(gui_window_width, gui_window_height) # set the main window max size
        self.setWindowTitle("mda_017_gui") # set the title of the main window

        ################################################################### menu bar #############################################################################
        main_window_menu_bar = self.menuBar() # this creates the menu abr for the main GUI window
        
        # "File" menu option
        file_menu = main_window_menu_bar.addMenu("File") # this adds the "File" option to the main window's menu bar
        exit_option = QtWidgets.QAction("Exit", self) # adds the "Exit" sub_option to "File" menu option
        exit_option.triggered.connect(qApp.quit) # setting the fnc of clicking "Exit" sub_option to quit application
        file_menu.addAction(exit_option) # adding "Exit" sub_option to "File" option
        
        # "Help" menu option
        help_menu = main_window_menu_bar.addMenu("Help") # this adds the "Help" option to the main window's menu bar
        hep_menu_about = QtWidgets.QAction("About", self) # this adds an "About" sub_option to the "Help" option
        hep_menu_about.triggered.connect(display_about_window) # this connects clicking the "About" to "..."
        help_menu.addAction(hep_menu_about) # adding "About" sub_option to the "Help" menu option
