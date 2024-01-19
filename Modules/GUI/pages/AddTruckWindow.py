from tkinter import Toplevel, Label, Entry, Button, StringVar, messagebox
from Modules.Truck import Truck
from Modules.TruckList import TruckList

# Pop up window to add new Truck
class AddTruckWindow:
    def __init__(self, app, confirm_callback):
        self.app = app

        parent = app.root
        self.confirm_callback = confirm_callback

        self.add_truck_window = Toplevel(parent)
        self.add_truck_window.title("Add Truck")
        
                # Set the dimensions of the window
        window_width = 400
        window_height = 300
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
        self.capacity_var = StringVar()
        self.capacity_entry = Entry(self.add_truck_window, textvariable=self.capacity_var, validate="key", validatecommand=(self.add_truck_window.register(self.validate_capacity), "%P"))
        self.capacity_entry.pack()

        Label(self.add_truck_window, text="Fuel Economy:").pack()
        self.fuel_var = StringVar()
        self.fuelEconomy_entry = Entry(self.add_truck_window, textvariable=self.fuel_var, validate="key", validatecommand=(self.add_truck_window.register(self.validate_speed), "%P"))
        self.fuelEconomy_entry.pack()        

        Label(self.add_truck_window, text="Max allowed Speed:").pack()
        self.truck_Vmax_var = StringVar()
        self.maxallowedspeed_entry = Entry(self.add_truck_window, textvariable=self.truck_Vmax_var,validate="key", validatecommand=(self.add_truck_window.register(self.validate_speed), "%P"))
        self.maxallowedspeed_entry.pack()        

        #brand, model, Capacity, fuelEconomy

        confirm_button = Button(self.add_truck_window, text="Add Truck", command=self.confirm_add_truck)
        confirm_button.pack()

    def confirm_add_truck(self):
        brand = self.brand_entry.get()
        model = self.model_entry.get()
        capacity = self.capacity_entry.get()
        fuelEconomy = self.fuelEconomy_entry.get()
        maxallowedspeed = self.maxallowedspeed_entry.get()

        if callable(self.confirm_callback):
            self.confirm_callback(brand, model)
            newTruck = Truck(brand, model, int(capacity), int(fuelEconomy), int(maxallowedspeed))
            truckList = TruckList()
            truckList.addTruck(newTruck)
            
            self.add_truck_window.destroy()
            self.app.destroy_previous_widgets()
            self.app.load_truck_data()
            self.app.selectDriver.show()

    def validate_speed(self, new_value):
        try:
            # Attempt to convert the input to an integer
            if new_value:
                int(new_value)
                if int(new_value) > 150:
                    messagebox.showerror("Error", "Max allowed speed cannot exceed 120 kilometers per hour.")
                    return False
            return True
        except ValueError:
            # If conversion fails, show an error message
            messagebox.showerror("Error", "Please enter a valid integer.")
            return False
        
    def validate_fuel(self, new_value):
        try:
            # Attempt to convert the input to an integer
            if new_value:
                int(new_value)
                if int(new_value) > 75:
                    messagebox.showerror("Error", "Maximum value for an average fuel consumption is 75 litres.")
                    return False
            return True
        except ValueError:
            # If conversion fails, show an error message
            messagebox.showerror("Error", "Please enter a valid integer.")
            return False
    
    def validate_capacity(self, new_value):
        try:
            # Attempt to convert the input to an integer
            if new_value:
                int(new_value)
                if int(new_value) > 50000:
                    messagebox.showerror("Error", "Please enter capacity value less than 50000 kilograms")
                    return False
            return True
        except ValueError:
            # If conversion fails, show an error message
            messagebox.showerror("Error", "Please enter a valid integer.")
            return False
