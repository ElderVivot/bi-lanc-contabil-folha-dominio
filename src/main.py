from services.connect_odbc import ConnectOdbc
from services.get_lanc_folha import GetLancFolha

connectOdbc = ConnectOdbc()
cursor = connectOdbc.connect()

getLancFolha = GetLancFolha(cursor)
getLancFolha.get()
