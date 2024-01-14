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
        fuelEconomy = getattr(self.truck, 'fuelEconomy')
        return (int) ((self.distance / 100.0) * fuelEconomy * self.priceList.getFuelPriceEuro())
    
    def calculateDriverTime(self):
        drivingTime = self.distance / getattr(self.payload, 'maxAllowedSpeed')
        restTime = (int) (drivingTime / 8)
        self.totalTime = drivingTime + restTime
        return self.totalTime

    def getPayloadMultiplier(self):
        if self.payload.type == 'PayloadDangerous':
            return 1.5
        elif self.payload.type == 'PayloadAnimal':
            return 1.2
        else:
            return 1
    
    def calculateDriverSalary(self):
        total = (self.totalTime * getattr(self.driver, 'hourlyBaseRate') * (1 + ((self.driver.getYearsOfExperience())/5))) * self.getPayloadMultiplier()
        return total