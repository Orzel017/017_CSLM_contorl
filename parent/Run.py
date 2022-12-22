import sys
# from Class_file import Child
from Parent_file import Parent
# import PyQt5
from PyQt5 import QtWidgets

############################################################## start gui ################################################################################

# ?
if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    mw = Parent()
    mw.show()
    sys.exit(app.exec_())
