from tkinter import ttk, StringVar, END
from Modules.Destination import Destination

# GUI select Destination page
class SelectDestination:
    def __init__(self, app):
        self.app = app

    # Traces every entered key to save the FromDestination value
    def onFromEntrySubmit(self, var, index, mode):
        self.app.fromDestination.setName(self.sv1.get()) 

    # Traces every entered key to save the ToDestination value
    def onToEntrySubmit(self, var, index, mode):
        self.app.toDestination.setName(self.sv2.get())

    # Labels and input forms for Destinations
    def show(self):
            self.app.destroy_previous_widgets()
            label_destination = ttk.Label(self.app.root, text="Select a Destination:")
            label_destination.pack(pady=10)


    # From destination
            dest_label1 = ttk.Label(self.app.root, text="From: ")
            dest_label1.pack(pady=10)
            self.sv1 = StringVar()
            entry_from = ttk.Entry(self.app.root, textvariable=self.sv1)
            entry_from.delete(0, END)
            entry_from.insert(0, self.app.fromDestination.getName())
            self.sv1.trace_add("write", self.onFromEntrySubmit)
            entry_from.pack(pady=10)

    # To destination
            dest_label2 = ttk.Label(self.app.root, text="To: ")
            dest_label2.pack(pady=10)
            self.sv2 = StringVar()
            entry_to = ttk.Entry(self.app.root, textvariable=self.sv2)
            entry_to.delete(0, END)
            entry_to.insert(0, self.app.toDestination.getName())
            self.sv2.trace_add("write", self.onToEntrySubmit)
            entry_to.pack(pady=10)

    # Button to return to the previous page
            prevPage = ttk.Button(self.app.root, text="Previous page", command=self.app.selectDriver.show)
            prevPage.pack(pady=10)
    
    # Button to go to the next page
            nextPage = ttk.Button(self.app.root, text="Summary", command=self.app.calculationPage.show)
            nextPage.pack(pady=10)