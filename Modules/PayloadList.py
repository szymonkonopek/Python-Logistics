import json
from Modules.PayloadAnimal import PayloadAnimal
from Modules.PayloadRegular import PayloadRegular
from Modules.PayloadDangerous import PayloadDangerous

# Class which constructs and operates functions on payloadList.json file 
class PayloadList:
    def __init__(self):
        with open('payloadList.json', 'r') as f:
            self.payloadList = json.load(f)

# Add Payload object to the payloadList.json
    def addPayload(self, payload):
        self.payloadList.append(self.payloadToJson(payload))
        with open('payloadList.json', 'w') as f:
            json.dump(self.payloadList, f, indent=4)


# Transforms Payload class object attributes to json dictionary format (depending on the type)
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
    
# Transforms json dictionary object to Payload class object
    @staticmethod
    def jsonToPayload(json_data):
        print(json_data)
        print("s")
        payload_type = json_data["type"]
        if payload_type == "PayloadRegular":
            return PayloadRegular(
                #json_data["id"],
                json_data["name"],
                # json_data["type"],
                json_data["maxAllowedSpeed"],
                json_data["weight"]
            )
        elif payload_type == "PayloadAnimal":
            return PayloadAnimal(
                #json_data["id"],
                json_data["name"],
                # json_data["type"],
                json_data["maxAllowedSpeed"],
                json_data["specialNeeds"]
            )
        elif payload_type == "PayloadDangerous":
            return PayloadDangerous(
                #json_data["id"],
                json_data["name"],
                # json_data["type"],
                json_data["maxAllowedSpeed"],
                json_data["levelOfDanger"]
            )
        else:
            raise ValueError(f"Unsupported payload type: {payload_type}")

# Deletes Payload with given id from payloadLis.json
    def deletePayload(self, payload_id):
        self.payloadList = [payload for payload in self.payloadList if payload['id'] != payload_id]
        with open('payloadList.json', 'w') as f:
            json.dump(self.payloadList, f, indent=4)

# Function which returns a Payload object from given id
    def getPayload(self, payload_id):
        with open('payloadList.json', 'r') as f:
            payloadList = json.load(f)
        for payload in payloadList:
            if payload['id'] == payload_id:
                return payload
        return None
    
# Function which retrun whole list of payload
    def getPayloadList(self):
        for i in range(len(self.payloadList)):
            self.payloadList[i] = self.jsonToPayload(self.payloadList[i])
        return self.payloadList