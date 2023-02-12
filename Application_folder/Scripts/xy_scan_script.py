"""
File name: "xy_scan.py"

Contents: scannign script for taking an xy image

Dates:
File originally made during summer 2022
File originally transitioned to new GUI: 01-14-202
Last modifed: 02-12-2023
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

# run XY scanning function
def run_xy_scan_script(): # this fnc runs the xy_scan per the user-entered parameters in the xy_scan qlineedits

    print("Hello world!")

#     ############################################################### begin scanning script #############################################################################################
        
#     ################################################################################## card 2 (AO) ########################################################################

#     # naming the instrument
#     scan_galvo_card_name = "cDAQ1Mod2"

#     # dictionary of analog output channels
#     scan_galvo_ao_channels = {f'{scan_galvo_card_name}/ao{i}': i for i in range(4)}

#     # defining the instrument (ni_9263)
#     scan_galvo = test.DAQAnalogOutputs("name_two", scan_galvo_card_name, scan_galvo_ao_channels)

#     ############################################################################### def other variables #####################################################################

#     ################### setting variales and array ####################

#     # counter read time:
#     scan_counter_acquisition_time = float(xy_scan_read_time_qlineedit.text())                          # note a reading time <0.05 s is likely too short

#     # def
#     grid_size = int(xy_scan_resolution_qlineedit.text())
#     grid_size_x = grid_size_y = grid_size

#     # def the initial driving voltage for the x-mirror
#     initial_x_driving_voltage = round(float(xy_scan_x_voltage_min_qlineedit.text()), 2)
#     # def the initial driving voltage for the y-mirror
#     initial_y_driving_voltage = round(float(xy_scan_y_voltage_min_qlineedit.text()), 2)

#     z_piezo_set_voltage = round(float(xy_scan_z_piezo_voltage_qlineedit.text()), 2)

#     # setup parameter for the program to use based on defined variables
#     x_driving_voltage_to_change = initial_x_driving_voltage
#     y_driving_voltage_to_change = initial_y_driving_voltage

#     # set desired end mirror voltages
#     desired_end_x_mirror_voltage = round(float(xy_scan_x_voltage_max_qlineedit.text()), 2)
#     desired_end_y_mirror_voltage = round(float(xy_scan_y_voltage_max_qlineedit.text()), 2)

#     # def the internal stepping voltages based on user-entered settings above
#     x_drive_voltage_step = round(((np.absolute(initial_x_driving_voltage)) + (desired_end_x_mirror_voltage)) / grid_size_x, 5
#     y_drive_voltage_step = round((np.absolute(initial_y_driving_voltage)) + (desired_end_y_mirror_voltage)) / grid_size_y, 5)

#     # create dataset to populate
#     global xy_scan_data_array
#     xy_scan_data_array = np.zeros((grid_size_x, grid_size_y))
#     global most_recent_data_array
#     most_recent_data_array = np.zeros((grid_size_x, grid_size_y))

#     # initializing variables to store read counter info.
#     output_value = 0
#     counter_value = 0

#     ################### resetting position of mirrors ####################

#     scan_galvo.voltage_cdaq1mod2ao0(initial_x_driving_voltage) # this is for the x-mirror

#     scan_galvo.voltage_cdaq1mod2ao1(initial_y_driving_voltage) # this is for the y-mirror

#     scan_galvo.voltage_cdaq1mod2ao2(z_piezo_set_voltage) # setting the z_piezo to z_piezo_set_voltage microns

#     ########################################################### setting up NI-DAQmx tasks and channels for counting ########################################################

#     with nidaqmx.Task() as task1, nidaqmx.Task() as counter_output_task: # this defines 2 NI-DAQmx tasks (one for the counter and one for the counter's clock)

#         # adding dig pulse train chan
#         counter_output_task.co_channels.add_co_pulse_chan_freq(
#             counter = "cDAQ1Mod1/ctr1",
#             name_to_assign_to_channel = "",
#             units = nidaqmx.constants.FrequencyUnits.HZ,
#             idle_state = nidaqmx.constants.Level.LOW,
#             initial_delay = 0.0,
#             freq = 1000,
#             duty_cycle = 0.50
#             )

#         # cfg implict timing
#         counter_output_task.timing.cfg_implicit_timing(
#             sample_mode = AcquisitionType.CONTINUOUS,
#             samps_per_chan = 1000000
#             )

#         # adding count egdes chan
#         task1.ci_channels.add_ci_count_edges_chan(
#             counter = "cDAQ1Mod1/ctr0",
#             name_to_assign_to_channel = "",
#             edge = nidaqmx.constants.Edge.RISING,
#             initial_count = 0,
#             count_direction = nidaqmx.constants.CountDirection.COUNT_UP
#             )

#         # cfg sample clk timing
#         task1.timing.cfg_samp_clk_timing(
#             rate = 1000,
#             source = "/cDAQ1/Ctr1InternalOutput",
#             active_edge = nidaqmx.constants.Edge.RISING,
#             sample_mode = AcquisitionType.CONTINUOUS,
#             samps_per_chan = 1000000
#             )
        
#         counter_output_task.start() # this starts the counter NI-DAQmx task
#         task1.start() # this starts the hardware-based internal clock NI-DAQmx task
                        
#     ######################################################################## X and Y scanning #########################################################################

#         for f in range(grid_size_y): # this loops for rows (y)

#             for k in range(grid_size_x): # this loops for columns (x)

#                 ################## important section #################

#                 for my_var_not_named_i in range(int(scan_counter_acquisition_time * 1000)): # this reads/lets the counter accumulate for the set time and returns value
#                     counter_value = task1.read()
#                     output_value += counter_value

#                 if f % 2 != 0: # this loop populates the created xy_scan_data_array (the if else strucuture is present bc of the snaking scanning pattern)
#                     xy_scan_data_array[f][((-k) + 1)] = (output_value - np.sum(xy_scan_data_array)) # add counter result to data array                           # saving (082422)
#                     output_value == 0
#                     counter_value == 0
#                 else:
#                     if f == 0 and k == 0:
#                         xy_scan_data_array[0][0] = output_value # add counter result to data array                                                      # saving
#                     else:
#                         xy_scan_data_array[f][k] = (output_value - np.sum(xy_scan_data_array)) # add counter result to data array                               # saving (082422)
#                 output_value = 0
#                 counter_value = 0

#                 ############# end important section ############

#                 if f % 2 == 0: # this loop adjusts for sweeping back and forth along each alternating row

#                     if k < (grid_size_x - 1):

#                         x_driving_voltage_to_change += x_drive_voltage_step # increment drive voltage forwards
#                         x_driving_voltage_to_change = round(x_driving_voltage_to_change, 5)
#                         scan_galvo.voltage_cdaq1mod2ao0(x_driving_voltage_to_change) # step x motor

#                     else:
#                         break
#                 else:
#                     if k < (grid_size_x - 1):

#                         x_driving_voltage_to_change -= x_drive_voltage_step # increment drive voltage backwards
#                         x_driving_voltage_to_change = round(x_driving_voltage_to_change, 5)
#                         scan_galvo.voltage_cdaq1mod2ao0(x_driving_voltage_to_change) # step x motor

#                     else:
#                         break

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
#             self.sc.figure.canvas.flush_events() #this line is very important
#             ##################### updating plot section ####################

#             if f < (grid_size_y - 1): # this loop prevents from scanning an upper undesired row

#                 y_driving_voltage_to_change += y_drive_voltage_step # increment drive voltage
#                 y_driving_voltage_to_change = roun(y_driving_voltage_to_change, 5)
#                 scan_galvo.voltage_cdaq1mod2ao1(y_driving_voltage_to_change) # step y motor

#             else:
#                 break

#         counter_output_task.stop() # this stops the counter NI-DAQmx task - free-ing the reserved cDAQ card resources
#         task1.stop() # this stops the hardware-based internal clock NI-DAQmx task - free-ing the reserved cDAQ card resources

#     scan_galvo.close() # this is where reeated scanning hinges on and needs to be re-implemented

#     ############################################################### end scanning script #############################################################################################

#     ############################################### plotting XY scan data in plot ####################################################
    
#     # self.sc.figure.clear() # is this needed after implementing live plot updating?
#     self.sc.axes.cla()

#     plot = self.sc.axes.pcolormesh(xy_scan_data_array, cmap = "pink")
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
#     self.sc.draw()

#     most_recent_data_array = xy_scan_data_array # make temp holding global data_array the same as xy_scan_data_array
