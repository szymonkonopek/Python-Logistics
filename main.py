from Modules.Transit import Transit
from Modules.Driver import Driver
from Modules.Truck import Truck
from Modules.Payload import Payload
from Modules.Destination import Destination
from Modules.PriceList import PriceList

driver = Driver("Walter", "White")
driver.setHireDate(2022,11,2)
driver.setHourlyBaseRate(8)
truck = Truck('Scania', 'Scania', 2000, 14)
payload = Payload('Dynamite', 'Dangerous', 80)
destA = Destination('Krakow')
destB = Destination('Lisbon')
priceList = PriceList()

transit = Transit(driver, truck, payload, destA, destB, priceList)
transit.getDistance()
print("fuel price:",transit.calculateFuelPrice())
print("driver time:",transit.calculateDriverTime())
print("driver salary: ",transit.calculateDriverSalary())

