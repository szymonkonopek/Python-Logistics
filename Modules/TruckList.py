import json
import uuid
from Modules.Truck import Truck

# Class which constructs and operates functions on truckList.json file 
class TruckList:
    def __init__(self):
        with open('truckList.json', 'r') as f:
            self.truckList = json.load(f)

# Add Truck object to the truckList.json
    def addTruck(self, truck):
        self.truckList.append(self.truckToJson(truck))
        print('trucklist', self.truckList)
        with open('truckList.json', 'w') as f:
            json.dump(self.truckList, f, indent=4)

# Transforms Truck class object attributes to json dictionary format
    def truckToJson(self, truck):
        return {
            "id": str(truck.id),
            "brand": truck.brand,
            "model": truck.model,
            "capacity": truck.capacity,
            "fuelEconomy": truck.fuelEconomy,
            "maxAllowedSpeed": truck.maxAllowedSpeed,
        }
    
# Transforms json dictionary object to Truck class object
    def jsonToTruck(self, truckJson):
        return Truck(truckJson['brand'], truckJson['model'], int(truckJson['capacity']), int(truckJson['fuelEconomy']), int(truckJson['maxAllowedSpeed']))

# Deletes Truck with given id from truckList.json
    def deleteTruck(self, truck_id):
        self.truckList = [truck for truck in self.truckList if truck['id'] != truck_id]
        with open('truckList.json', 'w') as f:
            json.dump(self.truckList, f)
    
# Function which returns a Truck object from given id
    def getTruck(self, truck_id):
        with open('truckList.json', 'r') as f:
            truckList = json.load(f)
        for truck in truckList:
            if truck['id'] == truck_id:
                return truck
        return None
    
# Function which retrun whole list of trucks
    def getTruckList(self):
        for i in range(len(self.truckList)):
            self.truckList[i] = self.jsonToTruck(self.truckList[i])
        return self.truckList

# Updates a Truck record in truckList.json
    def updateTruck(self, truck_id, truck):
        for i in range(len(self.truckList)):
            if self.truckList[i]['id'] == truck_id:
                self.truckList[i] = truck
                with open('truckList.json', 'w') as f:
                    json.dump(self.truckList, f)
                return True
        return False