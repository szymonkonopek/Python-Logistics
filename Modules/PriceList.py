# Class for fetching price lists
class PriceList:
    def __init__(self):
        self.fuelPriceEuro = 1.6

    def getFuelPriceEuro(self):
        return self.fuelPriceEuro
    
    # implement here dependencies of additional costs whether it's regular/dangarous or animal payload