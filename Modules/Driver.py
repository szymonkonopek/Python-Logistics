from datetime import date


class Driver:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname
        self.hireDate = None
        self.hourlyBaseRate = None
    

    def setHireDate(self, year, month, day):
        try:
            if (date(year,month,day) > date.today()):
                print("Hire date cannot be set in the future.")
            else:
                self.hireDate = date(year=year, month=month, day=day)
                print("Hire date has been set to: " + self.hireDate.strftime("%x") + ".")
        except ValueError as e:
            print(f"An error has occured: {e}")

    def setHourlyBaseRate(self, rate):
        if (self.hireDate != None):
            self.hourlyBaseRate = rate
            print("Horly rate has been set to: " + str(self.hourlyBaseRate) +" PLN.")
        else:
            print("Firstly set hire date.")