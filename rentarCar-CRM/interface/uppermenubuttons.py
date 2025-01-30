from customtkinter import *

class UpperMenuButtons():
    def __init__(self, master, root, frame):
        self.__master = master
        self.__root = root
        self.__frame = frame
        self.clientButton()
        self.vehicleButton()
        self.rentButton()

    def clientButton(self):
        self.client_bt = CTkButton(self.__master, corner_radius=0, text='Clientes', font=('',14), fg_color='#1C1C1C', text_color='#808080')
        self.client_bt.place(relx=0.002, rely=0.1, relwidth=0.1, relheight=0.7)
        self.client_bt.configure(command=self.clientWindowCall)

    def clientWindowCall(self):
        from client_window import ClientWindow
        self.__frame.place_forget()
        self.client_window = ClientWindow(self.__root)

    def vehicleButton(self):
        self.vehicle_bt = CTkButton(self.__master, corner_radius=0, text='Veículos', font=('',14), fg_color='#1C1C1C', text_color='#808080')
        self.vehicle_bt.place(relx=0.1, rely=0.1, relwidth=0.1, relheight=0.7)
        self.vehicle_bt.configure(command=self.vehicleWindowCall)

    def vehicleWindowCall(self):
        from vehicle_window import VehicleWindow
        self.__frame.place_forget()
        self.vehicle_window = VehicleWindow(self.__root)

    def rentButton(self):
        self.rent_bt = CTkButton(self.__master, corner_radius=0, text='Alugueis', font=('',14), fg_color='#1C1C1C', text_color='#808080')
        self.rent_bt.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.7)
        self.rent_bt.configure(command=self.rentWindowCall)

    def rentWindowCall(self):
        from rent_window import RentWindow
        self.__frame.place_forget()
        self.rent_window = RentWindow(self.__root)