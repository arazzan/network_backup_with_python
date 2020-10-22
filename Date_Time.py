import datetime


def Current_Date_Time():
    date_time_now = datetime.datetime.now()
    month_now = date_time_now.strftime("%B")
    date_now = date_time_now.strftime("%d")
    year_now = date_time_now.strftime("%Y")
    time_now = date_time_now.strftime("%H%M%S")
    return f'{date_now}-{month_now}-{year_now}_{time_now}'


def Current_Date():
    date_time_now = datetime.datetime.now()
    month_now = date_time_now.strftime("%B")
    date_now = date_time_now.strftime("%d")
    year_now = date_time_now.strftime("%Y")
    return f'{date_now}-{month_now}-{year_now}'


def Current_Year():
    date_time_now = datetime.datetime.now()
    year_now = date_time_now.strftime("%Y")
    return f'{year_now}'


def Current_Month():
    date_time_now = datetime.datetime.now()
    month_now = date_time_now.strftime("%B")
    return f'{month_now}'


def Current_Date():
    date_time_now = datetime.datetime.now()
    date_now = date_time_now.strftime("%d")
    return f'{date_now}'
