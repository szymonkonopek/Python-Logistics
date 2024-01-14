import json
from datetime import date

# Class which constructs and operates functions on driversList.json file 
class DriversList():
    def __init__(self):
        with open('driversList.json', 'r') as f:
            self.driversList = json.load(f)

# Add Driver object to the truckList.json
    def addDriver(self, driver):
        self.driversList.append(self.driverToJson(driver))
        print('drivers list', self.driversList)
        with open('driversList.json', 'w') as f:
            json.dump(self.driversList, f, indent=4)

# Transforms Driver class object attributes to json dictionary format
    def driverToJson(self, driver):
        return {
            "id": str(driver.id),
            "name": driver.name,
            "surname": driver.surname,
            "hireDate": driver.hireDate, 
            "hourlyBaseRate": driver.hourlyBaseRate
        }
    
# Deletes Driver from json file
    def deleteDriver(self, driver_id):
        self.driversList = [driver for driver in self.driversList if driver['id'] != driver_id]
        with open('driversList.json', 'w') as f:
            json.dump(self.driversList, f)
    
# Function which returns a Driver object from given id
    def getDriver(self, driver_id):
        for driver in self.driversList:
            if driver['id'] == driver_id:
                return driver
        return None

# Function which retrun whole list of drivers
    def getDriversList(self):
        return self.driversList
    
# Updates a Driver record in driversList.json
    def updateDriver(self, driver_id, driver):
        for i in range(len(self.driversList)):
            if self.driversList[i]['id'] == driver_id:
                self.driversList[i] = driver
                with open('driversList.json', 'w') as f:
                    json.dump(self.driversList, f)
                return True
        return False