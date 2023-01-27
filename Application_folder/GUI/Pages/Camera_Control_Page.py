"""
File name: "Camera_Control_Page.py"

Contents: UI elements to control the CMOS camera

Dates:
Originally created: 01-27-2023
Last modified: 01-27-2023
Original author: MDA
Last modified by: MDA

Notes:

TODO:
*ThorCam API integration
"""

######################################################################################## start package imports ########################################################################################

from PyQt5.QtWidgets import (QHBoxLayout, QFrame, QLabel) # submodules from PyQt5.QtWidgets

########################################################################################## end package imports ########################################################################################

def build_camera_control_page(self): # define build_welcome_page to setup the camera control page UI elements

    ##################################################################################### start create layout #########################################################################################

    self.behind_layout = QHBoxLayout() # create a QHBoxLayout

    self.behind_layout.setSpacing(1) # control space between widgets

    self.behind_layout.setContentsMargins(0, 0, 0, 0) # control margin between widgets(for on background widget spacing)

    ##################################################################################### end create layout ###########################################################################################

    ######################################################################################## start frames #############################################################################################

    # creating two QFrames
    self.camera_control_settings_left = QFrame() # create left
    self.camera_control_image_right = QFrame() # create right

    self.camera_control_settings_left.setFixedWidth(150)

    # adding widgets to background QFrames
    self.behind_layout.addWidget(self.camera_control_settings_left) # left
    self.behind_layout.addWidget(self.camera_control_image_right) # right

    # frame edge styling
    self.camera_control_settings_left.setFrameShape(QFrame.StyledPanel) # top
    self.camera_control_image_right.setFrameShape(QFrame.StyledPanel) # bottom

    ######################################################################################### end frames ##############################################################################################

    ###################################################################################### start contents #############################################################################################

    self.welcome_title_widget = QLabel("CMOS Camera Control Page") # create title widget

    self.welcome_title_widget.setParent(self.camera_control_image_right) # designate parent of title widget

    self.welcome_title_widget.move(450, 300) # position the title

    ####################################################################################### end contents ##############################################################################################

    ##################################################################################### start finalize page #########################################################################################

    self.Camera_control_page.setLayout(self.behind_layout) # display camera control page UI elements

    ##################################################################################### end finalize page ###########################################################################################
