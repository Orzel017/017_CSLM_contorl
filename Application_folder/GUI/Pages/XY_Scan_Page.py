"""
File name: "XY_Scan_Page.py"

Contents: UI elements to control Xy image taking

Dates:
Originally created: 01-17-2023
Last modified: 04-07-2023
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

import PyQt5 # generic PyQt5 module import

from PyQt5.QtWidgets import (QHBoxLayout, QFrame, QLabel, QLineEdit, QPushButton) # submodules from PyQt5.QtWidgets

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

class test_class:

    def __init__(self):
        self.output_plot_area = output_plot_area

    def print_hello():
        print("Hello world!")

    # creating the function to take and xy iamge based on user parameters
    def run_xy_scan_script(self, parent = None): # define the function/script 

        # super().run_xy_scan_script(parent)

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

            # configuring the sampling of the digital pulse train using `cfg_implicit_timing``
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
            array_size = 300 # designate the array size for the completed image data
            data_array = numpy.zeros((array_size, array_size)) # create an empty data array according to `array_size`

            initial_x_driving_voltage = -0.15
            initial_y_driving_voltage = -0.15
            desired_end_x_mirror_voltage = 0.15
            desired_end_y_mirror_voltage = 0.15

            x_driving_voltage_to_change = round(initial_x_driving_voltage, 5)
            y_driving_voltage_to_change = round(initial_y_driving_voltage, 5)
            x_drive_voltage_step = round(((numpy.absolute(initial_x_driving_voltage)) + (desired_end_x_mirror_voltage)) / array_size, 5)
            y_drive_voltage_step = round(((numpy.absolute(initial_y_driving_voltage)) + (desired_end_y_mirror_voltage)) / array_size, 5)

            x_mirror_task.write(0.0)
            y_mirror_task.write(0.0)
            output_value = 0

            ################################################################################ end script prelimaries #######################################################################################
            from tqdm import trange
            for f in trange(array_size): # rows

                for k in range(array_size): # columns

                    counter_value = input_counter_task.read(6)[-1]
                    output_value += counter_value
                    if f % 2 != 0: # this loop populates the created xy_scan_data_array (the if else strucuture is present bc of the snaking scanning pattern)
                        data_array[f][((-k) + 1)] = (output_value - numpy.sum(data_array)) # add counter result to data array
                        output_value == 0
                        counter_value == 0
                    else:
                        if f == 0 and k == 0:
                            data_array[0][0] = output_value # add counter result to data array
                        else:
                            data_array[f][k] = (output_value - numpy.sum(data_array)) # add counter result to data array
                    output_value = 0
                    counter_value = 0

                    if f % 2 == 0: # this loop adjusts for sweeping back and forth along each alternating row
                        if k < (array_size - 1):
                            x_driving_voltage_to_change += x_drive_voltage_step # increment drive voltage forwards
                            x_driving_voltage_to_change = round(x_driving_voltage_to_change, 3)
                            x_mirror_task.write(x_driving_voltage_to_change)
                        else:
                            break
                    else:
                        if k < (array_size - 1):
                            x_driving_voltage_to_change -= x_drive_voltage_step # increment drive voltage backwards
                            x_driving_voltage_to_change = round(x_driving_voltage_to_change, 3)
                            x_mirror_task.write(x_driving_voltage_to_change)
                        else:
                            break

                if f < (array_size - 1): # this loop prevents from scanning an upper undesired row
                    y_driving_voltage_to_change += y_drive_voltage_step # increment drive voltage
                    y_mirror_task.write(y_driving_voltage_to_change)
                else:
                    break

            internal_clock_task.stop()
            input_counter_task.stop()
            x_mirror_task.stop()
            y_mirror_task.stop()
        
        # test_class.build_xy_scan_page.self.output_plot_area.axes.pcolormesh(data_array, cmap = "inferno") # plot the data array
        # self.output_plot_area.axes.pcolormesh(data_array, cmap = "inferno") # plot the data array
        # output_plot_area.axes.pcolormesh(data_array, cmap = "inferno") # plot the data array

        output_plot_area.axes.pcolormesh(data_array, cmap = "inferno") # plot the data array
        output_plot_area.figure.canvas.draw()
        output_plot_area.figure.canvas.flush_events() # this line is very important

        print("finished")

        # print(data_array)

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

        self.take_xy_image_button.clicked.connect(test_class.run_xy_scan_script)

        # old below
        # self.take_xy_image_button.clicked.connect(Helper_Functions.start_xy_image) # start the xy scan process by calling the resolution validation function
        # this framework is limited currently to only validating resolution
        # old above

        # save image data (function connection needs to be made) widget
        self.save_raw_image_data_widget = QPushButton("Save raw image data below:", self) # create the save raw image data button

        self.save_raw_image_data_widget.setParent(self.xy_scan_input_left_side) # set the "parent" bound of the save scan raw image data button

        self.save_raw_image_data_widget.resize(148, 20) # resize the save raw image data button

        self.save_raw_image_data_widget.move(control_widgets_left_justify_modifier, control_widgets_top_justify_modifier + 586) # set the position of the save raw image data button

        self.save_raw_image_data_widget.clicked.connect(GUI_Helper_Functions.print_hello_world) # temporary button print response

        # save raw image data qlineedit
        self.save_raw_image_data_qlineedit = QLineEdit(self) # create the qlineedit to save raw image data

        self.save_raw_image_data_qlineedit.setParent(self.xy_scan_input_left_side) # designate parent of the save raw image data qlineedit
        
        self.save_raw_image_data_qlineedit.resize(203, 20) # set the size of the save raw image data qlineedit

        self.save_raw_image_data_qlineedit.move(control_widgets_left_justify_modifier, 627) # set the position of the save raw image data qlineedit

        # save raw image data file extension label widget
        self.save_raw_image_data_extension_label_widget = QLabel("\".npy\"", self) # create the save raw image data extension label widget

        self.save_raw_image_data_extension_label_widget.setParent(self.xy_scan_input_left_side) # designate the parent of the save raw image data extension label widget

        self.save_raw_image_data_extension_label_widget.move(control_widgets_left_justify_modifier + 204, 627) # set the position of the save raw image data extension label widget

        ########################################################################################## end control area #######################################################################################

        ####################################################################################### start plot area ###########################################################################################

        plot_dimension_match_aspect_ratio = 6.88 # designtate fixed dimension variable for image area to be square based on set DPI -below

        # self.output_plot_area = plot
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
