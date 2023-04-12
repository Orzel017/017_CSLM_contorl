"""
File name: "Broad_Band_Light_Control_Page.py"

Contents: UI elements to communicate witht eh borad band light source

Dates:
Originally created: 04-09-2023
Last modifed: 04-12-2023
Original author: MDA
Last modified by: MDA

Notes:

TODO:

"""

######################################################################################## start package imports ########################################################################################

from PyQt5.QtWidgets import (QVBoxLayout, QFrame, QWidget, QLabel, QHBoxLayout) # submodules from PyQt5.QtWidgets

from PyQt5.QtGui import QFont # submodule from PyQt5.QtGui

from PyQt5 import QtCore

########################################################################################## end package imports ########################################################################################

def build_broad_band_light_source_control_page(self): # define build_broad_band_light_source_control_page to setup the broad band light source control UI elements

    ################################################################################## start layout setup #############################################################################################

    self.background_layout = QVBoxLayout() # create a QVBoxLayout

    self.background_layout.setSpacing(1) # control space between widgets

    self.background_layout.setContentsMargins(0, 0, 0, 0) # control margin between widgets(for on background widget spacing)

    ################################################################################## end layout setup ###############################################################################################

    ################################################################################## start window setup #############################################################################################

    # creating two QFrames
    self.broad_band_source_top_one_frame = QFrame() # create top frame
    self.broad_band_source_middle_two_frame = QFrame() # create middle frame
    self.broad_band_source_bottom_three_frame = QFrame() # create the bottom frame

    # adding widgets to background QFrames
    self.background_layout.addWidget(self.broad_band_source_top_one_frame) # top
    self.background_layout.addWidget(self.broad_band_source_middle_two_frame) # middle
    self.background_layout.addWidget(self.broad_band_source_bottom_three_frame) # bottom

    # frame edge styling
    self.broad_band_source_top_one_frame.setFrameShape(QFrame.StyledPanel) # top
    self.broad_band_source_middle_two_frame.setFrameShape(QFrame.StyledPanel) # middle
    self.broad_band_source_bottom_three_frame.setFrameShape(QFrame.StyledPanel) # bottom

    #################################################################################### end window setup #############################################################################################

    ###################################################################################### start contents #############################################################################################

    ###

    # self.container = QWidget()
    # self.container.setContentsMargins(0, 0, 0, 0)
    # # self.Thor_Labs_MBB1F_LED_sub_background_layout = QHBoxLayout(self.container)
    # self.Thor_Labs_MBB1F_LED_sub_background_layout = QHBoxLayout()
    # self.test_left_window = QFrame()
    # self.container.resize(150, 100)
    # # self.Thor_Labs_MBB1F_LED_sub_background_layout.setGeometry(QtCore.QRect(50, 50, 100, 300))
    # self.test_middle_window = QFrame()
    # self.test_right_window = QFrame()
    # self.test_middle_window.setParent(self.broad_band_source_top_one_frame)
    # # self.test_left_window.setFixedHeight(55)
    # self.Thor_Labs_MBB1F_LED_sub_background_layout.addWidget(self.test_left_window)
    # self.Thor_Labs_MBB1F_LED_sub_background_layout.addWidget(self.test_middle_window)
    # self.Thor_Labs_MBB1F_LED_sub_background_layout.addWidget(self.test_right_window)
    # self.test_left_window.setFrameShape(QFrame.StyledPanel)
    # self.container.setLayout(self.Thor_Labs_MBB1F_LED_sub_background_layout)
    # self.test_middle_window.setFrameShape(QFrame.StyledPanel)
    # self.test_right_window.setFrameShape(QFrame.StyledPanel)
    # self.Thor_Labs_MBB1F_LED_sub_background_layout.setSpacing(1) # control space between widgets
    # self.broad_band_source_top_one_frame.setLayout(self.Thor_Labs_MBB1F_LED_sub_background_layout)
    # self.Thor_Labs_MBB1F_LED_sub_background_layout.setContentsMargins(2, 45, 2, 2) # control margin between widgets(for on background widget spacing)
    # self.Thor_Labs_MBB1F_LED_sub_background_layout.SetFixedSize(100, 100)

    self.test_background_layout = QVBoxLayout()
    self.test_frame_one = QFrame()
    self.test_frame_two = QFrame()
    self.test_background_layout.addWidget(self.test_frame_one)
    self.test_background_layout.addWidget(self.test_frame_two)
    self.background_layout.addLayout(self.test_background_layout)

    ###

    # # Thor Labs MBB1F1 LED information title widget
    # self.Thor_Labs_MBB1F1_LED_information_title_widget = QLabel("Information:")
    # next

    # # Thor Labs MBB1F1 LED status title widget
    # self.Thor_Labs_MBB1F1_LED_status_title_widget = QLabel("Source status:")
    # self.Thor_Labs_MBB1F1_LED_status_title_widget.setFont(QFont("Times", 8))
    # self.Thor_Labs_MBB1F1_LED_status_title_widget.setParent(self.broad_band_source_top_one_frame)
    # self.Thor_Labs_MBB1F1_LED_status_title_widget.move(700, 20)

    # # Thor Labs MBB1F1 LED status indicator widget
    # self.Thor_Labs_MBB1F1_LED_status_indicator_widget = QLabel("OFF")
    # self.Thor_Labs_MBB1F1_LED_status_indicator_widget.setFont(QFont("Times", 10))
    # self.Thor_Labs_MBB1F1_LED_status_indicator_widget.setParent(self.broad_band_source_top_one_frame)
    # self.Thor_Labs_MBB1F1_LED_status_indicator_widget.move(720, 50)

    ###################################################################################################################################################################################################

                        # # Thor Labs MBB1F1 LED name widget
                        # self.Thor_Labs_MBB1F1_LED_name_widget = QLabel("Thor Labs MBB1F1 LED:") # create the Thor Labs MBB1F1 name widget

                        # # self.Thor_Labs_MBB1F1_LED_name_widget.setFont(QFont("Times", 8)) # adjust font size of the Thor Labs MBB1F1 name widget

                        # self.Thor_Labs_MBB1F1_LED_name_widget.setParent(self.broad_band_source_top_one_frame) # designate parent of the Thor Labs MBB1F1 name widget to (top) frame

                        # self.Thor_Labs_MBB1F1_LED_name_widget.move(3, 20) # position the Thor Labs MBB1F1 LED name  widget

                        # # title widget
                        # self.broad_band_page_title_widget = QLabel("Broad band light source management:") # create the title widget

                        # self.broad_band_page_title_widget.setFont(QFont("Times", 9)) # adjust font size of title widget

                        # self.broad_band_page_title_widget.setParent(self.broad_band_source_top_one_frame) # designate parent of title widget (top) frame

                        # # self.broad_band_page_title_widget.move(362, 0) # position the title widget
                        # self.broad_band_page_title_widget.move(50, 0) # position the title widget
                        # self.broad_band_page_title_widget.show()

    # Alt broad band source (one) two widget
    self.alt_broad_band_source_one_name_widget = QLabel("Alternate source space (2):") # create the alt broad band source one name widget

    # self.alt_broad_band_source_one_name_widget.setFont(QFont("Times", 8)) # adjust font size of the alt broad band source one name widget

    self.alt_broad_band_source_one_name_widget.setParent(self.broad_band_source_middle_two_frame) # designate parent of alt broad band source one name widget to the (middle) frame

    self.alt_broad_band_source_one_name_widget.move(3, 2) # position the alt broad band source one name widget

    ###################################################################################################################################################################################################

    # Alt broad band source (two) two widget
    self.alt_broad_band_source_two_name_widget = QLabel("Alternate source space (3):") # create the alt broad band source two name widget

    # self.alt_broad_band_source_two_name_widget.setFont(QFont("Times", 8)) # adjust font size of the alt broad band source two name widget

    self.alt_broad_band_source_two_name_widget.setParent(self.broad_band_source_bottom_three_frame) # designate parent of alt broad band source two name widget to the (bottom) frame

    self.alt_broad_band_source_two_name_widget.move(3, 2) # position the alt broad band source two name widget

    ####################################################################################### end contents ##############################################################################################

    ##################################################################################### start finalize page #########################################################################################

    self.Broad_band_light_source_control_page.setLayout(self.background_layout) # display broad band light source control page UI elements

    ##################################################################################### end finalize page ###########################################################################################

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
