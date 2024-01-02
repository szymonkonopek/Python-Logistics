from tkinter import Toplevel, Label, Entry, Button
import uuid
import string
from Modules.GUI.pages.DriverManager import DriverManager

class AddDriverWindow:
    def __init__(self, parent, confirm_callback):
        self.parent = parent
        self.confirm_callback = confirm_callback

        self.add_driver_window = Toplevel(parent)
        self.add_driver_window.title("Add Driver")
        
        window_width = 400
        window_height = 200
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
        Label(self.add_driver_window, text="hire date:").pack()
        self.hireDate_entry = Entry(self.add_driver_window)
        self.hireDate_entry.pack()
        
        #hourly base rate
        Label(self.add_driver_window, text="hourly base rate:").pack()
        self.hourlyBase_entry = Entry(self.add_driver_window)
        self.hourlyBase_entry.pack()

        confirm_button = Button(self.add_driver_window, text="Add Driver", command=self.confirm_add_driver)
        confirm_button.pack()

    def confirm_add_driver(self):
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        hireDate = self.hireDate_entry.get()
        hourlyBase = self.hourlyBase_entry.get()
        
        if callable(self.confirm_callback):
            self.confirm_callback(name, surname, hireDate, hourlyBase)
            driverId = str(uuid.uuid1())
            DriverManager.add_driver(driverId ,name, surname, hireDate, hourlyBase)

        self.add_driver_window.destroy()