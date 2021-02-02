from services.connect_odbc import ConnectOdbc
from services.get_lanc_folha import GetLancFolha

connectOdbc = ConnectOdbc()
connection = connectOdbc.connect()

getLancFolha = GetLancFolha(connection)
getLancFolha.get()
