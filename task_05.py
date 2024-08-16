import datetime
def date_in_future(integer):
    current_date = datetime.datetime.today()
    if not integer:
        return current_date.replace(microsecond=0)
    future_date = datetime.datetime.today() + datetime.timedelta(days=integer)
    future_date = future_date.replace(microsecond=0)
    return future_date
