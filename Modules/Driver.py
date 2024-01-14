from datetime import date
import uuid

class Driver:
    def __init__(self, name, surname, hireDate, hourlyBaseRate) -> None:
        self.name = name
        self.surname = surname
        self.hireDate = hireDate
        self.hourlyBaseRate = hourlyBaseRate
        self.id = uuid.uuid1()
    
    def getNameSurname(self):
        return self.name + " " + self.surname

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
            print("Hourly rate has been set to: " + str(self.hourlyBaseRate) +" EURO.")
        else:
            print("Firstly set hire date.")

    def getYearsOfExperience(self):
        yearsOfExperience = date.today().year - self.hireDate.year
        return yearsOfExperience
