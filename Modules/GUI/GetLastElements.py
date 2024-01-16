from Modules.Driver import Driver
from Modules.Truck import Truck
from Modules.PayloadList import PayloadList
from Modules.DriversList import DriversList
from Modules.TruckList import TruckList
import json

def GetLastDriver():
    json_file = "driversList.json"
    with open(json_file, 'r') as file:
        drivers_data = json.load(file)

    if drivers_data:
        last_driver_data = drivers_data[-1]
        
        lastDriverId = last_driver_data.get('id', '')
        return DriversList.jsonToDriver(DriversList, DriversList.getDriver(DriversList, lastDriverId))
    else:
        return None
    
def GetLastTruck():
    json_file = "truckList.json"
    with open(json_file, 'r') as file:
        truck_data = json.load(file)
        
    if truck_data:
        last_truck_data = truck_data[-1]
        lastTruckId = last_truck_data.get('id', '')
        return TruckList.jsonToTruck(TruckList, TruckList.getTruck(TruckList, lastTruckId))
    else :
        return None
    
    
def GetLastPayload():
    json_file = "payloadList.json"
    with open(json_file, 'r') as file:
        payload_data = json.load(file)
        
    if payload_data:
        last_payload_data = payload_data[-1]
        lastpayloadId = last_payload_data.get('id', '')
        return PayloadList.jsonToPayload(PayloadList, PayloadList.getPayload(PayloadList, lastpayloadId))
    else :
        return None
    
