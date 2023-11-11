from datetime import date


class Driver:
    def __init__(self, name,surname) -> None:
        self.name = name
        self.surname = surname
        self.hireDate = None

    def setHireDate(self, year, month, day):
        try:
            if (year > date.today().year):
                print("Hire date cannot be set in the future.")
            else:
                self.hireDate = date(year=year, month=month, day=day)
                print(self.hireDate.strftime("%x"))
        except ValueError as e:
            print(f"An error has occured: {e}")


driver = Driver("Jan", "Kowalski")

driver.setHireDate(2022,12,31)