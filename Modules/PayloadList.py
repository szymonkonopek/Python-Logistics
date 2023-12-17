import json
import uuid
from Modules.Payload import Payload
from Modules.PayloadAnimal import PayloadAnimal
from Modules.PayloadRegular import PayloadRegular
from Modules.PayloadDangerous import PayloadDangerous

class PayloadList:
    def __init__(self):
        with open('payloadList.json', 'r') as f:
            self.payloadList = json.load(f)

    # def addPayload(self, payload):
    #     self.payloadList.append(self.payloadToJson(payload))
    #     print('payloadList', self.payloadList)
    #     with open('payloadList.json', 'w') as f:
    #         json.dump(self.payloadList, f, indent=4)
