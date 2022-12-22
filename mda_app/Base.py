# base_file.py
# last modified: 12-22-22

#################################################################### imports ###################################################################################

####################### reference about window #####################
# from About_Window import Make_About_Window
# from Parent_file import Parent
# from Class_file import Child

from Resolution_Error_Window import Make_Error_Window

# general packages
import sys
import nidaqmx
from nidaqmx.constants import AcquisitionType
import numpy as np
import pyqtgraph as pg
from datetime import date

import qcodes_contrib_drivers.drivers.NationalInstruments.DAQ as test

# MatPlotLib plotting packages
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib as mpl
import matplotlib.pyplot as plt

# PyQt5, this is the framework that builds the GUI
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QLabel
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox

#################### scaling issues in virtual machine ###############
# import PyQt5.QtCore as QtCore
from PyQt5 import QtCore

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True) # enable highdpi scaling
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) # use highdpi icons
# https://leomoon.com/journal/python/high-dpi-scaling-in-pyqt5/
#################### end ######################

############### global variable ##############
any_script_run_one_Q = False # for multiple scanning

############### prelims #######################
get_todays_date = date.today() # this is used for creating the final plot's plot labels

todays_date = get_todays_date.strftime("%m%d%Y") # this is used for creating the final plot's plot labels

################################################################## "Make_Error_Window_2" Class ######################################################################
class Make_Error_Window_2(QtWidgets.QMainWindow): # create the "Make_Error_Window_2" for displaying a new window with error content

    # ?
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet("background-color: red;")

        self.title = "Error" # define the title of the error window

        self.top = 350 # set the display location of the error window
        self.left = 675 # can this be set to the center of the screen regardles of the position of the main window?

        self.error_window_width  = 205 # define the width of the error window
        self.error_window_height = 50 # define the height of the error window

        self.setMaximumSize(self.error_window_width, self.error_window_height) # set the maximum size of the error window
        self.setMinimumSize(self.error_window_width, self.error_window_height) # set the minimum size of the error window

        # begin content of the error window
        error_window_left_justify_adjust = 5 # optional adjustment parameter for the content of the error window (left justify)

        error_window_top_justify_adjust = 5 # optional adjustment parameter for the content of the error window (top justify)

        error_window_content_line_1 = QLabel("ERROR!", self)
        error_window_content_line_1.move(60 + error_window_left_justify_adjust, 0 + error_window_top_justify_adjust)
        error_window_content_line_1.resize(300, 15)

        error_window_content_line_2 = QLabel("Adjust address to save", self)
        error_window_content_line_2.move(40 + error_window_left_justify_adjust, 15 + error_window_top_justify_adjust)
        error_window_content_line_2.resize(300, 15)

        # end content of the error window

        self.setWindowTitle(self.title) # set the title of the displayed error window
        self.setGeometry(self.left, self.top, self.error_window_width, self.error_window_height) # set the geometry (size) of the displayed error window

################################################### MatPlotLib class ######################################################################################
class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent = None, width = 10, height = 10, dpi = 1000):

        # fig = Figure(figsize = (width, height), dpi = dpi)
        # self.axes = fig.add_subplot()
        self.fig, self.axes = plt.subplots(figsize=(width, height), dpi=dpi, tight_layout = True)
        super(MplCanvas, self).__init__(self.fig)

#################################################################### END #######################################################################################
