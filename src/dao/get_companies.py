import pandas as pd
import json


class GetCompanies():
    def __init__(self, connection):
        self._connection = connection

    def get(self):
        try:
            dataframe = pd.read_sql_query("SELECT * FROM bethadba.geempre ORDER BY codi_emp", self._connection)
            dataframe_to_json = json.loads(dataframe.to_json(orient='records', date_format='iso'))
            # print(dataframe_to_json)
            return dataframe_to_json
        except Exception as e:
            print('- Não foi possível executar a consulta')
            print(e)