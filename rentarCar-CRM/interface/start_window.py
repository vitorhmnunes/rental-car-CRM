from customtkinter import *
from uppermenubuttons import UpperMenuButtons
from base_frame import BaseFrame

class StartWindow(BaseFrame):
    def __init__(self, master):
        super().__init__(master)
        self.upper_menu_buttons = UpperMenuButtons(master=self.upper_corner_frame, root=self.master, frame=self)
        self.leftFrameLabel()
        self.centralFrameLabels()
        self.centralTextEntries()
        self.centralEntriesButtons()
        self.centralTextboxes()

    def leftFrameLabel(self):
        self.text = CTkLabel(self.left_corner_frame, text='Car\nRental\nInterface', text_color='#2F4F4F', font=('impact', 50), justify='left')
        self.text.place(relx=0.1, rely=0.25, relwidth=0.8, relheight=0.5)

    def centralFrameLabels(self):
        self.text1 = CTkLabel(self, text='Acesso Rápido', text_color='#808080', font=('', 18), justify='left')
        self.text1.place(relx=0.33, rely=0.07, relwidth=0.2, relheight=0.07)

        self.text2 = CTkLabel(self, text='Cliente', text_color='#808080', font=('', 14), justify='left')
        self.text2.place(relx=0.36, rely=0.13, relwidth=0.1, relheight=0.07)

        self.text3 = CTkLabel(self, text='Alugueis', text_color='#808080', font=('', 14), justify='left')
        self.text3.place(relx=0.36, rely=0.5, relwidth=0.1, relheight=0.07)

        self.text4 = CTkLabel(self, text='ou', text_color='#808080', font=('', 14), justify='center')
        self.text4.place(relx=0.632, rely=0.57, relwidth=0.1, relheight=0.07) 

    def centralTextEntries(self):
        self.cpf_entry = CTkEntry(self, fg_color='#1C1C1C', placeholder_text='CPF (000.000.000-00)', placeholder_text_color='#FFFFFF', font=('', 14))
        self.cpf_entry.place(relx=0.40, rely=0.2, relwidth=0.37, relheight=0.06)

        self.code_entry = CTkEntry(self, fg_color='#1C1C1C', placeholder_text='Código do aluguel', placeholder_text_color='#FFFFFF', font=('', 14))
        self.code_entry.place(relx=0.40, rely=0.57, relwidth=0.2, relheight=0.06)

        self.date_entry = CTkEntry(self, fg_color='#1C1C1C', placeholder_text='Código do veículo', placeholder_text_color='#FFFFFF', font=('', 14))
        self.date_entry.place(relx=0.71, rely=0.57, relwidth=0.2, relheight=0.06)

    def centralEntriesButtons(self):
        self.cpf_search_button = CTkButton(self, corner_radius=5, text='IR', font=('',14), fg_color='#1C1C1C', text_color='#FFFFFF', border_width=1.4, border_color='#696969')
        self.cpf_search_button.place(relx=0.78, rely=0.2, relwidth=0.1, relheight=0.06)

        self.code_search_button = CTkButton(self, corner_radius=5, text='IR', font=('',14), fg_color='#1C1C1C', text_color='#FFFFFF', border_width=1.4, border_color='#696969')
        self.code_search_button.place(relx=0.61, rely=0.57, relwidth=0.05, relheight=0.06)

        self.date_search_button = CTkButton(self, corner_radius=5, text='IR', font=('',14), fg_color='#1C1C1C', text_color='#FFFFFF', border_width=1.4, border_color='#696969')
        self.date_search_button.place(relx=0.92, rely=0.57, relwidth=0.05, relheight=0.06)

    def centralTextboxes(self):
        self.client_tb = CTkTextbox(self, corner_radius=5, fg_color='#1C1C1C', text_color='#FFFFFF', scrollbar_button_color='#FFFFFF', scrollbar_button_hover_color='#FFFFFF', font=('', 12), state='disabled', border_width=2 )
        self.client_tb.place(relx=0.36, rely=0.28, relwidth=0.6, relheight=0.2)

        self.vehicle_tb = CTkTextbox(self, corner_radius=5, fg_color='#1C1C1C', text_color='#FFFFFF', scrollbar_button_color='#FFFFFF', scrollbar_button_hover_color='#FFFFFF', font=('', 12), state='disabled', border_width=2 )
        self.vehicle_tb.place(relx=0.36, rely=0.66, relwidth=0.6, relheight=0.26)
