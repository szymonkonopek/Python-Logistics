import tkinter as tk
from tkinter import ttk
import json

class TruckChooserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Truck Chooser App")

        self.root.geometry("600x400")

        self.load_truck_data()
        self.load_driver_data()

        self.create_widgets()

    def load_truck_data(self):
        with open(r'truckList.json', 'r') as file:
            self.truck_data = json.load(file)

    def load_driver_data(self):
        with open(r'driversList.json', 'r') as file:
            self.driver_data = json.load(file)

    def create_widgets(self):
        label_truck = ttk.Label(self.root, text="Select a Truck:")
        label_truck.pack(pady=10)

        self.selected_truck = tk.StringVar()
        truck_models = [truck['model'] for truck in self.truck_data]
        self.truck_dropdown = ttk.Combobox(self.root, values=truck_models, textvariable=self.selected_truck)
        self.truck_dropdown.pack(pady=10)

        label_driver = ttk.Label(self.root, text="Select a Driver:")
        label_driver.pack(pady=10)

        self.selected_driver = tk.StringVar()
        driver_names = [f"{driver['name']} {driver['surname']}" for driver in self.driver_data]
        self.driver_dropdown = ttk.Combobox(self.root, values=driver_names, textvariable=self.selected_driver)
        self.driver_dropdown.pack(pady=10)

        show_info_button = ttk.Button(self.root, text="Show Info", command=self.show_info)
        show_info_button.pack(pady=10)

    def show_info(self):
        selected_truck_model = self.selected_truck.get()
        selected_driver_name = self.selected_driver.get()

        selected_truck = next((truck for truck in self.truck_data if truck['model'] == selected_truck_model), None)
        selected_driver = next((driver for driver in self.driver_data if f"{driver['name']} {driver['surname']}" == selected_driver_name), None)

        if selected_truck and selected_driver:
            info_window = tk.Toplevel(self.root)
            info_window.title("Information")

            info_label = ttk.Label(info_window, text=f"Truck Information:\n"
                                                     f"Brand: {selected_truck['brand']}\n"
                                                     f"Model: {selected_truck['model']}\n"
                                                     f"Capacity: {selected_truck['capacity']}\n"
                                                     f"Fuel Economy: {selected_truck['fuelEconomy']}\n"
                                                     f"Other Things: {selected_truck['otherThings']}\n\n"
                                                     f"Driver Information:\n"
                                                     f"Name: {selected_driver['name']}\n"
                                                     f"Surname: {selected_driver['surname']}\n"
                                                     f"Hire Date: {selected_driver['hireDate']}\n"
                                                     f"Hourly Base Rate: {selected_driver['hourlyBaseRate']}")
            info_label.pack(padx=20, pady=20)
        else:
            error_label = ttk.Label(self.root, text="Error: Selected truck or driver not found.")
            error_label.pack(pady=10, fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = TruckChooserApp(root)
    root.mainloop()
