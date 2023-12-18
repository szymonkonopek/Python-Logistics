from tkinter import ttk


class CalculationPage:
    def __init__(self, app):
        self.app = app
        self.driver = "Walter White"
    def show(self):
        self.app.destroy_previous_widgets()
        label_calculation = ttk.Label(self.app.root, text="Calculation:")
        label_calculation.pack(pady=10)

        label_driver = ttk.Label(self.app.root, text=f"Driver: {self.app.selectedDriver}")
        label_driver.pack(pady=10)

        label_truck = ttk.Label(self.app.root, text=f"Truck: {self.app.selectedTruck}")
        label_truck.pack(pady=10)

        label_payload = ttk.Label(self.app.root, text=f"Payload: {self.app.selectedPayload}")
        label_payload.pack(pady=10)

        label_from = ttk.Label(self.app.root, text=f"From: {self.app.fromDestination}")
        label_from.pack(pady=10)

        label_to = ttk.Label(self.app.root, text=f"To: {self.app.toDestination}")
        label_to.pack(pady=10)
    

        calculate_button = ttk.Button(self.app.root, text="Calculate", command=self.app.selectDestination.show)
        calculate_button.pack(pady=10)
        

        prevPage = ttk.Button(self.app.root, text="Previous", command=self.app.selectDestination.show)
        prevPage.pack(pady=10)