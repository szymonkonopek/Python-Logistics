import json
from datetime import date
from tkinter import Button

from Modules.GUI.pages.SelectBaseInfo import SelectBaseInfo
from Modules.GUI.pages.SelectDestination import SelectDestination
from Modules.GUI.pages.CalculationPage import CalculationPage
from Modules.GUI.pages.Info import Info
from Modules.Transit import Transit
from Modules.GUI.pages.AddDriverWindow import AddDriverWindow
from Modules.GUI.pages.AddPayloadWindow import AddPayloadWindow
from Modules.GUI.pages.AddTruckWindow import AddTruckWindow
from Modules.GUI.GetLastElements import GetLastDriver
from Modules.GUI.GetLastElements import GetLastTruck
from Modules.GUI.GetLastElements import GetLastPayload


from Modules.Truck import Truck
from Modules.Driver import Driver
from Modules.PayloadDangerous import PayloadDangerous
from Modules.PriceList import PriceList
from Modules.Destination import Destination


class TruckChooserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Truck Chooser App")
        
        # Dynamic variables while choosing a driver, truck or payload
        self.selectedDriver = Driver("","","",0)
        self.selectedPayload = PayloadDangerous("","",0)
        self.selectedTruck = Truck("","",0,0,0)

        # Select Destination
        self.fromDestination = Destination()
        self.toDestination = Destination()

        self.distance = ""
        self.fuelPrice = ""
        self.driverTime = ""
        self.driverSalary = ""
        
        self.selectDriver = SelectBaseInfo(self)
        self.selectDestination = SelectDestination(self)
        self.calculationPage = CalculationPage(self)
        self.info = Info(self)



        self.root.geometry("600x600")

        self.load_truck_data()
        self.load_driver_data()
        self.load_payload_data()


        self.selectDriver.show()


    def calculate(self):
        try: 
            transit = Transit(
                self.selectedDriver,
                self.selectedTruck, 
                self.selectedPayload, 
                self.fromDestination.getName(), 
                self.toDestination.getName(), 
                PriceList())
            
            transit.getDistance()

            self.distance = getattr(transit, 'distance')
            self.fuelPrice = transit.calculateFuelPrice()
            self.driverTime = transit.calculateDriverTime()
            self.driverSalary = transit.calculateDriverSalary()

            self.calculationPage.show()
            self.calculationPage.showCalculations()
        
        except Exception as e:
            print(e, "Error: Calculation failed.")

        

    def load_truck_data(self):
        with open(r'truckList.json', 'r') as file:
            self.truck_data = json.load(file)

    def load_driver_data(self):
        with open(r'driversList.json', 'r') as file:
            self.driver_data = json.load(file)
    
    def load_payload_data(self):
        with open(r'payloadList.json', 'r') as file:
            self.payload_data = json.load(file)

    def destroy_previous_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
        
    def add_driver(self):
        add_driver_window = AddDriverWindow(self, self.confirm_add_driver)

    def add_truck(self):
        add_truck_window = AddTruckWindow(self, self.confirm_add_truck)

    def add_payload(self):
        add_payload_window = AddPayloadWindow(self, self.confirm_add_payload, "PayloadRegular")

    def confirm_add_driver(self, name, surname, hireDate, hourlyBase ):
        print(f"Adding new driver: {name} {surname}")

    def confirm_add_truck(self, brand, model):
        print(f"Adding new truck: {brand} {model}")

    def confirm_add_payload(self, name, payload_type):
        print(f"Adding new payload: {name} {payload_type}")

   