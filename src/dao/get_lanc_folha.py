import pandas as pd
import json


class GetLancFolha():
    def __init__(self, connection):
        self._connection = connection

    def get(self, codiEmp):
        try:
            dataframe = pd.read_sql_query(f"SELECT * FROM bethadba.ctlancto WHERE codi_emp = {codiEmp} AND orig_lan = 13", self._connection)
            dataframe_to_json = json.loads(dataframe.to_json(orient='records', date_format='iso'))
            print(dataframe_to_json)
            # for data in dataframe_to_json:
            #     print(data)
        except Exception as e:
            print('- Não foi possível executar a consulta')
            print(e)