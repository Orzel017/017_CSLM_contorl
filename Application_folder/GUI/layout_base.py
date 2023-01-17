"""
Made: 01-14-2023

Modified: 01-17-2023
"""

import sys

from PyQt5.QtWidgets import (QApplication, QListWidget, QCheckBox, QRadioButton, QHBoxLayout, QWidget, QStackedWidget, QLineEdit, QFormLayout, QLabel)

import page_1, page_2, page_3

class GUI_Background(QWidget):

    def __init__(self):

        super(GUI_Background, self).__init__()

        ######################################### start main GUI window ###########################################
        # overall application dimensions
        gui_window_height = 650 # define the main window height. Old was 470
        gui_window_width = 1000 # define the main window width. Old was 800

        self.setGeometry(400, 200, gui_window_width, gui_window_height) # `.setgeometry()` function arguments run: x-coord, y-coord, width, height

        # scaling of the main app window
        self.setMinimumSize(gui_window_width, gui_window_height) # set the main window min size
        self.setMaximumSize(gui_window_width, gui_window_height) # set the main window max size

        # asthetics
        self.setWindowTitle("mda_gui") # set the title of the main app window
        ############################################## end main GUI window ####################################################

        ###################################################### start left half main GUI window #################################################
        self.leftlist = QListWidget()
        self.leftlist.insertItem (0, "Item 1")
        self.leftlist.insertItem (1, "Item 2")
        self.leftlist.insertItem (2, "Item 3")
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
	
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.leftlist)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        
        self.leftlist.currentRowChanged.connect(self.display_index_page)

        self.show()
            
    def display_index_page(self, i):

        self.Stack.setCurrentIndex(i)
		
def main():

   application = QApplication(sys.argv)

   ex = GUI_Background()

   sys.exit(application.exec_())
	
if __name__ == '__main__':
   main()