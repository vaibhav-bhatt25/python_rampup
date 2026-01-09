from datetime import datetime

def dates_difference(from_date,to_date,difference):
    format_date="%y-%m-%d"
    date1 = datetime.strptime(from_date, format_date)
    date2 = datetime.strptime(to_date, format_date)
    result=date2-date1

    return result.days<difference



start_date="25-07-25"
end_date="25-08-03"
difference=10

print(dates_difference(start_date,end_date,difference))
