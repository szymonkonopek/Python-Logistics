from tkinter import Toplevel, Label, Entry, Button

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


        # Example: Add Entry widgets for entering truck information
        Label(self.add_truck_window, text="Brand:").pack()
        self.brand_entry = Entry(self.add_truck_window)
        self.brand_entry.pack()

        Label(self.add_truck_window, text="Model:").pack()
        self.model_entry = Entry(self.add_truck_window)
        self.model_entry.pack()

        # Example: Add a button to confirm and add the new truck
        confirm_button = Button(self.add_truck_window, text="Add Truck", command=self.confirm_add_truck)
        confirm_button.pack()

    def confirm_add_truck(self):
        # Get the entered information
        brand = self.brand_entry.get()
        model = self.model_entry.get()

        # Call the confirm callback with the entered information
        if callable(self.confirm_callback):
            self.confirm_callback(brand, model)

        # Close the add truck window
        self.add_truck_window.destroy()
