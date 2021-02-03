from dao.connect_odbc import ConnectOdbc
from dao.get_companies import GetCompanies
from services.process_lanc_folha import ProcessLancFolha
from utils.treate_date import returnAsDate
from utils.functions import returnMonthsOfYear

dateStartStr = '01/09/2020'
dateEndStr = '31/01/2022'
dateStart = returnAsDate(dateStartStr)
dateEnd = returnAsDate(dateEndStr)

year = dateStart.year
startYear = dateStart.year
startMonth = dateStart.month
endYear = dateEnd.year
endMonth = dateEnd.month

while year <= endYear:
    months = returnMonthsOfYear(year, startMonth, startYear, endMonth, endYear)
    
    for month in months:
        print(year, month, 1)
        print(year, month, )
    
    # for month in months:
    year += 1




# connectOdbc = ConnectOdbc()
# connection = connectOdbc.connect()

# getCompanies = GetCompanies(connection)
# companies = getCompanies.get()

# processLancFolha = ProcessLancFolha(connection, companies)
# processLancFolha.processLancamentos()
