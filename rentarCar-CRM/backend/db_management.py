import pyodbc

class DbManagement:
    def __init__(self):
        self.__connection_data = (
        "Driver={SQL Server};"
        "Server=LAPTOP-VTQHJ55M\SQLEXPRESS;"
        "Database=CarRental;"
        )
        self.connection()
    
    def connection(self):
      self.connect = pyodbc.connect(self.__connection_data)
     



   