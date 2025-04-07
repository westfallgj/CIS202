import tkinter

class MyGUI:

    def __init__(self):
        # Create the main window widget
        self.main_window = tkinter.Tk()

        # Create top/bottom Frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create a Label widget containing the text
        self.label1 = tkinter.Label(self.top_frame, text='Hello World')
        #self.label1 = tkinter.Label(self.main_window, text='Hello World')
        self.label2 = tkinter.Label(self.top_frame, text='This is my GUI')
        #self.label2 = tkinter.Label(self.main_window, text='This is my GUI')

        # Call the Label widget's pack method.
        self.label1.pack(side='top')
        self.label2.pack(side='top')

        # Create more Label widget containing the text
        self.label3 = tkinter.Label(self.bottom_frame, text='Label 3')
        self.label4 = tkinter.Label(self.bottom_frame, text='Label 4')

        # Call the Label widget's pack method.
        self.label3.pack(side='left')
        self.label4.pack(side='right')

        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()

# Create gui instance
my_gui = MyGUI()
