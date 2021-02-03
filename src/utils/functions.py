def returnMonthsOfYear(year, filterMonthStart, filterYearStart, filterMonthEnd, filterYearEnd):
    if year == filterYearStart and year == filterYearEnd:
        months = list(range(filterMonthStart, filterMonthEnd+1)) # o mais 1 é pq o range pega só pega do inicial até o último antes do final, exemplo: range(0,3) = [0,1,2]
    elif year == filterYearStart:
        months = list(range(filterMonthStart, 13))
    elif year == filterYearEnd:
        months = list(range(1, filterMonthEnd+1))
    else:
        months = list(range(1,13))

    return months