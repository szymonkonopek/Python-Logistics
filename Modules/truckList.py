import json
import uuid


class TruckList:
    def __init__(self):
        with open('truckList.json', 'r') as f:
            self.truckList = json.load(f)

    def addTruck(self, truck):
        self.truckList.append(truck)
        with open('truckList.json', 'w') as f:
            json.dump(self.truckList, f)

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
        return self.truckList
    
    def updateTruck(self, truck_id, truck):
        for i in range(len(self.truckList)):
            if self.truckList[i]['id'] == truck_id:
                self.truckList[i] = truck
                with open('truckList.json', 'w') as f:
                    json.dump(self.truckList, f)
                return True
        return False