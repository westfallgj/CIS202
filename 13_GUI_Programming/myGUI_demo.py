import tkinter

class MyGUI:
    """
    A simple GUI application to display personal information.
    """
    def __init__(self):
        """
        Initializes the MyGUI application.

        Creates the main window, frames, labels, and buttons, then
        starts the Tkinter main loop.
        """
        # Create the main window widget
        self.main_window = tkinter.Tk()

        # Create StringVar objects.
        self.name_var = tkinter.StringVar()
        self.street_var = tkinter.StringVar()
        self.cityzip_var = tkinter.StringVar()

        # Create top/bottom
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create info label
        self.name_label = tkinter.Label(self.top_frame, textvariable=self.name_var)
        self.street_label = tkinter.Label(self.top_frame, textvariable=self.street_var)
        self.cityzip_label = tkinter.Label(self.top_frame, textvariable=self.cityzip_var)
 
        # Create button widget. 
        self.info_button = tkinter.Button(self.bottom_frame, text='Show Info', command=self.display_info)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit Program', command=self.main_window.destroy)

        # Call the button pack method.
        self.info_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the labels
        self.name_label.pack()
        self.street_label.pack()
        self.cityzip_label.pack()
        
        # Pack the frames
        self.top_frame.pack(padx=5, pady=5)
        self.bottom_frame.pack(padx=20, pady=20)

        # Enter the tkinter main loop
        tkinter.mainloop()

    # display_info
    def display_info(self):
        """
        Sets personal information labels in the top frame.
        """
        # Display info dialog box
        self.name_var.set('George Westfall')
        self.street_var.set('1197 Cree Dr.')
        self.cityzip_var.set('Colorado Springs, CO 80915')

# Create gui instance
my_gui = MyGUI()