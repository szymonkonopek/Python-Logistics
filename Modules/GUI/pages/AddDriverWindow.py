from datetime import datetime
from tkinter import *
from tkinter import messagebox
from tkcalendar import DateEntry
import uuid
import string
from Modules.Driver import Driver
from Modules.DriversList import DriversList

# Pop up to add new Driver
class AddDriverWindow:
    def __init__(self, app, confirm_callback):
        self.app = app

        parent = app.root
        self.confirm_callback = confirm_callback

        self.add_driver_window = Toplevel(parent)
        self.add_driver_window.title("Add Driver")
        
        window_width = 400
        window_height = 300
        screen_width = parent.winfo_screenwidth()
        screen_height = parent.winfo_screenheight()
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2

        self.add_driver_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        Label(self.add_driver_window, text="Name:").pack()
        self.name_entry = Entry(self.add_driver_window)
        self.name_entry.pack()

        Label(self.add_driver_window, text="Surname:").pack()
        self.surname_entry = Entry(self.add_driver_window)
        self.surname_entry.pack()
        
        #hire date
        Label(self.add_driver_window, text="Hire date:").pack()
        self.hireDate_entry = DateEntry(self.add_driver_window, maxdate=datetime.now(), date_pattern='yyyy-mm-dd')
        self.hireDate_entry.pack()
        
        #hourly base rate
        self.hourlyBaseRate_var = StringVar()
        Label(self.add_driver_window, text="Hourly base rate in dollars:").pack()
        self.hourlyBase_entry = Entry(self.add_driver_window, textvariable=self.hourlyBaseRate_var, validate="key", validatecommand=(self.add_driver_window.register(self.validate_input), "%P"))
        self.hourlyBase_entry.pack()

        confirm_button = Button(self.add_driver_window, text="Add Driver", command=self.confirm_add_driver)
        confirm_button.pack()

    def confirm_add_driver(self):
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        hireDate_str = self.hireDate_entry.get()
        hireDate_obj = datetime.strptime(hireDate_str, '%Y-%m-%d').date()
        formatted_hireDate = hireDate_obj.strftime('%m/%d/%Y')
        hourlyBase = self.hourlyBase_entry.get()
        
        if callable(self.confirm_callback):
            self.confirm_callback(name, surname, formatted_hireDate, hourlyBase)
            new_driver = Driver(name, surname, formatted_hireDate, int(hourlyBase))
            drivers_list = DriversList()
            drivers_list.addDriver(new_driver)

        self.add_driver_window.destroy()
        self.app.destroy_previous_widgets()
        self.app.load_driver_data()
        self.app.selectDriver.show()


    def validate_input(self, new_value):
        try:
            # Attempt to convert the input to an integer
            if new_value:
                int(new_value)
            return True
        except ValueError:
            # If conversion fails, show an error message
            messagebox.showerror("Error", "Please enter a valid integer.")
            return False