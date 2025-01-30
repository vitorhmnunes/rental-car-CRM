from customtkinter import *

class BaseFrame(CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(corner_radius=0, fg_color='#272727')
        self.place(relx=0, rely=0, relwidth= 1, relheight=1)
        self.frames()
    
    def frames(self):
        self.left_corner_frame = CTkFrame(self, corner_radius=0, fg_color='#1C1C1C', border_color='#000000', border_width=1)
        self.left_corner_frame.place(relx=0, rely=0, relwidth= 0.33, relheight=1 )

        self.upper_corner_frame = CTkFrame(self, corner_radius=0, fg_color='#1C1C1C', border_color='#000000', border_width=1 )
        self.upper_corner_frame.place(relx=0, rely=0, relwidth= 1, relheight=0.06 )

    def leftCrudLabel(self):
        self.left_label = CTkLabel(self.left_corner_frame, text_color='#2F4F4F', font=('impact', 50), justify='left' )
        self.left_label.place(relx=0.12, rely=0.2, relwidth=0.6, relheight=0.15)

    def leftCrudButtons(self):
        self.create_bt = CTkButton(self.left_corner_frame, corner_radius=500, text='ADICIONAR', font=('',14), fg_color='#272727', text_color='#808080', border_width=1, border_color='#000000')
        self.create_bt.place(relx=0.15, rely=0.37, relwidth=0.7, relheight=0.13)

        self.read_bt = CTkButton(self.left_corner_frame, corner_radius=500, text='LISTAR', font=('',14), fg_color='#272727', text_color='#808080', border_width=1, border_color='#000000')
        self.read_bt.place(relx=0.15, rely=0.51, relwidth=0.7, relheight=0.13)

        self.update_bt = CTkButton(self.left_corner_frame, corner_radius=500, text='ALTERAR', font=('',14), fg_color='#272727', text_color='#808080', border_width=1, border_color='#000000')
        self.update_bt.place(relx=0.15, rely=0.65, relwidth=0.7, relheight=0.13)

        self.delete_bt = CTkButton(self.left_corner_frame, corner_radius=500, text='EXCLUIR', font=('',14), fg_color='#272727', text_color='#808080', border_width=1, border_color='#000000')
        self.delete_bt.place(relx=0.15, rely=0.79, relwidth=0.7, relheight=0.13)

    def rightBaseFrame(self):
        self.right_frame = CTkFrame(self, corner_radius=0, fg_color='#272727')
        self.right_frame.place(relx=0.33, rely=0.06, relwidth= 0.66, relheight=0.94)


class BasicCrudWindow():
    def __init__(self, master):
        self.__master = master
  

    def labels(self):
        self.txt1 = CTkLabel(self.__master, text_color='#808080', font=('', 18), justify='left')
        self.txt1.place(relx=0.01, rely=0.01, relwidth=0.25, relheight=0.07)

        self.txt2 = CTkLabel(self.__master, text_color='#808080', font=('', 14), justify='left')
        self.txt2.place(relx=0.01, rely=0.1, relwidth=0.2, relheight=0.07)

    def textEntries(self):
        self.primary_key_entry = CTkEntry(self.__master, fg_color='#1C1C1C', placeholder_text_color='#FFFFFF', font=('', 14))
        self.primary_key_entry.place(relx=0.08, rely=0.17, relwidth=0.7, relheight=0.09)

    def sendButton(self):
        self.send_bt = CTkButton(self.__master, corner_radius=100, text='IR', font=('',14), fg_color='#1C1C1C', text_color='#FFFFFF', border_width=1.4, border_color='#696969')
        self.send_bt.place(relx=0.8, rely=0.18, relwidth=0.15, relheight=0.08)

    def textBox(self):
        self.tb = CTkTextbox(self.__master, corner_radius=5, fg_color='#1C1C1C', text_color='#FFFFFF', scrollbar_button_color='#FFFFFF', scrollbar_button_hover_color='#FFFFFF', font=('', 12), state='disabled', border_width=2 )
        self.tb.place(relx=0.08, rely=0.35, relwidth=0.8, relheight=0.4)

    def confirmButton(self):
        self.confirm_bt = CTkButton(self.__master, corner_radius=100, font=('',14), fg_color='#1C1C1C', text_color='#FFFFFF', border_width=1.4, border_color='#696969')
        self.confirm_bt.place(relx=0.4, rely=0.8, relwidth=0.2, relheight=0.09)
    



