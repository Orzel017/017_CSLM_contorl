"""
File name: "XY_Scan_Page.py"

Contents: UI elements to control Xy image taking

Dates:
Originally created: 01-17-2023
Last modified: 02-04-2023
Original author: MDA
Last modified by: MDA

Notes:

TODO:
*Fill UI elements from previous GUI
"""

######################################################################################## start package imports ########################################################################################

import sys # generic sys module import

import path # module for accessing parent folder directories

from PyQt5.QtWidgets import (QHBoxLayout, QFrame, QLabel) # submodules from PyQt5.QtWidgets

import matplotlib # generic Matplotlib import

matplotlib.use("Qt5Agg") # tailor matplotlib package for use in PyQt5?

current_file_directory = path.Path(__file__).abspath() # access current file's directory in folder structure

sys.path.append(current_file_directory.parent.parent.parent) # append triple parent of current file (in folder structure)

from Helper_Utilities import Plotting_Setup # access Plotting_Setup file from parent directorie's subfolder

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

    self.welcome_title_widget = QLabel("XY Scan Page") # create title widget

    self.welcome_title_widget.setParent(self.xy_scan_input_left_side) # designate parent of title widget

    self.welcome_title_widget.move(100, 100) # position the title

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
