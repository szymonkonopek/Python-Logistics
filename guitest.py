import tkinter as tk
from tkinter import ttk
import json

class TruckChooserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Truck Chooser App")
        
        self.root.geometry("600x400")

        self.load_truck_data()

        self.create_widgets()

    def load_truck_data(self):
        with open(r'truckList.json', 'r') as file:
            self.truck_data = json.load(file)

    def create_widgets(self):
        label = ttk.Label(self.root, text="Select a Truck:")
        label.pack(pady=10)

        self.selected_truck = tk.StringVar()

        truck_models = [truck['model'] for truck in self.truck_data]
        self.truck_dropdown = ttk.Combobox(self.root, values=truck_models, textvariable=self.selected_truck)
        self.truck_dropdown.pack(pady=10)

        show_info_button = ttk.Button(self.root, text="Show Truck Info", command=self.show_truck_info)
        show_info_button.pack(pady=10)

    def show_truck_info(self):
        selected_truck_model = self.selected_truck.get()

        selected_truck = next((truck for truck in self.truck_data if truck['model'] == selected_truck_model), None)

        if selected_truck:
            info_window = tk.Toplevel(self.root)
            info_window.title("Truck Information")

            info_label = ttk.Label(info_window, text=f"Brand: {selected_truck['brand']}\n"
                                                      f"Model: {selected_truck['model']}\n"
                                                      f"Capacity: {selected_truck['capacity']}\n"
                                                      f"Fuel Economy: {selected_truck['fuelEconomy']}\n"
                                                      f"Other Things: {selected_truck['otherThings']}")
            info_label.pack(padx=50, pady=50)
        else:
            error_label = ttk.Label(self.root, text="Error: Selected truck not found.")
            error_label.pack(pady=10, fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = TruckChooserApp(root)
    root.mainloop()
