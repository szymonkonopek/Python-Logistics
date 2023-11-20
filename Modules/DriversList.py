import json
from datetime import date

class DriversList():
    def __init__(self):
        with open('driversList.json', 'r') as f:
            self.driversList = json.load(f)

    def addDriver(self, driver):
        self.driversList.append(self.driverToJson(driver))
        print('drivers list', self.driversList)
        with open('driversList.json', 'w') as f:
            json.dump(self.driversList, f, indent=4)

    def driverToJson(self, driver):
        return {
            "id": str(driver.id),
            "name": driver.name,
            "surname": driver.surname,
            "hireDate": driver.hireDate.strftime("%x"), 
            "hourlyBaseRate": driver.hourlyBaseRate
        }

    def deletedriver(self, driver_id):
        self.driversList = [driver for driver in self.driversList if driver['id'] != driver_id]
        with open('driversList.json', 'w') as f:
            json.dump(self.driversList, f)
    
    def getDriver(self, driver_id):
        for driver in self.driversList:
            if driver['id'] == driver_id:
                return driver
        return None
    
    def getdriversList(self):
        return self.driversList
    
    def updateDriver(self, driver_id, driver):
        for i in range(len(self.driversList)):
            if self.driversList[i]['id'] == driver_id:
                self.driversList[i] = driver
                with open('driversList.json', 'w') as f:
                    json.dump(self.driversList, f)
                return True
        return False