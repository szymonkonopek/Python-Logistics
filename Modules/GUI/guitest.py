import tkinter as tk
from tkinter import ttk
import json

class TruckChooserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Truck Chooser App")

        # Load truck data from JSON file
        self.load_truck_data()

        # Create and set up GUI components
        self.create_widgets()

    def load_truck_data(self):
        # Load truck data from the provided JSON file ('truckList.py')
        with open('truckList.py', 'r') as file:
            self.truck_data = json.load(file)

    def create_widgets(self):
        # Dropdown menu to choose a truck
        label = ttk.Label(self.root, text="Select a Truck:")
        label.pack(pady=10)

        # Create a StringVar to store the selected truck
        self.selected_truck = tk.StringVar()

        # Populate the dropdown menu with truck models
        truck_models = [truck['model'] for truck in self.truck_data]
        self.truck_dropdown = ttk.Combobox(self.root, values=truck_models, textvariable=self.selected_truck)
        self.truck_dropdown.pack(pady=10)

        # Button to display selected truck information
        show_info_button = ttk.Button(self.root, text="Show Truck Info", command=self.show_truck_info)
        show_info_button.pack(pady=10)

    def show_truck_info(self):
        # Get the selected truck model
        selected_truck_model = self.selected_truck.get()

        # Find the selected truck in the data
        selected_truck = next((truck for truck in self.truck_data if truck['model'] == selected_truck_model), None)

        if selected_truck:
            # Display truck information (you can customize this part)
            info_window = tk.Toplevel(self.root)
            info_window.title("Truck Information")

            info_label = ttk.Label(info_window, text=f"Brand: {selected_truck['brand']}\n"
                                                      f"Model: {selected_truck['model']}\n"
                                                      f"Capacity: {selected_truck['capacity']}\n"
                                                      f"Fuel Economy: {selected_truck['fuelEconomy']}\n"
                                                      f"Other Things: {selected_truck['otherThings']}")
            info_label.pack(padx=20, pady=20)
        else:
            # Display an error if the selected truck is not found
            error_label = ttk.Label(self.root, text="Error: Selected truck not found.")
            error_label.pack(pady=10, fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = TruckChooserApp(root)
    root.mainloop()
