from datetime import date, datetime
import uuid

# Driver class initiation
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
# Additional salary is based on the Drivers' experience
    def getYearsOfExperience(self):
        hireDate_obj = datetime.strptime(self.hireDate,'%m/%d/%Y')
        yearsOfExperience = int(datetime.now().year - hireDate_obj.year)
        return yearsOfExperience
