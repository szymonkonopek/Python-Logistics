from Modules.Gpt import Gpt

class Transit:
    def __init__(self, driver, truck, payload, destA, destB, priceList):
        self.driver = driver
        self.truck = truck
        self.payload = payload
        self.destA = destA
        self.destB = destB
        self.priceList = priceList

        

    def getDistance(self):
        self.distance = Gpt.calcDistance(self.destA, self.destB)
        return self.distance

    def calculateFuelPrice(self):
        fuelEconomy = getattr(self.truck, 'fuel_economy')
        print(self.distance, fuelEconomy)
        return (int) ((self.distance / 100.0) * fuelEconomy * self.priceList.getFuelPriceEuro())
    
    def calculateDriverTime(self):
        drivingTime = self.distance / getattr(self.payload, 'maxAllowedSpeed')
        restTime = (int) (drivingTime / 8)
        totalTime = drivingTime + restTime
        return totalTime
        