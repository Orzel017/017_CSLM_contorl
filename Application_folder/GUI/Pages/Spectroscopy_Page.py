"""
File name: "Spectroscopy_Page.py"

Contents: welcome page UI elements

Dates:
Originally created: 02-05-202
Last modifed: 02-05-2023
Original author: MDA
Last modified by: MDA

Notes:

TODO:
*Build page using Seabreeze API for data output
"""

######################################################################################## start package imports ########################################################################################

import sys # generic sys module import

import path # module for accessing parent folder directories

from PyQt5.QtWidgets import (QVBoxLayout, QFrame, QLabel) # submodules from PyQt5.QtWidgets

from PyQt5.QtGui import QFont # submodule from PyQt5.QtGui

import matplotlib # generic Matplotlib import

matplotlib.use("Qt5Agg") # tailor matplotlib package for use in PyQt5?

current_file_directory = path.Path(__file__).abspath() # access current file's directory in folder structure

sys.path.append(current_file_directory.parent.parent.parent) # append triple parent of current file (in folder structure)

from Helper_Utilities import Plotting_Setup # access Plotting_Setup file from parent directorie's subfolder

########################################################################################## end package imports ########################################################################################

def build_spectroscopy_page(self): # define build_spectroscopy_page to setup the spectroscopy page UI elements

    ##################################################################################### start create layout #########################################################################################

    self.behind_layout = QVBoxLayout() # create a QVBoxLayout

    self.behind_layout.setSpacing(1) # control space between widgets

    self.behind_layout.setContentsMargins(0, 0, 0, 0) # control margin between widgets(for on background widget spacing)

    ##################################################################################### end create layout ###########################################################################################

    ######################################################################################## start frames #############################################################################################

    # creating two QFrames
    self.spectrometer_input_control_upper = QFrame() # create top
    self.spectrometer_output_lower = QFrame() # create bottom

    self.spectrometer_input_control_upper.setFixedHeight(100) # adjust height of top frame

    # adding widgets to background QFrames
    self.behind_layout.addWidget(self.spectrometer_input_control_upper) # top
    self.behind_layout.addWidget(self.spectrometer_output_lower) # bottom

    # frame edge styling
    self.spectrometer_input_control_upper.setFrameShape(QFrame.StyledPanel) # top
    self.spectrometer_output_lower.setFrameShape(QFrame.StyledPanel) # bottom

    ######################################################################################### end frames ##############################################################################################

    ###################################################################################### start contents #############################################################################################

    # title widget
    self.spectroscopy_page_title_widget = QLabel("Spectrometer Interface:") # create the spectrometer interface title widget

    self.spectroscopy_page_title_widget.setFont(QFont("Times", 8)) # adjust font size of title widget

    self.spectroscopy_page_title_widget.setParent(self.spectrometer_input_control_upper) # designate parent of title widget

    self.spectroscopy_page_title_widget.move(10, 10) # position the title

    # sudo-global variables
    control_widgets_upper_justification_modifer = 25

    control_widgets_left_justification_modifer = 3

    #################################################################################### start control area ###########################################################################################

    ##################################################################################### end control area ############################################################################################

    ####################################################################################### start plot area ###########################################################################################

    # dimensions of plot area
    spectrometer_output_plot_width = 9.29 # designtate the set width of output plot area

    spectrometer_output_plot_height = 4.0 # designtate the set height of output plot area

    self.spectrometer_output_plot_area = Plotting_Setup.MatPlotLib_Canvas(self, canvas_width = spectrometer_output_plot_width, canvas_height = spectrometer_output_plot_height,
                                                             canvas_dpi = 100) # create plot area from MatPlotLib_Canvas class

    self.spectrometer_output_plot_area.move(1, 1) # adjust spacing to match output lower QFrame

    self.spectrometer_output_plot_area.setParent(self.spectrometer_output_lower) # designate parent of plot area widget

    # set sizes of initial axes labels
    self.spectrometer_output_plot_area.axes.xaxis.set_tick_params(labelsize = 6) # x-axis
    self.spectrometer_output_plot_area.axes.yaxis.set_tick_params(labelsize = 6) # y-axis

    ######################################################################################## end plot area ############################################################################################

    ####################################################################################### end contents ##############################################################################################

    ##################################################################################### start finalize page #########################################################################################

    self.Spectroscopy_page.setLayout(self.behind_layout) # display spectroscopy page UI elements

    ##################################################################################### end finalize page ###########################################################################################
