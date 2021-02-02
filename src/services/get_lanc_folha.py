class GetLancFolha():
    def __init__(self, cursor):
        self._cursor = cursor

    def get(self):
        self._cursor.execute("SELECT * FROM bethadba.ctlancto WHERE codi_emp = 5 AND orig_lan = 13")
        rows = self._cursor.fetchall()
        for row in rows:
            print(row)