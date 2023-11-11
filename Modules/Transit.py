from Gpt import Gpt

class Transit():
    def __init__(self, driver, truck, payload, destA, destB):
        self.driver = driver
        self.truck = truck
        self.payload = payload
        self.destA = destA
        self.destB = destB

    def calculateDistance(self,destA, destB):
        return Gpt.calcDistance(destA, destB)
    
    
    

    
    

    
