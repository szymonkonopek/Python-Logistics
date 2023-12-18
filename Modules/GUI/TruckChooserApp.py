import json
from datetime import date

from Modules.GUI.pages.SelectBaseInfo import SelectBaseInfo
from Modules.GUI.pages.SelectDestination import SelectDestination
from Modules.GUI.pages.CalculationPage import CalculationPage
from Modules.GUI.pages.Info import Info
from Modules.Transit import Transit

from Modules.Truck import Truck
from Modules.Driver import Driver
from Modules.PayloadDangerous import PayloadDangerous
from Modules.PriceList import PriceList


class TruckChooserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Truck Chooser App")

        # to są wartości które są wpisane na stałe, trzeba zrobić tak zeby sie dynamicznie zmienaly
        self.selectedDriver = Driver("Walter", "White", 8, date(2000,1,1))
        self.selectedPayload = PayloadDangerous('Dynamite', maxAllowedSpeed=80, levelOfDanger=90)

        self.selectedTruck = Truck('Scania truck', 'Scania', 2000, 14, self.selectedPayload.getMaxAllowedSpeed)

        self.fromDestination = "Krakow"
        self.toDestination = "Mielno"

        self.distance = ""
        self.fuelPrice = ""
        self.driverTime = ""
        self.driverSalary = ""

        self.root.geometry("600x600")

        self.load_truck_data()
        self.load_driver_data()
        self.load_payload_data()

        self.selectDriver = SelectBaseInfo(self)
        self.selectDestination = SelectDestination(self)
        self.calculationPage = CalculationPage(self)
        self.info = Info(self)
        
        self.selectDriver.show()

    def calculate(self):
        transit = Transit(
            self.selectedDriver,
            self.selectedTruck, 
            self.selectedPayload, 
            self.fromDestination, 
            self.toDestination, 
            PriceList())
        
        transit.getDistance()

        self.distance = getattr(transit, 'distance')
        self.fuelPrice = transit.calculateFuelPrice()
        self.driverTime = transit.calculateDriverTime()
        self.driverSalary = transit.calculateDriverSalary()

        self.calculationPage.show()
        self.calculationPage.showCalculations()


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

   