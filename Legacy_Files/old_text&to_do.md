## old comments from mda_b00_gui

<!--
# QCoDeS -this only imports needed classes from a document not other QCoDeS functionality
# from qcodes_contrib_drivers.drivers.NationalInstruments.DAQ import *
# from qcodes_contrib_drivers.drivers.NationalInstruments.class_file import *
-->

# TODO: remove unused imports
# TODO: update naming conventions throughout scripts and entire file
# TODO: can about window be set to the center of the screen regardles of the position of the main window?
# TODO: fix allowing scans to be run one after the other. Will "Try... Except" work?
# 090122 this above is fixed. However, the fix lies in the implementation of validating the resolution input. If the input-validation framework changes 
# (as it should bc it is limited to only checking reoslution now) the allowed-repeated-scanning functionality MUST be re-written
# TODO: cont. below

"""
Input validation (resolution, min and max voltages for axes)
Multile scans w/out closing programs (scan_galvo.close) (use Try... Except?) -fixed; not ideal
Saving scan data/images
Progress (scanning) bar
Live plot updating?
Point size minimum based on wavelength of used laser
input validation method is currently only limited to checking resolutions setting per each scan
"""

############################# OLD ####################################
# def clear_plot():
#     print("Hello world!")
#     plot_res = 3.89
#     self.sc = MplCanvas(self, width = plot_res, height = plot_res, dpi = 110)                         # changing dpi does something to scale of figure
#     self.sc.move(2, 2)
#     self.sc.setParent(right_window)
#     self.sc.axes.xaxis.set_tick_params(labelsize = 8)
#     self.sc.axes.yaxis.set_tick_params(labelsize = 8)
###################################################################

<!--
Old README:

# 017_CSLM_control

About: ISEC room 017 CSLM control software

## Dates:

102822 $\rightarrow{}$ 12-21-22

## Old text from b00_gui:

Dates: 102822 -> 112222

Author: Miles D. Ackerman (undergraduate during the summer of 2022). Email: miles.ackerman1@gmail.com

General info:
This file makes a GUI to control the room-temp NV center-based measurement setup in LISE room B00 in the Lukin Group in the Harvard PHY dept. The setup
is a confocal laser scanning microscope. A galvo steers a laser beam at 518 nm (butteryfly) through a 4F telescope setup. An excitation and a collection
path (both use fiber coupling) are present. The sample stage is manually-controlled by positioning dials. Additionally, the z-axis of the microscope
objective is controlled by a piezo. This entire setup is controlled by a NI-cDAQ (model 9147). The NI-DAQmx is the National Insturments API that is 
used to communicate with the cDAQ device. Info. about this device can be found at:
https://nidaqmx-python.readthedocs.io/en/latest/https://nidaqmx-python.readthedocs.io/en/latest/. Two cards/modules are present in the cDAQ chassis: 1.
NI-9402 (four bi-directional digital input/output (I/O) channels -also featuring programmable internal clocks for counting). Info about the NI-9402 
module can be found at: https://www.ni.com/en-us/support/model.ni-9402.htmlhttps://www.ni.com/en-us/support/model.ni-9402.html. This module functions 
as a counter based on an internal clock within the module. The parameters for creating a counter assigned to this module when it is created in each 
scanning script. The counter requires the use of two of the four available channels on this cDAQ card. One channel is for input (from the APD on the
optical bench), and one channel for the hardware-timed clock to "run" the counter. Currently (as of 081522) only one counter (analog input) channel 
can be created at a time. In order to change this functionality, the source code for this contributed drivers package must be edited. And 2. NI-9263 
(four analog output channels (-10 V to +10 V). This module's info can be found at: 
https://www.ni.com/en-us/support/model.ni-9263.htmlhttps://www.ni.com/en-us/support/model.ni-9263.html. This moduel is used for programmable digital 
output. This functionality is largely used for controlling the servo motors on the ThorLab's galvo (by writing a sequence of voltages to them). Here,
all available digital output channels are created in one line: `ni_9263_ao_channels` where a single channel can be accessed at a time. The main 
function of this application is running confocal scannign scripts in different planes (the XY plane at a specified Z height, the XZ plane across a 
specified z-range, and the YZ plane at a specified X range). The GUI is split into 2 main setions, a left-half and a right-half section. The left-hand 
section contains the input controls for running a specific scanning script. On the bottom of the left-hand section is an option to save the dataset 
that was just scan and plotted on the right. Additionally, a text output box is present at the bottom of the left_window section. This is where the 
user-entered scanning parameters are printed to. Here, the use ahs the option to select and then copy the scan parameter info for keeping a record. 
there is also the option (currently commented out) to print this same info w/ its same format to the terminal. The right-hand section conatins the 
output plot from a run scan. Include info more: this application impements live plotting for each scanning option.

For the user of this application:
1. This application was built within a virtual environment on this computer called: "NV_control" it can be found through the
user/miniconda3/envs/NV_control. Within this enviornment THIS file and additonal referenec packages can be found
2. Only limited input-validation/error checking has been implemented so far. Please be advised when running scanning programs. The LIMIT of the voltage 
that can be driven to either mirror (or the objective's z_piezo) is 10 V. DO NOT EXCEED THIS VALUE. The system (as a cause of NI-DAQmx error 
checking) will likely refuse such a request, but it is best practice to avoid.

Helpful info. when reading through this application code:
1. The NI-cDAQ card (chasis) is called (this can be changed using the NI-MAX software when the NI-DAQ card is connected to this computer)
"cDAQ1". Additional info. about the cDAQ device and its inserted modules (as of 081522 only ni_9402 and ni_9263) can be viewed in the NI-MAX software.
This software opens automatically when the cDAQ device is connected to this computer
2. The first module inserted into the cDAQ card (the NI-9402 module) is called "mod1". This naming pattern follows the available slots within the 
cDAQ chasis (there are four available slots)
3. The second module in the cDAQ chasis (the NI-9263 module) is called "mod2" following in suit
-->


02-12-2023
Old xy scanning comments
"""
    This runs X and Y only scan. It currently creates and then populates a user defined size numpy array according to a set counter acquisition time and a motor
step voltage setting. Additionally, the initial driving voltage for the X and Y motors can be set according to the desired scanning range. This scanning program runs in a snake
pattern, it scan the first row left to right, moves up one row, 
then scans right to left and continues. Alternatives would be scanning left to right, and resetting the position of the laser on the next higher row and scanning again left 
to right OR scanning in a "circular" patter either CW or CCW from outside to inside or inside to outside. The chosen method was picked for simplicity of understanding. The 
scanning loops are present within NI-DAQmx tasks to speed up the program. Starting and stopping a NI-DAQmx task repeatedly slows down the program dramatically. So, the 
counter and hardware clock task are started once, then the scanning program is run, and then the counter and clock tasks are closed -un-reserving the hardware resources. 
This cell uses the "DAQAnalogOutputs" function from a written class file at:
C:/Users/lukin2dmaterials/miniconda3/envs/qcodes/Lib/site-packages/qcodes_contrib_drivers/drivers/NationalInstruments/class_file. Slashes are reversed to run
"""