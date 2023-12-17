import json
from PayloadAnimal import PayloadAnimal
from PayloadRegular import PayloadRegular
from PayloadDangerous import PayloadDangerous

class PayloadList:
    def __init__(self):
        with open('payloadList.json', 'r') as f:
            self.payloadList = json.load(f)

    def addPayload(self, payload):
        payload_data = {
            "payloadType": payload.__class__.__name__,
            "payload": self.payloadToJson(payload)
        }
        self.payloadList.append(payload_data)
        with open('payloadList.json', 'w') as f:
            json.dump(self.payloadList, f, indent=4)

    def payloadToJson(self, payload):
        if isinstance(payload, PayloadRegular):
            return {
                "id": str(payload.id),
                "name": payload.name,
                "type": payload.type,
                "maxAllowedSpeed": payload.maxAllowedSpeed,
                "weight": payload.weight
            }
        elif isinstance(payload, PayloadAnimal):
            return {
                "id": str(payload.id),
                "name": payload.name,
                "type": payload.type,
                "maxAllowedSpeed": payload.maxAllowedSpeed,
                "specialNeeds": payload.specialNeeds
            }
        elif isinstance(payload, PayloadDangerous):
            return {
                "id": str(payload.id),
                "name": payload.name,
                "type": payload.type,
                "maxAllowedSpeed": payload.maxAllowedSpeed,
                "levelOfDanger": payload.levelOfDanger
            }

# Przykłady użycia:
payloadList = PayloadList()

# Dodawanie obiektów różnych klas do listy
payload_regular = PayloadRegular("RegularPayload", "Regular", 100, 50)
payloadList.addPayload(payload_regular)

payload_animal = PayloadAnimal("AnimalPayload", "Animal", 80, "Special needs")
payloadList.addPayload(payload_animal)

payload_dangerous = PayloadDangerous("DangerousPayload", "Dangerous", 120, "High")
payloadList.addPayload(payload_dangerous)
