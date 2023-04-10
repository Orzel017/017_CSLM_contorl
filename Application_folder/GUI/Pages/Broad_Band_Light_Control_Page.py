"""
File name: "Broad_Band_Light_Control_Page.py"

Contents: UI elements to communicate witht eh borad band light source

Dates:
Originally created: 04-09-2023
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

"""
# -*- coding: utf-8 -*-
"""
# Example of C Libraries for TLUP in Python 3 with CTypes

"""
import os
import time
from ctypes import *

lib = cdll.LoadLibrary("Application_folder\Libraries\TLUP_64.dll")

deviceCount = c_uint32()
lib.TLUP_findRsrc(0,byref(deviceCount))
print("devices found: " + str(deviceCount.value))

LEDName = create_string_buffer(256)
lib.TLUP_getRsrcName(0, 0, LEDName)

upled_handle=c_int(0)
res=lib.TLUP_init(LEDName.value, 0, 0, byref(upled_handle))

currentsetpoint=c_double(0.4) # current setpoint in Ampere
lib.TLUP_setLedCurrentSetpoint(upled_handle,currentsetpoint)

lib.TLUP_switchLedOutput(upled_handle, 1)
print("finished")
# lib.TLUP_switchLedOutput(upled_handle,1)
# time.sleep(3)
# lib.TLUP_switchLedOutput(upled_handle,0)

# lib.TLUP_close(upled_handle)

"""
