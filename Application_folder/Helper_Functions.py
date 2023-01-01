"""
text

123022 - 123122

"""

# import Main_Window

from Welcome_window import Setup_Welcome_Window

from Window_Contents import Setup_Main_Window_Contents

# from Main_Window import Setup_Main_Window_Background

def display_welcome_window(self):

    print("display welcome called")

    # Setup_Welcome_Window()

    self.welcome_window_contents = Setup_Welcome_Window(parent = None)

    self.setCentralWidget(self.welcome_window_contents)

    # item = Setup_Welcome_Window(parent = None)

    # Main_Window.Setup_Main_Window_Background.setCentralWidget(item)

    print("welcome displayed (?)")

def display_window_contents(self):

    print("display window contents called")

    # Setup_Welcome_Window.hide()

    self.window_contents_child = Setup_Main_Window_Contents(parent = None)

    self.setCentralWidget(self.window_contents_child)

    # self.window_contents_child.show()

    print("window contents displayed (?)")
