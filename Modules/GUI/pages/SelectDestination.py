from tkinter import ttk

class SelectDestination:
    def __init__(self, app):
        self.app = app
    def show(self):
            self.app.destroy_previous_widgets()
            label_destination = ttk.Label(self.app.root, text="Select a Destination:")
            label_destination.pack(pady=10)

            dest_label1 = ttk.Label(self.app.root, text="From: ")
            dest_label1.pack(pady=10)
            entry_from = ttk.Entry(self.app.root)
            entry_from.pack(pady=10)

            dest_label2 = ttk.Label(self.app.root, text="To: ")
            dest_label2.pack(pady=10)
            entry_from = ttk.Entry(self.app.root)
            entry_from.pack(pady=10)

            prevPage = ttk.Button(self.app.root, text="Previous", command=self.app.selectDriver.show)
            prevPage.pack(pady=10)

            nextPage = ttk.Button(self.app.root, text="Next", command=self.app.calculationPage.show)
            nextPage.pack(pady=10)