"""
File name: "Welcome_window.py"

Contents: wlecome window content (and brief tutorial messages?)

Dates:
Originally created: 12-30-2022
Last modifed: 12-30-2022
Original author: MDA
Last modified by: MDA

Notes:

TODO:
*

"""

############################################################################################## start imports ##########################################################################################

from PyQt5 import QtWidgets # QtWidgets module

from PyQt5.QtWidgets import QFrame, QLabel, QPushButton # submodules from QtWidgets

# import pyqtgraph as pg # pyqtgraph import (grphing package from PyQt)

############################################################################################# end imports #############################################################################################

test_bool = True

class Setup_Welcome_Window(QtWidgets.QWidget):#, **kwargs): # kwargs needed?

    # setup welcome window object
    def __init__(self, parent = None):#, **kwargs): # kwargs needed?

        super().__init__(parent) # inheritance?

    ##################### start welcome window functions ################

        def test_change_window_function():

            print("hello")

            print(test_bool)

    ###################### end welcome window functions #################

        # test window frame
        test_window = QFrame(self)
        test_window.setFrameShape(QFrame.StyledPanel)
        test_window.setFixedSize(300, 300)

        # test QLabel
        xy_scan_x_voltage_min_widget = QLabel("test_QLabel", self) # widget
        xy_scan_x_voltage_min_widget.setParent(test_window)
        xy_scan_x_voltage_min_widget.move(25, 90)

        # test change window button
        test_button = QPushButton("click me!", self) # button
        test_button.setParent(test_window)
        test_button.resize(60, 40)
        test_button.move(80, 110)
        test_button.clicked.connect(test_change_window_function) #
