from datetime import datetime,timedelta

def days_before(date,difference):
    format_date="%y-%m-%d"
    obj = datetime.strptime(date, format_date)
    result_date=obj-timedelta(days=diff)
    output=result_date.strftime("%y-%m-%d")

    return output


date="25-07-25"
diff=7
print(days_before(date,diff))