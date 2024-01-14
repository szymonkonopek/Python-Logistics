import tkinter as tk
from tkinter import ttk
import json

# GUI select Base information page, to select Driver, Truck and Payload
class SelectBaseInfo():
    def __init__(self, app):
        self.app = app

# Shows every label and form input
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

        label_payload = ttk.Label(self.app.root, text="Select a Payload:")
        label_payload.pack(pady=10)

        self.app.selected_payload = tk.StringVar()
        payload_names = [f"{payload['name']}" for payload in self.app.payload_data]
        self.app.payload_dropdown = ttk.Combobox(self.app.root, values=payload_names, textvariable=self.app.selected_payload)
        self.app.payload_dropdown.pack(pady=10)

        show_info_button = ttk.Button(self.app.root, text="Show Info", command=self.app.info.show)
        show_info_button.pack(pady=10)

        nextPage = ttk.Button(self.app.root, text="Next", command=self.app.selectDestination.show)
        nextPage.pack(pady=10)

# Button to add new Driver, Truck or Payload
        add_driver_button = ttk.Button(self.app.root, text="Add Driver", command=self.app.add_driver)
        add_truck_button = ttk.Button(self.app.root, text="Add Truck", command=self.app.add_truck)
        add_payload_button = ttk.Button(self.app.root, text="Add Payload", command=self.app.add_payload)
        
        add_driver_button.pack(pady=10)
        add_truck_button.pack(pady=10)
        add_payload_button.pack(pady=10)
        
        
        

