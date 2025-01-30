from customtkinter import *
from start_window import StartWindow
from base_frame import BaseFrame
from client_window import ClientWindow
from vehicle_window import VehicleWindow
from gobackbutton import GoBackButton

class Root(CTk):

    def __init__(self):
        super().__init__()
        self.geometry('900x500')
        self.title("Car Rental")
        self.geometry('900x500')
        self.resizable(True, True)
        self.maxsize(width=1100, height=700)
        self.minsize(width=700, height=300)
        self.start_window = StartWindow(self)



        
    
app = Root()
app.mainloop()

