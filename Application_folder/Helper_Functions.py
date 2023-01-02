"""
File name: "Helper_Functions.py"

Contents: multiple helper fuctions for use within multiple files (applications are currently displaying different windows only)

Dates:
Originally created: 12-30-2022
Last modifed: 01-02-2023
Original author: MDA
Last modified by: MDA

Notes: there seems to be no reason to separate these functions any further than accessing them all from one file (this file)

TODO:
*
"""

############################################################################################## start imports ##########################################################################################

# imports below are only from other files within application_folder
from Welcome_window import Setup_Welcome_Window # import `Setup_Welcome_Window` from "Welcome_window"

from Window_Contents import Setup_Main_Window_Contents # import `Setup_Main_Window_Contents` from "Window_Contents"

############################################################################################# end imports #############################################################################################

def display_welcome_window(self): # define display_welcome_window to display the welcome window contents on the Main_Window

    # print("display welcome called")                                                                                                                                       # temporary print statement

    self.welcome_window_contents = Setup_Welcome_Window(parent = None) # designate welcome_window_contents by calling `Setup_Welcome_Window()`

    self.setCentralWidget(self.welcome_window_contents) # dispaly welcome window contents by setting the central widget

    # print("welcome displayed (?)")                                                                                                                                        # temporary print statement

def display_window_contents(self): # define display_window_contents to display the main window contents on the Main_Window

    # print("display window contents called")                                                                                                                               # temporary print statement

    self.main_window_contents = Setup_Main_Window_Contents(parent = None) # designated the main window contents by calling `Setup_Main_Window_Contents()`

    self.setCentralWidget(self.main_window_contents) # display main window contents by setting the central widget

    # print("window contents displayed (?)")                                                                                                                                # temporary print statement
