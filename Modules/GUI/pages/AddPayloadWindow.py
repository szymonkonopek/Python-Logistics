from tkinter import Toplevel, Label, Entry, Button
import uuid
from Modules.GUI.pages.PayloadManager import PayloadManager


class AddPayloadWindow:
    def __init__(self, parent, confirm_callback):
        self.parent = parent
        self.confirm_callback = confirm_callback

        self.add_payload_window = Toplevel(parent)
        self.add_payload_window.title("Add Payload")
        
        window_width = 400
        window_height = 200
        screen_width = parent.winfo_screenwidth()
        screen_height = parent.winfo_screenheight()
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2

        self.add_payload_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        Label(self.add_payload_window, text="Name:").pack()
        self.name_entry = Entry(self.add_payload_window)
        self.name_entry.pack()

        Label(self.add_payload_window, text="Type:").pack()
        self.type_entry = Entry(self.add_payload_window)
        self.type_entry.pack()
        
        Label(self.add_payload_window, text="Max allowed speed:").pack()
        self.Vmax_entry = Entry(self.add_payload_window)
        self.Vmax_entry.pack()
        
        #Label(self.add_payload_window, text="level Of Danger:").pack()
        #self.dangerLevel_entry = Entry(self.add_payload_window)
        #self.dangerLevel_entry.pack()
        #maxAllowedSpeed, levelOfDanger

        confirm_button = Button(self.add_payload_window, text="Add Payload", command=self.confirm_add_payload)
        confirm_button.pack()

    def confirm_add_payload(self):
        name = self.name_entry.get()
        payload_type = self.type_entry.get()
        Vmax = self.Vmax_entry.get()
        #dangerLevel = self.dangerLevel_entry.get()

        if callable(self.confirm_callback):
            self.confirm_callback(name, payload_type)
            payloadId = str(uuid.uuid1())
            PayloadManager.add_payload(payloadId, name, payload_type, Vmax )

        self.add_payload_window.destroy()
