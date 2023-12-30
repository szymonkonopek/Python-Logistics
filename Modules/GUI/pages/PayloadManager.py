import json

class PayloadManager:
    @staticmethod
    def add_payload(id, name, type, maxAllowedSpeed, **payload_attributes):
        # Load existing data from the JSON file
        with open('payloadList.json', 'r') as file:
            data = json.load(file)

        # Create a new payload entry
        new_payload = {
            "id": id,
            "name": name,
            "type": type,
            "maxAllowedSpeed": maxAllowedSpeed,
            **payload_attributes
        }

        # Add the new payload to the existing data
        data.append(new_payload)

        # Write the updated data back to the JSON file
        with open('payloadList.json', 'w') as file:
            json.dump(data, file, indent=4)


