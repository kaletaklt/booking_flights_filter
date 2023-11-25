from datetime import date, timedelta


def get_dates(yyyy, mm, dd, duration):
    start_date = (date(yyyy, mm, dd))
    end_date = start_date + timedelta(days=duration)
    return start_date, end_date
