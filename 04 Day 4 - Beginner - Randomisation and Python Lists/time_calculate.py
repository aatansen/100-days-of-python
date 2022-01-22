import datetime
current_date_and_time = datetime.datetime.now()
print(current_date_and_time)
# OUTPUT
# 2020-03-27 19:01:31.340242


hours_added = datetime.timedelta(hours = 9,minutes=40)

future_date_and_time = current_date_and_time + hours_added

print(future_date_and_time)
# OUTPUT
# 2020-03-28 00:01:31.340242