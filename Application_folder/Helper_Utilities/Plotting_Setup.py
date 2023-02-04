"""
File name: "Plotting_Setup.py"

Contents: framework to build the plotting area (and Matplotlib Canvas)

Dates:
Originally separated/organized: 12-21-2022
Last modifed: 02-04-2022
Original author: MDA
Last modified by: MDA

Notes:

TODO:
*Many things will change with alternative data visualization
*More will change with the (potential) addition of a second plotting area/canvas
*Consider the use of a single plotting area (for additional methods -including tiling) in the GUI
"""

########################################################################################## start imports ##############################################################################################

import matplotlib # generic MatPlotLib import

matplotlib.use("Qt5Agg") # tailor matplotlib package for use in PyQt5?

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg # tailor matplotlib package for use in PyQt5? A backend?

import matplotlib.pyplot # import pyplot submodule

############################################################################################ end imports ##############################################################################################

########################################################################################### start prelims #############################################################################################

# prelims go here

############################################################################################ end prelims ##############################################################################################

########################################################################### start MatPlotLib_Canvas class #############################################################################################
class MatPlotLib_Canvas(FigureCanvasQTAgg):

    def __init__(self, parent, canvas_width, canvas_height, canvas_dpi):

        # fig = Figure(figsize = (width, height), dpi = dpi) # old
        
        # self.axes = fig.add_subplot() # old

        self.figure, self.axes = matplotlib.pyplot.subplots(figsize = (canvas_width, canvas_height), dpi = canvas_dpi, tight_layout = True)

        super(MatPlotLib_Canvas, self).__init__(self.figure)

############################################################################# end MatPlotLib_Canvas class #############################################################################################
