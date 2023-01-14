"""
File name: "Window_Contents.py"

Contents: main window content (curently including scanning scripts -this will be changed later as they will be moved)

Dates:
Originally separated/organized: 12-21-2022
Last modifed: 01-14-2023
Original author: MDA
Last modified by: MDA

Notes:

TODO:
*Move scanning scripts to other files (would they need to be changed to classes?)
**This presents numerous issues with data handling and transfer from file to file
"""

############################################################################################## start imports ##########################################################################################

# NI-DAQmx API imports
import nidaqmx # general API import

from nidaqmx.constants import (AcquisitionType, FrequencyUnits, CountDirection, Edge) # API constant(s) import(s)

import numpy as np # numpy for arrays

# import sys
# sys.path.insert(0, "./Application_folder/Drivers")
# import Drivers
# from Drivers import cDAQ

# from import cDAQ as test

from Drivers import cDAQ as test

# MatPlotLib plotting packages
import matplotlib # generica Matplotlib import

matplotlib.use("Qt5Agg") # tailor matplotlib package for use in PyQt5?

# datetime module
from datetime import date # date module import

# PyQt5, this is the framework that builds the GUI windows
import PyQt5 # general PyQt5 framework import

from PyQt5 import QtWidgets # QtWidgets module

from PyQt5.QtWidgets import QFrame, QTextEdit, QPushButton, QHBoxLayout, QLabel, QSplitter, QLineEdit, QMenu # submodules from QtWidgets

from PyQt5.QtGui import QFont # QFont from QtGui

from PyQt5.QtCore import Qt # Qt module from QtCore

import pyqtgraph as pg # pyqtgraph import (grphing package from PyQt)

# imports from other files within folder structure
from Plotting_Setup import MplCanvas # import MplCanvas class from "Plotting_Setup.py"

from Resolution_Error_Window import Make_Error_Window # import Make_Error_Window class from "Resolution_Error_Window.py"

from Additional_Error_Window import Make_Error_Window_2 # import Make_Error_Window_2 class from "Additional_Error_Window.py"

############################################################################################# end imports #############################################################################################

########################################################################################### start prelims #############################################################################################

get_todays_date = date.today() # this is used for creating the final plot's plot labels

todays_date = get_todays_date.strftime("%m%d%Y") # this is used for creating the final plot's plot labels

any_script_run_one_Q = False # global variable for multiple scanning

############################################################################################ end prelims ##############################################################################################

# define main window contents class
class Setup_Main_Window_Contents(QtWidgets.QWidget):#, **kwargs): # kwargs needed?

    # define main window contents object?
    def __init__(self, parent = None):#, **kwargs): # kwargs needed?

        super().__init__(parent) # inheritance?

        self.hbox = QHBoxLayout(self)

        plotwin = pg.GraphicsLayoutWidget(show = True)
    
        ############################################################# left half window #####################################################################
        self.left_window = QFrame(self)
        self.left_window.setFrameShape(QFrame.StyledPanel)
        self.left_window.setFixedSize(340, 510)

        # QTextEdit display for printing scan parameters to GUI window
        """
        This creates a textbox located in the lower left hand corner of the GUI. It is set (parent) to the left_window. When any scan script is run the 
        parameters enterd by the user are collected from their respective QLineedits and then printed in a list to this QTextBox. This allows the user 
        select and copy the parameters they used quickly in order to save them to an external file as documentation of scans run.

        Room for improvement:
        1. The date (get from "todays_date" that is already implemented) could be added to the first line of any scans parameter printing fnc
        2. The info printed to this QTextBox could also and/or be saved to an external file for record/documentation
        """

        parameters_dsiplay_text_box = QTextEdit(self.left_window)
        parameters_dsiplay_text_box.resize(320, 113)
        parameters_dsiplay_text_box.move(10, 309)
        parameters_dsiplay_text_box.setParent(self.left_window)

        ############################################################### right half window ###################################################################
        self.right_window = QFrame(self)
        self.right_window.setFrameShape(QFrame.StyledPanel)
        self.right_window.setFixedSize(600, 600)

        ##################################################### plot in right window ##################################################################

        plot_res = 5.42
        self.sc = MplCanvas(self, canvas_width = plot_res, canvas_height = plot_res, canvas_dpi = 110)                                                                      # changing dpi does something to scale of figureure
        self.sc.move(2, 2)
        self.sc.setParent(self.right_window)
        self.sc.axes.xaxis.set_tick_params(labelsize = 8)
        self.sc.axes.yaxis.set_tick_params(labelsize = 8)

        ############################################################# split left and right windows #########################################################
        
        self.splitter1 = QSplitter(Qt.Horizontal)
        self.splitter1.addWidget(self.left_window)
        self.splitter1.addWidget(self.right_window)
        self.hbox.addWidget(self.splitter1) # set layout and show window
        self.setLayout(self.hbox)
        self.show()

        ############################################################# scanning (XY, XZ, & YZ) section ############################################################################
        
        ##################################### overall ####################################

        ############ begin save data section ###############
        self.save_scan_data_button = QPushButton("Save scan data:", self) # create the save scan data button
        self.save_scan_data_button.setParent(self.left_window) # set the "parent" bound of the save scan data button
        self.save_scan_data_button.resize(90, 20) # resize the save scan data button
        self.save_scan_data_button.move(10, 280) # position the save scan data button in the left winodw
        self.save_scan_data_button.clicked.connect(save_scan_data_fnc)

        save_scan_data_qlineedit = QLineEdit(self) # qlineedit
        save_scan_data_qlineedit.setParent(self.left_window)
        save_scan_data_qlineedit.resize(189, 20)
        save_scan_data_qlineedit.move(105, 280)

        save_scan_data_extension_widget = QLabel("\".npy\"", self) # widget
        save_scan_data_extension_widget.setParent(self.left_window),
        save_scan_data_extension_widget.move(297, 288 - 5)
        ############ end save data section ###############

        ###
        self.set_galvo_to_zero_button = QPushButton("Zero galvo", self)
        self.set_galvo_to_zero_button.setParent(self.left_window)
        self.set_galvo_to_zero_button.resize(70, 20)
        self.set_galvo_to_zero_button.move(80, 480)
        self.set_galvo_to_zero_button.clicked.connect(zero_galvo_function)
        ##

        # scan widgets overall "Scanning"
        scan_widget_overall = QLabel("Scanning options:")
        scan_widget_overall.setFont(QFont("Times font", 6))
        scan_widget_overall.setParent(self.left_window)
        scan_widget_overall.move(120, 10)

        indiv_scan_labels_y_height = 25

        row_y_adjust = 5

        overall_y_adjust = 10

        #########################################################################################
        ########################################### XY scanning #################################
        #########################################################################################

        xy_scan_widgets_left_x_justify = 5
        xy_scan_parameters_validated_Q = False

        # XY scan
        self.xy_scan_label_widget = QLabel("XY scan", self) # widget
        self.xy_scan_label_widget.setParent(self.left_window)
        self.xy_scan_label_widget.move(12 + 10, indiv_scan_labels_y_height + overall_y_adjust)
        self.xy_scan_label_widget.show()

        # resolution
        xy_scan_resolution_widget = QLabel("Res:", self) # widget
        xy_scan_resolution_widget.setParent(self.left_window)
        xy_scan_resolution_widget.move(xy_scan_widgets_left_x_justify, 40 + row_y_adjust + overall_y_adjust)
        xy_scan_resolution_widget.show()

        xy_scan_resolution_qlineedit = QLineEdit(self) # qclineedit
        xy_scan_resolution_qlineedit.setParent(self.left_window)
        xy_scan_resolution_qlineedit.move(30, 40 + row_y_adjust + overall_y_adjust)
        xy_scan_resolution_qlineedit.resize(55, 15)
        xy_scan_resolution_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        # read time
        xy_scan_read_time_widget = QLabel("APD_t:", self) # widget
        xy_scan_read_time_widget.setParent(self.left_window)
        xy_scan_read_time_widget.move(xy_scan_widgets_left_x_justify, 65 + row_y_adjust + overall_y_adjust)

        xy_scan_read_time_qlineedit = QLineEdit(self) # qclineedit
        xy_scan_read_time_qlineedit.setParent(self.left_window)
        xy_scan_read_time_qlineedit.move(40, 65 + row_y_adjust + overall_y_adjust)
        xy_scan_read_time_qlineedit.resize(45, 15)
        xy_scan_read_time_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)
        
        # x voltage (min and max)
        xy_scan_x_voltage_min_widget = QLabel("x_V_min:", self) # widget
        xy_scan_x_voltage_min_widget.setParent(self.left_window)
        xy_scan_x_voltage_min_widget.move(xy_scan_widgets_left_x_justify, 90 + row_y_adjust + overall_y_adjust)

        xy_scan_x_voltage_min_qlineedit = QLineEdit(self) # qclineedit
        xy_scan_x_voltage_min_qlineedit.setParent(self.left_window)
        xy_scan_x_voltage_min_qlineedit.move(50, 90 + row_y_adjust + overall_y_adjust)
        xy_scan_x_voltage_min_qlineedit.resize(35, 15)
        xy_scan_x_voltage_min_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        xy_scan_x_voltage_max_widget = QLabel("x_V_max:", self) # widget
        xy_scan_x_voltage_max_widget.setParent(self.left_window)
        xy_scan_x_voltage_max_widget.move(xy_scan_widgets_left_x_justify, 115 + row_y_adjust + overall_y_adjust)

        xy_scan_x_voltage_max_qlineedit = QLineEdit(self) # qclineedit
        xy_scan_x_voltage_max_qlineedit.setParent(self.left_window)
        xy_scan_x_voltage_max_qlineedit.move(55, 115 + row_y_adjust + overall_y_adjust)
        xy_scan_x_voltage_max_qlineedit.resize(30, 15)
        xy_scan_x_voltage_max_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        # y voltage (min and max)
        xy_scan_y_voltage_min_widget = QLabel("y_V_min:", self) # widget
        xy_scan_y_voltage_min_widget.setParent(self.left_window)
        xy_scan_y_voltage_min_widget.move(xy_scan_widgets_left_x_justify, 140 + row_y_adjust + overall_y_adjust)

        xy_scan_y_voltage_min_qlineedit = QLineEdit(self) # qclineedit
        xy_scan_y_voltage_min_qlineedit.setParent(self.left_window)
        xy_scan_y_voltage_min_qlineedit.move(50, 140 + row_y_adjust + overall_y_adjust)
        xy_scan_y_voltage_min_qlineedit.resize(35, 15)
        xy_scan_y_voltage_min_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        xy_scan_y_voltage_max_widget = QLabel("y_V_max:", self) # widget
        xy_scan_y_voltage_max_widget.setParent(self.left_window)
        xy_scan_y_voltage_max_widget.move(xy_scan_widgets_left_x_justify, 165 + row_y_adjust + overall_y_adjust)

        xy_scan_y_voltage_max_qlineedit = QLineEdit(self) # qclineedit
        xy_scan_y_voltage_max_qlineedit.setParent(self.left_window)
        xy_scan_y_voltage_max_qlineedit.move(55, 165 + row_y_adjust + overall_y_adjust)
        xy_scan_y_voltage_max_qlineedit.resize(30, 15)
        xy_scan_y_voltage_max_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)
        
        # z piezo
        xy_scan_z_piezo_voltage_widget = QLabel("z_V:", self) # widget
        xy_scan_z_piezo_voltage_widget.setParent(self.left_window)
        xy_scan_z_piezo_voltage_widget.move(xy_scan_widgets_left_x_justify, 190 + row_y_adjust + overall_y_adjust)

        xy_scan_z_piezo_voltage_qlineedit = QLineEdit(self) # qclineedit
        xy_scan_z_piezo_voltage_qlineedit.setParent(self.left_window)
        xy_scan_z_piezo_voltage_qlineedit.move(30, 190 + row_y_adjust + overall_y_adjust)
        xy_scan_z_piezo_voltage_qlineedit.resize(55, 15)
        xy_scan_z_piezo_voltage_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        # run xy scan button
        xy_scan_run_button = QPushButton("run\nXY scan", self) # button
        xy_scan_run_button.setParent(self.left_window)
        xy_scan_run_button.resize(60, 40)
        xy_scan_run_button.move(10, 215 + row_y_adjust + overall_y_adjust)
        xy_scan_run_button.clicked.connect(xy_scan_resolution_validation_fnc) # this framework is limited currently to only validating resolution

        #######################################################################################
        ####################################### XZ scanning ###################################
        #######################################################################################

        xz_scan_widgets_left_x_justify = 130

        # scan widget 2 "XZ"
        scan_widget_2 = QLabel("XZ scan", self)
        scan_widget_2.setParent(self.left_window)
        scan_widget_2.move(145 + 5, indiv_scan_labels_y_height + overall_y_adjust)

        # resolution
        xz_scan_resolution_widget = QLabel("Res:", self) # widget
        xz_scan_resolution_widget.setParent(self.left_window)
        xz_scan_resolution_widget.move(xz_scan_widgets_left_x_justify, 40 + row_y_adjust + overall_y_adjust)

        xz_scan_resolution_qlineedit = QLineEdit(self) # qclineedit
        xz_scan_resolution_qlineedit.setParent(self.left_window)
        xz_scan_resolution_qlineedit.move(25 + xz_scan_widgets_left_x_justify, 40 + row_y_adjust + overall_y_adjust)
        xz_scan_resolution_qlineedit.resize(55, 15)
        xz_scan_resolution_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        # read time
        xz_scan_read_time_widget = QLabel("APD_t:", self) # widget
        xz_scan_read_time_widget.setParent(self.left_window)
        xz_scan_read_time_widget.move(xz_scan_widgets_left_x_justify, 65 + row_y_adjust + overall_y_adjust)

        xz_scan_read_time_qlineedit = QLineEdit(self) # qclineedit
        xz_scan_read_time_qlineedit.setParent(self.left_window)
        xz_scan_read_time_qlineedit.move(35 + xz_scan_widgets_left_x_justify, 65 + row_y_adjust + overall_y_adjust)
        xz_scan_read_time_qlineedit.resize(45, 15)
        xz_scan_read_time_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)
        
        # x voltage (min and max)
        xz_scan_x_voltage_min_widget = QLabel("x_V_min:", self) # widget
        xz_scan_x_voltage_min_widget.setParent(self.left_window)
        xz_scan_x_voltage_min_widget.move(xz_scan_widgets_left_x_justify, 90 + row_y_adjust + overall_y_adjust)

        xz_scan_x_voltage_min_qlineedit = QLineEdit(self) # qclineedit
        xz_scan_x_voltage_min_qlineedit.setParent(self.left_window)
        xz_scan_x_voltage_min_qlineedit.move(45 + xz_scan_widgets_left_x_justify, 90 + row_y_adjust + overall_y_adjust)
        xz_scan_x_voltage_min_qlineedit.resize(35, 15)
        xz_scan_x_voltage_min_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        xz_scan_x_voltage_max_widget = QLabel("x_V_max:", self) # widget
        xz_scan_x_voltage_max_widget.setParent(self.left_window)
        xz_scan_x_voltage_max_widget.move(xz_scan_widgets_left_x_justify, 115 + row_y_adjust + overall_y_adjust)

        xz_scan_x_voltage_max_qlineedit = QLineEdit(self) # qclineedit
        xz_scan_x_voltage_max_qlineedit.setParent(self.left_window)
        xz_scan_x_voltage_max_qlineedit.move(50 + xz_scan_widgets_left_x_justify, 115 + row_y_adjust + overall_y_adjust)
        xz_scan_x_voltage_max_qlineedit.resize(30, 15)
        xz_scan_x_voltage_max_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        # y voltage single setting
        xz_scan_y_voltage_widget = QLabel("y_V:", self) # widget
        xz_scan_y_voltage_widget.setParent(self.left_window)
        xz_scan_y_voltage_widget.move(xz_scan_widgets_left_x_justify, 140 + row_y_adjust + overall_y_adjust)

        xz_scan_y_voltage_qlineedit = QLineEdit(self) # qclineedit
        xz_scan_y_voltage_qlineedit.setParent(self.left_window)
        xz_scan_y_voltage_qlineedit.move(25 + xz_scan_widgets_left_x_justify, 140 + row_y_adjust + overall_y_adjust)
        xz_scan_y_voltage_qlineedit.resize(55, 15)
        xz_scan_y_voltage_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)
                                
        # z piezo (min and max)
        xz_scan_z_piezo_min_voltage_widget = QLabel("z_V_min:", self) # widget
        xz_scan_z_piezo_min_voltage_widget.setParent(self.left_window)
        xz_scan_z_piezo_min_voltage_widget.move(xz_scan_widgets_left_x_justify, 165 + row_y_adjust + overall_y_adjust)

        xz_scan_z_piezo_min_voltage_qlineedit = QLineEdit(self) # qclineedit
        xz_scan_z_piezo_min_voltage_qlineedit.setParent(self.left_window)
        xz_scan_z_piezo_min_voltage_qlineedit.move(45 + xz_scan_widgets_left_x_justify, 165 + row_y_adjust + overall_y_adjust)
        xz_scan_z_piezo_min_voltage_qlineedit.resize(35, 15)
        xz_scan_z_piezo_min_voltage_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        xz_scan_z_piezo_max_voltage_widget = QLabel("z_V_max:", self) # widget
        xz_scan_z_piezo_max_voltage_widget.setParent(self.left_window)
        xz_scan_z_piezo_max_voltage_widget.move(xz_scan_widgets_left_x_justify, 190 + row_y_adjust + overall_y_adjust)

        xz_scan_z_piezo_max_voltage_qlineedit = QLineEdit(self) # qclineedit
        xz_scan_z_piezo_max_voltage_qlineedit.setParent(self.left_window)
        xz_scan_z_piezo_max_voltage_qlineedit.move(50 + xz_scan_widgets_left_x_justify, 190 + row_y_adjust + overall_y_adjust)
        xz_scan_z_piezo_max_voltage_qlineedit.resize(30, 15)
        xz_scan_z_piezo_max_voltage_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        # run xz scan button
        xz_scan_run_button = QPushButton("run\nXZ scan", self) # button
        xz_scan_run_button.setParent(self.left_window)
        xz_scan_run_button.resize(60, 40)
        xz_scan_run_button.move(10 + xz_scan_widgets_left_x_justify, 215 + row_y_adjust + overall_y_adjust)
        xz_scan_run_button.clicked.connect(xz_scan_resolution_validation_fnc) # this framework is limited currently to only validating resolution

        #####################################################################################
        ####################################### YZ scanning #################################
        #####################################################################################

        yz_scan_widgets_left_x_justify = 255

        # scan widget 3 "YZ"
        scan_widget_3 = QLabel("YZ scan", self)
        scan_widget_3.setParent(self.left_window)
        scan_widget_3.move(265 + 14, indiv_scan_labels_y_height + overall_y_adjust)

        # resolution
        yz_scan_resolution_widget = QLabel("Res:", self) # widget
        yz_scan_resolution_widget.setParent(self.left_window)
        yz_scan_resolution_widget.move(yz_scan_widgets_left_x_justify, 40 + row_y_adjust + overall_y_adjust)

        yz_scan_resolution_qlineedit = QLineEdit(self) # qclineedit
        yz_scan_resolution_qlineedit.setParent(self.left_window)
        yz_scan_resolution_qlineedit.move(25 + yz_scan_widgets_left_x_justify, 40 + row_y_adjust + overall_y_adjust)
        yz_scan_resolution_qlineedit.resize(55, 15)
        yz_scan_resolution_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        # read time
        yz_scan_read_time_widget = QLabel("APD_t:", self) # widget
        yz_scan_read_time_widget.setParent(self.left_window)
        yz_scan_read_time_widget.move(yz_scan_widgets_left_x_justify, 65 + row_y_adjust + overall_y_adjust)

        yz_scan_read_time_qlineedit = QLineEdit(self) # qclineedit
        yz_scan_read_time_qlineedit.setParent(self.left_window)
        yz_scan_read_time_qlineedit.move(35 + yz_scan_widgets_left_x_justify, 65 + row_y_adjust + overall_y_adjust)
        yz_scan_read_time_qlineedit.resize(45, 15)
        yz_scan_read_time_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)
        
        # y voltage (min and max)
        yz_scan_y_voltage_min_widget = QLabel("y_V_min:", self) # widget
        yz_scan_y_voltage_min_widget.setParent(self.left_window)
        yz_scan_y_voltage_min_widget.move(yz_scan_widgets_left_x_justify, 90 + row_y_adjust + overall_y_adjust)

        yz_scan_y_voltage_min_qlineedit = QLineEdit(self) # qclineedit
        yz_scan_y_voltage_min_qlineedit.setParent(self.left_window)
        yz_scan_y_voltage_min_qlineedit.move(45 + yz_scan_widgets_left_x_justify, 90 + row_y_adjust + overall_y_adjust)
        yz_scan_y_voltage_min_qlineedit.resize(35, 15)
        yz_scan_y_voltage_min_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        yz_scan_y_voltage_max_widget = QLabel("y_V_max:", self) # widget
        yz_scan_y_voltage_max_widget.setParent(self.left_window)
        yz_scan_y_voltage_max_widget.move(yz_scan_widgets_left_x_justify, 115 + row_y_adjust + overall_y_adjust)

        yz_scan_y_voltage_max_qlineedit = QLineEdit(self) # qclineedit
        yz_scan_y_voltage_max_qlineedit.setParent(self.left_window)
        yz_scan_y_voltage_max_qlineedit.move(50 + yz_scan_widgets_left_x_justify, 115 + row_y_adjust + overall_y_adjust)
        yz_scan_y_voltage_max_qlineedit.resize(30, 15)
        yz_scan_y_voltage_max_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        # x voltage single setting
        yz_scan_x_voltage_widget = QLabel("x_V:", self) # widget
        yz_scan_x_voltage_widget.setParent(self.left_window)
        yz_scan_x_voltage_widget.move(yz_scan_widgets_left_x_justify, 140 + row_y_adjust + overall_y_adjust)

        yz_scan_x_voltage_qlineedit = QLineEdit(self) # qclineedit
        yz_scan_x_voltage_qlineedit.setParent(self.left_window)
        yz_scan_x_voltage_qlineedit.move(25 + yz_scan_widgets_left_x_justify, 140 + row_y_adjust + overall_y_adjust)
        yz_scan_x_voltage_qlineedit.resize(55, 15)
        yz_scan_x_voltage_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)
                                
        # z piezo (min and max)
        yz_scan_z_piezo_min_voltage_widget = QLabel("z_V_min:", self) # widget
        yz_scan_z_piezo_min_voltage_widget.setParent(self.left_window)
        yz_scan_z_piezo_min_voltage_widget.move(yz_scan_widgets_left_x_justify, 165 + row_y_adjust + overall_y_adjust)

        yz_scan_z_piezo_min_voltage_qlineedit = QLineEdit(self) # qclineedit
        yz_scan_z_piezo_min_voltage_qlineedit.setParent(self.left_window)
        yz_scan_z_piezo_min_voltage_qlineedit.move(45 + yz_scan_widgets_left_x_justify, 165 + row_y_adjust + overall_y_adjust)
        yz_scan_z_piezo_min_voltage_qlineedit.resize(35, 15)
        yz_scan_z_piezo_min_voltage_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        yz_scan_z_piezo_max_voltage_widget = QLabel("z_V_max:", self) # widget
        yz_scan_z_piezo_max_voltage_widget.setParent(self.left_window)
        yz_scan_z_piezo_max_voltage_widget.move(yz_scan_widgets_left_x_justify, 190 + row_y_adjust + overall_y_adjust)

        yz_scan_z_piezo_max_voltage_qlineedit = QLineEdit(self) # qclineedit
        yz_scan_z_piezo_max_voltage_qlineedit.setParent(self.left_window)
        yz_scan_z_piezo_max_voltage_qlineedit.move(50 + yz_scan_widgets_left_x_justify, 190 + row_y_adjust + overall_y_adjust)
        yz_scan_z_piezo_max_voltage_qlineedit.resize(30, 15)
        yz_scan_z_piezo_max_voltage_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        # run yz scan button
        yz_scan_run_button = QPushButton("run\nYZ scan", self) # button
        yz_scan_run_button.setParent(self.left_window)
        yz_scan_run_button.resize(60, 40)
        yz_scan_run_button.move(15 + yz_scan_widgets_left_x_justify, 215 + row_y_adjust + overall_y_adjust)
        yz_scan_run_button.clicked.connect(yz_scan_resolution_validation_fnc) # this framework is limited currently to only validating resolution

####################################################################### context menu ######################################################################

    def contextMenuEvent(self, event): # context (right-click) menu

        cmenu = QMenu(self)
        cmenuoneAct = cmenu.addAction("one")
        cmenutwoAct = cmenu.addAction("two")
        cmenuthreeAct = cmenu.addAction("three")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
