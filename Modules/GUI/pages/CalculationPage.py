from tkinter import ttk


class CalculationPage:
    def __init__(self, app):
        self.app = app
        self.driver = "Walter White"
    def show(self):
        self.app.destroy_previous_widgets()
        label_calculation = ttk.Label(self.app.root, text="Calculation:")
        label_calculation.pack(pady=10)

        label_driver = ttk.Label(self.app.root, text=f"Driver: {self.app.selectedDriver.getNameSurname()}")
        label_driver.pack(pady=10)

        label_truck = ttk.Label(self.app.root, text=f"Truck: {self.app.selectedTruck.getBrandModel()}")
        label_truck.pack(pady=10)

        label_payload = ttk.Label(self.app.root, text=f"Payload: {self.app.selectedPayload.getName()}")
        label_payload.pack(pady=10)

        label_from = ttk.Label(self.app.root, text=f"From: {self.app.fromDestination}")
        label_from.pack(pady=10)

        label_to = ttk.Label(self.app.root, text=f"To: {self.app.toDestination}")
        label_to.pack(pady=10)
    
        prevPage = ttk.Button(self.app.root, text="Previous", command=self.app.selectDestination.show)
        prevPage.pack(pady=10)
    
        calculate_button = ttk.Button(self.app.root, text="Calculate", command=self.app.calculate)
        calculate_button.pack(pady=10)

    def showCalculations(self):
        label_distance = ttk.Label(self.app.root, text=f"Distance: {self.app.distance}")
        label_distance.pack(pady=10)

        label_fuelPrice = ttk.Label(self.app.root, text=f"Fuel Price: {self.app.fuelPrice}")
        label_fuelPrice.pack(pady=10)

        label_driverTime = ttk.Label(self.app.root, text=f"Driver Time: {self.app.driverTime}")
        label_driverTime.pack(pady=10)

        label_driverSalary = ttk.Label(self.app.root, text=f"Driver Salary: {self.app.driverSalary}")
        label_driverSalary.pack(pady=10)
    

  