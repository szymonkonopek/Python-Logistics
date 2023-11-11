from Modules.Gpt import Gpt

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
        self.distance = Gpt.calcDistance(self.destA, self.destB)
        return self.distance

    def calculateFuelPrice(self):
        fuelEconomy = getattr(self.truck, 'fuel_economy')
        return (int) ((self.distance / 100.0) * fuelEconomy * self.priceList.getFuelPriceEuro())
    
    def calculateDriverTime(self):
        drivingTime = self.distance / getattr(self.payload, 'maxAllowedSpeed')
        restTime = (int) (drivingTime / 8)
        self.totalTime = drivingTime + restTime
        return self.totalTime
    
    def calculateDriverSalary(self):
        total = self.totalTime * getattr(self.driver, 'hourlyBaseRate') * (1 + ((self.driver.getYearsOfExperience())/5))
        return total