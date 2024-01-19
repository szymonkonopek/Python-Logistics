from tkinter import messagebox, ttk

class CalculationPage:
    def __init__(self, app):
        self.app = app

    def show(self):
        self.app.destroy_previous_widgets()

        label_driver = ttk.Label(self.app.root, text="Driver")
        label_driver.grid(row=1, column=1, pady=10, padx=10)

        label_driver = ttk.Label(self.app.root, text=f"{self.app.selectedDriver.getNameSurname()}")
        label_driver.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        label_driver = ttk.Label(self.app.root, text=f"Hire date: {self.app.selectedDriver.hireDate}")
        label_driver.grid(row=3, column=1, pady=10, padx=10, sticky="w")

        label_driver = ttk.Label(self.app.root, text=f"Base hourly rate: {self.app.selectedDriver.hourlyBaseRate}$")
        label_driver.grid(row=4, column=1, pady=10, padx=10, sticky="w")

        label_truck = ttk.Label(self.app.root, text="Truck")
        label_truck.grid(row=1, column=2, pady=10, padx=10)

        label_truck = ttk.Label(self.app.root, text=f"{self.app.selectedTruck.getBrandModel()}")
        label_truck.grid(row=2, column=2, pady=10, padx=10, sticky="w")

        label_truck = ttk.Label(self.app.root, text=f"Max speed: {self.app.selectedTruck.maxAllowedSpeed} km/h")
        label_truck.grid(row=3, column=2, pady=10, padx=10, sticky="w")

        label_truck = ttk.Label(self.app.root, text=f"Capacity: {self.app.selectedTruck.capacity} kg")
        label_truck.grid(row=4, column=2, pady=10,padx=10, sticky="w")

        label_truck = ttk.Label(self.app.root, text=f"Fuel economy: {self.app.selectedTruck.fuelEconomy} l/100km")
        label_truck.grid(row=5, column=2, pady=10, padx=10,sticky="w")

        label_payload = ttk.Label(self.app.root, text="Payload")
        label_payload.grid(row=1, column=3, pady=10, padx=10)

        label_payload = ttk.Label(self.app.root, text=f"Name: {self.app.selectedPayload.getName()}")
        label_payload.grid(row=2, column=3, pady=10, padx=10,sticky="w")

        label_payload = ttk.Label(self.app.root, text=f"Type: {self.app.selectedPayload.type}")
        label_payload.grid(row=3, column=3, pady=10, padx=10, sticky="w")

        label_payload = ttk.Label(self.app.root, text=f"Max speed: {self.app.selectedPayload.maxAllowedSpeed} km/h")
        label_payload.grid(row=4, column=3, pady=10, padx=10, sticky="w")

        if (self.app.selectedPayload.type == "PayloadRegular"):
            label_payload = ttk.Label(self.app.root, text=f"Weight: {self.app.selectedPayload.weight} kg")
            label_payload.grid(row=5, column=3, pady=10, padx=10, sticky="w")

        elif (self.app.selectedPayload.type == "PayloadDangerous"):
            label_payload = ttk.Label(self.app.root, text=f"Class of danger: {self.app.selectedPayload.levelOfDanger}")
            label_payload.grid(row=5, column=3, pady=10,padx=10, sticky="w")

        else:
            label_payload = ttk.Label(self.app.root, text=f"Special needs: {self.app.selectedPayload.specialNeeds}")
            label_payload.grid(row=5, column=3, pady=10, padx=10, sticky="w")
        
        label_payload = ttk.Label(self.app.root, text="Transit")
        label_payload.grid(row=1, column=4, pady=10, padx=10,)

        label_from = ttk.Label(self.app.root, text=f"From: {self.app.fromDestination.getName()}")
        label_from.grid(row=3, column=4, pady=10, padx=10)

        label_to = ttk.Label(self.app.root, text=f"To: {self.app.toDestination.getName()}")
        label_to.grid(row=4, column=4, pady=10, padx=10)

        prev_page_button = ttk.Button(self.app.root, text="Previous", command=self.app.selectDestination.show)
        prev_page_button.grid(row=6, column=2, pady=10, padx=10)

        calculate_button = ttk.Button(self.app.root, text="Calculate", command=self.app.calculate)
        calculate_button.grid(row=6, column=3, pady=10, padx=10)

    def showCalculations(self):
        if self.app.selectedPayload.type == "PayloadRegular" and self.app.selectedPayload.weight > self.app.selectedTruck.capacity:
            messagebox.showerror("Error", "Payload weighs more than the available capacity of a selected truck.\nPlease choose proper truck.")
        else:
            label_distance = ttk.Label(self.app.root, text=f"Distance: {self.app.distance} km")
            label_distance.grid(row=7, column=1, pady=10, padx=10)

            label_fuel_price = ttk.Label(self.app.root, text=f"Fuel Price: {self.app.fuelPrice} $")
            label_fuel_price.grid(row=7, column=2, pady=10, padx=10, sticky="w")

            label_driver_time = ttk.Label(self.app.root, text=f"Driver Time: {self.app.driverTime} hours")
            label_driver_time.grid(row=7, column=3, pady=10, padx=10)

            label_driver_salary = ttk.Label(self.app.root, text=f"Total salary: {self.app.driverSalary} $")
            label_driver_salary.grid(row=7, column=4, pady=10, padx=10)

            calculate_button = ttk.Button(self.app.root, text="Restart calculator", command=self.app.selectDriver.show)
            calculate_button.grid(row=8, column=2,columnspan=2,padx=10, pady=10)
