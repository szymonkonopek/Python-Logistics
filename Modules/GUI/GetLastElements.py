from Modules.Driver import Driver
from Modules.Truck import Truck
from Modules.PayloadList import PayloadList
from Modules.DriversList import DriversList
from Modules.TruckList import TruckList
import json

def getLastDriver():
    drivers_data = DriversList()

    if drivers_data:
        return DriversList.jsonToDriver(drivers_data.getDriversList()[-1])
    
def getLastTruck():
    truck_data = TruckList()

    if truck_data:
        return truck_data.getTruckList()[-1]
    
def getLastPayload():
    payload_data = PayloadList()
        
    if payload_data:
        return PayloadList.jsonToPayload(payload_data.getPayloadList()[-1])
    
