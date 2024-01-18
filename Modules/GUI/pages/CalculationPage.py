from tkinter import messagebox, ttk

class CalculationPage:
    def __init__(self, app):
        self.app = app

    def show(self):
        self.app.destroy_previous_widgets()

        label_driver = ttk.Label(self.app.root, text=f"Driver:")
        label_driver.grid(row=1, column=1, pady=10, sticky="w")

        label_driver = ttk.Label(self.app.root, text=f"{self.app.selectedDriver.getNameSurname()}")
        label_driver.grid(row=2, column=1, pady=10, sticky="w")

        label_driver = ttk.Label(self.app.root, text=f"Hire date: {self.app.selectedDriver.hireDate}")
        label_driver.grid(row=3, column=1, pady=10, sticky="w")

        label_driver = ttk.Label(self.app.root, text=f"Base hourly rate: {self.app.selectedDriver.hourlyBaseRate}")
        label_driver.grid(row=4, column=1, pady=10, sticky="w")

        label_truck = ttk.Label(self.app.root, text=f"Truck:")
        label_truck.grid(row=1, column=2, pady=10, sticky="w")

        label_truck = ttk.Label(self.app.root, text=f"{self.app.selectedTruck.getBrandModel()}")
        label_truck.grid(row=2, column=2, pady=10, sticky="w")

        label_truck = ttk.Label(self.app.root, text=f"Max speed: {self.app.selectedTruck.maxAllowedSpeed}")
        label_truck.grid(row=3, column=2, pady=10, sticky="w")

        label_truck = ttk.Label(self.app.root, text=f"Capacity: {self.app.selectedTruck.capacity}")
        label_truck.grid(row=4, column=2, pady=10, sticky="w")

        label_truck = ttk.Label(self.app.root, text=f"Fuel economy: {self.app.selectedTruck.fuelEconomy}")
        label_truck.grid(row=5, column=2, pady=10, sticky="w")

        label_payload = ttk.Label(self.app.root, text=f"Payload: {self.app.selectedPayload.getName()}")
        label_payload.grid(row=1, column=3, pady=10, sticky="w")

        label_from = ttk.Label(self.app.root, text=f"From: {self.app.fromDestination.getName()}")
        label_from.grid(row=2, column=3, pady=10, sticky="w")

        label_to = ttk.Label(self.app.root, text=f"To: {self.app.toDestination.getName()}")
        label_to.grid(row=3, column=3, pady=10, sticky="w")

        prev_page_button = ttk.Button(self.app.root, text="Previous", command=self.app.selectDestination.show)
        prev_page_button.grid(row=5, column=1, pady=10, sticky="w")

        calculate_button = ttk.Button(self.app.root, text="Calculate", command=self.app.calculate)
        calculate_button.grid(row=6, column=1, pady=10, sticky="w")

    def showCalculations(self):
        if self.app.selectedPayload.type == "PayloadRegular" and self.app.selectedPayload.weight > self.app.selectedTruck.capacity:
            error_label = ttk.Label(self.app.root, text="Error: Payload weighs more than the available capacity of a selected truck.\n"
                                    "Please choose proper truck.")
            error_label.config(foreground="red")
            error_label.grid(row=8, column=1, pady=10, sticky="w")
        else:
            label_distance = ttk.Label(self.app.root, text=f"Distance: {self.app.distance} km")
            label_distance.grid(row=8, column=1, pady=10, sticky="w")

            label_fuel_price = ttk.Label(self.app.root, text=f"Fuel Price: {self.app.fuelPrice} $")
            label_fuel_price.grid(row=9, column=1, pady=10, sticky="w")

            label_driver_time = ttk.Label(self.app.root, text=f"Driver Time: {self.app.driverTime} hours")
            label_driver_time.grid(row=10, column=1, pady=10, sticky="w")

            label_driver_salary = ttk.Label(self.app.root, text=f"Driver total salary: {self.app.driverSalary} $")
            label_driver_salary.grid(row=11, column=1, pady=10, sticky="w")

            calculate_button = ttk.Button(self.app.root, text="Restart calculator")
            calculate_button.grid(row=12, column=1, pady=10, sticky="w")
