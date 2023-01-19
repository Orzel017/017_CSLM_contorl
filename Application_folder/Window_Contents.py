"""
File name: "Window_Contents.py"

Contents: main window content (curently including scanning scripts -this will be changed later as they will be moved)

Dates:
Originally separated/organized: 12-21-2022
Last modifed: 01-18-2023
Original author: MDA
Last modified by: MDA

Notes:

TODO:
*Move scanning scripts to other files (would they need to be changed to classes?)
**This presents numerous issues with data handling and transfer from file to file
"""

############################################################################################## start imports ##########################################################################################
import csv
# NI-DAQmx API imports
import nidaqmx # general API import

from nidaqmx.constants import (AcquisitionType, FrequencyUnits, CountDirection, Edge) # API constant(s) import(s)

import numpy as np # numpy for arrays

# import sys
# sys.path.insert(0, "./Application_folder/Drivers")
# import Drivers
# from Drivers import cDAQ

# from import cDAQ as test

from Drivers import cDAQ as test

# MatPlotLib plotting packages
import matplotlib # generica Matplotlib import

matplotlib.use("Qt5Agg") # tailor matplotlib package for use in PyQt5?

# datetime module
from datetime import date # date module import

# PyQt5, this is the framework that builds the GUI windows
import PyQt5 # general PyQt5 framework import

from PyQt5 import QtWidgets # QtWidgets module

from PyQt5.QtWidgets import QFrame, QTextEdit, QPushButton, QHBoxLayout, QLabel, QSplitter, QLineEdit, QMenu # submodules from QtWidgets

from PyQt5.QtGui import QFont # QFont from QtGui

from PyQt5.QtCore import Qt # Qt module from QtCore

import pyqtgraph as pg # pyqtgraph import (grphing package from PyQt)

# imports from other files within folder structure
from Plotting_Setup import MplCanvas # import MplCanvas class from "Plotting_Setup.py"

from Resolution_Error_Window import Make_Error_Window # import Make_Error_Window class from "Resolution_Error_Window.py"

from Additional_Error_Window import Make_Error_Window_2 # import Make_Error_Window_2 class from "Additional_Error_Window.py"

############################################################################################# end imports #############################################################################################

########################################################################################### start prelims #############################################################################################

get_todays_date = date.today() # this is used for creating the final plot's plot labels

todays_date = get_todays_date.strftime("%m%d%Y") # this is used for creating the final plot's plot labels

any_script_run_one_Q = False # global variable for multiple scanning

############################################################################################ end prelims ##############################################################################################

# define main window contents class
class Setup_Main_Window_Contents(QtWidgets.QWidget):#, **kwargs): # kwargs needed?

    # define main window contents object?
    def __init__(self, parent = None):#, **kwargs): # kwargs needed?

        super().__init__(parent) # inheritance?

        self.hbox = QHBoxLayout(self)

        plotwin = pg.GraphicsLayoutWidget(show = True)

        ####################################################################### Setup_Main_Window_Contents functions ##################################################################################
        
        def zero_galvo_function():
            zero_galvo_card_name = "cDAQ1Mod2"
            zero_galvo_ao_channels = {f"{zero_galvo_card_name}/ao{i}": i for i in range(4)}
            zero_galvo = test.DAQAnalogOutputs("zero_galvo_name", zero_galvo_card_name, zero_galvo_ao_channels)
            zero_galvo.voltage_cdaq1mod2ao0(0.0)
            zero_galvo.voltage_cdaq1mod2ao0(0.0)
            zero_galvo.close()

        ########## overall #################

        # display invalid resolution error window fnc
        def display_resolution_error_window_fnc(): # this fnc calls the "Make_Error_Window" class to display an eror message indicating user input is not validated
            self.Make_Error_Window = Make_Error_Window()
            self.Make_Error_Window.show()

        # display invalid saving address error window fnc   
        def display_save_address_length_error_window_fnc(): # this fnc calls the "Make_Error_Window" class to display an eror message indicating user input is not validated
            self.Make_Error_Window_2 = Make_Error_Window_2()
            self.Make_Error_Window_2.show()

        # save most recent scan data fnc
        def save_scan_data_fnc(): # this fnc works for any scanning script

            """
            How this works/applies to each scanning script:
            In any scanning script (XY, XZ, and YZ), a data_array is created according to the user-specified grid_size. It is a Numpy array of zeros that will be
            populated throughout the scanning program as it progresses. At the same time of that data-array created a global variable called "most_recent_data_array"
            is created and is then set to the same size matching the scan-specific data_array. At the end of the scanning scipt this temporary data array is matched to
            the scan's specific data array, value for value. Now "most_recent-data_array" is called (since it is defined to be Global) below for saving. This
            """

            saving_scan_error_bool = False # setting up a bool value for error checking below

            print("save_scan_data_fnc called")                                               # delete later
            print("@address :" + save_scan_data_qlineedit.text())                                               # delete later

            # while loop for error checking if address to save data at has length > 0
            while saving_scan_error_bool is False:

                if len(str(save_scan_data_qlineedit.text())) == 0: # checking if length of specified saving address is > 0

                    # print("EXCEPTION!")                                                       # safe to delete
                    display_save_address_length_error_window_fnc()                              # fix to new window. Only a test now
                    break # condition remains False; not saved; exit

                elif len(str(save_scan_data_qlineedit.text())) > 0: # checking the length of the specified address is greater than 0

                    saving_scan_error_bool == True # adjusting the value of the current bool to True
                    address_to_save_scan_data_at = save_scan_data_qlineedit.text() # creating a variable as the specified (now error-checked) address
                    np.save(str(address_to_save_scan_data_at), most_recent_data_array) # saving the correct data array
                    print("saved")
                    break # data has been successfully save; so exit checking loop

        ########### XY scanning #############
        # print/display XY scan parameters fnc
        def print_XY_scan_parameters_fnc(self, parent = Setup_Main_Window_Contents): # this fnc does...

            # print("XY_SCAN PARAMETERS/INFO: ", end = "")                                    # this prints to the terminal
            # print("XY_scan resolution = %d, " % int(xy_scan_resolution_qlineedit.text()), end = "")
            # print("XY_scan counter read time = %2f, " % round(float(xy_scan_read_time_qlineedit.text()), 2), end = "")
            # print("XY_scan min x driving voltage = %2f, " % float(xy_scan_x_voltage_min_qlineedit.text()), end = "")
            # print("XY_scan max x driving voltage = %2f, " % float(xy_scan_x_voltage_max_qlineedit.text()), end = "")
            # print("XY_scan min y driving voltage = %2f, " % float(xy_scan_y_voltage_min_qlineedit.text()), end = "")
            # print("XY_scan max y driving voltage = %2f, " % float(xy_scan_y_voltage_max_qlineedit.text()), end = "")
            # print("XY_scan z-piezo driving voltage = %2f." % float(xy_scan_z_piezo_voltage_qlineedit.text()))

            # need to clear text box first
            parameters_dsiplay_text_box.clear()

            # this prints to the QTextBox in the left_window. The output of the user-selected scan parameters is printed below
            parameters_dsiplay_text_box.setPlainText(
                                                        "XY_SCAN PARAMETERS/INFO:\n"
                                                        "XY_scan resolution = " + str(int(xy_scan_resolution_qlineedit.text())) + "\n"
                                                        "XY_scan counter read time = " + str(float(xy_scan_read_time_qlineedit.text())) + "\n"
                                                        "XY_scan min x driving voltage = " + str(float(xy_scan_x_voltage_min_qlineedit.text())) + "\n"
                                                        "XY_scan max x driving voltage = " + str(float(xy_scan_x_voltage_max_qlineedit.text())) + "\n"
                                                        "XY_scan min y driving voltage = " + str(float(xy_scan_y_voltage_min_qlineedit.text())) + "\n"
                                                        "XY_scan max y driving voltage = " + str(float(xy_scan_y_voltage_max_qlineedit.text())) + "\n"
                                                        "XY_scan z-piezo driving voltage = " + str(float(xy_scan_z_piezo_voltage_qlineedit.text()))
                                                        )
    ##############################################################################################################################################################################################################################################
        # run XY scanning function
        def run_xy_scan_fnc(): # this fnc runs the xy_scan per the user-entered parameters in the xy_scan qlineedits

            """
            This runs X and Y only scan. It currently creates and then populates a user defined size numpy array according to a set counter acquisition time and a motor
step voltage setting. Additionally, the initial driving voltage for the X and Y motors can be set according to the desired scanning range. This scanning program runs in a snake pattern, it scan the first row left to right, moves up one row, 
then scans right to left and continues. Alternatives would be scanning left to right, and resetting the position of the laser on the next higher row and scanning again left 
to right OR scanning in a "circular" patter either CW or CCW from outside to inside or inside to outside. The chosen method was picked for simplicity of understanding. The 
scanning loops are present within NI-DAQmx tasks to speed up the program. Starting and stopping a NI-DAQmx task repeatedly slows down the program dramatically. So, the 
counter and hardware clock task are started once, then the scanning program is run, and then the counter and clock tasks are closed -un-reserving the hardware resources. 
This cell uses the "DAQAnalogOutputs" function from a written class file at:
C:/Users/lukin2dmaterials/miniconda3/envs/qcodes/Lib/site-packages/qcodes_contrib_drivers/drivers/NationalInstruments/class_file. Slashes are reversed to run
            """

            ############################################################### begin scanning script #############################################################################################
            
            my_file = open("data_file.csv", "w", encoding="UTF8") # open the file in the write mode

            writer = csv.writer(my_file) # make the writer?

            ################################################################################## card 2 (AO) ########################################################################

            # naming the instrument
            scan_galvo_card_name = "cDAQ1Mod2"

            # dictionary of analog output channels
            scan_galvo_ao_channels = {f'{scan_galvo_card_name}/ao{i}': i for i in range(4)}

            # defining the instrument (ni_9263)
            scan_galvo = test.DAQAnalogOutputs("name_two", scan_galvo_card_name, scan_galvo_ao_channels)

            ############################################################################### def other variables ####################################################################

            ################### setting variales and array ####################

            # counter read time:
            # scan_counter_acquisition_time = float(xy_scan_read_time_qlineedit.text())                          # note a reading time <0.05 s is likely too short
            scan_counter_acquisition_time = 0.05

            # def
            grid_size = int(xy_scan_resolution_qlineedit.text())
            # grid_size = 3
            grid_size_x = grid_size_y = grid_size

            # def the initial driving voltage for the x-mirror
            # initial_x_driving_voltage = round(float(xy_scan_x_voltage_min_qlineedit.text()), 2)
            initial_x_driving_voltage = -0.1
            # def the initial driving voltage for the y-mirror
            # initial_y_driving_voltage = round(float(xy_scan_y_voltage_min_qlineedit.text()), 2)
            initial_y_driving_voltage = -0.1

            # z_piezo_set_voltage = round(float(xy_scan_z_piezo_voltage_qlineedit.text()), 2)
            z_piezo_set_voltage = 0.0

            # setup parameter for the program to use based on defined variables
            x_driving_voltage_to_change = initial_x_driving_voltage
            y_driving_voltage_to_change = initial_y_driving_voltage

            # set desired end mirror voltages
            # desired_end_x_mirror_voltage = round(float(xy_scan_x_voltage_max_qlineedit.text()), 2)
            desired_end_x_mirror_voltage = 0.1
            # desired_end_y_mirror_voltage = round(float(xy_scan_y_voltage_max_qlineedit.text()), 2)
            desired_end_y_mirror_voltage = 0.1

            # def the internal stepping voltages based on user-entered settings above
            x_drive_voltage_step = ((np.absolute(initial_x_driving_voltage)) + (desired_end_x_mirror_voltage)) / grid_size_x
            y_drive_voltage_step = ((np.absolute(initial_y_driving_voltage)) + (desired_end_y_mirror_voltage)) / grid_size_y

            # create dataset to populate
            global xy_scan_data_array
            xy_scan_data_array = np.zeros((grid_size_x, grid_size_y))
            global most_recent_data_array
            most_recent_data_array = np.zeros((grid_size_x, grid_size_y))

            # initializing variables to store read counter info.
            output_value = 0
            counter_value = 0

            ################### resetting position of mirrors ####################

            scan_galvo.voltage_cdaq1mod2ao0(initial_x_driving_voltage) # this is for the x-mirror

            scan_galvo.voltage_cdaq1mod2ao1(initial_y_driving_voltage) # this is for the y-mirror

            scan_galvo.voltage_cdaq1mod2ao2(z_piezo_set_voltage) # setting the z_piezo to z_piezo_set_voltage microns

            ########################################################### setting up NI-DAQmx tasks and channels for counting ########################################################

            with nidaqmx.Task() as task1, nidaqmx.Task() as counter_output_task: # this defines 2 NI-DAQmx tasks (one for the counter and one for the counter's clock)

                # adding dig pulse train chan
                counter_output_task.co_channels.add_co_pulse_chan_freq(
                    counter = "cDAQ1Mod1/ctr1",
                    name_to_assign_to_channel = "",
                    units = nidaqmx.constants.FrequencyUnits.HZ,
                    idle_state = nidaqmx.constants.Level.LOW,
                    initial_delay = 0.0,
                    freq = 1000,
                    duty_cycle = 0.50
                    )

                # cfg implict timing
                counter_output_task.timing.cfg_implicit_timing(
                    sample_mode = AcquisitionType.CONTINUOUS,
                    samps_per_chan = 1000000
                    )

                # adding count egdes chan
                task1.ci_channels.add_ci_count_edges_chan(
                    counter = "cDAQ1Mod1/ctr0",
                    name_to_assign_to_channel = "",
                    edge = nidaqmx.constants.Edge.RISING,
                    initial_count = 0,
                    count_direction = nidaqmx.constants.CountDirection.COUNT_UP
                    )

                # cfg sample clk timing
                task1.timing.cfg_samp_clk_timing(
                    rate = 1000,
                    source = "/cDAQ1/Ctr1InternalOutput",
                    active_edge = nidaqmx.constants.Edge.RISING,
                    sample_mode = AcquisitionType.CONTINUOUS,
                    samps_per_chan = 1000000
                    )
                
                counter_output_task.start() # this starts the counter NI-DAQmx task
                task1.start() # this starts the hardware-based internal clock NI-DAQmx task

                def get_counter_number():
                    output_value = 0
                    for counter_increment_variable in range(int(scan_counter_acquisition_time * 1000)): # this reads/lets the counter accumulate for the set time and returns value
                        counter_value = task1.read()
                        output_value += counter_value
                        # print(output_value)
                        
                    return output_value
                                
            ######################################################################## X and Y scanning #########################################################################

                for f in range(grid_size_y): # this loops for rows (y)

                    for k in range(grid_size_x): # this loops for columns (x)

                        ################## important section #################

                        counter_number = get_counter_number()
                        # print("counter_number = %s" % counter_number)

                        if f % 2 != 0: # this loop populates the created xy_scan_data_array (the if else strucuture is present bc of the snaking scanning pattern)

                            xy_scan_data_array[f][k] = counter_number - np.sum(xy_scan_data_array)

                            # xy_scan_data_array[f][((-k) + 1)] = (output_value - np.sum(xy_scan_data_array)) # add counter result to data array                                                                              # saving!
                            # print((output_value - np.sum(xy_scan_data_array)))
                            # print(type((output_value - np.sum(xy_scan_data_array))))
                            # thing = np.array([(output_value - np.sum(xy_scan_data_array))])
                            # print(type(np.array([(output_value - np.sum(xy_scan_data_array))])))
                            # print(type(thing))
                            # print(xy_scan_data_array)
                            # print((output_value - np.sum(xy_scan_data_array)))

                            # writer.writerow([counter_number])                                                                                                                                                                          # csv
                            # output_value == 0
                            # counter_value == 0
                        else:
                            # if f == 0 and k == 0:
                            #     xy_scan_data_array[0][0] = counter_number # add counter result to data array                                                                                                                  # saving!
                            #     # writer.writerow([100000])                                                                                                                                                                        # csv
                        # else:
                            # xy_scan_data_array[f][k] = (output_value - np.sum(xy_scan_data_array)) # add counter result to data array                                                                                   # saving (082422)!
                            xy_scan_data_array[f][k] = counter_number - np.sum(xy_scan_data_array)
                            # print(output_value - np.sum(xy_scan_data_array)+1)
                            # writer.writerow([output_value])                                                                                                                                                                        # csv

                        # print("Column print: %s" % xy_scan_data_array)   
                        # output_value = 0
                        # counter_value = 0

                        counter_number = 0
                        # print("Supposed to be 0: %s" % counter_number)

                        ############# end important section ############

                        if f % 2 == 0: # this loop adjusts for sweeping back and forth along each alternating row

                            if k < (grid_size_x - 1):

                                x_driving_voltage_to_change += x_drive_voltage_step # increment drive voltage forwards
                                scan_galvo.voltage_cdaq1mod2ao0(x_driving_voltage_to_change) # step x motor

                            else:
                                break
                        else:
                            if k < (grid_size_x - 1):

                                x_driving_voltage_to_change -= x_drive_voltage_step # increment drive voltage backwards
                                scan_galvo.voltage_cdaq1mod2ao0(x_driving_voltage_to_change) # step x motor

                            else:
                                break

                    ##################### updating plot section ####################
                    # self.sc.axes.cla() # this does not seem to be needed

                    # print("Row print: %s" % xy_scan_data_array)

                    self.sc.axes.pcolormesh(xy_scan_data_array, cmap = "pink")
                    # self.sc.axes.set_xticks(np.arange(0, grid_size + 10, grid_size / 2), [initial_x_driving_voltage, int((initial_x_driving_voltage + desired_end_x_mirror_voltage) / 2), desired_end_x_mirror_voltage])
                    # self.sc.axes.set_yticks(np.arange(0, grid_size + 10, grid_size / 2), [initial_y_driving_voltage, int((initial_y_driving_voltage + desired_end_y_mirror_voltage) / 2), desired_end_y_mirror_voltage])
                    self.sc.axes.xaxis.set_tick_params(labelsize = 6)
                    self.sc.axes.yaxis.set_tick_params(labelsize = 6)

                    self.sc.axes.set_xlabel("x_mirror_driving_voltage_(V)", fontsize = 6, labelpad = -2)
                    self.sc.axes.set_ylabel("y_mirror_driving_voltage_(V)", fontsize = 6, labelpad = -9)

                    self.sc.figure.canvas.draw()
                    self.sc.figure.canvas.flush_events() #this line is very important
                    ##################### updating plot section ####################

                    if f < (grid_size_y - 1): # this loop prevents from scanning an upper undesired row

                        y_driving_voltage_to_change += y_drive_voltage_step # increment drive voltage
                        scan_galvo.voltage_cdaq1mod2ao1(y_driving_voltage_to_change) # step y motor

                    else:
                        break

                counter_output_task.stop() # this stops the counter NI-DAQmx task - free-ing the reserved cDAQ card resources
                task1.stop() # this stops the hardware-based internal clock NI-DAQmx task - free-ing the reserved cDAQ card resources

            scan_galvo.close() # this is where reeated scanning hinges on and needs to be re-implemented

            ############################################################### end scanning script #############################################################################################

            my_file.close()
            # my_file_output = np.genfromtxt("data_file.csv", delimiter = ",")
            # print(my_file_output)
            # fixed_shape = np.reshape(my_file_output, (grid_size, grid_size))

            ############################################### plotting XY scan data in plot ####################################################
            
            # self.sc.figure.clear() # is this needed after implementing live plot updating?
            self.sc.axes.cla()

            xy_scan_data_array[0][0] = xy_scan_data_array[2][1]

            print("Final data array: %s" % xy_scan_data_array)

            plot = self.sc.axes.pcolormesh(xy_scan_data_array, cmap = "pink")
            # self.sc.axes.set_xticks(np.arange(0, grid_size + 10, grid_size / 2), [initial_x_driving_voltage, int((initial_x_driving_voltage + desired_end_x_mirror_voltage) / 2), desired_end_x_mirror_voltage])
            # self.sc.axes.set_yticks(np.arange(0, grid_size + 10, grid_size / 2), [initial_y_driving_voltage, int((initial_y_driving_voltage + desired_end_y_mirror_voltage) / 2), desired_end_y_mirror_voltage])
            
            self.xy_scan_plot_colorbar = self.sc.figure.colorbar(plot, ax = self.sc.axes)
            self.xy_scan_plot_colorbar.formatter.set_powerlimits((0, 0))
            
            self.sc.axes.xaxis.set_tick_params(labelsize = 6)
            self.sc.axes.yaxis.set_tick_params(labelsize = 6)
            self.xy_scan_plot_colorbar.ax.tick_params(labelsize = 6)
            self.sc.axes.set_xlabel("x_mirror_driving_voltage_(V)", fontsize = 6, labelpad = -2)
            self.sc.axes.set_ylabel("y_mirror_driving_voltage_(V)", fontsize = 6, labelpad = -9)
            self.sc.axes.set_title("XY_scan_%s_z-piezo@%d_microns" % (todays_date, int((z_piezo_set_voltage * 10))), fontsize = 6)
            self.sc.draw()

            most_recent_data_array = xy_scan_data_array # make temp holding global data_array the same as xy_scan_data_array
##############################################################################################################################################################################################################################################
        # xy_scan resolution check then run fnc
        def xy_scan_resolution_validation_fnc():

            self.sc.axes.cla()

            # the try-except frameworks are used to refresh the plotted figures -removing the color bars associated with a previous plotted data
            try:
                self.xy_scan_plot_colorbar.remove()

            except (AttributeError, ValueError):
                pass
        
            try:
                self.yz_scan_plot_colorbar.remove()

            except (AttributeError, ValueError):
                pass

            try:
                self.xz_scan_plot_colorbar.remove()
            
            except (AttributeError, ValueError):
                pass
        
        #################################### resolution checking ##################################

            res_min_condition = 0 # set the min allowed resolution for scanning
            res_max_condition = 2000 # set the max allowed resolution for scanning

            xy_scan_resolution_test_condition = False # define resolution validation bool for xy scan

            while xy_scan_resolution_test_condition is False: # this initiates checking the resolution parameter
                xy_scan_resolution_test_condition == True
                # print_XY_scan_parameters_fnc(self) # call the print user-entered parameters fnc
                run_xy_scan_fnc() # call the run xy scan method fnc
                break

                # # checking for out of bounds of min and max conditions above
                # # TODO: or negative or not a number or too large
                # if int(xy_scan_resolution_qlineedit.text()) < res_min_condition or int(xy_scan_resolution_qlineedit.text()) > res_max_condition:

                #     display_resolution_error_window_fnc() # call the error message pop-up window
                #     break # exit the checking loop: failed

                # # if parameter is in bounds; run scan
                # elif int(xy_scan_resolution_qlineedit.text()) >= res_min_condition and int(xy_scan_resolution_qlineedit.text()) <= res_max_condition:

                #     xy_scan_resolution_test_condition == True
                #     print_XY_scan_parameters_fnc(self) # call the print user-entered parameters fnc
                #     run_xy_scan_fnc() # call the run xy scan method fnc
                #     break # exit the checking loop: passed

        ########### XZ scanning #############
        # print_XZ_scan_parameters_fnc
        def print_XZ_scan_parameters_fnc(self, parent = Setup_Main_Window_Contents): # this fnc does...

            # print("XZ_SCAN PARAMETERS/INFO: ", end = "")                                    # this prints to the terminal
            # print("XZ_scan resolution = %d, " % int(xz_scan_resolution_qlineedit.text()), end = "")
            # print("XZ_scan counter read time = %2f, " % round(float(xz_scan_read_time_qlineedit.text()), 2), end = "")
            # print("XZ_scan min x driving voltage = %2f, " % float(xz_scan_x_voltage_min_qlineedit.text()), end = "")
            # print("XZ_scan max x driving voltage = %2f, " % float(xz_scan_x_voltage_max_qlineedit.text()), end = "")
            # print("XZ_scan y driving voltage = %2f, " % float(xz_scan_y_voltage_qlineedit.text()), end = "")
            # print("XZ_scan z-piezo min driving voltage = %2f, " % float(xz_scan_z_piezo_min_voltage_qlineedit.text()), end = "")
            # print("XZ_scan z-piezo max driving voltage = %2f." % float(xz_scan_z_piezo_max_voltage_qlineedit.text()))


            # need to clear text box first
            self.parameters_dsiplay_text_box.clear()

            # this prints to the QTextBox in the left_window. The output of the user-selected scan parameters is printed below
            self.parameters_dsiplay_text_box.setPlainText(
                                                        "XZ_SCAN PARAMETERS/INFO:\n"
                                                        "XZ_scan resolution = " + str(int(xz_scan_resolution_qlineedit.text())) + "\n"
                                                        "XZ_scan counter read time = " + str(float(xz_scan_read_time_qlineedit.text())) + "\n"
                                                        "XZ_scan min x driving voltage = " + str(float(xz_scan_x_voltage_min_qlineedit.text())) + "\n"
                                                        "XZ_scan max x driving voltage = " + str(float(xz_scan_x_voltage_max_qlineedit.text())) + "\n"
                                                        "XZ_scan y driving voltage = " + str(float(xz_scan_y_voltage_qlineedit.text())) + "\n"
                                                        "XZ_scan z-piezo min driving voltage = " + str(float(xz_scan_z_piezo_min_voltage_qlineedit.text())) + "\n"
                                                        "XZ_scan z-piezo max driving voltage = " + str(float(xz_scan_z_piezo_max_voltage_qlineedit.text()))
                                                        )
        
        # run XZ scan fnc
        def run_xz_scan_fnc(): # this fnc runs the xy_scan per the user-entered parameters in the xy_scan qlineedits

            """
            This cell runs a XZ scan. It currently creates and then populates a user defined size numpy array according to a set counter acquisition time and a motor
step voltage setting. Additionally, the initial driving voltage for the X and Y motors can be set according to the desired scanning range. This scanning program runs in a snake pattern, it scan the first row left to right, moves up one row, 
then scans right to left and continues. Alternatives would be scanning left to right, and resetting the position of the laser on the next higher row and scanning again left 
to right OR scanning in a "circular" patter either CW or CCW from outside to inside or inside to outside. The chosen method was picked for simplicity of understanding. The 
scanning loops are present within NI-DAQmx tasks to speed up the program. Starting and stopping a NI-DAQmx task repeatedly slows down the program dramatically. So, the 
counter and hardware clock task are started once, then the scanning program is run, and then the counter and clock tasks are closed -un-reserving the hardware resources. 
This cell uses the "DAQAnalogOutputs" function from a written class file at:
C:/Users/lukin2dmaterials/miniconda3/envs/qcodes/Lib/site-packages/qcodes_contrib_drivers/drivers/NationalInstruments/class_file. Slashes are reversed to run
            """

            ################################################################################## card 2 (AO) ########################################################################

            # naming the instrument
            scan_galvo_card_name = "cDAQ1Mod2"

            # dictionary of analog output channels
            scan_galvo_ao_channels = {f'{scan_galvo_card_name}/ao{i}': i for i in range(4)}

            # defining the instrument (ni_9263)
            scan_galvo = DAQAnalogOutputs("name_two", scan_galvo_card_name, scan_galvo_ao_channels)

            ############################################################################### def other variables #####################################################################

            ################### setting variales and array ####################

            # counter read time:
            scan_counter_acquisition_time = float(xz_scan_read_time_qlineedit.text())                                     # note a reading time <0.05 s is likely too short

            # def grid_size of scan (resolution)
            grid_size = int(xz_scan_resolution_qlineedit.text())

            # def the initial driving voltage for the x-mirror
            initial_x_driving_voltage = float(xz_scan_x_voltage_min_qlineedit.text())
            # def the initial driving voltage for the y-mirror
            initial_y_driving_voltage = float(xz_scan_y_voltage_qlineedit.text())
            #
            initial_z_piezo_driving_voltage = float(xz_scan_z_piezo_min_voltage_qlineedit.text())

            # set desired end mirror voltages
            desired_end_x_mirror_voltage = float(xz_scan_x_voltage_max_qlineedit.text())
            desired_end_z_piezo_voltage = float(xz_scan_z_piezo_max_voltage_qlineedit.text())

            # setup parameter for the program to use based on defined variables
            x_driving_voltage_to_change = initial_x_driving_voltage
            z_piezo_driving_voltage_to_change = initial_z_piezo_driving_voltage

            # def the internal stepping voltages based on user-entered settings above
            x_drive_voltage_step = ((np.absolute(initial_x_driving_voltage)) + (desired_end_x_mirror_voltage)) / grid_size
            z_piezo_drive_voltage_step = (initial_z_piezo_driving_voltage + (desired_end_z_piezo_voltage)) / grid_size

            # create dataset to populate
            global xz_scan_data_array
            xz_scan_data_array = np.zeros((grid_size, grid_size))
            global most_recent_data_array
            most_recent_data_array = np.zeros((grid_size, grid_size))

            # initializing variables to store read counter info.
            output_value = 0
            counter_value = 0

            ################### resetting position of mirrors ####################

            scan_galvo.voltage_cdaq1mod2ao0(initial_x_driving_voltage) # this is for setting the initial x voltage

            scan_galvo.voltage_cdaq1mod2ao1(initial_y_driving_voltage) # this is for fixing the x-mirror at defined setting (voltage)

            scan_galvo.voltage_cdaq1mod2ao2(initial_z_piezo_driving_voltage) # starting z-piezo at 0.0 V (0 microns); this variable will increase during scanning

            ########################################################### setting up NI-DAQmx tasks and channels for counting ########################################################

            with nidaqmx.Task() as task1, nidaqmx.Task() as counter_output_task: # this defines 2 NI-DAQmx tasks (one for the counter and one for the counter's clock)

                # adding dig pulse train chan
                counter_output_task.co_channels.add_co_pulse_chan_freq(
                    counter = "cDAQ1Mod1/ctr1",
                    name_to_assign_to_channel = "",
                    units = FrequencyUnits.HZ,
                    idle_state = nidaqmx.constants.Level.LOW,
                    initial_delay = 0.0,
                    freq = 1000,
                    duty_cycle = 0.5
                    )

                # cfg implict timing
                counter_output_task.timing.cfg_implicit_timing(
                    sample_mode = AcquisitionType.CONTINUOUS,
                    samps_per_chan = 1
                    )

                # adding count egdes chan
                task1.ci_channels.add_ci_count_edges_chan(
                    counter = "cDAQ1Mod1/ctr0",
                    name_to_assign_to_channel = "",
                    edge = Edge.RISING,
                    initial_count = 0,
                    count_direction = CountDirection.COUNT_UP
                    )

                # cfg sample clk timing
                task1.timing.cfg_samp_clk_timing(
                    rate = 1000,
                    source = "/cDAQ1/Ctr1InternalOutput",
                    active_edge = Edge.RISING,
                    sample_mode = AcquisitionType.CONTINUOUS,
                    samps_per_chan = 1
                    )
                
                counter_output_task.start() # this starts the counter NI-DAQmx task
                task1.start() # this starts the hardware-based internal clock NI-DAQmx task
                        
                ####################################################################### x and z scanning #########################################################################

                for f in range(grid_size): # this loops for stacks in z

                    for k in range(grid_size): # this loops for columns (varying y voltage/setting)

                        ################## important section #################

                        for my_var_not_named_i in range(int(scan_counter_acquisition_time * 1000)): # this reads/lets the counter accumulate for the set time and returns value
                            counter_value = task1.read()
                            output_value += counter_value

                        if f % 2 != 0: # this loop populates the created xz_scan_data_array (the if else strucuture is present bc of the snaking scanning pattern)
                            xz_scan_data_array[f][((-k) + 1)] = (output_value - np.sum(xz_scan_data_array)) # add counter result to data array                           # saving (082422)
                            output_value == 0
                            counter_value == 0
                        else:
                            if f == 0 and k == 0:
                                xz_scan_data_array[0][0] = output_value # add counter result to data array                                                      # saving
                            else:
                                xz_scan_data_array[f][k] = (output_value - np.sum(xz_scan_data_array)) # add counter result to data array                               # saving (082422)
                        output_value = 0
                        counter_value = 0

                        ############# end important section ############

                        if f % 2 == 0: # this loop adjusts for sweeping back and forth along each alternating row
                            if k < (grid_size - 1):
                                x_driving_voltage_to_change += x_drive_voltage_step # increment y mirro drive voltage forwards
                                scan_galvo.voltage_cdaq1mod2ao0(x_driving_voltage_to_change) # step y mirror
                            else:
                                break
                        else:
                            if k < (grid_size - 1):
                                x_driving_voltage_to_change -= x_drive_voltage_step # increment y mirror drive voltage backwards
                                scan_galvo.voltage_cdaq1mod2ao0(x_driving_voltage_to_change) # step y mirror
                            else:
                                break
                    
                    ##################### updating plot section ####################
                    # self.sc.axes.cla() # this does not seem to be needed
                    self.sc.axes.pcolormesh(xz_scan_data_array, cmap = "inferno")
                    self.sc.axes.set_xticks(np.arange(0, grid_size + 10, grid_size / 2), [initial_x_driving_voltage, int((initial_x_driving_voltage + desired_end_x_mirror_voltage) / 2), desired_end_x_mirror_voltage])
                    self.sc.axes.set_yticks(np.arange(0, grid_size + 10, grid_size / 2), [int(initial_z_piezo_driving_voltage * 10), (int(initial_z_piezo_driving_voltage * 10) + int(desired_end_z_piezo_voltage * 10)) / 2, int(desired_end_z_piezo_voltage * 10)])
                    self.sc.axes.xaxis.set_tick_params(labelsize = 8)
                    self.sc.axes.yaxis.set_tick_params(labelsize = 8)
                    self.sc.axes.set_xlabel("x_mirror_driving_voltage_(V)", fontsize = 8)
                    self.sc.axes.set_ylabel("objective_z-piezo_height_(microns)", fontsize = 8)
                    self.sc.figure.canvas.draw()
                    self.sc.figure.canvas.flush_events()
                    ##################### updating plot section ####################

                    if f < (grid_size - 1): # this loop
                        z_piezo_driving_voltage_to_change += z_piezo_drive_voltage_step # increment drive voltage
                        scan_galvo.voltage_cdaq1mod2ao2(z_piezo_driving_voltage_to_change) # step z
                    else:
                        break

                counter_output_task.stop() # this stops the counter NI-DAQmx task - free-ing the reserved cDAQ card resources
                task1.stop() # this stops the hardware-based internal clock NI-DAQmx task - free-ing the reserved cDAQ card resources

            scan_galvo.close()
            ############################################ end XZ scanning script #################################################

            ############################################### plotting XZ scan data in plot ####################################################
            self.sc.axes.cla()
            xz_scan_plot = self.sc.axes.pcolormesh(xz_scan_data_array, cmap = "inferno")
            xz_scan_plot_colorbar = self.sc.figure.colorbar(xz_scan_plot, ax = self.sc.axes, pad = 0.02, aspect = 15)
            xz_scan_plot_colorbar.formatter.set_powerlimits((0, 0))
            self.sc.axes.xaxis.set_tick_params(labelsize = 8)
            self.sc.axes.yaxis.set_tick_params(labelsize = 8)
            xz_scan_plot_colorbar.ax.tick_params(labelsize = 7)
            self.sc.axes.set_xticks(np.arange(0, grid_size + 10, grid_size / 2), [initial_x_driving_voltage, int((initial_x_driving_voltage + desired_end_x_mirror_voltage) / 2), desired_end_x_mirror_voltage])
            self.sc.axes.set_yticks(np.arange(0, grid_size + 10, grid_size / 2), [int(initial_z_piezo_driving_voltage * 10), (int(initial_z_piezo_driving_voltage * 10) + int(desired_end_z_piezo_voltage * 10)) / 2, int(desired_end_z_piezo_voltage * 10)])
            self.sc.axes.set_xlabel("x_mirror_driving_voltage_(V)", fontsize = 8)
            self.sc.axes.set_ylabel("objective_z-piezo_height_(microns)", fontsize = 8)
            self.sc.axes.set_title("XZ_scan_%s_y_voltage=%f_V" % (todays_date, initial_y_driving_voltage), fontsize = 8)
            self.sc.draw()

            most_recent_data_array = xz_scan_data_array

        # xz_scan resolution check then run fnc
        def xz_scan_resolution_validation_fnc():

            self.sc.axes.cla()

            try:
                self.xz_scan_plot_colorbar.remove()

            except (AttributeError, ValueError):
                pass

            try:
                self.yz_scan_plot_colorbar.remove()

            except (AttributeError, ValueError):
                pass
            
            try:
                self.xy_scan_plot_colorbar.remove()
            
            except (AttributeError, ValueError):
                pass

            res_min_condition = 20 # set the min allowed resolution for scanning
            res_max_condition = 900 # set the max allowed resolution for scanning

            xz_scan_resolution_test_condition = False # define resolution validation bool for xz scan

            while xz_scan_resolution_test_condition is False: # this initiates checking the resolution parameter

                # checking for out of bounds of min and max conditions above
                if int(xz_scan_resolution_qlineedit.text()) < res_min_condition or int(xz_scan_resolution_qlineedit.text()) > res_max_condition: # TODO: or negative or not a number or too large

                    display_resolution_error_window_fnc() # call the error message pop-up window
                    break # exit the checking loop: failed

                # if parameter is in bounds; run scan
                elif int(xz_scan_resolution_qlineedit.text()) >= res_min_condition and int(xz_scan_resolution_qlineedit.text()) <= res_max_condition:

                    xz_scan_resolution_test_condition == True
                    print_XZ_scan_parameters_fnc(self) # call the print user-entered parameters fnc
                    run_xz_scan_fnc() # call the run xz scan method fnc
                    break # exit the checking loop: passed

        ########################## YZ scanning ############################

        # print_YZ_scan_parameters_fnc
        def print_YZ_scan_parameters_fnc(self, parent = Setup_Main_Window_Contents): # this fnc does...

            # print("YZ_SCAN PARAMETERS/INFO: ", end = "")
            # print("YZ_scan resolution = %d, " % int(yz_scan_resolution_qlineedit.text()), end = "")
            # print("YZ_scan counter read time = %2f, " % round(float(yz_scan_read_time_qlineedit.text()), 2), end = "")
            # print("YZ_scan min Y driving voltage = %2f, " % float(yz_scan_y_voltage_min_qlineedit.text()), end = "")
            # print("YZ_scan max Y driving voltage = %2f, " % float(yz_scan_y_voltage_max_qlineedit.text()), end = "")
            # print("YZ_scan X driving voltage = %2f, " % float(yz_scan_x_voltage_qlineedit.text()), end = "")
            # print("YZ_scan z-piezo min driving voltage = %2f, " % float(yz_scan_z_piezo_min_voltage_qlineedit.text()), end = "")
            # print("YZ_scan z-piezo max driving voltage = %2f." % float(yz_scan_z_piezo_max_voltage_qlineedit.text()))

            # need to clear text box first
            self.parameters_dsiplay_text_box.clear()

            # this prints to the QTextBox in the left_window. The output of the user-selected scan parameters is printed below
            self.parameters_dsiplay_text_box.setPlainText(
                        "YZ_SCAN PARAMETERS/INFO:\n"
                        "YZ_scan resolution = " + str(int(yz_scan_resolution_qlineedit.text())) + "\n"
                        "YZ_scan counter read time = " + str(float(yz_scan_read_time_qlineedit.text())) + "\n"
                        "YZ_scan min Y driving voltage = " + str(float(yz_scan_y_voltage_min_qlineedit.text())) + "\n"
                        "YZ_scan max Y driving voltage = " + str(float(yz_scan_y_voltage_max_qlineedit.text())) + "\n"
                        "YZ_scan X driving voltage = " + str(float(yz_scan_x_voltage_qlineedit.text())) + "\n'"
                        "YZ_scan z-piezo min driving voltage = " + str(float(yz_scan_z_piezo_min_voltage_qlineedit.text())) + "\n"
                        "YZ_scan z-piezo max driving voltage = " + str(float(yz_scan_z_piezo_max_voltage_qlineedit.text()))
                                                        )
                
        # run YZ scan function
        def run_yz_scan_fnc(): # this fnc runs the YZ scan script
            # print("YZ scan started")

            """
            This cell runs a YZ only scan. It currently creates and then populates a user defined size numpy array according to a set counter acquisition time and a motor
step voltage setting. Additionally, the initial driving voltage for the X and Y motors can be set according to the desired scanning range. This scanning program runs in a snake pattern, it scan the first row left to right, moves up one row, 
then scans right to left and continues. Alternatives would be scanning left to right, and resetting the position of the laser on the next higher row and scanning again left 
to right OR scanning in a "circular" patter either CW or CCW from outside to inside or inside to outside. The chosen method was picked for simplicity of understanding. The 
scanning loops are present within NI-DAQmx tasks to speed up the program. Starting and stopping a NI-DAQmx task repeatedly slows down the program dramatically. So, the 
counter and hardware clock task are started once, then the scanning program is run, and then the counter and clock tasks are closed -un-reserving the hardware resources. 
This cell uses the "DAQAnalogOutputs" function from a written class file at:
C:/Users/lukin2dmaterials/miniconda3/envs/qcodes/Lib/site-packages/qcodes_contrib_drivers/drivers/NationalInstruments/class_file. Slashes are reversed to run
            """

            ################################################################################## card 2 (AO) ########################################################################

            # naming the instrument
            scan_galvo_card_name = "cDAQ1Mod2"

            # dictionary of analog output channels
            scan_galvo_ao_channels = {f'{scan_galvo_card_name}/ao{i}': i for i in range(4)}

            # defining the instrument (ni_9263)
            scan_galvo = DAQAnalogOutputs("name_two", scan_galvo_card_name, scan_galvo_ao_channels)

            ############################################################################### def other variables #####################################################################

            ################### setting variales and array ####################

            # counter read time:
            scan_counter_acquisition_time = 0.05                                                                               # note a reading time <0.05 s is likely too short

            # def
            grid_size = int(yz_scan_resolution_qlineedit.text())

            # def the initial driving voltage for the x-mirror
            initial_x_driving_voltage = float(yz_scan_x_voltage_qlineedit.text())

            # def the initial driving voltage for the y-mirror
            initial_y_driving_voltage = float(yz_scan_y_voltage_min_qlineedit.text())
            #
            initial_z_piezo_driving_voltage = float(yz_scan_z_piezo_min_voltage_qlineedit.text())

            # setup parameter for the program to use based on defined variables
            y_driving_voltage_to_change = initial_y_driving_voltage
            z_piezo_driving_voltage_to_change = initial_z_piezo_driving_voltage

            # set desired end mirror voltages
            desired_end_y_mirror_voltage = float(yz_scan_y_voltage_max_qlineedit.text())
            desired_end_z_piezo_voltage = float(yz_scan_z_piezo_max_voltage_qlineedit.text())

            # def the internal stepping voltages based on user-entered settings above
            y_drive_voltage_step = ((np.absolute(initial_y_driving_voltage)) + (desired_end_y_mirror_voltage)) / grid_size
            z_piezo_drive_voltage_step = (initial_z_piezo_driving_voltage + (desired_end_z_piezo_voltage)) / grid_size

            # create dataset to populate
            global yz_scan_data_array
            yz_scan_data_array = np.zeros((grid_size, grid_size))
            global most_recent_data_array
            most_recent_data_array = np.zeros((grid_size, grid_size))

            # initializing variables to store read counter info.
            output_value = 0
            counter_value = 0

            ################### resetting position of mirrors ####################

            scan_galvo.voltage_cdaq1mod2ao0(initial_x_driving_voltage) # this is for fixing the x-mirror at defined setting (voltage)

            scan_galvo.voltage_cdaq1mod2ao1(initial_y_driving_voltage) # this is for setting the initial x voltage

            scan_galvo.voltage_cdaq1mod2ao2(initial_z_piezo_driving_voltage) # starting z-piezo at 0.0 V (0 microns); this variable will increase during scanning

            ########################################################### setting up NI-DAQmx tasks and channels for counting ########################################################

            with nidaqmx.Task() as task1, nidaqmx.Task() as counter_output_task: # this defines 2 NI-DAQmx tasks (one for the counter and one for the counter's clock)

                # adding dig pulse train chan
                counter_output_task.co_channels.add_co_pulse_chan_freq(
                    counter = "cDAQ1Mod1/ctr1",
                    name_to_assign_to_channel = "",
                    units = FrequencyUnits.HZ,
                    idle_state = nidaqmx.constants.Level.LOW,
                    initial_delay = 0.0,
                    freq = 1000,
                    duty_cycle = 0.5
                    )

                # cfg implict timing
                counter_output_task.timing.cfg_implicit_timing(
                    sample_mode = AcquisitionType.CONTINUOUS,
                    samps_per_chan = 1
                    )

                # adding count egdes chan
                task1.ci_channels.add_ci_count_edges_chan(
                    counter = "cDAQ1Mod1/ctr0",
                    name_to_assign_to_channel = "",
                    edge = Edge.RISING,
                    initial_count = 0,
                    count_direction = CountDirection.COUNT_UP
                    )

                # cfg sample clk timing
                task1.timing.cfg_samp_clk_timing(
                    rate = 1000,
                    source = "/cDAQ1/Ctr1InternalOutput",
                    active_edge = Edge.RISING,
                    sample_mode = AcquisitionType.CONTINUOUS,
                    samps_per_chan = 1
                    )
                
                counter_output_task.start() # this starts the counter NI-DAQmx task
                task1.start() # this starts the hardware-based internal clock NI-DAQmx task
                        
            ####################################################################### x and z scanning #########################################################################

                for f in range(grid_size): # this loops for stacks in z

                    for k in range(grid_size): # this loops for columns (varying y voltage/setting)

                        ################## important section #################

                        for my_var_not_named_i in range(int(scan_counter_acquisition_time * 1000)): # this reads/lets the counter accumulate for the set time and returns value
                            counter_value = task1.read()
                            output_value += counter_value

                        if f % 2 != 0: # this loop populates the created yz_scan_data_array (the if else strucuture is present bc of the snaking scanning pattern)
                            yz_scan_data_array[f][((-k) + 1)] = (output_value - np.sum(yz_scan_data_array)) # add counter result to data array                           # saving (082422)
                            output_value == 0
                            counter_value == 0
                        else:
                            if f == 0 and k == 0:
                                yz_scan_data_array[0][0] = output_value # add counter result to data array                                                      # saving
                            else:
                                yz_scan_data_array[f][k] = (output_value - np.sum(yz_scan_data_array)) # add counter result to data array                               # saving (082422)
                        output_value = 0
                        counter_value = 0

                        ############# end important section ############

                        if f % 2 == 0: # this loop adjusts for sweeping back and forth along each alternating row
                            if k < (grid_size - 1):
                                y_driving_voltage_to_change += y_drive_voltage_step # increment y mirro drive voltage forwards
                                scan_galvo.voltage_cdaq1mod2ao1(y_driving_voltage_to_change) # step y mirror
                            else:
                                break
                        else:
                            if k < (grid_size - 1):
                                y_driving_voltage_to_change -= y_drive_voltage_step # increment y mirror drive voltage backwards
                                scan_galvo.voltage_cdaq1mod2ao1(y_driving_voltage_to_change) # step y mirror
                            else:
                                break
                    
                    ##################### updating plot section ####################
                    # self.sc.axes.cla() # this does not seem to be needed
                    self.sc.axes.pcolormesh(yz_scan_data_array, cmap = "inferno")
                    self.sc.axes.set_xticks(np.arange(0, grid_size + 10, grid_size / 2), [initial_y_driving_voltage, int((initial_y_driving_voltage + desired_end_y_mirror_voltage) / 2), desired_end_y_mirror_voltage])
                    self.sc.axes.set_yticks(np.arange(0, grid_size + 10, grid_size / 2), [int(initial_z_piezo_driving_voltage * 10), (int(initial_z_piezo_driving_voltage * 10) + int(desired_end_z_piezo_voltage * 10)) / 2, int(desired_end_z_piezo_voltage * 10)])
                    self.sc.axes.xaxis.set_tick_params(labelsize = 8)
                    self.sc.axes.yaxis.set_tick_params(labelsize = 8)
                    self.sc.axes.set_xlabel("y_mirror_driving_voltage_(V)", fontsize = 8)
                    self.sc.axes.set_ylabel("objective_z-piezo_height_(microns)", fontsize = 8)
                    self.sc.figure.canvas.draw()
                    self.sc.figure.canvas.flush_events()
                    ##################### updating plot section ####################

                    if f < (grid_size - 1): # this loop
                        z_piezo_driving_voltage_to_change += z_piezo_drive_voltage_step # increment drive voltage
                        scan_galvo.voltage_cdaq1mod2ao2(z_piezo_driving_voltage_to_change) # step z
                    else:
                        break

                counter_output_task.stop() # this stops the counter NI-DAQmx task - free-ing the reserved cDAQ card resources
                task1.stop() # this stops the hardware-based internal clock NI-DAQmx task - free-ing the reserved cDAQ card resources

            scan_galvo.close()

            ############################################### plotting YZ scan data in plot ####################################################
            self.sc.axes.cla()
            yz_scan_plot = self.sc.axes.pcolormesh(yz_scan_data_array, cmap = "pink")
            yz_scan_plot_colorbar = self.sc.figure.colorbar(yz_scan_plot, ax = self.sc.axes, pad = 0.02, aspect = 15)
            yz_scan_plot_colorbar.formatter.set_powerlimits((0, 0))
            self.sc.axes.xaxis.set_tick_params(labelsize = 8)
            self.sc.axes.yaxis.set_tick_params(labelsize = 8)
            yz_scan_plot_colorbar.ax.tick_params(labelsize = 7)
            self.sc.axes.set_xticks(np.arange(0, grid_size + 10, grid_size / 2), [initial_y_driving_voltage, int((initial_y_driving_voltage + desired_end_y_mirror_voltage) / 2), desired_end_y_mirror_voltage])
            self.sc.axes.set_yticks(np.arange(0, grid_size + 10, grid_size / 2), [int(initial_z_piezo_driving_voltage * 10), (int(initial_z_piezo_driving_voltage * 10) + int(desired_end_z_piezo_voltage * 10)) / 2, int(desired_end_z_piezo_voltage * 10)])
            self.sc.axes.set_xlabel("y_mirror_driving_voltage_(V)", fontsize = 8)
            self.sc.axes.set_ylabel("objective_z-piezo_height_(microns)", fontsize = 8)
            self.sc.axes.set_title("YZ_scan_%s_x_voltage=%f_V" % (todays_date, initial_x_driving_voltage), fontsize = 8)
            self.sc.draw()
            most_recent_data_array = yz_scan_data_array
    
        # yz_scan resolution check then run fnc
        def yz_scan_resolution_validation_fnc():

            self.sc.axes.cla()

            try:
                self.yz_scan_plot_colorbar.remove()

            except (AttributeError, ValueError):
                pass
            
            try:
                self.xy_scan_plot_colorbar.remove()
            
            except (AttributeError, ValueError):
                pass
                
            try:
                self.xz_scan_plot_colorbar.remove()
            
            except (AttributeError, ValueError):
                pass

            res_min_condition = 20 # set the min allowed resolution for scanning
            res_max_condition = 900 # set the max allowed resolution for scanning

            yz_scan_resolution_test_condition = False # define resolution validation bool for yz scan

            while yz_scan_resolution_test_condition is False: # this initiates checking the resolution parameter

                # checking for out of bounds of min and max conditions above
                if int(yz_scan_resolution_qlineedit.text()) < res_min_condition or int(yz_scan_resolution_qlineedit.text()) > res_max_condition: # TODO: or negative or not a number or too large

                    display_resolution_error_window_fnc() # call the error message pop-up window
                    break # exit the checking loop: failed

                # if parameter is in bounds; run scan
                elif int(yz_scan_resolution_qlineedit.text()) >= res_min_condition and int(yz_scan_resolution_qlineedit.text()) <= res_max_condition:

                    yz_scan_resolution_test_condition == True
                    print_YZ_scan_parameters_fnc(self) # call the print user-entered parameters fnc
                    run_yz_scan_fnc() # call the run yz scan method fnc
                    break # exit the checking loop: passed

        ############################################################# left half window #####################################################################
        self.left_window = QFrame(self)
        self.left_window.setFrameShape(QFrame.StyledPanel)
        self.left_window.setFixedSize(340, 510)

        # QTextEdit display for printing scan parameters to GUI window
        """
        This creates a textbox located in the lower left hand corner of the GUI. It is set (parent) to the left_window. When any scan script is run the 
        parameters enterd by the user are collected from their respective QLineedits and then printed in a list to this QTextBox. This allows the user 
        select and copy the parameters they used quickly in order to save them to an external file as documentation of scans run.

        Room for improvement:
        1. The date (get from "todays_date" that is already implemented) could be added to the first line of any scans parameter printing fnc
        2. The info printed to this QTextBox could also and/or be saved to an external file for record/documentation
        """

        parameters_dsiplay_text_box = QTextEdit(self.left_window)
        parameters_dsiplay_text_box.resize(320, 113)
        parameters_dsiplay_text_box.move(10, 309)
        parameters_dsiplay_text_box.setParent(self.left_window)

        ############################################################### right half window ###################################################################
        self.right_window = QFrame(self)
        self.right_window.setFrameShape(QFrame.StyledPanel)
        self.right_window.setFixedSize(600, 600)

        ##################################################### plot in right window ##################################################################

        plot_res = 5.42
        self.sc = MplCanvas(self, canvas_width = plot_res, canvas_height = plot_res, canvas_dpi = 110)                                                                      # changing dpi does something to scale of figureure
        self.sc.move(2, 2)
        self.sc.setParent(self.right_window)
        self.sc.axes.xaxis.set_tick_params(labelsize = 8)
        self.sc.axes.yaxis.set_tick_params(labelsize = 8)

        ############################################################# split left and right windows #########################################################
        
        self.splitter1 = QSplitter(Qt.Horizontal)
        self.splitter1.addWidget(self.left_window)
        self.splitter1.addWidget(self.right_window)
        self.hbox.addWidget(self.splitter1) # set layout and show window
        self.setLayout(self.hbox)
        self.show()

        ############################################################# scanning (XY, XZ, & YZ) section ############################################################################
        
        ##################################### overall ####################################

        ############ begin save data section ###############
        self.save_scan_data_button = QPushButton("Save scan data:", self) # create the save scan data button
        self.save_scan_data_button.setParent(self.left_window) # set the "parent" bound of the save scan data button
        self.save_scan_data_button.resize(90, 20) # resize the save scan data button
        self.save_scan_data_button.move(10, 280) # position the save scan data button in the left winodw
        self.save_scan_data_button.clicked.connect(save_scan_data_fnc)

        save_scan_data_qlineedit = QLineEdit(self) # qlineedit
        save_scan_data_qlineedit.setParent(self.left_window)
        save_scan_data_qlineedit.resize(189, 20)
        save_scan_data_qlineedit.move(105, 280)

        save_scan_data_extension_widget = QLabel("\".npy\"", self) # widget
        save_scan_data_extension_widget.setParent(self.left_window),
        save_scan_data_extension_widget.move(297, 288 - 5)
        ############ end save data section ###############

        ###
        self.set_galvo_to_zero_button = QPushButton("Zero galvo", self)
        self.set_galvo_to_zero_button.setParent(self.left_window)
        self.set_galvo_to_zero_button.resize(70, 20)
        self.set_galvo_to_zero_button.move(80, 480)
        self.set_galvo_to_zero_button.clicked.connect(zero_galvo_function)
        ##

        # scan widgets overall "Scanning"
        scan_widget_overall = QLabel("Scanning options:")
        scan_widget_overall.setFont(QFont("Times font", 6))
        scan_widget_overall.setParent(self.left_window)
        scan_widget_overall.move(120, 10)

        indiv_scan_labels_y_height = 25

        row_y_adjust = 5

        overall_y_adjust = 10

        #########################################################################################
        ########################################### XY scanning #################################
        #########################################################################################

        xy_scan_widgets_left_x_justify = 5
        xy_scan_parameters_validated_Q = False

        # XY scan
        self.xy_scan_label_widget = QLabel("XY scan", self) # widget
        self.xy_scan_label_widget.setParent(self.left_window)
        self.xy_scan_label_widget.move(12 + 10, indiv_scan_labels_y_height + overall_y_adjust)
        self.xy_scan_label_widget.show()

        # resolution
        xy_scan_resolution_widget = QLabel("Res:", self) # widget
        xy_scan_resolution_widget.setParent(self.left_window)
        xy_scan_resolution_widget.move(xy_scan_widgets_left_x_justify, 40 + row_y_adjust + overall_y_adjust)
        xy_scan_resolution_widget.show()

        xy_scan_resolution_qlineedit = QLineEdit(self) # qclineedit
        xy_scan_resolution_qlineedit.setParent(self.left_window)
        xy_scan_resolution_qlineedit.move(30, 40 + row_y_adjust + overall_y_adjust)
        xy_scan_resolution_qlineedit.resize(55, 15)
        xy_scan_resolution_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        # read time
        xy_scan_read_time_widget = QLabel("APD_t:", self) # widget
        xy_scan_read_time_widget.setParent(self.left_window)
        xy_scan_read_time_widget.move(xy_scan_widgets_left_x_justify, 65 + row_y_adjust + overall_y_adjust)

        xy_scan_read_time_qlineedit = QLineEdit(self) # qclineedit
        xy_scan_read_time_qlineedit.setParent(self.left_window)
        xy_scan_read_time_qlineedit.move(40, 65 + row_y_adjust + overall_y_adjust)
        xy_scan_read_time_qlineedit.resize(45, 15)
        xy_scan_read_time_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)
        
        # x voltage (min and max)
        xy_scan_x_voltage_min_widget = QLabel("x_V_min:", self) # widget
        xy_scan_x_voltage_min_widget.setParent(self.left_window)
        xy_scan_x_voltage_min_widget.move(xy_scan_widgets_left_x_justify, 90 + row_y_adjust + overall_y_adjust)

        xy_scan_x_voltage_min_qlineedit = QLineEdit(self) # qclineedit
        xy_scan_x_voltage_min_qlineedit.setParent(self.left_window)
        xy_scan_x_voltage_min_qlineedit.move(50, 90 + row_y_adjust + overall_y_adjust)
        xy_scan_x_voltage_min_qlineedit.resize(35, 15)
        xy_scan_x_voltage_min_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        xy_scan_x_voltage_max_widget = QLabel("x_V_max:", self) # widget
        xy_scan_x_voltage_max_widget.setParent(self.left_window)
        xy_scan_x_voltage_max_widget.move(xy_scan_widgets_left_x_justify, 115 + row_y_adjust + overall_y_adjust)

        xy_scan_x_voltage_max_qlineedit = QLineEdit(self) # qclineedit
        xy_scan_x_voltage_max_qlineedit.setParent(self.left_window)
        xy_scan_x_voltage_max_qlineedit.move(55, 115 + row_y_adjust + overall_y_adjust)
        xy_scan_x_voltage_max_qlineedit.resize(30, 15)
        xy_scan_x_voltage_max_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        # y voltage (min and max)
        xy_scan_y_voltage_min_widget = QLabel("y_V_min:", self) # widget
        xy_scan_y_voltage_min_widget.setParent(self.left_window)
        xy_scan_y_voltage_min_widget.move(xy_scan_widgets_left_x_justify, 140 + row_y_adjust + overall_y_adjust)

        xy_scan_y_voltage_min_qlineedit = QLineEdit(self) # qclineedit
        xy_scan_y_voltage_min_qlineedit.setParent(self.left_window)
        xy_scan_y_voltage_min_qlineedit.move(50, 140 + row_y_adjust + overall_y_adjust)
        xy_scan_y_voltage_min_qlineedit.resize(35, 15)
        xy_scan_y_voltage_min_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        xy_scan_y_voltage_max_widget = QLabel("y_V_max:", self) # widget
        xy_scan_y_voltage_max_widget.setParent(self.left_window)
        xy_scan_y_voltage_max_widget.move(xy_scan_widgets_left_x_justify, 165 + row_y_adjust + overall_y_adjust)

        xy_scan_y_voltage_max_qlineedit = QLineEdit(self) # qclineedit
        xy_scan_y_voltage_max_qlineedit.setParent(self.left_window)
        xy_scan_y_voltage_max_qlineedit.move(55, 165 + row_y_adjust + overall_y_adjust)
        xy_scan_y_voltage_max_qlineedit.resize(30, 15)
        xy_scan_y_voltage_max_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)
        
        # z piezo
        xy_scan_z_piezo_voltage_widget = QLabel("z_V:", self) # widget
        xy_scan_z_piezo_voltage_widget.setParent(self.left_window)
        xy_scan_z_piezo_voltage_widget.move(xy_scan_widgets_left_x_justify, 190 + row_y_adjust + overall_y_adjust)

        xy_scan_z_piezo_voltage_qlineedit = QLineEdit(self) # qclineedit
        xy_scan_z_piezo_voltage_qlineedit.setParent(self.left_window)
        xy_scan_z_piezo_voltage_qlineedit.move(30, 190 + row_y_adjust + overall_y_adjust)
        xy_scan_z_piezo_voltage_qlineedit.resize(55, 15)
        xy_scan_z_piezo_voltage_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        # run xy scan button
        xy_scan_run_button = QPushButton("run\nXY scan", self) # button
        xy_scan_run_button.setParent(self.left_window)
        xy_scan_run_button.resize(60, 40)
        xy_scan_run_button.move(10, 215 + row_y_adjust + overall_y_adjust)
        xy_scan_run_button.clicked.connect(xy_scan_resolution_validation_fnc) # this framework is limited currently to only validating resolution

        #######################################################################################
        ####################################### XZ scanning ###################################
        #######################################################################################

        xz_scan_widgets_left_x_justify = 130

        # scan widget 2 "XZ"
        scan_widget_2 = QLabel("XZ scan", self)
        scan_widget_2.setParent(self.left_window)
        scan_widget_2.move(145 + 5, indiv_scan_labels_y_height + overall_y_adjust)

        # resolution
        xz_scan_resolution_widget = QLabel("Res:", self) # widget
        xz_scan_resolution_widget.setParent(self.left_window)
        xz_scan_resolution_widget.move(xz_scan_widgets_left_x_justify, 40 + row_y_adjust + overall_y_adjust)

        xz_scan_resolution_qlineedit = QLineEdit(self) # qclineedit
        xz_scan_resolution_qlineedit.setParent(self.left_window)
        xz_scan_resolution_qlineedit.move(25 + xz_scan_widgets_left_x_justify, 40 + row_y_adjust + overall_y_adjust)
        xz_scan_resolution_qlineedit.resize(55, 15)
        xz_scan_resolution_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        # read time
        xz_scan_read_time_widget = QLabel("APD_t:", self) # widget
        xz_scan_read_time_widget.setParent(self.left_window)
        xz_scan_read_time_widget.move(xz_scan_widgets_left_x_justify, 65 + row_y_adjust + overall_y_adjust)

        xz_scan_read_time_qlineedit = QLineEdit(self) # qclineedit
        xz_scan_read_time_qlineedit.setParent(self.left_window)
        xz_scan_read_time_qlineedit.move(35 + xz_scan_widgets_left_x_justify, 65 + row_y_adjust + overall_y_adjust)
        xz_scan_read_time_qlineedit.resize(45, 15)
        xz_scan_read_time_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)
        
        # x voltage (min and max)
        xz_scan_x_voltage_min_widget = QLabel("x_V_min:", self) # widget
        xz_scan_x_voltage_min_widget.setParent(self.left_window)
        xz_scan_x_voltage_min_widget.move(xz_scan_widgets_left_x_justify, 90 + row_y_adjust + overall_y_adjust)

        xz_scan_x_voltage_min_qlineedit = QLineEdit(self) # qclineedit
        xz_scan_x_voltage_min_qlineedit.setParent(self.left_window)
        xz_scan_x_voltage_min_qlineedit.move(45 + xz_scan_widgets_left_x_justify, 90 + row_y_adjust + overall_y_adjust)
        xz_scan_x_voltage_min_qlineedit.resize(35, 15)
        xz_scan_x_voltage_min_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        xz_scan_x_voltage_max_widget = QLabel("x_V_max:", self) # widget
        xz_scan_x_voltage_max_widget.setParent(self.left_window)
        xz_scan_x_voltage_max_widget.move(xz_scan_widgets_left_x_justify, 115 + row_y_adjust + overall_y_adjust)

        xz_scan_x_voltage_max_qlineedit = QLineEdit(self) # qclineedit
        xz_scan_x_voltage_max_qlineedit.setParent(self.left_window)
        xz_scan_x_voltage_max_qlineedit.move(50 + xz_scan_widgets_left_x_justify, 115 + row_y_adjust + overall_y_adjust)
        xz_scan_x_voltage_max_qlineedit.resize(30, 15)
        xz_scan_x_voltage_max_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        # y voltage single setting
        xz_scan_y_voltage_widget = QLabel("y_V:", self) # widget
        xz_scan_y_voltage_widget.setParent(self.left_window)
        xz_scan_y_voltage_widget.move(xz_scan_widgets_left_x_justify, 140 + row_y_adjust + overall_y_adjust)

        xz_scan_y_voltage_qlineedit = QLineEdit(self) # qclineedit
        xz_scan_y_voltage_qlineedit.setParent(self.left_window)
        xz_scan_y_voltage_qlineedit.move(25 + xz_scan_widgets_left_x_justify, 140 + row_y_adjust + overall_y_adjust)
        xz_scan_y_voltage_qlineedit.resize(55, 15)
        xz_scan_y_voltage_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)
                                
        # z piezo (min and max)
        xz_scan_z_piezo_min_voltage_widget = QLabel("z_V_min:", self) # widget
        xz_scan_z_piezo_min_voltage_widget.setParent(self.left_window)
        xz_scan_z_piezo_min_voltage_widget.move(xz_scan_widgets_left_x_justify, 165 + row_y_adjust + overall_y_adjust)

        xz_scan_z_piezo_min_voltage_qlineedit = QLineEdit(self) # qclineedit
        xz_scan_z_piezo_min_voltage_qlineedit.setParent(self.left_window)
        xz_scan_z_piezo_min_voltage_qlineedit.move(45 + xz_scan_widgets_left_x_justify, 165 + row_y_adjust + overall_y_adjust)
        xz_scan_z_piezo_min_voltage_qlineedit.resize(35, 15)
        xz_scan_z_piezo_min_voltage_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        xz_scan_z_piezo_max_voltage_widget = QLabel("z_V_max:", self) # widget
        xz_scan_z_piezo_max_voltage_widget.setParent(self.left_window)
        xz_scan_z_piezo_max_voltage_widget.move(xz_scan_widgets_left_x_justify, 190 + row_y_adjust + overall_y_adjust)

        xz_scan_z_piezo_max_voltage_qlineedit = QLineEdit(self) # qclineedit
        xz_scan_z_piezo_max_voltage_qlineedit.setParent(self.left_window)
        xz_scan_z_piezo_max_voltage_qlineedit.move(50 + xz_scan_widgets_left_x_justify, 190 + row_y_adjust + overall_y_adjust)
        xz_scan_z_piezo_max_voltage_qlineedit.resize(30, 15)
        xz_scan_z_piezo_max_voltage_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        # run xz scan button
        xz_scan_run_button = QPushButton("run\nXZ scan", self) # button
        xz_scan_run_button.setParent(self.left_window)
        xz_scan_run_button.resize(60, 40)
        xz_scan_run_button.move(10 + xz_scan_widgets_left_x_justify, 215 + row_y_adjust + overall_y_adjust)
        xz_scan_run_button.clicked.connect(xz_scan_resolution_validation_fnc) # this framework is limited currently to only validating resolution

        #####################################################################################
        ####################################### YZ scanning #################################
        #####################################################################################

        yz_scan_widgets_left_x_justify = 255

        # scan widget 3 "YZ"
        scan_widget_3 = QLabel("YZ scan", self)
        scan_widget_3.setParent(self.left_window)
        scan_widget_3.move(265 + 14, indiv_scan_labels_y_height + overall_y_adjust)

        # resolution
        yz_scan_resolution_widget = QLabel("Res:", self) # widget
        yz_scan_resolution_widget.setParent(self.left_window)
        yz_scan_resolution_widget.move(yz_scan_widgets_left_x_justify, 40 + row_y_adjust + overall_y_adjust)

        yz_scan_resolution_qlineedit = QLineEdit(self) # qclineedit
        yz_scan_resolution_qlineedit.setParent(self.left_window)
        yz_scan_resolution_qlineedit.move(25 + yz_scan_widgets_left_x_justify, 40 + row_y_adjust + overall_y_adjust)
        yz_scan_resolution_qlineedit.resize(55, 15)
        yz_scan_resolution_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        # read time
        yz_scan_read_time_widget = QLabel("APD_t:", self) # widget
        yz_scan_read_time_widget.setParent(self.left_window)
        yz_scan_read_time_widget.move(yz_scan_widgets_left_x_justify, 65 + row_y_adjust + overall_y_adjust)

        yz_scan_read_time_qlineedit = QLineEdit(self) # qclineedit
        yz_scan_read_time_qlineedit.setParent(self.left_window)
        yz_scan_read_time_qlineedit.move(35 + yz_scan_widgets_left_x_justify, 65 + row_y_adjust + overall_y_adjust)
        yz_scan_read_time_qlineedit.resize(45, 15)
        yz_scan_read_time_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)
        
        # y voltage (min and max)
        yz_scan_y_voltage_min_widget = QLabel("y_V_min:", self) # widget
        yz_scan_y_voltage_min_widget.setParent(self.left_window)
        yz_scan_y_voltage_min_widget.move(yz_scan_widgets_left_x_justify, 90 + row_y_adjust + overall_y_adjust)

        yz_scan_y_voltage_min_qlineedit = QLineEdit(self) # qclineedit
        yz_scan_y_voltage_min_qlineedit.setParent(self.left_window)
        yz_scan_y_voltage_min_qlineedit.move(45 + yz_scan_widgets_left_x_justify, 90 + row_y_adjust + overall_y_adjust)
        yz_scan_y_voltage_min_qlineedit.resize(35, 15)
        yz_scan_y_voltage_min_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        yz_scan_y_voltage_max_widget = QLabel("y_V_max:", self) # widget
        yz_scan_y_voltage_max_widget.setParent(self.left_window)
        yz_scan_y_voltage_max_widget.move(yz_scan_widgets_left_x_justify, 115 + row_y_adjust + overall_y_adjust)

        yz_scan_y_voltage_max_qlineedit = QLineEdit(self) # qclineedit
        yz_scan_y_voltage_max_qlineedit.setParent(self.left_window)
        yz_scan_y_voltage_max_qlineedit.move(50 + yz_scan_widgets_left_x_justify, 115 + row_y_adjust + overall_y_adjust)
        yz_scan_y_voltage_max_qlineedit.resize(30, 15)
        yz_scan_y_voltage_max_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        # x voltage single setting
        yz_scan_x_voltage_widget = QLabel("x_V:", self) # widget
        yz_scan_x_voltage_widget.setParent(self.left_window)
        yz_scan_x_voltage_widget.move(yz_scan_widgets_left_x_justify, 140 + row_y_adjust + overall_y_adjust)

        yz_scan_x_voltage_qlineedit = QLineEdit(self) # qclineedit
        yz_scan_x_voltage_qlineedit.setParent(self.left_window)
        yz_scan_x_voltage_qlineedit.move(25 + yz_scan_widgets_left_x_justify, 140 + row_y_adjust + overall_y_adjust)
        yz_scan_x_voltage_qlineedit.resize(55, 15)
        yz_scan_x_voltage_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)
                                
        # z piezo (min and max)
        yz_scan_z_piezo_min_voltage_widget = QLabel("z_V_min:", self) # widget
        yz_scan_z_piezo_min_voltage_widget.setParent(self.left_window)
        yz_scan_z_piezo_min_voltage_widget.move(yz_scan_widgets_left_x_justify, 165 + row_y_adjust + overall_y_adjust)

        yz_scan_z_piezo_min_voltage_qlineedit = QLineEdit(self) # qclineedit
        yz_scan_z_piezo_min_voltage_qlineedit.setParent(self.left_window)
        yz_scan_z_piezo_min_voltage_qlineedit.move(45 + yz_scan_widgets_left_x_justify, 165 + row_y_adjust + overall_y_adjust)
        yz_scan_z_piezo_min_voltage_qlineedit.resize(35, 15)
        yz_scan_z_piezo_min_voltage_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        yz_scan_z_piezo_max_voltage_widget = QLabel("z_V_max:", self) # widget
        yz_scan_z_piezo_max_voltage_widget.setParent(self.left_window)
        yz_scan_z_piezo_max_voltage_widget.move(yz_scan_widgets_left_x_justify, 190 + row_y_adjust + overall_y_adjust)

        yz_scan_z_piezo_max_voltage_qlineedit = QLineEdit(self) # qclineedit
        yz_scan_z_piezo_max_voltage_qlineedit.setParent(self.left_window)
        yz_scan_z_piezo_max_voltage_qlineedit.move(50 + yz_scan_widgets_left_x_justify, 190 + row_y_adjust + overall_y_adjust)
        yz_scan_z_piezo_max_voltage_qlineedit.resize(30, 15)
        yz_scan_z_piezo_max_voltage_qlineedit.setAlignment(PyQt5.QtCore.Qt.AlignRight)

        # run yz scan button
        yz_scan_run_button = QPushButton("run\nYZ scan", self) # button
        yz_scan_run_button.setParent(self.left_window)
        yz_scan_run_button.resize(60, 40)
        yz_scan_run_button.move(15 + yz_scan_widgets_left_x_justify, 215 + row_y_adjust + overall_y_adjust)
        yz_scan_run_button.clicked.connect(yz_scan_resolution_validation_fnc) # this framework is limited currently to only validating resolution

####################################################################### context menu ######################################################################

    def contextMenuEvent(self, event): # context (right-click) menu

        cmenu = QMenu(self)
        cmenuoneAct = cmenu.addAction("one")
        cmenutwoAct = cmenu.addAction("two")
        cmenuthreeAct = cmenu.addAction("three")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
