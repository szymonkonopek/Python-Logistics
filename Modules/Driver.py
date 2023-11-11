import datetime


class Driver:
    def __init__(self, name,surname) -> None:
        self.name = name
        self.surname = surname
        self.hireDate = None
    

    def setHireDate(self, year, month, day):
        self.hireDate = datetime.datetime(year=year, month=month, day=day)
        print("Hire date has been set: " + self.hireDate.strftime("%x"))


driver = Driver("Jan", "Kowalski")

driver.setHireDate(2022,7,12)