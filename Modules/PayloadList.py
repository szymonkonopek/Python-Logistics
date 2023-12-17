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
    
    def jsonToPayload(self, payloadJson):
        payload_type = payloadJson.get("payloadType", "")
        payload_data = payloadJson.get("payload", {})

        if payload_type == "PayloadRegular":
            return PayloadRegular(
                payload_data["name"],
                payload_data["type"],
                payload_data["maxAllowedSpeed"],
                payload_data["weight"]
            )
        elif payload_type == "PayloadAnimal":
            return PayloadAnimal(
                payload_data["name"],
                payload_data["type"],
                payload_data["maxAllowedSpeed"],
                payload_data["specialNeeds"]
            )
        elif payload_type == "PayloadDangerous":
            return PayloadDangerous(
                payload_data["name"],
                payload_data["type"],
                payload_data["maxAllowedSpeed"],
                payload_data["levelOfDanger"]
            )
        else:
            raise ValueError(f"Unsupported payload type: {payload_type}")

    def deletePayload(self, payload_id):
        self.payloadList = [payload for payload in self.payloadList if payload['payload']['id'] != payload_id]
        with open('payloadList.json', 'w') as f:
            json.dump(self.payloadList, f, indent=4)

    def getPayload(self, payload_id):
        for payload in self.payloadList:
            if payload["payload"]['id'] == payload_id:
                return payload
        return None
    
    def getPayloadList(self):
        for i in range(len(self.payloadList)):
            self.payloadList[i] = self.jsonToPayload(self.payloadList[i])
        return self.payloadList

# Przykłady użycia:
# payloadList = PayloadList()

# # Dodawanie obiektów różnych klas do listy
# payload_regular = PayloadRegular("RegularPayload", "Regular", 100, 50)
# payloadList.addPayload(payload_regular)

# payload_animal = PayloadAnimal("AnimalPayload", "Animal", 80, "Special needs")
# payloadList.addPayload(payload_animal)

# payload_dangerous = PayloadDangerous("DangerousPayload", "Dangerous", 120, "High")
# payloadList.addPayload(payload_dangerous)

# payload_list = PayloadList()

# # Wczytywanie danych z pliku JSON
# with open('payloadList.json', 'r') as f:
#     json_data = json.load(f)

# # Tworzenie obiektów na podstawie danych z pliku JSON
# for payload_json in json_data:
#     payload_object = payload_list.jsonToPayload(payload_json)

# payloadList = PayloadList()

# payloadList.getPayloadList()