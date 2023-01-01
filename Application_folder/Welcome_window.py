"""
File name: "Welcome_window.py"

Contents: wlecome window content (and brief tutorial messages?)

Dates:
Originally created: 12-30-2022
Last modifed: 12-31-2022
Original author: MDA
Last modified by: MDA

Notes:

TODO:
*

"""

############################################################################################## start imports ##########################################################################################

from PyQt5 import QtWidgets # QtWidgets module

from PyQt5.QtWidgets import QFrame, QLabel, QPushButton # submodules from QtWidgets
from PyQt5.QtGui import QWindow
import Main_Window

import Helper_Functions

# from Helper_Functions import display_window_contents

# from Main_Window import second_child_widget

# import pyqtgraph as pg # pyqtgraph import (grphing package from PyQt)

############################################################################################# end imports #############################################################################################

# global test_bool
# test_bool = True

class Setup_Welcome_Window(QtWidgets.QMainWindow):#, **kwargs): # kwargs needed?

    test_bool = True

    # setup welcome window object
    def __init__(self, parent = None):#, **kwargs): # kwargs needed?

        super().__init__(parent) # inheritance?

    ##################### start welcome window functions ################

        # def test_change_window_function():

        #     # print("hello")

        #     # print("(welcome)" + str(self.test_bool))

        #     # global test_bool
        #     test_bool = False

        #     # print("(welcome)" + str(test_bool))

        #     # print("hello world!")

        #     display_window_contents(self)

        #     # second_child_widget = Setup_Main_Window_Contents(parent = self)
        #     # Main_Window.Setup_Main_Window_Background.setCentralWidget(second_child_widget)

        #     # print("finished transition")

        def temp_fnc_1():

            self.test_window.hide()
            self.welcome_qLabel.hide()
            self.test_window.hide()
            # print("****")
            # Setup_Welcome_Window.hide()
            Helper_Functions.display_window_contents(self)

    ###################### end welcome window functions #################

        # test window frame
        self.test_window = QFrame(self)
        self.test_window.setFrameShape(QFrame.StyledPanel)
        self.test_window.setFixedSize(300, 300)

        # test QLabel
        self.welcome_qLabel = QLabel("Welcome Window", self) # widget
        self.welcome_qLabel.setParent(self.test_window)
        self.welcome_qLabel.move(25, 90)

        # test change window button
        self.test_button = QPushButton("click me!", self) # button
        self.test_button.setParent(self.test_window)
        self.test_button.resize(60, 40)
        self.test_button.move(80, 110)
        # test_button.clicked.connect(Helper_Functions.display_window_contents(self)) #
        self.test_button.clicked.connect(temp_fnc_1)
