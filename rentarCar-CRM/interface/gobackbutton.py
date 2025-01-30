from customtkinter import *
from start_window import StartWindow

class GoBackButton():
    def __init__(self, master, root, frame):
        self.__master = master
        self.__root = root
        self.__frame = frame
        self.goBackButton()
        
    def goBackButton(self):
        self.go_back_button = CTkButton(master=self.__master,text='<- VOLTAR', fg_color='#272727', text_color='#808080', font=('', 12), border_width=1, border_color='#000000')
        self.go_back_button.place(relx=0.7, rely=0.07, relwidth=0.25, relheight=0.05)
        self.go_back_button.configure(command= self.startWindowCall)
        
    def startWindowCall(self):
        self.__frame.place_forget()
        self.start_window = StartWindow(self.__root)
        
    
