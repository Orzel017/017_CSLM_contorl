"""
File name: "xy_scan.py"

Contents: scannign script for taking an xy image

Dates:
File originally made during summer 2022
File originally transitioned to new GUI: 01-14-202
Last modifed: 04-7-2023
Original author: MDA
Last modified by: MDA

Notes:
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

TODO:

"""

######################################################################################## start package imports ########################################################################################

import nidaqmx # import National Instruments (NI) DAQmx API package

import numpy # import numpy package

import sys

import path

current_file_directory = path.Path(__file__).abspath() # access current file's directory in folder structure

sys.path.append(current_file_directory.parent.parent.parent) # append triple parent of current file (in folder structure)

from GUI.Pages import XY_Scan_Page

from GUI import GUI_Window_Contents

########################################################################################## end package imports ########################################################################################

def run_xy_scan_script():
    return 4

# creating the function to take and xy iamge based on user parameters
def run_xy_scan_script_two(): # define the function/script 

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
        array_size = 3 # designate the array size for the completed image data
        data_array = numpy.zeros((array_size, array_size)) # create an empty data array according to `array_size``

        initial_x_driving_voltage = -0.25
        initial_y_driving_voltage = -0.35
        desired_end_x_mirror_voltage = 0.35
        desired_end_y_mirror_voltage = 0.25

        x_driving_voltage_to_change = round(initial_x_driving_voltage, 5)
        y_driving_voltage_to_change = round(initial_y_driving_voltage, 5)
        x_drive_voltage_step = round(((numpy.absolute(initial_x_driving_voltage)) + (desired_end_x_mirror_voltage)) / array_size, 5)
        y_drive_voltage_step = round(((numpy.absolute(initial_y_driving_voltage)) + (desired_end_y_mirror_voltage)) / array_size, 5)

        x_mirror_task.write(0.0)
        y_mirror_task.write(0.0)
        output_value = 0

        ################################################################################ end script prelimaries #######################################################################################

        for f in range(array_size): # rows

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









#             ##################### updating plot section ####################
#             # self.sc.axes.cla() # this does not seem to be needed

#             self.sc.axes.pcolormesh(xy_scan_data_array, cmap = "pink")
#             self.sc.axes.set_xticks(np.arange(0, grid_size + 10, grid_size / 2), [initial_x_driving_voltage, int((initial_x_driving_voltage + desired_end_x_mirror_voltage) / 2), desired_end_x_mirror_voltage])
#             self.sc.axes.set_yticks(np.arange(0, grid_size + 10, grid_size / 2), [initial_y_driving_voltage, int((initial_y_driving_voltage + desired_end_y_mirror_voltage) / 2), desired_end_y_mirror_voltage])
#             self.sc.axes.xaxis.set_tick_params(labelsize = 6)
#             self.sc.axes.yaxis.set_tick_params(labelsize = 6)

#             self.sc.axes.set_xlabel("x_mirror_driving_voltage_(V)", fontsize = 6, labelpad = -2)
#             self.sc.axes.set_ylabel("y_mirror_driving_voltage_(V)", fontsize = 6, labelpad = -9)

#             self.sc.figure.canvas.draw()
#             self.sc.figure.canvas.flush_events() # this line is very important
#             ##################### updating plot section ####################

#             if f < (grid_size_y - 1): # this loop prevents from scanning an upper undesired row

#                 y_driving_voltage_to_change += y_drive_voltage_step # increment drive voltage
#                 y_driving_voltage_to_change = roun(y_driving_voltage_to_change, 5)
#                 scan_galvo.voltage_cdaq1mod2ao1(y_driving_voltage_to_change) # step y motor

#             else:
#                 break

#         internal_clock_task.stop() # this stops the counter NI-DAQmx task - free-ing the reserved cDAQ card resources
#         input_counter_task.stop() # this stops the hardware-based internal clock NI-DAQmx task - free-ing the reserved cDAQ card resources

#     scan_galvo.close() # this is where reeated scanning hinges on and needs to be re-implemented

#     ############################################################### end scanning script #############################################################################################

#     ############################################### plotting XY scan data in plot ####################################################
    
#     # self.sc.figure.clear() # is this needed after implementing live plot updating?
    # self.output_plot_area.axes.cla()
    # XY_Scan_Page.child.do_something_to_plot(self)

    # GUI_Window_Contents.Build_GUI_Constant_Contents.temp_plot_area.axes.pcolormesh(data_array, cmap = "pink")

    # plot = self.output_plot_area.axes.pcolormesh(data_array, cmap = "pink")
#     self.sc.axes.set_xticks(np.arange(0, grid_size + 10, grid_size / 2), [initial_x_driving_voltage, int((initial_x_driving_voltage + desired_end_x_mirror_voltage) / 2), desired_end_x_mirror_voltage])
#     self.sc.axes.set_yticks(np.arange(0, grid_size + 10, grid_size / 2), [initial_y_driving_voltage, int((initial_y_driving_voltage + desired_end_y_mirror_voltage) / 2), desired_end_y_mirror_voltage])
    
#     # self.xy_scan_plot_colorbar = self.sc.figure.colorbar(plot, ax = self.sc.axes, pad = -2, shrink = 0.5, aspect = 15)
#     # self.xy_scan_plot_colorbar.formatter.set_powerlimits((0, 0))
    
#     self.sc.axes.xaxis.set_tick_params(labelsize = 6)
#     self.sc.axes.yaxis.set_tick_params(labelsize = 6)
#     # self.xy_scan_plot_colorbar.ax.tick_params(labelsize = 3)
#     self.sc.axes.set_xlabel("x_mirror_driving_voltage_(V)", fontsize = 6, labelpad = -2)
#     self.sc.axes.set_ylabel("y_mirror_driving_voltage_(V)", fontsize = 6, labelpad = -9)
#     self.sc.axes.set_title("XY_scan_%s_z-piezo@%d_microns" % (todays_date, int((z_piezo_set_voltage * 10))), fontsize = 6)
    # self.output_plot_area.draw()

#     most_recent_data_array = xy_scan_data_array # make temp holding global data_array the same as xy_scan_data_array
    return data_array
