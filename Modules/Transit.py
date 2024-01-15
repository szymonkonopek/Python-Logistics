# from Modules.Gpt import Gpt
from Modules.GoogleMaps import GoogleMaps
from Modules.PriceList import PriceList

# Class for calculating all of the Transit dependecies like Fuel Price, Driver's Time, Driver's experience
class Transit:
    def __init__(self, driver, truck, payload, destA, destB, priceList):
        self.driver = driver
        self.truck = truck
        self.payload = payload
        self.destA = destA
        self.destB = destB
        self.priceList = priceList
        self.totalTime = None

    def getDistance(self):
        self.distance = GoogleMaps.calcDistance(self.destA, self.destB)
        return self.distance

# An average price of fuel based on the covered distance and average fuel economy of a Truck
    def calculateFuelPrice(self):
        fuelEconomy = getattr(self.truck, 'fuelEconomy')
        return (int) ((self.distance / 100.0) * fuelEconomy * self.priceList.getFuelPriceEuro())
    
# Drivers' total driving time is based on the covered distance, max allowed speed (based on payload) and driver's rest time for every 8 hours of driving.
# Time after work is not counted (eg. for sleep, meals).
# Also, if the payload type is Animal and the special needs are required, then the breaks are done every 4 hours, for the Animal safety.
    def calculateDriverTime(self):
        drivingTime = self.distance / getattr(self.payload, 'maxAllowedSpeed')
        if (self.payload.type == "PayloadAnimal" and self.payload.specialNeeds == True):
            restTime = (int) (drivingTime / 4)
        else: 
            restTime = (int) (drivingTime / 8)
        self.totalTime = drivingTime + restTime
        return self.totalTime

# Depending on the kind of the Payload, the multiplier of the salary variable may differ
    def getPayloadMultiplier(self):
        if self.payload.type == 'PayloadDangerous':
            return 1.5
        elif self.payload.type == 'PayloadAnimal':
            return 1.2
        else:
            return 1
        
# Aditional cost
    def additionalCost(self):
        if (self.payload.type == "PayloadDangerous"):
            return PriceList.getPayloadDangerousPrice(self.payload.levelOfDanger) * (self.getDistance() / 100)
        return 0
        
    
# Function to calculate Drivers' salary
    def calculateDriverSalary(self):
        total = (self.totalTime * getattr(self.driver, 'hourlyBaseRate') * (1 + ((self.driver.getYearsOfExperience())/5))) * self.getPayloadMultiplier() + self.additionalCost()
        return total