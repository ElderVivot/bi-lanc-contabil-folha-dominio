from dao.get_lanc_folha import GetLancFolha

class ProcessLancFolha():
    def __init__(self, connection, companies):
        self._connection = connection
        self._companies = companies

    def processLancamentos(self):
        getLancFolha = GetLancFolha(self._connection)

        for companie in self._companies:
            codiEmp = companie['codi_emp']
            print(f'- Processando empresa {codiEmp}')
            getLancFolha.get(codiEmp)