from tkinter import Toplevel, Label, Entry, Button

class AddDriverWindow:
    def __init__(self, parent, confirm_callback):
        self.parent = parent
        self.confirm_callback = confirm_callback

        self.add_driver_window = Toplevel(parent)
        self.add_driver_window.title("Add Driver")
        
                # Set the dimensions of the window
        window_width = 400
        window_height = 200
        screen_width = parent.winfo_screenwidth()
        screen_height = parent.winfo_screenheight()
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2

        self.add_driver_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")


        # Example: Add Entry widgets for entering driver information
        Label(self.add_driver_window, text="Name:").pack()
        self.name_entry = Entry(self.add_driver_window)
        self.name_entry.pack()

        Label(self.add_driver_window, text="Surname:").pack()
        self.surname_entry = Entry(self.add_driver_window)
        self.surname_entry.pack()

        # Example: Add a button to confirm and add the new driver
        confirm_button = Button(self.add_driver_window, text="Add Driver", command=self.confirm_add_driver)
        confirm_button.pack()

    def confirm_add_driver(self):
        # Get the entered information
        name = self.name_entry.get()
        surname = self.surname_entry.get()

        # Call the confirm callback with the entered information
        if callable(self.confirm_callback):
            self.confirm_callback(name, surname)

        # Close the add driver window
        self.add_driver_window.destroy()