from db_management import DbManagement
import pandas as pd
import re 

class Client ():
    def __init__(self, cpf, name, adress, phone_number ):
        self.cpf = cpf
        self.name = name
        self.adress = adress
        self.phone_number = phone_number
        self.db = DbManagement()

    def searchCpf(self, cpf):
        command = """SELECT Cpf FROM Client;"""
        dados = pd.read_sql(command, self.db.connection)

        if cpf in dados:
            return 1
        else:
            return 0

    def searchRentByCpf(self, cpf):
        command = "SELECT Cpf FROM Rent"
        dados = pd.read_sql(command, self.db.connection)

        if cpf in dados:
            return 1
        else:
            return 0

    def verifyCpfFormat(self, cpf):
        cpf_copy = cpf
        cpf_copy = re.sub('[.-]', '', cpf_copy )

        if cpf.lenght < 14:
            return 0
        elif (cpf[3] != '.') or (cpf[7] != '.') or (cpf[11] != '-'):
            return 0
        elif not cpf_copy.isnumeric():
            return 0
        else:
            return 1
     
    def verifyPhoneNumberFormat(self, phone_number):
        phone_copy = phone_number
        phone_copy = re.sub('[()-]', '', phone_copy) 

        if phone_number.lenght < 14:
            return 0
        elif (phone_number[0] != '(') or (phone_number[3] != ')') or (phone_number[9] != '-'):
            return 0
        elif not phone_copy.isnumeric():
            return 0
        else:
            return 1
        
    def isNull(self, cliente):
        if not (cliente.cpf or cliente.name or cliente.phone_number):
            return True
        else:
            return False
    
    def create(self, cliente, textbox):
        if self.isNull(cliente):
            textbox.configure(text='CPF, Nome ou Telefone vazios. Campos obrigatórios.')

        elif self.verifyCpfFormat(cliente.cpf) == 0:
            textbox.configure(text='CPF fora do formato exigido')
        
        elif self.verifyPhoneNumberFormat(cliente.phone_number) == 0:
            textbox.configure(text='Número fora do formato exigido')

        elif self.searchCpf(cliente.cpf) == 1:
            textbox.configure(text='O CPF informado já está cadastrado')

        else:
            cursor = self.db.connect.cursor()
            sql_command = f"""INSERT INTO Client (Cpf, Name, Adress, PhoneNumber)
            VALUES('{cliente.cpf}','{cliente.name}','{cliente.adress}','{cliente.phone_number}');
            """
            cursor.execute(sql_command)
            cursor.commit()
            textbox.configure(text='Cliente adicionado com sucesso!!')
        
    
    def read(self, cpf, textbox):
        if not cpf:
            textbox.configure(text='Erro! Informe o CPF que deseja buscar.')

        elif self.verifyCpfFormat == 0:
            textbox.configure(text='CPF fora do formato exigido')
        
        elif self.searchCpf(cpf) == 0:
            textbox.configure(text='CPF não encontrado')
        
        else:
            sql_command = f"SELECT Name, Adress, PhoneNumber FROM Client WHERE Cpf = {cpf};"
            data = pd.read_sql(sql_command, self.db.connection)
            #formatar a data para aparecer na textbox
            client_info = f"CPF: {cpf} || Nome: {data['Name']} || Telefone: {data['PhoneNumber']} || Endereço: {data['Adress']}"

            if self.searchRentByCpf(cpf) == 0:
                sql_command2 = f"SELECT Code, VehicleCode, InicialDate, FinalDate FROM Rent WHERE Cpf = {cpf};"
                dados = pd.read_sql(sql_command2, self.db.connection)

                #Itera o DataBase Dados e armazena as informações dos rents em rent_info. Para caso tenha mais de um aluguel no mesmo CPF
                for i in dados:
                    rent_info = rent_info + f"{i['Code']}, {i['VehicleCode']}, {i['InicialDate']}, {i['FinalDate']}\n"

                rent_data = 'Alugueis:\n' + rent_info
                textbox.configure(text=rent_data)
           

    def update(self, cpf, new_data, textbox, confirm_button):

        if not cpf:
            textbox.configure(text='Erro! Informe o CPF que deseja buscar.')

        elif self.verifyCpfFormat == 0:
            textbox.configure(text='CPF fora do formato exigido')
        
        elif self.searchCpf(cpf) == 0:
            textbox.configure(text='CPF não encontrado')
        
        else:
            confirm_button.configure(state="normal")
            confirm_button.configure(command=self.updating_record(self.db)) #enviando a conexão server sql para a função de alteração
        

        def updating_record(self, db):
            cursor = db.connect.cursor()
            sql_command = f"UPDATE Client SET Name = {new_data[0]}, SET Adress = {new_data[1]}, SET PhoneNumber = {new_data[2]} WHERE Cpf = {cpf};"
            cursor.execute(sql_command)
            cursor.commit()
            textbox.configure(text="Cliente alterado com sucesso!!")
            confirm_button.configure(state="disabled")



    def delete(self):
        pass
    

'''     cursor = connect.cursor()
        command = """"""
        cursor.execute(command)
        cursor.commit() #usado para editar o banco de dados. Caso for somente leitura não precisa do commit
'''