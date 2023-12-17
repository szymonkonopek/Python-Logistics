import json
from Modules.GUI.pages.SelectBaseInfo import SelectBaseInfo
from Modules.GUI.pages.SelectDestination import SelectDestination
from Modules.GUI.pages.CalculationPage import CalculationPage
from Modules.GUI.pages.Info import Info

class TruckChooserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Truck Chooser App")

        self.root.geometry("600x400")

        self.load_truck_data()
        self.load_driver_data()
        self.load_payload_data()

        self.selectDriver = SelectBaseInfo(self)
        self.selectDestination = SelectDestination(self)
        self.calculationPage = CalculationPage(self)
        self.info = Info(self)
        
        self.selectDriver.show()

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

   