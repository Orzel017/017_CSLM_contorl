"""
text


"""

# import Main_Window

from Welcome_window import Setup_Welcome_Window

from Window_Contents import Setup_Main_Window_Contents

def display_welcome_window(self):

    print("display welcome called")

    # Setup_Welcome_Window()

    self.setCentralWidget(Setup_Welcome_Window(parent = None))

    # item = Setup_Welcome_Window(parent = None)

    # Main_Window.Setup_Main_Window_Background.setCentralWidget(item)

    print("welcome displayed (?)")

def display_window_contents(self):

    print("display window contents called")

    self.setCentralWidget(Setup_Main_Window_Contents(parent = None))

    print("window contents displayed (?)")
