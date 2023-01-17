"""
Made: 01-14-2023

Modified: 01-17-2023
"""

######################################################################################## start package imports ########################################################################################

import sys # import system-specific parameters and functions

from PyQt5 import QtWidgets # import QtWidgets from PyQt5 for building the window

from PyQt5.QtWidgets import (QApplication, QListWidget, QHBoxLayout, QWidget, QStackedWidget, qApp, QMenuBar) # import submodules from PyQt5.QtWidgets

from PyQt5 import QtCore # import QtCore for viewing on high-dpi resolution monitors

import page_1, page_2, page_3








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

class GUI_Background(QtWidgets.QMainWindow):

    ################################################################################### start GUI_Background functions ################################################################################

    def display_index_page(self, i):

        self.Stack.setCurrentIndex(i)
    
    #################################################################################### end GUI_Background functions #################################################################################

    def __init__(self):

        super(GUI_Background, self).__init__()

        ######################################### start main GUI window UI elements ###########################################

        # overall application dimensions
        gui_window_height = 650 # define the main window height. Old was 470
        gui_window_width = 1000 # define the main window width. Old was 800

        self.setGeometry(400, 200, gui_window_width, gui_window_height) # `.setgeometry()` function arguments run: x-coord, y-coord, width, height

        # scaling of the main app window
        self.setMinimumSize(gui_window_width, gui_window_height) # set the main window min size
        self.setMaximumSize(gui_window_width, gui_window_height) # set the main window max size

        # asthetics
        self.setWindowTitle("MDA_GUI") # set the title of the main app window

        ############################################## end main GUI window UI elements ####################################################

        ########################################################################################## start menu bar #####################################################################################

        main_window_menu_bar = self.menuBar() # create the menu bar for the main app window
        
        ####################################################################################### "File" menu bar item ##################################################################################
        file_menu_bar_item = main_window_menu_bar.addMenu("File") # add the "File" item to the main window's menu bar

        # exit_app_file_sub_item = QtWidgets.QAction("Exit", self) # adds the "Exit" sub-item to "File" menu item

        # file_menu_bar_item.addAction(exit_app_file_sub_item) # adding an action to the "Exit" sub-item

        # exit_app_file_sub_item.triggered.connect(qApp.quit) # setting the function of clicking "Exit" sub_option to quit application

        ############################################################################################ end menu bar #####################################################################################

        ###################################################### start left half main GUI window #################################################

        self.leftlist = QListWidget()
        self.leftlist.insertItem (0, "Item 1")
        self.leftlist.insertItem (1, "Item 2")
        self.leftlist.insertItem (2, "Item 3")

        self.leftlist.currentRowChanged.connect(self.display_index_page)

        ##################################################### end left half main GUI window #####################################################

        ###################################################### start right half main GUI window #################################################
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
        ##################################################### end right half main GUI window #################################################

        ################################### start finalize GUI main window #################################


        # self.setCentralWidget(self.Stack)


        self.main_widget = QtWidgets.QWidget(self)
        # self.main_widget.setFocus()
        # self.setCentralWidget(self.main_widget)

        # self.hbox = QHBoxLayout(self)
        # self.hbox.addWidget(self.leftlist)
        # self.hbox.addWidget(self.Stack)
        # self.main_widget.setLayout(self.hbox)

        from PyQt5 import QtGui
        # self.setCentralWidget(self.main_widget)
        # self.mainLayout = hbox(self.mainWidget)
        # self.hLayout = QtGui.QHBoxLayout()
        # self.hbox.addLayout(self.hLayout)



        # self.setLayout(hbox)

        # self.leftlist.currentRowChanged.connect(GUI_Helper_Functions.display_index_page)

        # self.show()                                                              # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        ###################################### end finalize GUI main window ########################
		
def main():

   application = QApplication(sys.argv)

   ex = GUI_Background()

   sys.exit(application.exec_())
	
if __name__ == '__main__':

   main()