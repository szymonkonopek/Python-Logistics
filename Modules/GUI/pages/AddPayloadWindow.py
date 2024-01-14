from tkinter import Toplevel, Label, Entry, Button, StringVar, ttk
import uuid
from Modules.GUI.pages.PayloadManager import PayloadManager
from Modules.PayloadRegular import PayloadRegular
from Modules.PayloadList import PayloadList
from Modules.PayloadAnimal import PayloadAnimal
from Modules.PayloadDangerous import PayloadDangerous

class AddPayloadWindow:
    def __init__(self, parent, confirm_callback, type):
        self.renderPayloadWindow(parent, confirm_callback, type)

    def renderPayloadWindow(self,parent, confirm_callback, type):
        self.parent = parent
        self.confirm_callback = confirm_callback

        self.add_payload_window = Toplevel(parent)
        self.add_payload_window.title("Add Payload")
        
        window_width = 400
        window_height = 300
        screen_width = parent.winfo_screenwidth()
        screen_height = parent.winfo_screenheight()
        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2

        self.add_payload_window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        Label(self.add_payload_window, text="Name:").pack()
        self.name_entry = Entry(self.add_payload_window)
        self.name_entry.pack()

        Label(self.add_payload_window, text="Type:").pack()
        # create a combobox
        self.selected_type = "aaa"
        self.payloadtype_cb = ttk.Combobox(self.add_payload_window, textvariable=self.selected_type)
        # get first 3 letters of every month name
        self.payloadtype_cb['values'] = ('PayloadRegular', 'PayloadAnimal', 'PayloadDangerous')
        # prevent typing a value
        self.payloadtype_cb['state'] = 'readonly'
        # place the widget
        self.payloadtype_cb.pack()
        
        Label(self.add_payload_window, text="Max allowed speed:").pack()
        self.Vmax_entry = Entry(self.add_payload_window)
        self.Vmax_entry.pack()

        if (type == 'PayloadRegular'):
            Label(self.add_payload_window, text="Weight:").pack()
        elif (type == 'PayloadAnimal'):
            Label(self.add_payload_window, text="Special Needs:").pack()
        elif (type == 'PayloadDangerous'):
            Label(self.add_payload_window, text="Level Of Danger:").pack()
        self.additionalInfo_entry = Entry(self.add_payload_window)
        self.additionalInfo_entry.pack()

        
        #Label(self.add_payload_window, text="level Of Danger:").pack()
        #self.dangerLevel_entry = Entry(self.add_payload_window)
        #self.dangerLevel_entry.pack()
        #maxAllowedSpeed, levelOfDanger

        confirm_button = Button(self.add_payload_window, text="Add Payload", command=self.confirm_add_payload)
        confirm_button.pack()

        self.payloadtype_cb.bind('<<ComboboxSelected>>', self.typeChanged)
    def typeChanged(self, event):
        print(self.payloadtype_cb.get())
        AddPayloadWindow(self.parent, self.confirm_callback, self.payloadtype_cb.get())
        self.add_payload_window.destroy()

        

    def confirm_add_payload(self):
        name = self.name_entry.get()
        payload_type = self.payloadtype_cb.get()
        Vmax = self.Vmax_entry.get()
        additionalInfo = int(self.additionalInfo_entry.get())
        #dangerLevel = self.dangerLevel_entry.get()

        if callable(self.confirm_callback):
            print(self.payloadtype_cb.get())
            self.confirm_callback(name, payload_type)
            payloadList = PayloadList()
            if (self.payloadtype_cb.get() == 'PayloadRegular'):
                newPayload = PayloadRegular(name, int(Vmax), additionalInfo)
                payloadList.addPayload(newPayload)
            elif (self.payloadtype_cb.get() == 'PayloadAnimal'):
                newPayload = PayloadAnimal(name, int(Vmax), additionalInfo)
                payloadList.addPayload(newPayload)
            elif (self.payloadtype_cb.get() == 'PayloadDangerous'):
                newPayload = PayloadDangerous(name, int(Vmax), additionalInfo)
                payloadList.addPayload(newPayload)
            
            self.add_payload_window.destroy()
