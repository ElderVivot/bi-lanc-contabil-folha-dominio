import pyodbc
import pandas as pd
import json

class ConnectOdbc():
    def __init__(self):
        self._connection = None

    def connect(self):
        try:
            # Using a DSN, but providing a password as well
            self._connection = pyodbc.connect(DSN='ContabilExterno', UID='CONSULTA', PWD='dominio')

            return self._connection
        except Exception as e:            
            print('- Não foi possível conectar no banco de dados')
            print(e)


# if __name__ == '__main__':
#     connectOdbc = ConnectOdbc()
#     connection = connectOdbc.connect()
