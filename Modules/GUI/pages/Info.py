from tkinter import ttk
import tkinter


class Info():
    def __init__(self,app):
        self.app = app
    def show(self):
            selected_truck_model = self.app.selected_truck.get()
            selected_driver_name = self.app.selected_driver.get()
            selected_payload = self.app.selected_payload.get()

            selected_truck = next((truck for truck in self.app.truck_data if truck['model'] == selected_truck_model), None)
            selected_driver = next((driver for driver in self.app.driver_data if f"{driver['name']} {driver['surname']}" == selected_driver_name), None)
            selected_payload = next((payload for payload in self.app.payload_data if f"{payload['name']}" == selected_payload), None)
            
            if selected_truck and selected_driver:
                info_window = tkinter.Toplevel(self.app.root)
                info_window.title("Information")

                info_label = ttk.Label(info_window, text=f"Truck Information:\n"
                                                        f"Brand: {selected_truck['brand']}\n"
                                                        f"Model: {selected_truck['model']}\n"
                                                        f"Capacity: {selected_truck['capacity']}\n"
                                                        f"Fuel Economy: {selected_truck['fuelEconomy']}\n"
                                                        #f"Other Things: {selected_truck['otherThings']}\n\n"
                                                        f"Driver Information:\n"
                                                        f"Name: {selected_driver['name']}\n"
                                                        f"Surname: {selected_driver['surname']}\n"
                                                        f"Hire Date: {selected_driver['hireDate']}\n"
                                                        f"Hourly Base Rate: {selected_driver['hourlyBaseRate']}")
                info_label.pack(padx=20, pady=20)
            else:
                error_label = ttk.Label(self.app.root, text="Error: Selected truck or driver not found.")
                error_label.pack(pady=10, fg="red")