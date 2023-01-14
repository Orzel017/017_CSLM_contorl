"""
Made: 01-14-2023
"""

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