"""
File name: "Helper_Functions.py"

Contents: multiple helper fuctions for use within multiple files

Dates:
Originally created: 12-30-2022
Last modifed: 05-01-2023
Original author: MDA
Last modified by: MDA

Notes: there seems to be no reason to separate these functions any further than accessing them all from one file (this file)

TODO:
*
"""

############################################################################################## start imports ##########################################################################################

import os # generic os module import

import numpy # numpy package for data array and saving

import pandas # pandas package for data array manipulation

############################################################################################# end imports #############################################################################################

########################################################################################## start functions ############################################################################################

def save_raw_image_data_function(address_to_save_raw_image_data, desktop_destination_check_box_state): # define the raw image data saving function (biased to numpy file extension)

    """
    This function saves the raw image data to a user-named file. It can be saved to a variety of destinations including the desktop and documents folders.
    """

    if len(address_to_save_raw_image_data) == 0:

        print("Error")
    
    else:

        # tuning user-input address type to be string
        if type(address_to_save_raw_image_data) != str: # get cases for when user-input is not string

            passing_address_to_save_raw_image_data = str(address_to_save_raw_image_data) # convert user-input file name to string

        else: # catch remaining cases
            passing_address_to_save_raw_image_data = address_to_save_raw_image_data # re-cast file name name

        # section to assemble desired file path to desired folder on computer (functionality extended to different machines)
        computer_path_to_desktop_string = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop") # obtain path to Desktop

        force_directory_slash_string = "\\" # initialize slash string for path assembly

        force_numpy_file_extension_string = ".npy" # initialize numpy file extension for path assembly

        # create the final saving address
        final_saving_address = computer_path_to_desktop_string + force_directory_slash_string + passing_address_to_save_raw_image_data + force_numpy_file_extension_string

        # completing data array converison for saving
        read_csv_data_array = pandas.read_csv("Application_folder\image_data_file.csv", sep = ',', header = None)

        converted_read_csv_data_array = numpy.array(read_csv_data_array) # cast the read csv data (via pandas) to numpy array

        numpy.save(final_saving_address, converted_read_csv_data_array) # saving the actual file

########################################################################################### end functions #############################################################################################

# # display invalid resolution error window fnc
# def display_resolution_error_window_fnc(): # this fnc calls the "Make_Error_Window" class to display an eror message indicating user input is not validated
#     self.Make_Error_Window = Make_Error_Window()
#     self.Make_Error_Window.show()

# # display invalid saving address error window fnc   
# def display_save_address_length_error_window_fnc(): # this fnc calls the "Make_Error_Window" class to display an eror message indicating user input is not validated
#     self.Make_Error_Window_2 = Make_Error_Window_2()
#     self.Make_Error_Window_2.show()

# # save most recent scan data fnc
# def save_scan_data_fnc(): # this fnc works for any scanning script

#     """
#     How this works/applies to each scanning script:
#     In any scanning script (XY, XZ, and YZ), a data_array is created according to the user-specified grid_size. It is a Numpy array of zeros that will be
#     populated throughout the scanning program as it progresses. At the same time of that data-array created a global variable called "most_recent_data_array"
#     is created and is then set to the same size matching the scan-specific data_array. At the end of the scanning scipt this temporary data array is matched to
#     the scan's specific data array, value for value. Now "most_recent-data_array" is called (since it is defined to be Global) below for saving. This
#     """

#     saving_scan_error_bool = False # setting up a bool value for error checking below

#     print("save_scan_data_fnc called")                                               # delete later
#     print("@address :" + save_scan_data_qlineedit.text())                                               # delete later

#     # while loop for error checking if address to save data at has length > 0
#     while saving_scan_error_bool is False:

#         if len(str(save_scan_data_qlineedit.text())) == 0: # checking if length of specified saving address is > 0

#             # print("EXCEPTION!")                                                       # safe to delete
#             display_save_address_length_error_window_fnc()                              # fix to new window. Only a test now
#             break # condition remains False; not saved; exit

#         elif len(str(save_scan_data_qlineedit.text())) > 0: # checking the length of the specified address is greater than 0

#             saving_scan_error_bool == True # adjusting the value of the current bool to True
#             address_to_save_scan_data_at = save_scan_data_qlineedit.text() # creating a variable as the specified (now error-checked) address
#             np.save(str(address_to_save_scan_data_at), most_recent_data_array) # saving the correct data array
#             print("saved")
#             break # data has been successfully save; so exit checking loop

# # print/display XY scan parameters fnc
# def print_XY_scan_parameters_fnc(self, parent = Setup_Main_Window_Contents): # this fnc does...

#     # print("XY_SCAN PARAMETERS/INFO: ", end = "")                                    # this prints to the terminal
#     # print("XY_scan resolution = %d, " % int(xy_scan_resolution_qlineedit.text()), end = "")
#     # print("XY_scan counter read time = %2f, " % round(float(xy_scan_read_time_qlineedit.text()), 2), end = "")
#     # print("XY_scan min x driving voltage = %2f, " % float(xy_scan_x_voltage_min_qlineedit.text()), end = "")
#     # print("XY_scan max x driving voltage = %2f, " % float(xy_scan_x_voltage_max_qlineedit.text()), end = "")
#     # print("XY_scan min y driving voltage = %2f, " % float(xy_scan_y_voltage_min_qlineedit.text()), end = "")
#     # print("XY_scan max y driving voltage = %2f, " % float(xy_scan_y_voltage_max_qlineedit.text()), end = "")
#     # print("XY_scan z-piezo driving voltage = %2f." % float(xy_scan_z_piezo_voltage_qlineedit.text()))

#     # need to clear text box first
#     parameters_dsiplay_text_box.clear()

#     # this prints to the QTextBox in the left_window. The output of the user-selected scan parameters is printed below
#     parameters_dsiplay_text_box.setPlainText(
#                                                 "XY_SCAN PARAMETERS/INFO:\n"
#                                                 "XY_scan resolution = " + str(int(xy_scan_resolution_qlineedit.text())) + "\n"
#                                                 "XY_scan counter read time = " + str(float(xy_scan_read_time_qlineedit.text())) + "\n"
#                                                 "XY_scan min x driving voltage = " + str(float(xy_scan_x_voltage_min_qlineedit.text())) + "\n"
#                                                 "XY_scan max x driving voltage = " + str(float(xy_scan_x_voltage_max_qlineedit.text())) + "\n"
#                                                 "XY_scan min y driving voltage = " + str(float(xy_scan_y_voltage_min_qlineedit.text())) + "\n"
#                                                 "XY_scan max y driving voltage = " + str(float(xy_scan_y_voltage_max_qlineedit.text())) + "\n"
#                                                 "XY_scan z-piezo driving voltage = " + str(float(xy_scan_z_piezo_voltage_qlineedit.text()))
#                                                 )

# xy_scan resolution check then run fnc
def start_xy_image():

    function_output = STOP_xy_scan_script.run_xy_scan_script()

    return function_output

#     self.sc.axes.cla()

#     # the try-except frameworks are used to refresh the plotted figures -removing the color bars associated with a previous plotted data
#     try:
#         self.xy_scan_plot_colorbar.remove()

#     except (AttributeError, ValueError):
#         pass

#     try:
#         self.yz_scan_plot_colorbar.remove()

#     except (AttributeError, ValueError):
#         pass

#     try:
#         self.xz_scan_plot_colorbar.remove()
    
#     except (AttributeError, ValueError):
#         pass

# #################################### resolution checking ##################################

#     res_min_condition = 20 # set the min allowed resolution for scanning
#     res_max_condition = 2000 # set the max allowed resolution for scanning

#     xy_scan_resolution_test_condition = False # define resolution validation bool for xy scan

#     while xy_scan_resolution_test_condition is False: # this initiates checking the resolution parameter

#         # checking for out of bounds of min and max conditions above
#         # TODO: or negative or not a number or too large
#         if int(xy_scan_resolution_qlineedit.text()) < res_min_condition or int(xy_scan_resolution_qlineedit.text()) > res_max_condition:

#             display_resolution_error_window_fnc() # call the error message pop-up window
#             break # exit the checking loop: failed

#         # if parameter is in bounds; run scan
#         elif int(xy_scan_resolution_qlineedit.text()) >= res_min_condition and int(xy_scan_resolution_qlineedit.text()) <= res_max_condition:

#             xy_scan_resolution_test_condition == True
#             print_XY_scan_parameters_fnc(self) # call the print user-entered parameters fnc
#             run_xy_scan_fnc() # call the run xy scan method fnc
#             break # exit the checking loop: passed

# # print_XZ_scan_parameters_fnc
# def print_XZ_scan_parameters_fnc(self, parent = Setup_Main_Window_Contents): # this fnc does...

#     # print("XZ_SCAN PARAMETERS/INFO: ", end = "")                                    # this prints to the terminal
#     # print("XZ_scan resolution = %d, " % int(xz_scan_resolution_qlineedit.text()), end = "")
#     # print("XZ_scan counter read time = %2f, " % round(float(xz_scan_read_time_qlineedit.text()), 2), end = "")
#     # print("XZ_scan min x driving voltage = %2f, " % float(xz_scan_x_voltage_min_qlineedit.text()), end = "")
#     # print("XZ_scan max x driving voltage = %2f, " % float(xz_scan_x_voltage_max_qlineedit.text()), end = "")
#     # print("XZ_scan y driving voltage = %2f, " % float(xz_scan_y_voltage_qlineedit.text()), end = "")
#     # print("XZ_scan z-piezo min driving voltage = %2f, " % float(xz_scan_z_piezo_min_voltage_qlineedit.text()), end = "")
#     # print("XZ_scan z-piezo max driving voltage = %2f." % float(xz_scan_z_piezo_max_voltage_qlineedit.text()))


#     # need to clear text box first
#     self.parameters_dsiplay_text_box.clear()

#     # this prints to the QTextBox in the left_window. The output of the user-selected scan parameters is printed below
#     self.parameters_dsiplay_text_box.setPlainText(
#                                                 "XZ_SCAN PARAMETERS/INFO:\n"
#                                                 "XZ_scan resolution = " + str(int(xz_scan_resolution_qlineedit.text())) + "\n"
#                                                 "XZ_scan counter read time = " + str(float(xz_scan_read_time_qlineedit.text())) + "\n"
#                                                 "XZ_scan min x driving voltage = " + str(float(xz_scan_x_voltage_min_qlineedit.text())) + "\n"
#                                                 "XZ_scan max x driving voltage = " + str(float(xz_scan_x_voltage_max_qlineedit.text())) + "\n"
#                                                 "XZ_scan y driving voltage = " + str(float(xz_scan_y_voltage_qlineedit.text())) + "\n"
#                                                 "XZ_scan z-piezo min driving voltage = " + str(float(xz_scan_z_piezo_min_voltage_qlineedit.text())) + "\n"
#                                                 "XZ_scan z-piezo max driving voltage = " + str(float(xz_scan_z_piezo_max_voltage_qlineedit.text()))
#                                                 )

# # xz_scan resolution check then run fnc
# def xz_scan_resolution_validation_fnc():

#     self.sc.axes.cla()

#     try:
#         self.xz_scan_plot_colorbar.remove()

#     except (AttributeError, ValueError):
#         pass

#     try:
#         self.yz_scan_plot_colorbar.remove()

#     except (AttributeError, ValueError):
#         pass
    
#     try:
#         self.xy_scan_plot_colorbar.remove()
    
#     except (AttributeError, ValueError):
#         pass

#     res_min_condition = 20 # set the min allowed resolution for scanning
#     res_max_condition = 900 # set the max allowed resolution for scanning

#     xz_scan_resolution_test_condition = False # define resolution validation bool for xz scan

#     while xz_scan_resolution_test_condition is False: # this initiates checking the resolution parameter

#         # checking for out of bounds of min and max conditions above
#         if int(xz_scan_resolution_qlineedit.text()) < res_min_condition or int(xz_scan_resolution_qlineedit.text()) > res_max_condition: # TODO: or negative or not a number or too large

#             display_resolution_error_window_fnc() # call the error message pop-up window
#             break # exit the checking loop: failed

#         # if parameter is in bounds; run scan
#         elif int(xz_scan_resolution_qlineedit.text()) >= res_min_condition and int(xz_scan_resolution_qlineedit.text()) <= res_max_condition:

#             xz_scan_resolution_test_condition == True
#             print_XZ_scan_parameters_fnc(self) # call the print user-entered parameters fnc
#             run_xz_scan_fnc() # call the run xz scan method fnc
#             break # exit the checking loop: passed

# # print_YZ_scan_parameters_fnc
# def print_YZ_scan_parameters_fnc(self, parent = Setup_Main_Window_Contents): # this fnc does...

#     # print("YZ_SCAN PARAMETERS/INFO: ", end = "")
#     # print("YZ_scan resolution = %d, " % int(yz_scan_resolution_qlineedit.text()), end = "")
#     # print("YZ_scan counter read time = %2f, " % round(float(yz_scan_read_time_qlineedit.text()), 2), end = "")
#     # print("YZ_scan min Y driving voltage = %2f, " % float(yz_scan_y_voltage_min_qlineedit.text()), end = "")
#     # print("YZ_scan max Y driving voltage = %2f, " % float(yz_scan_y_voltage_max_qlineedit.text()), end = "")
#     # print("YZ_scan X driving voltage = %2f, " % float(yz_scan_x_voltage_qlineedit.text()), end = "")
#     # print("YZ_scan z-piezo min driving voltage = %2f, " % float(yz_scan_z_piezo_min_voltage_qlineedit.text()), end = "")
#     # print("YZ_scan z-piezo max driving voltage = %2f." % float(yz_scan_z_piezo_max_voltage_qlineedit.text()))

#     # need to clear text box first
#     self.parameters_dsiplay_text_box.clear()

#     # this prints to the QTextBox in the left_window. The output of the user-selected scan parameters is printed below
#     self.parameters_dsiplay_text_box.setPlainText(
#                 "YZ_SCAN PARAMETERS/INFO:\n"
#                 "YZ_scan resolution = " + str(int(yz_scan_resolution_qlineedit.text())) + "\n"
#                 "YZ_scan counter read time = " + str(float(yz_scan_read_time_qlineedit.text())) + "\n"
#                 "YZ_scan min Y driving voltage = " + str(float(yz_scan_y_voltage_min_qlineedit.text())) + "\n"
#                 "YZ_scan max Y driving voltage = " + str(float(yz_scan_y_voltage_max_qlineedit.text())) + "\n"
#                 "YZ_scan X driving voltage = " + str(float(yz_scan_x_voltage_qlineedit.text())) + "\n'"
#                 "YZ_scan z-piezo min driving voltage = " + str(float(yz_scan_z_piezo_min_voltage_qlineedit.text())) + "\n"
#                 "YZ_scan z-piezo max driving voltage = " + str(float(yz_scan_z_piezo_max_voltage_qlineedit.text()))
#                                                 )

# # yz_scan resolution check then run fnc
# def yz_scan_resolution_validation_fnc():

#     self.sc.axes.cla()

#     try:
#         self.yz_scan_plot_colorbar.remove()

#     except (AttributeError, ValueError):
#         pass
    
#     try:
#         self.xy_scan_plot_colorbar.remove()
    
#     except (AttributeError, ValueError):
#         pass
        
#     try:
#         self.xz_scan_plot_colorbar.remove()
    
#     except (AttributeError, ValueError):
#         pass

#     res_min_condition = 20 # set the min allowed resolution for scanning
#     res_max_condition = 900 # set the max allowed resolution for scanning

#     yz_scan_resolution_test_condition = False # define resolution validation bool for yz scan

#     while yz_scan_resolution_test_condition is False: # this initiates checking the resolution parameter

#         # checking for out of bounds of min and max conditions above
#         if int(yz_scan_resolution_qlineedit.text()) < res_min_condition or int(yz_scan_resolution_qlineedit.text()) > res_max_condition: # TODO: or negative or not a number or too large

#             display_resolution_error_window_fnc() # call the error message pop-up window
#             break # exit the checking loop: failed

#         # if parameter is in bounds; run scan
#         elif int(yz_scan_resolution_qlineedit.text()) >= res_min_condition and int(yz_scan_resolution_qlineedit.text()) <= res_max_condition:

#             yz_scan_resolution_test_condition == True
#             print_YZ_scan_parameters_fnc(self) # call the print user-entered parameters fnc
#             run_yz_scan_fnc() # call the run yz scan method fnc
#             break # exit the checking loop: passed
