import json

class TruckManager:
    @staticmethod
    def add_truck(id, brand, model, capacity, fuelEconomy, **truck_attributes):
        # Load existing data from the JSON file
        with open('truckList.json', 'r') as file:
            data = json.load(file)

        # Create a new truck entry
        new_truck = {
            "id": id,
            "brand": brand,
            "model": model,
            "capacity": capacity,
            "fuelEconomy": fuelEconomy,
            **truck_attributes
        }

        # Add the new truck to the existing data
        data.append(new_truck)

        # Write the updated data back to the JSON file
        with open('truckList.json', 'w') as file:
            json.dump(data, file, indent=4)
