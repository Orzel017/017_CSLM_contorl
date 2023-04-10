"""
File name: "Broad_Band_Light_Control_Page.py"

Contents: UI elements to communicate witht eh borad band light source

Dates:
Originally created: 04-09-2023
Last modifed: 04-09-2023
Original author: MDA
Last modified by: MDA

Notes:

TODO:

"""

######################################################################################## start package imports ########################################################################################

from PyQt5.QtWidgets import (QVBoxLayout, QFrame, QLabel) # submodules from PyQt5.QtWidgets

from PyQt5.QtGui import QFont # submodule from PyQt5.QtGui

########################################################################################## end package imports ########################################################################################

def build_broad_band_light_source_control_page(self): # define build_broad_band_light_source_control_page to setup the broad band light source control UI elements

    ##################################################################################### start create layout #########################################################################################

    self.behind_layout = QVBoxLayout() # create a QVBoxLayout

    self.behind_layout.setSpacing(1) # control space between widgets

    self.behind_layout.setContentsMargins(0, 0, 0, 0) # control margin between widgets(for on background widget spacing)

    ##################################################################################### end create layout ###########################################################################################

    ######################################################################################## start frames #############################################################################################

    # creating two QFrames
    self.welcome_background_frame_top = QFrame() # create top
    self.welcome_background_frame_bottom = QFrame() # create bottom

    self.welcome_background_frame_top.setFixedHeight(500) # adjust height of top frame

    # adding widgets to background QFrames
    self.behind_layout.addWidget(self.welcome_background_frame_top) # top
    self.behind_layout.addWidget(self.welcome_background_frame_bottom) # bottom

    # frame edge styling
    self.welcome_background_frame_top.setFrameShape(QFrame.StyledPanel) # top
    self.welcome_background_frame_bottom.setFrameShape(QFrame.StyledPanel) # bottom

    ######################################################################################### end frames ##############################################################################################

    ###################################################################################### start contents #############################################################################################
    
    

    ####################################################################################### end contents ##############################################################################################

    ##################################################################################### start finalize page #########################################################################################

    self.Broad_band_light_source_control_page.setLayout(self.behind_layout) # display broad band light source control page UI elements

    ##################################################################################### end finalize page ###########################################################################################
