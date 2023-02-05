"""
File name: "XY_Scan_Page.py"

Contents: UI elements to control Xy image taking

Dates:
Originally created: 01-17-2023
Last modified: 02-05-2023
Original author: MDA
Last modified by: MDA

Notes:

TODO:
*Fill UI elements from previous GUI
"""

######################################################################################## start package imports ########################################################################################

import sys # generic sys module import

import path # module for accessing parent folder directories

import PyQt5 # generic PyQt5 module import

from PyQt5.QtWidgets import (QHBoxLayout, QFrame, QLabel, QLineEdit, QPushButton) # submodules from PyQt5.QtWidgets

from PyQt5.QtGui import QFont # submodule from PyQt5.QtGui

import matplotlib # generic Matplotlib import

matplotlib.use("Qt5Agg") # tailor matplotlib package for use in PyQt5?

current_file_directory = path.Path(__file__).abspath() # access current file's directory in folder structure

sys.path.append(current_file_directory.parent.parent.parent) # append triple parent of current file (in folder structure)

from Helper_Utilities import Plotting_Setup # access Plotting_Setup file from parent directorie's subfolder

from GUI_Helper_Utilities import GUI_Helper_Functions # access GUI_Helper_Functions from parent directorie's subfolder

########################################################################################## end package imports ########################################################################################

def build_xy_scan_page(self): # define build_welcome_page to setup the xy scan page UI elements

    ##################################################################################### start create layout #########################################################################################

    self.behind_layout = QHBoxLayout() # create a QHBoxLayout

    self.behind_layout.setSpacing(1) # control space between widgets

    self.behind_layout.setContentsMargins(0, 0, 0, 0) # control margin between widgets(for on background widget spacing)

    ##################################################################################### end create layout ###########################################################################################

    ######################################################################################## start frames #############################################################################################

    # creating two QFrames
    self.xy_scan_input_left_side = QFrame() # create left
    self.xy_scan_output_right_side = QFrame() # create right

    # manual dimensions
    maintain_aspect_ratio_one_to_one_dimension = 691 # designate fixed dimension variable for image area to be square
    self.xy_scan_output_right_side.setFixedSize(maintain_aspect_ratio_one_to_one_dimension, maintain_aspect_ratio_one_to_one_dimension) # set fixed dimensions of image area

    # adding widgets to background QFrames
    self.behind_layout.addWidget(self.xy_scan_input_left_side) # left
    self.behind_layout.addWidget(self.xy_scan_output_right_side) # right

    # frame edge styling
    self.xy_scan_input_left_side.setFrameShape(QFrame.StyledPanel) # top
    self.xy_scan_output_right_side.setFrameShape(QFrame.StyledPanel) # bottom

    ######################################################################################### end frames ##############################################################################################

    ###################################################################################### start contents #############################################################################################

    # title widget
    self.title_widget = QLabel("Take XY Image:") # create title widget

    self.title_widget.setFont(QFont("Times", 8)) # adjust font size of title widget

    self.title_widget.setParent(self.xy_scan_input_left_side) # designate parent of title widget

    self.title_widget.move(82, 0) # position the title widget

    # sudo-global variables
    control_widgets_left_justify_modifier = 3 # left-justification

    control_widgets_top_justify_modifier = 20 # top-justification

    ######################################################################################### start control area ######################################################################################

    # resolution widget
    self.resolution_widget = QLabel("Resolution:", self) # create resolution widget

    self.resolution_widget.setFont(QFont("Times", 8)) # adjust font size of resolution widget

    self.resolution_widget.setParent(self.xy_scan_input_left_side) # designate parent of resolution widget

    self.resolution_widget.move(control_widgets_left_justify_modifier, control_widgets_top_justify_modifier) # position resolution widget

    # resolution QLineEdit
    self.resolution_qlineedit = QLineEdit(self) # create resolution qlineedit

    self.resolution_qlineedit.setParent(self.xy_scan_input_left_side) # designate parent of resolution qlineedit

    self.resolution_qlineedit.move(control_widgets_left_justify_modifier + 60, control_widgets_top_justify_modifier) # position resolution qlineedit

    self.resolution_qlineedit.resize(40, 15) # resize resolution qlineedit

    self.resolution_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight) # align input text to right-side

    # pixels widget
    self.pixels_widget = QLabel("pixels", self) # create resolution widget

    self.pixels_widget.setFont(QFont("Times", 8)) # adjust font size of resolution widget

    self.pixels_widget.setParent(self.xy_scan_input_left_side) # designate parent of resolution widget

    self.pixels_widget.move(control_widgets_left_justify_modifier + 105, control_widgets_top_justify_modifier) # position resolution widget

    # resolution disclaimer widget
    self.resolution_disclaimer_widget = QLabel("Note: aspect ratio is 1:1", self) # create resolution widget

    self.resolution_disclaimer_widget.setFont(QFont("Times", 8)) # adjust font size of resolution widget

    self.resolution_disclaimer_widget.setParent(self.xy_scan_input_left_side) # designate parent of resolution widget

    self.resolution_disclaimer_widget.move(control_widgets_left_justify_modifier, control_widgets_top_justify_modifier + 15) # position resolution widget

    # # read time
    # xy_scan_read_time_widget = QLabel("APD_t:", self) # widget
    # xy_scan_read_time_widget.setParent(self.left_window)
    # xy_scan_read_time_widget.move(xy_scan_widgets_left_x_justify, 65 + row_y_adjust + overall_y_adjust)

    # xy_scan_read_time_qlineedit = QLineEdit(self) # qclineedit
    # xy_scan_read_time_qlineedit.setParent(self.left_window)
    # xy_scan_read_time_qlineedit.move(40, 65 + row_y_adjust + overall_y_adjust)
    # xy_scan_read_time_qlineedit.resize(45, 15)
    # xy_scan_read_time_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)
    
    # minimum x driving voltage widget
    self.minimum_x_driving_voltage_widget = QLabel("Min x-voltage:", self) # create minimum x driving voltage widget

    self.minimum_x_driving_voltage_widget.setParent(self.xy_scan_input_left_side) # designate parent of minimum x driving voltage widget

    self.minimum_x_driving_voltage_widget.move(control_widgets_left_justify_modifier, control_widgets_top_justify_modifier + 40) # position minimum x driving voltage widget

    # minimum x driving voltage qlineedit
    self.minimum_x_driving_voltage_qlineedit = QLineEdit(self) # create minimum x driving voltage qlineedit

    self.minimum_x_driving_voltage_qlineedit.setParent(self.xy_scan_input_left_side) # designated parent of minimum x driving voltage qlineedit

    self.minimum_x_driving_voltage_qlineedit.move(control_widgets_left_justify_modifier + 74, control_widgets_top_justify_modifier + 42) # position minimum x driving voltage qlineedit

    self.minimum_x_driving_voltage_qlineedit.resize(40, 15) # set size of minimum x driving voltage qlineedit

    self.minimum_x_driving_voltage_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight) # align input text to right-side

    # minimum x driving voltage unit label widget
    self.minimum_x_driving_voltage_unit_label_widget = QLabel("volts", self) # create minimum x driving voltage unit label widget

    self.minimum_x_driving_voltage_unit_label_widget.setFont(QFont("Times", 8)) # adjust font size of minimum x driving voltage unit label widget

    self.minimum_x_driving_voltage_unit_label_widget.setParent(self.xy_scan_input_left_side) # designate parent of minimum x driving voltage unit label widget

    self.minimum_x_driving_voltage_unit_label_widget.move(control_widgets_left_justify_modifier + 118, control_widgets_top_justify_modifier + 42) # position minimum x driving voltage unit label widget

    # maximum x driving voltage widget
    self.maximum_x_driving_voltage_widget = QLabel("Max x-voltage:", self) # create maximum x driving voltage widget

    self.maximum_x_driving_voltage_widget.setParent(self.xy_scan_input_left_side) # designate parent of maximum x driving voltage widget

    self.maximum_x_driving_voltage_widget.move(control_widgets_left_justify_modifier, control_widgets_top_justify_modifier + 65) # position maximum x driving voltage widget

    # maximum x driving voltage qlineedit
    self.maximum_x_driving_voltage_qlineedit = QLineEdit(self) # create maximum x driving voltage qlineedit

    self.maximum_x_driving_voltage_qlineedit.setParent(self.xy_scan_input_left_side) # designated parent of maximum x driving voltage qlineedit

    self.maximum_x_driving_voltage_qlineedit.move(control_widgets_left_justify_modifier + 74, control_widgets_top_justify_modifier + 67) # position maximum x driving voltage qlineedit

    self.maximum_x_driving_voltage_qlineedit.resize(40, 15) # set size of maximum x driving voltage qlineedit

    self.maximum_x_driving_voltage_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight) # align input text to right-side

    # maximum x driving voltage unit label widget
    self.maximum_x_driving_voltage_unit_label_widget = QLabel("volts", self) # create maximum x driving voltage unit label widget

    self.maximum_x_driving_voltage_unit_label_widget.setFont(QFont("Times", 8)) # adjust font size of maximum x driving voltage unit label widget

    self.maximum_x_driving_voltage_unit_label_widget.setParent(self.xy_scan_input_left_side) # designate parent of maximum x driving voltage unit label widget

    # position maximum x driving voltage unit label widget
    self.maximum_x_driving_voltage_unit_label_widget.move(control_widgets_left_justify_modifier + 118, control_widgets_top_justify_modifier + 67)

    # minimum x driving voltage widget
    self.minimum_y_driving_voltage_widget = QLabel("Min y-voltage:", self) # create minimum y driving voltage widget

    self.minimum_y_driving_voltage_widget.setParent(self.xy_scan_input_left_side) # designate parent of minimum y driving voltage widget

    self.minimum_y_driving_voltage_widget.move(control_widgets_left_justify_modifier, control_widgets_top_justify_modifier + 93) # position minimum y driving voltage widget

    # minimum y driving voltage qlineedit
    self.minimum_y_driving_voltage_qlineedit = QLineEdit(self) # create minimum y driving voltage qlineedit

    self.minimum_y_driving_voltage_qlineedit.setParent(self.xy_scan_input_left_side) # designated parent of minimum y driving voltage qlineedit

    self.minimum_y_driving_voltage_qlineedit.move(control_widgets_left_justify_modifier + 74, control_widgets_top_justify_modifier + 95) # position minimum y driving voltage qlineedit

    self.minimum_y_driving_voltage_qlineedit.resize(40, 15) # set size of minimum y driving voltage qlineedit

    self.minimum_y_driving_voltage_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight) # align input text to right-side

    # minimum y driving voltage unit label widget
    self.minimum_y_driving_voltage_unit_label_widget = QLabel("volts", self) # create minimum y driving voltage unit label widget

    self.minimum_y_driving_voltage_unit_label_widget.setFont(QFont("Times", 8)) # adjust font size of minimum y driving voltage unit label widget

    self.minimum_y_driving_voltage_unit_label_widget.setParent(self.xy_scan_input_left_side) # designate parent of minimum y driving voltage unit label widget

    self.minimum_y_driving_voltage_unit_label_widget.move(control_widgets_left_justify_modifier + 118, control_widgets_top_justify_modifier + 95) # position minimum y driving voltage unit label widget

    # maximum y driving voltage widget
    self.maximum_y_driving_voltage_widget = QLabel("Max y-voltage:", self) # create maximum y driving voltage widget

    self.maximum_y_driving_voltage_widget.setParent(self.xy_scan_input_left_side) # designate parent of maximum y driving voltage widget

    self.maximum_y_driving_voltage_widget.move(control_widgets_left_justify_modifier, control_widgets_top_justify_modifier + 118) # position maximum y driving voltage widget

    # maximum y driving voltage qlineedit
    self.maximum_y_driving_voltage_qlineedit = QLineEdit(self) # create maximum y driving voltage qlineedit

    self.maximum_y_driving_voltage_qlineedit.setParent(self.xy_scan_input_left_side) # designated parent of maximum y driving voltage qlineedit

    self.maximum_y_driving_voltage_qlineedit.move(control_widgets_left_justify_modifier + 74, control_widgets_top_justify_modifier + 120) # position maximum x driving voltage qlineedit

    self.maximum_y_driving_voltage_qlineedit.resize(40, 15) # set size of maximum y driving voltage qlineedit

    self.maximum_y_driving_voltage_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight) # align input text to right-side

    # maximum y driving voltage unit label widget
    self.maximum_y_driving_voltage_unit_label_widget = QLabel("volts", self) # create maximum y driving voltage unit label widget

    self.maximum_y_driving_voltage_unit_label_widget.setFont(QFont("Times", 8)) # adjust font size of maximum y driving voltage unit label widget

    self.maximum_y_driving_voltage_unit_label_widget.setParent(self.xy_scan_input_left_side) # designate parent of maximum y driving voltage unit label widget

    # position maximum y driving voltage unit label widget
    self.maximum_y_driving_voltage_unit_label_widget.move(control_widgets_left_justify_modifier + 118, control_widgets_top_justify_modifier + 120)

    # # z piezo
    # xy_scan_z_piezo_voltage_widget = QLabel("z_V:", self) # widget
    # xy_scan_z_piezo_voltage_widget.setParent(self.left_window)
    # xy_scan_z_piezo_voltage_widget.move(xy_scan_widgets_left_x_justify, 190 + row_y_adjust + overall_y_adjust)

    # xy_scan_z_piezo_voltage_qlineedit = QLineEdit(self) # qclineedit
    # xy_scan_z_piezo_voltage_qlineedit.setParent(self.left_window)
    # xy_scan_z_piezo_voltage_qlineedit.move(30, 190 + row_y_adjust + overall_y_adjust)
    # xy_scan_z_piezo_voltage_qlineedit.resize(55, 15)
    # xy_scan_z_piezo_voltage_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

    # run take xy image button
    self.take_xy_image_button = QPushButton("Run\nXY image", self) # create a button to take xy image

    self.take_xy_image_button.setParent(self.xy_scan_input_left_side) # designate parent of take xy image button

    self.take_xy_image_button.resize(60, 40) # set size of the take xy image button

    self.take_xy_image_button.move(control_widgets_left_justify_modifier + 79, control_widgets_top_justify_modifier + 628)

    self.take_xy_image_button.clicked.connect(GUI_Helper_Functions.print_hello_world) # temporary button print response

    # self.take_xy_image_button.clicked.connect(xy_scan_resolution_validation_fnc) # this framework is limited currently to only validating resolution

    ########################################################################################## end control area #######################################################################################

    ####################################################################################### start plot area ###########################################################################################

    plot_dimension_match_aspect_ratio = 6.88 # designtate fixed dimension variable for image area to be square based on set DPI -below

    self.output_plot_area = Plotting_Setup.MatPlotLib_Canvas(self, canvas_width = plot_dimension_match_aspect_ratio, canvas_height = plot_dimension_match_aspect_ratio,
                                                             canvas_dpi = 100) # create plot area from MatPlotLib_Canvas class

    self.output_plot_area.move(1, 1) # adjust spacing to match output right QFrame

    self.output_plot_area.setParent(self.xy_scan_output_right_side) # designate parent of plot area widget

    # set sizes of initial axes labels
    self.output_plot_area.axes.xaxis.set_tick_params(labelsize = 6) # x-axis
    self.output_plot_area.axes.yaxis.set_tick_params(labelsize = 6) # y-axis

    ######################################################################################## end plot area ############################################################################################

    ####################################################################################### end contents ##############################################################################################

    ##################################################################################### start finalize page #########################################################################################

    self.XY_scan_page.setLayout(self.behind_layout) # display xy scan page UI elements

    ##################################################################################### end finalize page ###########################################################################################
