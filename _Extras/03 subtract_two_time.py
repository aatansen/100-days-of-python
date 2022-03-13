from datetime import datetime
past_date = '28/02/22 13:27:19'
past_date = datetime.strptime(past_date, '%d/%m/%y %H:%M:%S')
current_date = '13/03/22 18:06:19'
current_date = datetime.strptime(current_date, '%d/%m/%y %H:%M:%S')

print (current_date-past_date)
# Feb 28, 2022, 1:27 PM