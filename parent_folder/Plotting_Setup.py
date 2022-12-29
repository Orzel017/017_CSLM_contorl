"""
File name: "Plotting_Setup.py"

Contents: framework to build the plotting area (and Matplotlib Canvas)

Dates:
Originally separated/organized: 12-21-2022
Last modifed: 12-23-2022
Original author: MDA
Last modified by: MDA

Notes:

TODO:
*Many things will change with alternative data visualization
*More will change with the (potential) addition of a second plotting area/canvas
*Consider the use of a single plotting area (for additional methods -including tiling) in the GUI
"""

########################################################################################## start imports ##############################################################################################

from datetime import date

# MatPlotLib plotting packages
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt

############################################################################################ end imports ##############################################################################################

########################################################################################### start prelims #############################################################################################

get_todays_date = date.today() # this is used for creating the final plot's plot labels

todays_date = get_todays_date.strftime("%m%d%Y") # this is used for creating the final plot's plot labels

############################################################################################ end prelims ##############################################################################################

############################################################################### start MplCanvas class ##################################################################################################
class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent = None, canvas_width = 10, canvas_height = 10, canvas_dpi = 1000):

        # fig = Figure(figsize = (width, height), dpi = dpi)
        
        # self.axes = fig.add_subplot()

        self.figure, self.axes = plt.subplots(figsize = (canvas_width, canvas_height), dpi = canvas_dpi, tight_layout = True)

        super(MplCanvas, self).__init__(self.figure)

################################################################################ end MplCanvas class ##################################################################################################
