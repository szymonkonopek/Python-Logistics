from Modules.Transit import Transit
from Modules.Driver import Driver
from Modules.Truck import Truck
from Modules.Payload import Payload
from Modules.Destination import Destination
from Modules.PriceList import PriceList

driver = Driver("Walter", "White")
truck = Truck('Scania', 'Scania', 2000, 14)
payload = Payload('Dynamite', 'Dangerous')
destA = Destination('Krakow')
destB = Destination('Lisbon')
priceList = PriceList()

transit = Transit(driver, truck, payload, destA, destB, priceList)
transit.calculatePriceForTrip()


