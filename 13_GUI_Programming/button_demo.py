import tkinter
import tkinter.messagebox

class MyGUI:

    def __init__(self):
        # Create the main window widget
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create info label
        self.label1 = tkinter.Label(self.top_frame, text='George Westfall')
        self.label2 = tkinter.Label(self.top_frame, text='1197 Cree Dr')
        self.label3 = tkinter.Label(self.top_frame, text='Colorado Springs, CO 80915')

        # Create button widget. 
        self.info_button = tkinter.Button(self.bottom_frame, text='Show Info', command=self.display_info)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit Program', command=self.main_window.destroy)

        # Call the button pack method.
        self.info_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames
        self.top_frame.pack(padx=5, pady=5)
        self.bottom_frame.pack(padx=20, pady=20)

        # Enter the tkinter main loop
        tkinter.mainloop()

    # display_info
    def display_info(self):
        # Display info dialog box
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

# Create gui instance
my_gui = MyGUI()