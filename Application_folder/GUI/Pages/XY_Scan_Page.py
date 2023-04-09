"""
File name: "XY_Scan_Page.py"

Contents: UI elements to control Xy image taking

Dates:
Originally created: 01-17-2023
Last modified: 04-09-2023
Original author: MDA
Last modified by: MDA

Notes:

TODO:
*Fill UI elements from previous GUI
*Save raw image data button needs to be setup
*z-piezo API with ThorLabs driver needs to be setup
"""

######################################################################################## start package imports ########################################################################################

import sys # generic sys module import

import path # module for accessing parent folder directories

from tqdm import trange # import trange function for progress bars during development

import PyQt5 # generic PyQt5 module import

from PyQt5.QtWidgets import (QHBoxLayout, QFrame, QLabel, QLineEdit, QPushButton, QComboBox) # submodules from PyQt5.QtWidgets

from PyQt5.QtGui import QFont # submodule from PyQt5.QtGui

import matplotlib # generic Matplotlib import

matplotlib.use("Qt5Agg") # tailor matplotlib package for use in PyQt5?

import nidaqmx # import National Instruments (NI) DAQmx API package

import numpy # import numpy package

current_file_directory = path.Path(__file__).abspath() # access current file's directory in folder structure

sys.path.append(current_file_directory.parent.parent.parent) # append triple parent of current file (in folder structure)

from Helper_Utilities import Plotting_Setup # access Plotting_Setup file from parent directorie's subfolder

from Helper_Utilities import Helper_Functions # access Helper_Functions file from parent directorie's subfolder

from GUI_Helper_Utilities import GUI_Helper_Functions # access GUI_Helper_Functions from parent directorie's subfolder

########################################################################################## end package imports ########################################################################################

#
global global_xy_image_data_array
global_xy_image_data_array = numpy.zeros((3, 3))

class test_class:

    def __init__(self): # what is this line?

        # define variables for use in entire class (all [2] functions)
        self.output_plot_area = output_plot_area # define output_plot_area
        self.resolution_qlineedit = resolution_qlineedit # define resolution_qlineedit
        self.minimum_x_driving_voltage_qlineedit = minimum_x_driving_voltage_qlineedit # define minimum_x_driving_voltage_qlineedit
        self.maximum_x_driving_voltage_qlineedit = maximum_x_driving_voltage_qlineedit # define maximum_x_driving_voltage_qlineedit
        self.minimum_y_driving_voltage_qlineedit = minimum_y_driving_voltage_qlineedit # define minimum_y_driving_voltage_qlineedit
        self.maximum_y_driving_voltage_qlineedit = maximum_y_driving_voltage_qlineedit # define maximum_y_driving_voltage_qlineedit
        self.save_raw_image_data_qlineedit = save_raw_image_data_qlineedit # define save_raw_image_data_qlineedit
        self.global_xy_image_data_array = global_xy_image_data_array
    
    #
    def re_plot_with_pink_color_map(self, parent = None):
        print(global_xy_image_data_array)
        output_plot_area.axes.pcolormesh(global_xy_image_data_array, cmap = "pink") # plot the data array
        output_plot_area.figure.canvas.draw() # draw the actual figure
        # output_plot_area.figure.canvas.flush_events() # this line is very important and serves what purpose? This was the crux of one of the first versions of live-plotting


    # creating the function to take and xy iamge based on user parameters
    def run_xy_scan_script(self, parent = None): # define the function/script 

        """
        * old text (outdated):
        *This runs X and Y only scan. It currently creates and then populates a user defined size numpy array according to a set counter acquisition time and a motor
        step voltage setting. Additionally, the initial driving voltage for the X and Y motors can be set according to the desired scanning range. This scanning program runs in a snake
        pattern, it scan the first row left to right, moves up one row, 
        then scans right to left and continues. Alternatives would be scanning left to right, and resetting the position of the laser on the next higher row and scanning again left 
        to right OR scanning in a "circular" patter either CW or CCW from outside to inside or inside to outside. The chosen method was picked for simplicity of understanding. The 
        scanning loops are present within NI-DAQmx tasks to speed up the program. Starting and stopping a NI-DAQmx task repeatedly slows down the program dramatically. So, the 
        counter and hardware clock task are started once, then the scanning program is run, and then the counter and clock tasks are closed -un-reserving the hardware resources. 
        This cell uses the "DAQAnalogOutputs" function from a written class file at:
        C:/Users/lukin2dmaterials/miniconda3/envs/qcodes/Lib/site-packages/qcodes_contrib_drivers/drivers/NationalInstruments/class_file. Slashes are reversed to run
        """

        # setting up NI-DAQmx tasks for hardware control
        with nidaqmx.Task() as internal_clock_task, nidaqmx.Task() as input_counter_task, nidaqmx.Task() as x_mirror_task, nidaqmx.Task() as y_mirror_task:

            """
            1. the `internal_clock_task` sets up and controls the internal hardware-based clock within the cDAQ device (from the NI-9402 module)
            2. the `input_counter_task` is for taking digital input from the physical counter on the NI-9402 module
            3. the `x_mirror_task` controls the driving of the x-mirror within the galvo unit (based on the NI-9263 module)
            4. the `y_mirror_task` controls the driving of the y-mirror within the galvo unit (based on the NI-9263 module)
            """

            ################################################################ start setting up the internal hardware clock for paired counting #############################################################

            # setting up a digital pulse train channel on the NI-9402 module using `add_co_pulse_chan_freq`
            internal_clock_task.co_channels.add_co_pulse_chan_freq(
                                                                    counter = "cDAQ1Mod1/ctr1", # designate the physical channel to be used for setting up the digital pulse train

                                                                    name_to_assign_to_channel = "internal_clock_task_digital_pulse_train", # give a name to the digtial pulse train channel

                                                                    units = nidaqmx.constants.FrequencyUnits.HZ, # set the units for the remaining input arguments to be in Hertz

                                                                    idle_state = nidaqmx.constants.Level.LOW, # designate the idle state of the digital pulse train channel to logic low

                                                                    initial_delay = 0.0, # incorporate a zero inital delay to the digitla pusle train

                                                                    freq = 1000, # set the frequency of pulses

                                                                    duty_cycle = 0.9 # set the duty cycle of pulses
                                                                    )

            # configuring the sampling of the digital pulse train using `cfg_implicit_timing`
            internal_clock_task.timing.cfg_implicit_timing(
                                                            sample_mode = nidaqmx.constants.AcquisitionType.FINITE, # setting the acquisition mode to a finite number of samples

                                                            samps_per_chan = 10000000 # when using the `FINITE` acquisition mode this argument sets the buffer size (use large buffer)
                                                            )

            ################################################################# end setting up the internal hardware clock for paired counting ##############################################################

            ########################################################################### start setting up the counting channel #############################################################################

            # setting up an input channel for counting digital pulses based on the frequency and configuration of the internal clock defined above using `add_ci_count_edges_chan`
            input_counter_task.ci_channels.add_ci_count_edges_chan(
                                                                    counter = "cDAQ1Mod1/ctr0", # designate the physical channel to be used for counting digital pulses

                                                                    name_to_assign_to_channel = "input_counter_task_digtial_pulse_input_channel",

                                                                    edge = nidaqmx.constants.Edge.RISING, # designate the counter to count on the rising edges of incoming digital pulses

                                                                    initial_count = 0, # start the inital value of the counter to be zero

                                                                    count_direction = nidaqmx.constants.CountDirection.COUNT_UP # setup the counter to count upwards (increasing)
                                                                    )

            # configure the sampling of the incoming pulses using `cfg_samp_clk_timing`
            input_counter_task.timing.cfg_samp_clk_timing(
                                                            rate = 10000000, # specifiy the sampling rate for counting incoming pulses in Hertz

                                                            # pair the internal clock defined above as the `internal_clock_task` to the counting channel defiend above as `input_counter_task`
                                                            source = "/cDAQ1/Ctr1InternalOutput",

                                                            active_edge = nidaqmx.constants.Edge.RISING, # set the counter to count on the rising edges of incoming digital pulses

                                                            sample_mode = nidaqmx.constants.AcquisitionType.FINITE, # configure the counter to acquire a finite number of samples

                                                            samps_per_chan = 10000000 # when acquiring a `FINITE` number of samples this argument sets the buffer size (use large buffer)
                                                            )
            
            ############################################################################ end setting up the counting channel ##############################################################################

            # setup the NI-9263 module and associated channels for analog voltage:
            x_mirror_task.ao_channels.add_ao_voltage_chan("cDAQ1Mod2/ao0") # add the analog voltage output channel for the x-mirror

            y_mirror_task.ao_channels.add_ao_voltage_chan("cDAQ1Mod2/ao1") # add the analog voltage output channel for the y-mirror

            ############################################################################## start script prelimaries #######################################################################################

            # start NI-9263 module tasks:
            x_mirror_task.start() # start the x-mirror task
            y_mirror_task.start() # start the y-mirror task

            # start NI-9402 module tasks:
            internal_clock_task.start() # start the internal_clock_task
            input_counter_task.start() # start the input_counter_task

            # setup the data array for populating with image data
            
            global_xy_image_data_array = numpy.zeros((3, 3))
            array_size = int(resolution_qlineedit.text()) # designate the array size based on user qlineedit input for the completed image data
            data_array = numpy.zeros((array_size, array_size)) # create an empty data array according to `array_size`

            # gather voltage data (to later be changed to distance data -requiring a formula) from user-input for driving galvo mirrors
            initial_x_driving_voltage = round(float(minimum_x_driving_voltage_qlineedit.text()), 3)
            initial_y_driving_voltage = round(float(minimum_y_driving_voltage_qlineedit.text()), 3)
            desired_end_x_mirror_voltage = round(float(maximum_x_driving_voltage_qlineedit.text()), 3)
            desired_end_y_mirror_voltage = round(float(maximum_y_driving_voltage_qlineedit.text()), 3)

            # setting desired stepping voltages for driving the galvo mirrors
            x_driving_voltage_to_change = round(initial_x_driving_voltage, 5)
            y_driving_voltage_to_change = round(initial_y_driving_voltage, 5)
            x_drive_voltage_step = round(((numpy.absolute(initial_x_driving_voltage)) + (desired_end_x_mirror_voltage)) / array_size, 5)
            y_drive_voltage_step = round(((numpy.absolute(initial_y_driving_voltage)) + (desired_end_y_mirror_voltage)) / array_size, 5)

            # zero-galvo section (to later be implemented via another script)
            x_mirror_task.write(0.0)
            y_mirror_task.write(0.0)

            output_value = 0

            ################################################################################ end script prelimaries #######################################################################################

            for row_iterator in trange(array_size): # loop/iterate over the desired number of rows
                
                for column_iterator in range(array_size): # loop/iterate over the desired number of columns
                    
                    # reading the (current) counter value
                    counter_value = input_counter_task.read(9)[-1] # read the actual and current counter value. This line is very important
                    # six is fast; and might cause problem

                    output_value += counter_value # increment the output value (to be used in the data array)

                    if row_iterator % 2 != 0: # this loop populates the created xy_scan_data_array (the if else strucuture is present bc of the snaking scanning pattern)

                        data_array[row_iterator][((-column_iterator) + 1)] = (output_value - numpy.sum(data_array)) # add counter result to data array

                        output_value == 0
                        counter_value == 0

                    else:
                        if row_iterator == 0 and column_iterator == 0:
                            data_array[0][0] = output_value # add counter result to data array

                        else:
                            data_array[row_iterator][column_iterator] = (output_value - numpy.sum(data_array)) # add counter result to data array
                        
                    output_value = 0
                    counter_value = 0

                    if row_iterator % 2 == 0: # this loop adjusts for sweeping back and forth along each alternating row

                        if column_iterator < (array_size - 1):

                            x_driving_voltage_to_change += x_drive_voltage_step # increment drive voltage forwards
                            x_driving_voltage_to_change = round(x_driving_voltage_to_change, 3)
                            x_mirror_task.write(x_driving_voltage_to_change)

                        else:
                            break

                    else:
                        if column_iterator < (array_size - 1):

                            x_driving_voltage_to_change -= x_drive_voltage_step # increment drive voltage backwards
                            x_driving_voltage_to_change = round(x_driving_voltage_to_change, 3)
                            x_mirror_task.write(x_driving_voltage_to_change)

                        else:
                            break
                
                # update plot here
                output_plot_area.axes.cla()
                output_plot_area.axes.pcolormesh(data_array, cmap = "inferno") # plot the data array
                output_plot_area.figure.canvas.draw() # draw the actual figure
                output_plot_area.figure.canvas.flush_events()

                if row_iterator < (array_size - 1): # this loop prevents from scanning an upper undesired row

                    y_driving_voltage_to_change += y_drive_voltage_step # increment drive voltage
                    y_mirror_task.write(y_driving_voltage_to_change)

                else:
                    break
            
            # stopping the NI-DAQmx tasks (all of them used above)
            internal_clock_task.stop() # stop the internal clock task within the cDAQ module
            input_counter_task.stop() # stop the input counter task -cease collecting data even though input voltage stream is always available

            x_mirror_task.stop() # stop the x-mirror task
            y_mirror_task.stop() # stop the y-mirror task

        # plot the completed data array

        global_xy_image_data_array += data_array

        output_plot_area.axes.pcolormesh(global_xy_image_data_array, cmap = "inferno") # plot the data array -using the defined colormap
        output_plot_area.figure.canvas.draw() # draw the actual figure
        output_plot_area.figure.canvas.flush_events() # this line is very important and serves what purpose? This was the crux of one of the first versions of live-plotting
        print(global_xy_image_data_array)
    # print(global_xy_image_data)
    
    def build_xy_scan_page(self, parent = None): # define build_welcome_page to setup the xy scan page UI elements

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
        global resolution_qlineedit # set gloabl qlineedit widget for use in other function on this page

        resolution_qlineedit = QLineEdit(self) # create resolution qlineedit

        resolution_qlineedit.setParent(self.xy_scan_input_left_side) # designate parent of resolution qlineedit

        resolution_qlineedit.move(control_widgets_left_justify_modifier + 60, control_widgets_top_justify_modifier) # position resolution qlineedit

        resolution_qlineedit.resize(40, 15) # resize resolution qlineedit

        resolution_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight) # align input text to right-side

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

        self.minimum_x_driving_voltage_widget.setFont(QFont("Times", 8))

        # minimum x driving voltage qlineedit
        global minimum_x_driving_voltage_qlineedit

        minimum_x_driving_voltage_qlineedit = QLineEdit(self) # create minimum x driving voltage qlineedit

        minimum_x_driving_voltage_qlineedit.setParent(self.xy_scan_input_left_side) # designated parent of minimum x driving voltage qlineedit

        minimum_x_driving_voltage_qlineedit.move(control_widgets_left_justify_modifier + 74, control_widgets_top_justify_modifier + 42) # position minimum x driving voltage qlineedit

        minimum_x_driving_voltage_qlineedit.resize(40, 15) # set size of minimum x driving voltage qlineedit

        minimum_x_driving_voltage_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight) # align input text to right-side

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
        global maximum_x_driving_voltage_qlineedit

        maximum_x_driving_voltage_qlineedit = QLineEdit(self) # create maximum x driving voltage qlineedit

        maximum_x_driving_voltage_qlineedit.setParent(self.xy_scan_input_left_side) # designated parent of maximum x driving voltage qlineedit

        maximum_x_driving_voltage_qlineedit.move(control_widgets_left_justify_modifier + 74, control_widgets_top_justify_modifier + 67) # position maximum x driving voltage qlineedit

        maximum_x_driving_voltage_qlineedit.resize(40, 15) # set size of maximum x driving voltage qlineedit

        maximum_x_driving_voltage_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight) # align input text to right-side

        # maximum x driving voltage unit label widget
        self.maximum_x_driving_voltage_unit_label_widget = QLabel("volts", self) # create maximum x driving voltage unit label widget

        self.maximum_x_driving_voltage_unit_label_widget.setFont(QFont("Times", 8)) # adjust font size of maximum x driving voltage unit label widget

        self.maximum_x_driving_voltage_unit_label_widget.setParent(self.xy_scan_input_left_side) # designate parent of maximum x driving voltage unit label widget

        self.maximum_x_driving_voltage_widget.setFont(QFont("Times", 8))

        # position maximum x driving voltage unit label widget
        self.maximum_x_driving_voltage_unit_label_widget.move(control_widgets_left_justify_modifier + 118, control_widgets_top_justify_modifier + 67)

        # minimum x driving voltage widget
        self.minimum_y_driving_voltage_widget = QLabel("Min y-voltage:", self) # create minimum y driving voltage widget

        self.minimum_y_driving_voltage_widget.setParent(self.xy_scan_input_left_side) # designate parent of minimum y driving voltage widget

        self.minimum_y_driving_voltage_widget.move(control_widgets_left_justify_modifier, control_widgets_top_justify_modifier + 93) # position minimum y driving voltage widget

        self.minimum_y_driving_voltage_widget.setFont(QFont("Times", 8))

        # minimum y driving voltage qlineedit
        global minimum_y_driving_voltage_qlineedit

        minimum_y_driving_voltage_qlineedit = QLineEdit(self) # create minimum y driving voltage qlineedit

        minimum_y_driving_voltage_qlineedit.setParent(self.xy_scan_input_left_side) # designated parent of minimum y driving voltage qlineedit

        minimum_y_driving_voltage_qlineedit.move(control_widgets_left_justify_modifier + 74, control_widgets_top_justify_modifier + 95) # position minimum y driving voltage qlineedit

        minimum_y_driving_voltage_qlineedit.resize(40, 15) # set size of minimum y driving voltage qlineedit

        minimum_y_driving_voltage_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight) # align input text to right-side

        # minimum y driving voltage unit label widget
        self.minimum_y_driving_voltage_unit_label_widget = QLabel("volts", self) # create minimum y driving voltage unit label widget

        self.minimum_y_driving_voltage_unit_label_widget.setFont(QFont("Times", 8)) # adjust font size of minimum y driving voltage unit label widget

        self.minimum_y_driving_voltage_unit_label_widget.setParent(self.xy_scan_input_left_side) # designate parent of minimum y driving voltage unit label widget

        self.minimum_y_driving_voltage_unit_label_widget.move(control_widgets_left_justify_modifier + 118, control_widgets_top_justify_modifier + 95) # position minimum y driving voltage unit label widget

        # maximum y driving voltage widget
        self.maximum_y_driving_voltage_widget = QLabel("Max y-voltage:", self) # create maximum y driving voltage widget

        self.maximum_y_driving_voltage_widget.setParent(self.xy_scan_input_left_side) # designate parent of maximum y driving voltage widget

        self.maximum_y_driving_voltage_widget.move(control_widgets_left_justify_modifier, control_widgets_top_justify_modifier + 118) # position maximum y driving voltage widget

        self.maximum_y_driving_voltage_widget.setFont(QFont("Times", 8))

        # maximum y driving voltage qlineedit
        global maximum_y_driving_voltage_qlineedit

        maximum_y_driving_voltage_qlineedit = QLineEdit(self) # create maximum y driving voltage qlineedit

        maximum_y_driving_voltage_qlineedit.setParent(self.xy_scan_input_left_side) # designated parent of maximum y driving voltage qlineedit

        maximum_y_driving_voltage_qlineedit.move(control_widgets_left_justify_modifier + 74, control_widgets_top_justify_modifier + 120) # position maximum x driving voltage qlineedit

        maximum_y_driving_voltage_qlineedit.resize(40, 15) # set size of maximum y driving voltage qlineedit

        maximum_y_driving_voltage_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight) # align input text to right-side

        # maximum y driving voltage unit label widget
        self.maximum_y_driving_voltage_unit_label_widget = QLabel("volts", self) # create maximum y driving voltage unit label widget

        self.maximum_y_driving_voltage_unit_label_widget.setFont(QFont("Times", 8)) # adjust font size of maximum y driving voltage unit label widget

        self.maximum_y_driving_voltage_unit_label_widget.setParent(self.xy_scan_input_left_side) # designate parent of maximum y driving voltage unit label widget

        # position maximum y driving voltage unit label widget
        self.maximum_y_driving_voltage_unit_label_widget.move(control_widgets_left_justify_modifier + 118, control_widgets_top_justify_modifier + 120)

        # run take xy image button
        self.take_xy_image_button = QPushButton("Run\nXY image", self) # create a button to take xy image

        self.take_xy_image_button.setParent(self.xy_scan_input_left_side) # designate parent of take xy image button

        self.take_xy_image_button.resize(60, 40) # set size of the take xy image button

        self.take_xy_image_button.move(control_widgets_left_justify_modifier + 79, control_widgets_top_justify_modifier + 628)

        self.take_xy_image_button.clicked.connect(test_class.run_xy_scan_script)

        # save image data (function connection needs to be made) widget
        self.save_raw_image_data_widget = QPushButton("Save raw image data below:", self) # create the save raw image data button

        self.save_raw_image_data_widget.setParent(self.xy_scan_input_left_side) # set the "parent" bound of the save scan raw image data button

        self.save_raw_image_data_widget.resize(148, 20) # resize the save raw image data button

        self.save_raw_image_data_widget.move(control_widgets_left_justify_modifier, control_widgets_top_justify_modifier + 586) # set the position of the save raw image data button

        self.save_raw_image_data_widget.clicked.connect(GUI_Helper_Functions.print_hello_world) # temporary button print response

        # save raw image data qlineedit
        global save_raw_image_data_qlineedit

        save_raw_image_data_qlineedit = QLineEdit(self) # create the qlineedit to save raw image data

        save_raw_image_data_qlineedit.setParent(self.xy_scan_input_left_side) # designate parent of the save raw image data qlineedit
        
        save_raw_image_data_qlineedit.resize(203, 20) # set the size of the save raw image data qlineedit

        save_raw_image_data_qlineedit.move(control_widgets_left_justify_modifier, 627) # set the position of the save raw image data qlineedit

        # save raw image data file extension label widget
        self.save_raw_image_data_extension_label_widget = QLabel("\".npy\"", self) # create the save raw image data extension label widget

        self.save_raw_image_data_extension_label_widget.setParent(self.xy_scan_input_left_side) # designate the parent of the save raw image data extension label widget

        self.save_raw_image_data_extension_label_widget.move(control_widgets_left_justify_modifier + 204, 627) # set the position of the save raw image data extension label widget

        # change color map of plot widegt
        self.change_color_map_widget = QLabel("Change image color map:", self) # create widget to change the image's color bar

        self.change_color_map_widget.setParent(self.xy_scan_input_left_side) # designate parent of the change plot color map widget

        self.change_color_map_widget.move(control_widgets_left_justify_modifier + 38, control_widgets_top_justify_modifier + 145) # position change plot's color map widget

        self.change_color_map_widget.setFont(QFont("Times", 8))

        # position adjust variables changing image color maps:
        changing_color_map_button_square_aspect_ratio_value = 35
        changing_color_map_button_y_adjust_value = 165

        # change color map (to pink)
        self.change_color_map_to_pink_button = QPushButton("Pink", self)
        self.change_color_map_to_pink_button.setParent(self.xy_scan_input_left_side)
        self.change_color_map_to_pink_button.resize(changing_color_map_button_square_aspect_ratio_value, changing_color_map_button_square_aspect_ratio_value)
        self.change_color_map_to_pink_button.move(control_widgets_left_justify_modifier + 40 - 3, control_widgets_top_justify_modifier + changing_color_map_button_y_adjust_value)
        self.change_color_map_to_pink_button.clicked.connect(test_class.re_plot_with_pink_color_map)

        # change color map (to Inferno)
        self.change_color_map_to_pink_Inferno = QPushButton("Inferno", self)
        self.change_color_map_to_pink_Inferno.setParent(self.xy_scan_input_left_side)
        self.change_color_map_to_pink_Inferno.resize(changing_color_map_button_square_aspect_ratio_value, changing_color_map_button_square_aspect_ratio_value)
        self.change_color_map_to_pink_Inferno.move(control_widgets_left_justify_modifier + 85 - 3, control_widgets_top_justify_modifier + changing_color_map_button_y_adjust_value)

        # change color map (to grayscale)
        self.change_color_map_to_pink_Greys = QPushButton("Greys", self)
        self.change_color_map_to_pink_Greys.setParent(self.xy_scan_input_left_side)
        self.change_color_map_to_pink_Greys.resize(changing_color_map_button_square_aspect_ratio_value, changing_color_map_button_square_aspect_ratio_value)
        self.change_color_map_to_pink_Greys.move(control_widgets_left_justify_modifier + 130 - 3, control_widgets_top_justify_modifier + changing_color_map_button_y_adjust_value)

        ########################################################################################## end control area #######################################################################################

        ####################################################################################### start plot area ###########################################################################################

        plot_dimension_match_aspect_ratio = 6.88 # designtate fixed dimension variable for image area to be square based on set DPI -below

        global output_plot_area

        output_plot_area = Plotting_Setup.MatPlotLib_Canvas(self, canvas_width = plot_dimension_match_aspect_ratio, canvas_height = plot_dimension_match_aspect_ratio,
                                                                canvas_dpi = 100) # create plot area from MatPlotLib_Canvas class

        output_plot_area.move(1, 1) # adjust spacing to match output right QFrame

        output_plot_area.setParent(self.xy_scan_output_right_side) # designate parent of plot area widget

        ######################################################################################## end plot area ############################################################################################

        ####################################################################################### end contents ##############################################################################################

        ##################################################################################### start finalize page #########################################################################################

        self.XY_scan_page.setLayout(self.behind_layout) # display xy scan page UI elements

        ##################################################################################### end finalize page ###########################################################################################
