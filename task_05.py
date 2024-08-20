import datetime
def date_in_future(integer):
    current_date = datetime.datetime.today()
    if not integer:        
        return current_date.replace(microsecond=0).strftime("%d-%m-%Y %H:%M:%S")
    future_date = datetime.datetime.today() + datetime.timedelta(days=integer)
    future_date = future_date.replace(microsecond=0)
    return future_date.strftime("%d-%m-%Y %H:%M:%S")
