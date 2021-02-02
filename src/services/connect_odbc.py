import pyodbc

class ConnectOdbc():
    def __init__(self):
        self._cnxn = None
        self._cursor = None

    def connect(self):
        # Using a DSN, but providing a password as well
        self._cnxn = pyodbc.connect(DSN='ContabilExterno', UID='CONSULTA', PWD='dominio')

        # Create a cursor from the connection
        self._cursor = self._cnxn.cursor()

        return self._cursor