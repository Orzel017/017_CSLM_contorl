"""
File name: "Run_GUI.py"

Contents: brief lines to run the GUI/application

Dates:
Originally separated/organized: 12-22-2022
Last modifed: 01-17-2023
Original author: MDA
Last modified by: MDA

Notes:
Currently, this software application is run out of an editor (consistently VSCode). "Run" is clicked from this file within the folder "MDA_App". The longer-term end goal of this software is to have 
one packaged application avaialble from the desktop of a designated machine and another copy available in an editor for making changes.
"""

########################################################################################## start imports ##############################################################################################

import sys # import system-specific parameters and functions

from layout_base import GUI_Background # import `GUI_Background` from "layout_base.py" file

from PyQt5 import QtWidgets # import QtWidgets for QApplication to build the whole application

############################################################################################ end imports ##############################################################################################

#################################################################################### start run gui ####################################################################################################

if __name__ == "__main__": # check name to run main file

    application = QtWidgets.QApplication(sys.argv) # setup command line arguments under "application"

    main_GUI_window = GUI_Background() # designate a "main_GUI_window" object

    main_GUI_window.show() # display the main application window

    sys.exit(application.exec_()) # enter the main event look of the application. See https://doc.qt.io/qt-6/qapplication.html#exec for more info. on `.exec()`

##################################################################################### end run gui #####################################################################################################
