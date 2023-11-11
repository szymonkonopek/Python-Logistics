from Modules.Gpt import Gpt

class Transit:
    def __init__(self, driver, truck, payload, destA, destB, priceList):
        self.driver = driver
        self.truck = truck
        self.payload = payload
        self.destA = destA
        self.destB = destB
        self.priceList = priceList

    def calculateDistance(self):
        return Gpt.calcDistance(self.destA, self.destB)

    def calculateRequiredFuelAmmount(self):
        return self.priceList.getattr()

    def calculatePriceForTrip(self):
        distance = self.calculateDistance()
        print(distance)


    

    

    
    

    
