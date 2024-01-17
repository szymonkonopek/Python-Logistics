from Modules.Transit import Transit
from Modules.Driver import Driver
from Modules.Truck import Truck
from Modules.Destination import Destination
from Modules.PriceList import PriceList
from Modules.PayloadDangerous import PayloadDangerous
from Modules.TruckList import TruckList
from Modules.DriversList import DriversList
from Modules.GUI.TruckChooserApp import TruckChooserApp

import tkinter as tk
from tkinter import ttk

if __name__ == "__main__":
    root = tk.Tk()
    app = TruckChooserApp(root)
    root.mainloop()
    
