from customtkinter import *

class AlertToplevelWindow(CTkToplevel):
    def __init__(self, *args, fg_color = '#1C1C1C', **kwargs):
        super().__init__(*args, fg_color=fg_color, **kwargs)
        self.title('Alert')
        self.geometry('285x150')
        self.resizable(False, False)
        self.label()
        self.buttons()

    def label(self):
        self.text1 = CTkLabel(self, text='Essa ação é permante!\nDeseja continuar?',text_color='#808080', font=('', 22))
        self.text1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.3)

    def cancelBtCallback(self):
        self.withdraw()

    def buttons(self):
        self.yes_bt = CTkButton(self, text='SIM', text_color='#800000', font=('', 18), fg_color='#1C1C1C', border_width=1.4, border_color='#696969')
        self.yes_bt.place(relx=0.05, rely=0.6, relwidth=0.4, relheight=0.3)

        self.cancel_bt = CTkButton(self, text='CANCELAR', text_color='#006400', font=('', 18), fg_color='#1C1C1C', border_width=1.4, border_color='#696969', command=self.cancelBtCallback)
        self.cancel_bt.place(relx=0.54, rely=0.6, relwidth=0.4, relheight=0.3)
