from tkinter import Toplevel, Label, Entry, Button
import uuid
from Modules.GUI.pages.TruckManager import TruckManager

class AddTruckWindow:
    def __init__(self, parent, confirm_callback):
        self.parent = parent
        self.confirm_callback = confirm_callback

        self.add_truck_window = Toplevel(parent)
        self.add_truck_window.title("Add Truck")
        
                # Set the dimensions of the window
        window_width = 400
        window_height = 200
        screen_width = parent.winfo_screenwidth()
        screen_height = parent.winfo_screenheight()
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2

        self.add_truck_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")


        Label(self.add_truck_window, text="Brand:").pack()
        self.brand_entry = Entry(self.add_truck_window)
        self.brand_entry.pack()

        Label(self.add_truck_window, text="Model:").pack()
        self.model_entry = Entry(self.add_truck_window)
        self.model_entry.pack()
        
        Label(self.add_truck_window, text="Capacity:").pack()
        self.capacity_entry = Entry(self.add_truck_window)
        self.capacity_entry.pack()

        Label(self.add_truck_window, text="Fuel Economy:").pack()
        self.fuelEconomy_entry = Entry(self.add_truck_window)
        self.fuelEconomy_entry.pack()        
        #brand, model, Capacity, fuelEconomy

        confirm_button = Button(self.add_truck_window, text="Add Truck", command=self.confirm_add_truck)
        confirm_button.pack()

    def confirm_add_truck(self):
        brand = self.brand_entry.get()
        model = self.model_entry.get()
        capacity = self.capacity_entry.get()
        fuelEconomy = self.fuelEconomy_entry.get()

        if callable(self.confirm_callback):
            self.confirm_callback(brand, model)
            truckId = str(uuid.uuid1())
            TruckManager.add_truck(truckId, brand, model, capacity, fuelEconomy)
            

        self.add_truck_window.destroy()
