import tkinter as tk
from tkinter import ttk
import json

class SelectDriverAndTruck():
    def __init__(self, app):
        self.app = app

    def show(self):
        self.app.destroy_previous_widgets()
        label_truck = ttk.Label(self.app.root, text="Select a Truck:")
        label_truck.pack(pady=10)

        self.app.selected_truck = tk.StringVar()
        truck_models = [truck['model'] for truck in self.app.truck_data]
        self.app.truck_dropdown = ttk.Combobox(self.app.root, values=truck_models, textvariable=self.app.selected_truck)
        self.app.truck_dropdown.pack(pady=10)

        label_driver = ttk.Label(self.app.root, text="Select a Driver:")
        label_driver.pack(pady=10)

        self.app.selected_driver = tk.StringVar()
        driver_names = [f"{driver['name']} {driver['surname']}" for driver in self.app.driver_data]
        self.app.driver_dropdown = ttk.Combobox(self.app.root, values=driver_names, textvariable=self.app.selected_driver)
        self.app.driver_dropdown.pack(pady=10)

        show_info_button = ttk.Button(self.app.root, text="Show Info", command=self.app.info.show)
        show_info_button.pack(pady=10)

        nextPage = ttk.Button(self.app.root, text="Next", command=self.app.selectDestination.show)
        nextPage.pack(pady=10)

