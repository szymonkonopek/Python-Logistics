from Modules.Transit import Transit
from Modules.Driver import Driver
from Modules.Truck import Truck
from Modules.Destination import Destination
from Modules.PriceList import PriceList
from Modules.PayloadDangerous import PayloadDangerous
from Modules.truckList import TruckList


driver = Driver("Walter", "White")
driver.setHireDate(2022,11,2)
driver.setHourlyBaseRate(8)
truckList = TruckList()
truck = Truck('Scania', 'Scania', 2000, 14, 'otherThings')
truckList.addTruck(truck)
truck2 = truckList.getTruckList()[0]
print(truck2["id"])
payload = PayloadDangerous('Dynamite', 'Dangerous', maxAllowedSpeed=80, levelOfDanger=90)
destA = Destination('Krakow')
destB = Destination('Lisbon')
priceList = PriceList()

transit = Transit(driver, truck, payload, destA, destB, priceList)
transit.getDistance()
print("fuel price:",transit.calculateFuelPrice())
print("driver time:",transit.calculateDriverTime())
print("driver salary: ",transit.calculateDriverSalary())

