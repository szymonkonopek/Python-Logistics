from Modules.Abstract.APayload import APayload

# An implementation of regular payload. 
# Price depends on the special needs.

class PayloadAnimal(APayload):
    def __init__(self, name, maxAllowedSpeed, specialNeeds):
        super().__init__(name, maxAllowedSpeed)
        self.type = __class__.__name__
        self.specialNeeds = specialNeeds