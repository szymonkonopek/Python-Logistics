from tkinter import ttk
import tkinter
from Modules.PayloadAnimal import PayloadAnimal
from Modules.PayloadDangerous import PayloadDangerous

from Modules.PayloadRegular import PayloadRegular

# GUI pop up about all of the selected information chosen on the first page
class Info():
    def __init__(self,app):
        self.app = app

    def show(self):
            selected_truck = self.app.selectedTruck
            selected_driver = self.app.selectedDriver
            selected_payload = self.app.selectedPayload
            
            if selected_truck.model != "" and selected_driver.name != "" and selected_payload.name != "":
                
                info_window = tkinter.Toplevel(self.app.root)
                info_window.title("Information")

                if isinstance(selected_payload, PayloadRegular):
                    payload_info = f"\nPayload Information:\nName: {selected_payload.name}\nType: {selected_payload.type}\nMax allowed speed: {selected_payload.maxAllowedSpeed} km/h\nWeight: {selected_payload.weight} kg\n"
                elif isinstance(selected_payload, PayloadAnimal):
                    payload_info = f"\nPayload Information:\nName: {selected_payload.name}\nType: {selected_payload.type}\nMax allowed speed: {selected_payload.maxAllowedSpeed} km/h\nSpecial needs: {selected_payload.specialNeeds}\n"
                elif isinstance(selected_payload, PayloadDangerous):
                    payload_info = f"\nPayload Information:\nName: {selected_payload.name}\nType: {selected_payload.type}\nMax allowed speed: {selected_payload.maxAllowedSpeed} km/h\nClass of danger: {selected_payload.levelOfDanger}\n"

                info_label = ttk.Label(info_window, text=f"Truck Information:\n"
                                                        f"Brand: {selected_truck.brand}\n"
                                                        f"Model: {selected_truck.model}\n"
                                                        f"Capacity: {selected_truck.capacity} kg\n"
                                                        f"Fuel Economy: {selected_truck.fuelEconomy} l/100km \n"
                                                        f"Max speed: {selected_truck.maxAllowedSpeed} km/h \n"
                                                        "\n"
                                                        f"Driver Information:\n"
                                                        f"Name: {selected_driver.name}\n"
                                                        f"Surname: {selected_driver.surname}\n"
                                                        f"Hire Date: {selected_driver.hireDate}\n"
                                                        f"Hourly Base Rate: {selected_driver.hourlyBaseRate}$"
                                                        "\n"
                                                        f"{payload_info}"
                                                        )
                info_label.pack(padx=20, pady=20)
            else:
                error_label = ttk.Label(self.app.root, text="Error: Selected truck, payload or driver not found.")
                error_label.config(foreground="red")
                error_label.pack(pady=10)