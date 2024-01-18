import tkinter as tk
from tkinter import ttk, StringVar, END
from tkinter import ttk
import json
from Modules.DriversList import DriversList
from Modules.TruckList import TruckList
from Modules.PayloadList import PayloadList

# GUI select Base information page, to select Driver, Truck and Payload
class SelectBaseInfo():
    def __init__(self, app):
        self.app = app

# Shows every label and form input
    def show(self):
        self.app.destroy_previous_widgets()

# Select Truck combobox
        label_truck = ttk.Label(self.app.root, text="Select a Truck:")
        label_truck.pack(pady=10)

        self.truck_variable = StringVar(value = self.app.selectedTruck.getBrandModel())
        truck_models = [f"{truck['brand']} {truck['model']}" for truck in self.app.truck_data]
        self.truck_dropdown = ttk.Combobox(self.app.root, values=truck_models, textvariable=self.truck_variable)
        self.truck_dropdown.pack(pady=10)

        # self.truck_dropdown.current()

        self.truck_dropdown.bind("<<ComboboxSelected>>", self.on_truck_selected)

# Select Driver combobox
        label_driver = ttk.Label(self.app.root, text="Select a Driver:")
        label_driver.pack(pady=10)

        self.driver_variable = StringVar(value = self.app.selectedDriver.getNameSurname())
        driver_names = [f"{driver['name']} {driver['surname']}" for driver in self.app.driver_data]
        self.driver_dropdown = ttk.Combobox(self.app.root, values=driver_names, textvariable=self.driver_variable)
        self.driver_dropdown.pack(pady=10)

        self.driver_dropdown.bind("<<ComboboxSelected>>", self.on_driver_selected)

# Select Payload combobox
        label_payload = ttk.Label(self.app.root, text="Select a Payload:")
        label_payload.pack(pady=10)

        self.payload_variable = StringVar(value = self.app.selectedPayload.getName())
        payload_names = [f"{payload['name']}" for payload in self.app.payload_data]
        self.payload_dropdown = ttk.Combobox(self.app.root, values=payload_names, textvariable=self.payload_variable)
        self.payload_dropdown.pack(pady=10)

        self.payload_dropdown.bind("<<ComboboxSelected>>", self.on_payload_selected)

# Show info and next page info
        show_info_button = ttk.Button(self.app.root, text="Show Info", command=self.app.info.show)
        show_info_button.pack(pady=10)

        nextPage = ttk.Button(self.app.root, text="Select destination", command=self.app.selectDestination.show)
        nextPage.pack(pady=10)

# Button to add new Driver, Truck or Payload
        add_driver_button = ttk.Button(self.app.root, text="Add Driver", command=self.app.add_driver)
        add_truck_button = ttk.Button(self.app.root, text="Add Truck", command=self.app.add_truck)
        add_payload_button = ttk.Button(self.app.root, text="Add Payload", command=self.app.add_payload)
        
        add_driver_button.pack(pady=10)
        add_truck_button.pack(pady=10)
        add_payload_button.pack(pady=10)
        
        
    def on_truck_selected(self, event):
        self.app.selectedTruck = TruckList.jsonToTruck(self.app.truck_data[self.truck_dropdown.current()])
        print( self.truck_dropdown.current())

    def on_driver_selected(self, event):
        self.app.selectedDriver = DriversList.jsonToDriver(self.app.driver_data[self.driver_dropdown.current()])

    def on_payload_selected(self, event):
        self.app.selectedPayload = PayloadList.jsonToPayload(self.app.payload_data[self.payload_dropdown.current()])