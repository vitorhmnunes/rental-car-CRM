from customtkinter import *
from base_frame import BaseFrame
from gobackbutton import GoBackButton
from uppermenubuttons import UpperMenuButtons
from base_frame import BasicCrudWindow
from alert_window import AlertToplevelWindow

class RentWindow(BaseFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.leftCrudLabel()
        self.leftCrudButtons()
        self.go_back_button = GoBackButton(master=self.left_corner_frame, root=self.master, frame=self)
        self.upper_menu_buttons = UpperMenuButtons(master=self.upper_corner_frame, root=self.master, frame=self)
        self.createRent()

    def leftCrudLabel(self):
        super().leftCrudLabel()
        self.left_label.configure(text='Aluguel')

    def createRent(self):
        self.rightBaseFrame()
        self.creat_client_window = CreateRentWindow(self.right_frame)

    def createWindowCall(self):
        self.right_frame.place_forget()
        self.rightBaseFrame()
        self.create_window = CreateRentWindow(self.right_frame)   

    def readWindowCall(self):
        self.right_frame.place_forget()
        self.rightBaseFrame()
        self.read_window = ReadRentWindow(master=self.right_frame)

    def updateWindowCall(self):
        self.right_frame.place_forget()
        self.rightBaseFrame()
        self.update_window = UpdateRentWindow(self.right_frame, root=self.master)

    def deleteWindowCall(self):
        self.right_frame.place_forget()
        self.rightBaseFrame()
        self.delete_window = DeleteRentWindow(self.right_frame, root=self.master)

    def leftCrudButtons(self):
        super().leftCrudButtons()
        self.create_bt.configure(command=self.createWindowCall)
        self.read_bt.configure(command=self.readWindowCall)
        self.update_bt.configure(command=self.updateWindowCall)
        self.delete_bt.configure(command=self.deleteWindowCall)


class CreateRentWindow():
    def __init__(self, master):
        self.__master = master
        self.labels()
        self.textEntries()
        self.submitButton()
  
    def labels(self):
        self.txt1 = CTkLabel(self.__master, text='Adicionar Aluguel', text_color='#808080', font=('', 18), justify='left')
        self.txt1.place(relx=0.01, rely=0.01, relwidth=0.25, relheight=0.07)
        
        self.txt2 = CTkLabel(self.__master, text='CPF', text_color='#808080', font=('', 14), justify='left')
        self.txt2.place(relx=0.19, rely=0.14, relwidth=0.2, relheight=0.07)

        self.txt3 = CTkLabel(self.__master, text='Código Veículo', text_color='#808080', font=('', 14), justify='left')
        self.txt3.place(relx=0.08, rely=0.37, relwidth=0.2, relheight=0.07)
        
        self.txt4 = CTkLabel(self.__master, text='Data Inical', text_color='#808080', font=('', 14), justify='left')
        self.txt4.place(relx=0.47, rely=0.37, relwidth=0.2, relheight=0.07)
        
        self.txt5 = CTkLabel(self.__master, text='Data Final', text_color='#808080', font=('', 14), justify='left')
        self.txt5.place(relx=0.21, rely=0.59, relwidth=0.2, relheight=0.07)

    def textEntries(self): 
        self.cpf_entry = CTkEntry(self.__master, fg_color='#1C1C1C', placeholder_text='000.000.000-00', placeholder_text_color='#FFFFFF', font=('', 14))
        self.cpf_entry.place(relx=0.24, rely=0.2, relwidth=0.5, relheight=0.09)

        self.vehicle_code_entry = CTkEntry(self.__master, fg_color='#1C1C1C', font=('', 14))
        self.vehicle_code_entry.place(relx=0.08, rely=0.43, relwidth=0.40, relheight=0.09)
      
        self.inicial_date_entry = CTkEntry(self.__master, fg_color='#1C1C1C', placeholder_text='00/00/0000', placeholder_text_color='#FFFFFF', font=('', 14))
        self.inicial_date_entry.place(relx=0.50, rely=0.43, relwidth=0.40, relheight=0.09)

        self.final_date_entry = CTkEntry(self.__master, fg_color='#1C1C1C', placeholder_text='00/00/0000', placeholder_text_color='#FFFFFF', font=('', 14))
        self.final_date_entry.place(relx=0.24, rely=0.65, relwidth=0.5, relheight=0.09)


    def textBox(self):
        pass #caso precise emitir alguma mensagem, posicionar no canto inferior direito, da mesma cor da  __master e sem borda

    def submitButton(self):
        self.rent_submit_button = CTkButton(self.__master,corner_radius=100, text='ADICIONAR', font=('',14), fg_color='#1C1C1C', text_color='#FFFFFF', border_width=1.4, border_color='#696969')
        self.rent_submit_button.place(relx=0.39, rely=0.85, relwidth=0.2, relheight=0.09)

        
class ReadRentWindow():
    def __init__(self, master):
        self.__master = master
        self.basic_crud = BasicCrudWindow(master=self.__master)
        self.readRentWidgets()

    def readRentWidgets(self):
        self.basic_crud.labels()
        self.basic_crud.txt1.configure(text='Listar Aluguel')
        self.basic_crud.txt2.configure(text='Código do aluguel  ou  Código do veículo')
        self.basic_crud.txt2.place(relx=0.01, rely=0.09, relwidth=0.56, relheight=0.09)

        self.basic_crud.textEntries()

        self.basic_crud.sendButton()

        self.basic_crud.textBox()


class UpdateRentWindow():
    def __init__(self, master, root):
        self.__master = master
        self.__root = root
        self.basic_crud = BasicCrudWindow(master=self.__master)
        self.updateRentWidgets()

    def updateRentWidgets(self):
        self.basic_crud.labels()
        self.basic_crud.txt1.configure(text='Alterar Aluguel')
        self.basic_crud.txt2.configure(text='Código do aluguel')
        self.basic_crud.txt2.place(relx=0.01, rely=0.09, relwidth=0.32, relheight=0.09)

        self.basic_crud.textEntries()

        self.basic_crud.sendButton()

        self.basic_crud.textBox()

        self.basic_crud.confirmButton()
        self.basic_crud.confirm_bt.configure(text='ALTERAR')
        self.basic_crud.confirm_bt.configure(command=self.infosWindowCall)

    def infosWindowCall(self):
        self.update_infos = UpdateInfosToplevelWindow(self.__root)


class UpdateInfosToplevelWindow(CTkToplevel):
    def __init__(self, *args, fg_color = '#272727', **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self.title('Alterar Veículo')
        self.geometry('600x500')
        self.resizable(False,False)
        self.labels()
        self.textEntries()
        self.submitButton()
        self.labels()
        self.textEntries()
        self.submitButton()
  
    def labels(self):
        self.txt1 = CTkLabel(self, text='Alterar Aluguel', text_color='#808080', font=('', 18), justify='left')
        self.txt1.place(relx=0.01, rely=0.01, relwidth=0.25, relheight=0.07)
        
        self.txt3 = CTkLabel(self, text='CPF', text_color='#808080', font=('', 14), justify='left')
        self.txt3.place(relx=0.18, rely=0.14, relwidth=0.2, relheight=0.07)

        self.txt4 = CTkLabel(self, text='Código Veículo', text_color='#808080', font=('', 14), justify='left')
        self.txt4.place(relx=0.08, rely=0.37, relwidth=0.2, relheight=0.07)
        
        self.txt5 = CTkLabel(self, text='Data Inical', text_color='#808080', font=('', 14), justify='left')
        self.txt5.place(relx=0.47, rely=0.37, relwidth=0.2, relheight=0.07)
        
        self.txt6 = CTkLabel(self, text='Data Final', text_color='#808080', font=('', 14), justify='left')
        self.txt6.place(relx=0.21, rely=0.59, relwidth=0.2, relheight=0.07)

    def textEntries(self): 
        self.cpf_entry = CTkEntry(self, fg_color='#1C1C1C', font=('', 14))
        self.cpf_entry.place(relx=0.24, rely=0.2, relwidth=0.5, relheight=0.09)

        self.vehicle_code_entry = CTkEntry(self, fg_color='#1C1C1C', font=('', 14))
        self.vehicle_code_entry.place(relx=0.08, rely=0.43, relwidth=0.40, relheight=0.09)
      
        self.inicial_date_entry = CTkEntry(self, fg_color='#1C1C1C', placeholder_text='00/00/0000', placeholder_text_color='#FFFFFF', font=('', 14))
        self.inicial_date_entry.place(relx=0.50, rely=0.43, relwidth=0.40, relheight=0.09)

        self.final_date_entry = CTkEntry(self, fg_color='#1C1C1C', placeholder_text='00/00/0000', placeholder_text_color='#FFFFFF', font=('', 14))
        self.final_date_entry.place(relx=0.24, rely=0.65, relwidth=0.5, relheight=0.09)


    def textBox(self):
        pass #caso precise emitir alguma mensagem, posicionar no canto inferior direito, da mesma cor da  __master e sem borda

    def submitButton(self):
        self.rent_submit_button = CTkButton(self,corner_radius=100, text='ALTERAR', font=('',14), fg_color='#1C1C1C', text_color='#FFFFFF', border_width=1.4, border_color='#696969')
        self.rent_submit_button.place(relx=0.28, rely=0.85, relwidth=0.2, relheight=0.09)

        self.cancel_button = CTkButton(self,corner_radius=100, text='CANCELAR', font=('',14), fg_color='#1C1C1C', text_color='#FFFFFF', border_width=1.4, border_color='#696969', command=self.cancelBtCallback)
        self.cancel_button.place(relx=0.5, rely=0.85, relwidth=0.2, relheight=0.09)

    def cancelBtCallback(self):
        self.withdraw()


class DeleteRentWindow():
    def __init__(self, master, root):
        self.__master = master
        self.__root = root
        self.basic_crud = BasicCrudWindow(master=self.__master)
        self.deleteRentWidgets()

    def deleteRentWidgets(self):
        self.basic_crud.labels()
        self.basic_crud.txt1.configure(text='Excluir Aluguel')
        self.basic_crud.txt2.configure(text='Código do aluguel')
        self.basic_crud.txt2.place(relx=0.01, rely=0.09, relwidth=0.32, relheight=0.09)

        self.basic_crud.textEntries()

        self.basic_crud.sendButton()

        self.basic_crud.textBox()

        self.basic_crud.confirmButton()
        self.basic_crud.confirm_bt.configure(text='EXCLUIR', command=self.alertToplevelCall)

    def alertToplevelCall(self):
        self.alert_window = AlertToplevelWindow(self.__root)      