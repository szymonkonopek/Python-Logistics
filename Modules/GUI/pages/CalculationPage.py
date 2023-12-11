from tkinter import ttk


class CalculationPage:
    def __init__(self, app):
        self.app = app
    def show(self):
        self.app.destroy_previous_widgets()
        label_calculation = ttk.Label(self.app.root, text="Calculation:")
        label_calculation.pack(pady=10)

        label_calculate = ttk.Label(self.app.root, text="Calculate the price of the transit.")
        label_calculate.pack(pady=10)
        calculate_button = ttk.Button(self.app.root, text="Calculate", command=self.app.selectDestination.show)
        calculate_button.pack(pady=10)
        

        prevPage = ttk.Button(self.app.root, text="Previous", command=self.app.selectDestination.show)
        prevPage.pack(pady=10)