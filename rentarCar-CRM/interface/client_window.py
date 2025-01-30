from customtkinter import *
from base_frame import BaseFrame
from base_frame import BasicCrudWindow
from gobackbutton import GoBackButton
from uppermenubuttons import UpperMenuButtons
from alert_window import AlertToplevelWindow

class ClientWindow(BaseFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.leftCrudLabel()
        self.leftCrudButtons()
        self.go_back_button = GoBackButton(master=self.left_corner_frame, root=self.master, frame=self)
        self.upper_menu_buttons = UpperMenuButtons(master=self.upper_corner_frame, root=self.master, frame=self)
        self.createClient()

    def leftCrudLabel(self):
        super().leftCrudLabel()
        self.left_label.configure(text='Cliente')

    def createClient(self):
        self.rightBaseFrame()
        self.creat_client_window = CreateClientWindow(self.right_frame)

    def createWindowCall(self):
        self.right_frame.place_forget()
        self.rightBaseFrame()
        self.create_window = CreateClientWindow(self.right_frame)

    def readWindowCall(self):
        self.right_frame.place_forget()
        self.rightBaseFrame()
        self.read_window = ReadClientWindow(master=self.right_frame)

    def updateWindowCall(self):
        self.right_frame.place_forget()
        self.rightBaseFrame()
        self.update_window = UpdateClientWindow(self.right_frame, root=self.master)
    
    def deleteWindowCall(self):
        self.right_frame.place_forget()
        self.rightBaseFrame()
        self.delete_window = DeleteClientWindow(self.right_frame, root=self.master)

    def leftCrudButtons(self):
        super().leftCrudButtons()
        self.create_bt.configure(command=self.createWindowCall)
        self.read_bt.configure(command=self.readWindowCall)
        self.update_bt.configure(command=self.updateWindowCall)
        self.delete_bt.configure(command=self.deleteWindowCall)


class CreateClientWindow():
    def __init__(self, master):
        self.__master = master
        self.labels()
        self.textEntries()
        self.submitButton()
  
    def labels(self):
        self.txt1 = CTkLabel(self.__master, text='Adicionar Cliente', text_color='#808080', font=('', 18), justify='left')
        self.txt1.place(relx=0.01, rely=0.01, relwidth=0.25, relheight=0.07)
      
        self.txt2 = CTkLabel(self.__master, text='CPF', text_color='#808080', font=('', 14), justify='left')
        self.txt2.place(relx=0.01, rely=0.1, relwidth=0.2, relheight=0.07)
        
        self.txt3 = CTkLabel(self.__master, text='Nome', text_color='#808080', font=('', 14), justify='left')
        self.txt3.place(relx=0.018, rely=0.27, relwidth=0.2, relheight=0.07)
       
        self.txt4 = CTkLabel(self.__master, text='Endereço', text_color='#808080', font=('', 14), justify='left')
        self.txt4.place(relx=0.019, rely=0.45, relwidth=0.24, relheight=0.07)
        
        self.txt5 = CTkLabel(self.__master, text='Telefone', text_color='#808080', font=('', 14), justify='left')
        self.txt5.place(relx=0.015, rely=0.64, relwidth=0.24, relheight=0.07)

    def textEntries(self): 
        self.cpf_entry = CTkEntry(self.__master, fg_color='#1C1C1C', placeholder_text='000.000.000-00', placeholder_text_color='#FFFFFF', font=('', 14))
        self.cpf_entry.place(relx=0.08, rely=0.17, relwidth=0.7, relheight=0.09)
      
        self.name_entry = CTkEntry(self.__master, fg_color='#1C1C1C', font=('', 14))
        self.name_entry.place(relx=0.08, rely=0.34, relwidth=0.7, relheight=0.09)
  
        self.adress_entry = CTkEntry(self.__master, fg_color='#1C1C1C', font=('', 14))
        self.adress_entry.place(relx=0.08, rely=0.53, relwidth=0.7, relheight=0.09)
      
        self.fone_entry = CTkEntry(self.__master, fg_color='#1C1C1C', placeholder_text='(00)00000-0000', placeholder_text_color='#FFFFFF', font=('', 14))
        self.fone_entry.place(relx=0.08, rely=0.71, relwidth=0.7, relheight=0.09)

    def textBox(self):
        pass #caso precise emitir alguma mensagem, posicionar no canto inferior direito, da mesma cor da  __master e sem borda

    def submitButton(self):
        self.client_submit_button = CTkButton(self.__master,corner_radius=100, text='ADICIONAR', font=('',14), fg_color='#1C1C1C', text_color='#FFFFFF', border_width=1.4, border_color='#696969')
        self.client_submit_button.place(relx=0.37, rely=0.85, relwidth=0.2, relheight=0.09)


class ReadClientWindow():
    def __init__(self, master):
        self.__master = master
        self.basic_crud = BasicCrudWindow(master=self.__master)
        self.readClientWidgets()

    def readClientWidgets(self):
        self.basic_crud.labels()
        self.basic_crud.txt1.configure(text='Listar Cliente')
        self.basic_crud.txt2.configure(text='CPF')

        self.basic_crud.textEntries()
        self.basic_crud.primary_key_entry.configure(placeholder_text='(000.000.000-00)')

        self.basic_crud.sendButton()

        self.basic_crud.textBox()
        

class UpdateClientWindow():
    def __init__(self, master, root):
        self.__master = master
        self.__root = root
        self.basic_crud = BasicCrudWindow(master=self.__master)
        self.updateClientWidgets()

    def updateClientWidgets(self):
        self.basic_crud.labels()
        self.basic_crud.txt1.configure(text='Alterar Cliente')
        self.basic_crud.txt2.configure(text='CPF')

        self.basic_crud.textEntries()
        self.basic_crud.primary_key_entry.configure(placeholder_text='(000.000.000-00)')

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
        self.title('Alterar Cliente')
        self.geometry('600x500')
        self.resizable(False,False)
        self.labels()
        self.textEntries()
        self.submitButton()
  
    def labels(self):
        self.txt1 = CTkLabel(self, text='Alterar Cliente', text_color='#808080', font=('', 18), justify='left')
        self.txt1.place(relx=0.01, rely=0.01, relwidth=0.25, relheight=0.07)
      
        self.txt2 = CTkLabel(self, text='Nome', text_color='#808080', font=('', 14), justify='left')
        self.txt2.place(relx=0.05, rely=0.14, relwidth=0.3, relheight=0.07)
        
        self.txt3 = CTkLabel(self, text='Endereço', text_color='#808080', font=('', 14), justify='left')
        self.txt3.place(relx=0.07, rely=0.33, relwidth=0.3, relheight=0.07)
       
        self.txt4 = CTkLabel(self, text='Telefone', text_color='#808080', font=('', 14), justify='left')
        self.txt4.place(relx=0.11, rely=0.54, relwidth=0.21, relheight=0.07)

    def textEntries(self): 
        self.name_entry = CTkEntry(self, fg_color='#1C1C1C', font=('', 14))
        self.name_entry.place(relx=0.15, rely=0.21, relwidth=0.7, relheight=0.09)
      
        self.adress_entry = CTkEntry(self, fg_color='#1C1C1C', font=('', 14))
        self.adress_entry.place(relx=0.15, rely=0.41, relwidth=0.7, relheight=0.09)
  
        self.phone_entry = CTkEntry(self, fg_color='#1C1C1C', placeholder_text='(00) 00000-0000', placeholder_text_color='#FFFFFF', font=('', 14))
        self.phone_entry.place(relx=0.15, rely=0.61, relwidth=0.7, relheight=0.09)
      

    def textBox(self):
        pass #caso precise emitir alguma mensagem, posicionar no canto inferior direito, da mesma cor da  __master e sem borda

    def submitButton(self):
        self.update_submit_button = CTkButton(self,corner_radius=100, text='ALTERAR', font=('',14), fg_color='#1C1C1C', text_color='#FFFFFF', border_width=1.4, border_color='#696969')
        self.update_submit_button.place(relx=0.28, rely=0.85, relwidth=0.2, relheight=0.09)

        self.cancel_button = CTkButton(self,corner_radius=100, text='CANCELAR', font=('',14), fg_color='#1C1C1C', text_color='#FFFFFF', border_width=1.4, border_color='#696969', command=self.cancelBtCallback)
        self.cancel_button.place(relx=0.5, rely=0.85, relwidth=0.2, relheight=0.09)

    def cancelBtCallback(self):
        self.withdraw()

        

class DeleteClientWindow():
    def __init__(self, master, root):
        self.__master = master
        self.__root = root
        self.basic_crud = BasicCrudWindow(master=self.__master)
        self.deleteClientWidgets()

    def deleteClientWidgets(self):
        self.basic_crud.labels()
        self.basic_crud.txt1.configure(text='Excluir Cliente')
        self.basic_crud.txt2.configure(text='CPF')

        self.basic_crud.textEntries()
        self.basic_crud.primary_key_entry.configure(placeholder_text='(000.000.000-00)')

        self.basic_crud.sendButton()

        self.basic_crud.textBox()

        self.basic_crud.confirmButton()
        self.basic_crud.confirm_bt.configure(text='EXCLUIR', command=self.alertToplevelCall)

    def alertToplevelCall(self):
        self.alert_window = AlertToplevelWindow(self.__root)

    
        
            


