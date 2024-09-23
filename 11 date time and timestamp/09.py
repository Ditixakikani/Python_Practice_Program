from datetime import datetime

from dateutil.relativedelta import relativedelta

given_date = datetime(2020, 2, 25).date()
newd_date=given_date+relativedelta(months=4)
print(newd_date)