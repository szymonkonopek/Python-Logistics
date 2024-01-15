# Class for fetching price lists
class PriceList:
    def __init__(self):
        self.fuelPriceEuro = 1.6

    def getFuelPriceEuro(self):
        return self.fuelPriceEuro
    
    # implement here dependencies of additional costs whether it's regular/dangarous or animal payload. Price is in Dollars $ per every 100km
    @staticmethod
    def getPayloadDangerousPrice(levelOfDanger):
    # 1 - type explosive
    # 2 - gases
    # 3 - flammable liquid
    # 4 - flammable solids
    # 5 - Oxidizing substances
    # 6 - toxic
    # 7 - Radioactive materials
    # 8 - Corrosive substances
    # 9 - various dangerous materials and items
        cases = {
            1: 2,
            2: 3,
            3: 5,
            4: 8,
            5: 13,
            6: 21,
            7: 34,
            8: 55,
            9: 5
        }
        return cases.get(levelOfDanger, "Invalid number")