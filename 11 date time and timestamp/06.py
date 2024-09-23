from datetime import datetime,timedelta
given_date = datetime(2020, 3, 22, 10, 0, 0)
print("given date",given_date)
days_to_add=7
res_date=given_date+timedelta(days=days_to_add,hours=12)
print ("new date",res_date)