"""
made: 01-17-2023

"""

from PyQt5.QtWidgets import (QApplication, QListWidget, QHBoxLayout, QWidget, QStackedWidget, qApp, QMenuBar) # import submodules from PyQt5.QtWidgets

import page_1, page_2, page_3

class Build_GUI_Constant_Contents(QWidget):

    def display_index_page(self, i):

        self.Stack.setCurrentIndex(i)

    def __init__(self, parent = None):

        super(Build_GUI_Constant_Contents, self).__init__(parent)

        self.hbox = QHBoxLayout(self)
        self.setLayout(self.hbox)

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

        # self.hbox.addWidget(self.Stack)

        self.hbox.addWidget(self.leftlist)
        self.hbox.addWidget(self.Stack)