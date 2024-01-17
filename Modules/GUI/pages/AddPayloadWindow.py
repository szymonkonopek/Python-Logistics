from tkinter import Toplevel, Label, Entry, Button, StringVar, ttk, messagebox
import uuid
from Modules.PayloadRegular import PayloadRegular
from Modules.PayloadList import PayloadList
from Modules.PayloadAnimal import PayloadAnimal
from Modules.PayloadDangerous import PayloadDangerous

# Pop up to add new payload
class AddPayloadWindow:
    def __init__(self,app, confirm_callback, type):
        self.app = app

        parent = app.root
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

        Label(self.add_payload_window, text="Name:").pack()
        self.name_entry = Entry(self.add_payload_window)
        self.name_entry.pack()
        
        Label(self.add_payload_window, text="Max allowed speed:").pack()
        self.Vmax_var = StringVar()
        self.Vmax_entry = Entry(self.add_payload_window, textvariable=self.Vmax_var, validate="key", validatecommand=(self.add_payload_window.register(self.validate_speed), "%P"))
        self.Vmax_entry.pack()

        if (type == 'PayloadRegular'):

            Label(self.add_payload_window, text="Weight:").pack()
            self.weight_var = StringVar()
            self.additionalInfo_entry = Entry(self.add_payload_window, textvariable=self.weight_var, validate="key", validatecommand=(self.add_payload_window.register(self.validate_weight), "%P"))
            self.additionalInfo_entry.pack()

        elif (type == 'PayloadAnimal'):

            Label(self.add_payload_window, text="Special Needs:").pack()
            Label(self.add_payload_window, text="Choose true or false, if the ").pack()
            Label(self.add_payload_window, text="payload requires more transport breaks.").pack()
            self.additionalInfo_cb = ttk.Combobox(self.add_payload_window)
            self.additionalInfo_cb['values'] = ('true', 'false')
            self.additionalInfo_cb['state'] = 'readonly'
            self.additionalInfo_cb.pack()
            self.additionalInfo_entry = self.additionalInfo_cb

        elif (type == 'PayloadDangerous'):
            
            Label(self.add_payload_window, text="Level Of Danger:").pack()
            Label(self.add_payload_window, text="Choose one class ").pack()
            Label(self.add_payload_window, text="among 9 available.").pack()
            self.additionalInfo_cb = ttk.Combobox(self.add_payload_window)
            self.additionalInfo_cb['values'] = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
            self.additionalInfo_cb['state'] = 'readonly'
            self.additionalInfo_cb.pack()
            self.additionalInfo_entry = self.additionalInfo_cb

        
        #Label(self.add_payload_window, text="level Of Danger:").pack()
        #self.dangerLevel_entry = Entry(self.add_payload_window)
        #self.dangerLevel_entry.pack()
        #maxAllowedSpeed, levelOfDanger

        confirm_button = Button(self.add_payload_window, text="Add Payload", command=self.confirm_add_payload)
        confirm_button.pack()

        self.payloadtype_cb.bind('<<ComboboxSelected>>', self.typeChanged)

    def typeChanged(self, event):
        print(self.payloadtype_cb.get())
        AddPayloadWindow(self.app, self.confirm_callback, self.payloadtype_cb.get())
        self.add_payload_window.destroy()

        
    def confirm_add_payload(self):
        name = self.name_entry.get()
        payload_type = self.payloadtype_cb.get()
        Vmax = self.Vmax_entry.get()
        additionalInfo = self.additionalInfo_entry.get()
        #dangerLevel = self.dangerLevel_entry.get()

        if callable(self.confirm_callback):
            print(self.payloadtype_cb.get())
            self.confirm_callback(name, payload_type)
            payloadList = PayloadList()
            if (self.payloadtype_cb.get() == 'PayloadRegular'):
                newPayload = PayloadRegular(name, int(Vmax), int(additionalInfo))
                payloadList.addPayload(newPayload)
            elif (self.payloadtype_cb.get() == 'PayloadAnimal'):
                newPayload = PayloadAnimal(name, int(Vmax), bool(additionalInfo))
                payloadList.addPayload(newPayload)
            elif (self.payloadtype_cb.get() == 'PayloadDangerous'):
                newPayload = PayloadDangerous(name, int(Vmax), int(additionalInfo))
                payloadList.addPayload(newPayload)
            
            self.add_payload_window.destroy()
            self.app.destroy_previous_widgets()
            self.app.load_payload_data()
            self.app.selectDriver.show()

    def validate_speed(self, new_value):
        try:
            # Attempt to convert the input to an integer
            if new_value:
                int(new_value)
                if int(new_value) > 150:
                    messagebox.showerror("Error", "Max allowed speed cannot exceed 120 kilometers per hour.")
                    return False
            return True
        except ValueError:
            # If conversion fails, show an error message
            messagebox.showerror("Error", "Please enter a valid integer.")
            return False
        
    def validate_weight(self, new_value):
        try:
            # Attempt to convert the input to an integer
            if new_value:
                int(new_value)
                if int(new_value) > 150:
                    messagebox.showerror("Error", "Max weight cannot exceed 22000 kilograms.")
                    return False
            return True
        except ValueError:
            # If conversion fails, show an error message
            messagebox.showerror("Error", "Please enter a valid integer.")
            return False