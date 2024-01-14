import json
import uuid
from Modules.Truck import Truck

class TruckList:
    def __init__(self):
        with open('truckList.json', 'r') as f:
            self.truckList = json.load(f)

    def addTruck(self, truck):
        self.truckList.append(self.truckToJson(truck))
        print('trucklist', self.truckList)
        with open('truckList.json', 'w') as f:
            json.dump(self.truckList, f, indent=4)

    def truckToJson(self, truck):
        return {
            "id": str(truck.id),
            "brand": truck.brand,
            "model": truck.model,
            "capacity": truck.capacity,
            "fuelEconomy": truck.fuelEconomy,
            "maxAllowedSpeed": truck.maxAllowedSpeed,
        }
    
    def jsonToTruck(self, truckJson):
        return Truck(truckJson['brand'], truckJson['model'], int(truckJson['capacity']), int(truckJson['fuelEconomy']), truckJson['otherThings'])

    def deleteTruck(self, truck_id):
        self.truckList = [truck for truck in self.truckList if truck['id'] != truck_id]
        with open('truckList.json', 'w') as f:
            json.dump(self.truckList, f)
    
    def getTruck(self, truck_id):
        for truck in self.truckList:
            if truck['id'] == truck_id:
                return truck
        return None
    
    def getTruckList(self):
        for i in range(len(self.truckList)):
            self.truckList[i] = self.jsonToTruck(self.truckList[i])
        print('hello')
        print(getattr(self.truckList[0], 'fuelEconomy'))
        return self.truckList
    
    def updateTruck(self, truck_id, truck):
        for i in range(len(self.truckList)):
            if self.truckList[i]['id'] == truck_id:
                self.truckList[i] = truck
                with open('truckList.json', 'w') as f:
                    json.dump(self.truckList, f)
                return True
        return False