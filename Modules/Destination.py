# Destination Class
class Destination:
    def __init__(self):
        self.name = ""

    def __str__(self):
        return self.name
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name