import json

class DriverManager:
    @staticmethod
    def add_driver(id, name, surname, hireDate, hourlyBaseRate):
        # Load existing data from the JSON file
        with open('driversList.json', 'r') as file:
            data = json.load(file)

        # Create a new driver entry
        new_driver = {
            "id": id,
            "name": name,
            "surname": surname,
            "hireDate": hireDate,
            "hourlyBaseRate": hourlyBaseRate
        }

        # Add the new driver to the existing data
        data.append(new_driver)

        # Write the updated data back to the JSON file
        with open('driversList.json', 'w') as file:
            json.dump(data, file, indent=4)
