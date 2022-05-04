# note from day 14:
import random
data = [1,2,4,5] # eample data ..main data is in list of key values
acc_a = random.choice(data)
acc_b = random.choice(data)
if acc_a == acc_b:
    acc_b = random.choice(data)

# # format the data 
def format_data(acc):
    acc_name = acc['name']
    acc_des = acc['description']
    acc_country = acc['country']
    return f'{acc_name}, a {acc_des}, from {acc_country}'

print(f'Compare A: {format_data(acc_a)}')
print(acc_a['follower_count'])
print('vs')
print(f'Compare B: {format_data(acc_b)}')
print(acc_b['follower_count'])