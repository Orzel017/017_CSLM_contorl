"""
File name: "Welcome_Page.py"

Contents: welcome page UI elements

Dates:
Originally created: 01-14-2023
Last modifed: 04-10-2023
Original author: MDA
Last modified by: MDA

Notes:

TODO:

"""

######################################################################################## start package imports ########################################################################################

from PyQt5.QtWidgets import (QVBoxLayout, QFrame, QLabel) # submodules from PyQt5.QtWidgets

from PyQt5.QtGui import QFont # submodule from PyQt5.QtGui

########################################################################################## end package imports ########################################################################################

def build_welcome_page(self): # define build_welcome_page to setup the welcome UI elements

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
    y_axis_offset_temp = -75

    # welcome widget (QLabel)
    self.application_welcome_widget = QLabel("Welcome to:", self) # create welcome widget

    self.application_welcome_widget.setParent(self.welcome_background_frame_top) # designate parent of welcome widget to top frame

    self.application_welcome_widget.setFont(QFont("Times", 12)) # set font and font size of welcome widget

    self.application_welcome_widget.move(397, 62 - y_axis_offset_temp) # position the welcome widget

    # title widget: (QLabel)
    self.welcome_title_widget = QLabel("MDA b017 GUI") # create the title widget (application name)

    self.welcome_title_widget.setParent(self.welcome_background_frame_top) # designate parent of title widget

    self.welcome_title_widget.setFont(QFont("Amagro", 38)) # set font of welcome page title widget

    self.welcome_title_widget.move(280, 80 - y_axis_offset_temp) # position the title
    
    # version widget (QLabel)
    self.application_version_widget = QLabel("Version:") # create the version QLabel

    self.application_version_widget.setParent(self.welcome_background_frame_top) # designate the parent of the version widget (top window)

    self.application_version_widget.setFont(QFont("Times", 11)) # set the font and font size of the version widget

    self.application_version_widget.move(401, 135 - y_axis_offset_temp) # position the version widget

    # version number widget: (QLabel)
    self.application_version_number_widget = QLabel("0.0") # create a version number widget (QLabel)

    self.application_version_number_widget.setParent(self.welcome_background_frame_top) # designate the parent of the version number widget

    self.application_version_number_widget.setFont(QFont("Arial", 11)) # set the font and font size of the version number widget

    self.application_version_number_widget.move(456, 138 - y_axis_offset_temp) # position the version number widget

    # developed by widget: (QLabel)
    self.developed_by_widget = QLabel("Developed by: Miles Ackerman") # create a developed by widget (QLabel)

    self.developed_by_widget.setParent(self.welcome_background_frame_top) # designate the parent of the developed by widget

    self.developed_by_widget.setFont(QFont("Arial", 9)) # set the font and font size of the developed by widget

    self.developed_by_widget.move(360, 158 - y_axis_offset_temp) # position the developed by widget

    # pre-link GitHub widget (QLabel)
    self.GitHub_link_indication_QLabel = QLabel("Click here to visit the application's:", self)
    self.GitHub_link_indication_QLabel.setFont(QFont("Times", 8))
    self.GitHub_link_indication_QLabel.move(200 + 115, 4)
    self.GitHub_link_indication_QLabel.setParent(self.welcome_background_frame_bottom)

    # GitHub link widget
    link_to_GitHub_code_repository = "<a href=\"https://github.com/Orzel017/017_CLSM_control\">GitHub Repository</a>"
    self.take_me_to_GitHub_widget = QLabel(self)
    self.take_me_to_GitHub_widget.setText(link_to_GitHub_code_repository)
    self.take_me_to_GitHub_widget.setParent(self.welcome_background_frame_bottom)
    self.take_me_to_GitHub_widget.move(373 + 115, 4) # position the
    self.take_me_to_GitHub_widget.setFont(QFont("Times", 8))
    self.take_me_to_GitHub_widget.setOpenExternalLinks(True)

    # setting colors of background frames:

    self.welcome_background_frame_top.setStyleSheet("background-color: #f5f5f5") # set background color

    self.welcome_background_frame_bottom.setStyleSheet("background-color: #ededed") # set background color

    ####################################################################################### end contents ##############################################################################################

    ##################################################################################### start finalize page #########################################################################################

    self.Welcome_page.setLayout(self.behind_layout) # display welcome page UI elements

    ##################################################################################### end finalize page ###########################################################################################
