import json
from Modules.PayloadAnimal import PayloadAnimal
from Modules.PayloadRegular import PayloadRegular
from Modules.PayloadDangerous import PayloadDangerous

class PayloadList:
    def __init__(self):
        with open('payloadList.json', 'r') as f:
            self.payloadList = json.load(f)

    def addPayload(self, payload):
        self.payloadList.append(self.payloadToJson(payload))
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
    
    def jsonToPayload(self, json_data):
        payload_type = json_data.get("type", None)
        if payload_type == "PayloadRegular":
            return PayloadRegular(
                json_data["id"],
                json_data["name"],
                json_data["type"],
                json_data["maxAllowedSpeed"],
                json_data["weight"]
            )
        elif payload_type == "PayloadAnimal":
            return PayloadAnimal(
                json_data["id"],
                json_data["name"],
                json_data["type"],
                json_data["maxAllowedSpeed"],
                json_data["specialNeeds"]
            )
        elif payload_type == "PayloadDangerous":
            return PayloadDangerous(
                json_data["id"],
                json_data["name"],
                json_data["type"],
                json_data["maxAllowedSpeed"],
                json_data["levelOfDanger"]
            )
        else:
            raise ValueError(f"Unsupported payload type: {payload_type}")

    def deletePayload(self, payload_id):
        self.payloadList = [payload for payload in self.payloadList if payload['id'] != payload_id]
        with open('payloadList.json', 'w') as f:
            json.dump(self.payloadList, f, indent=4)

    def getPayload(self, payload_id):
        for payload in self.payloadList:
            if payload['id'] == payload_id:
                return payload
        return None
    
    def getPayloadList(self):
        for i in range(len(self.payloadList)):
            self.payloadList[i] = self.jsonToPayload(self.payloadList[i])
        return self.payloadList

#Przykłady użycia:
# payloadList = PayloadList()

# # Dodawanie obiektów różnych klas do listy
# payload_regular = PayloadRegular("Coal", 100, 50)
# payloadList.addPayload(payload_regular)

# payload_animal = PayloadAnimal("Zebras", 80, "Special needs")
# payloadList.addPayload(payload_animal)

# payload_dangerous = PayloadDangerous("Oil", 120, "High")
# payloadList.addPayload(payload_dangerous)

# payloadList.deletePayload("id")