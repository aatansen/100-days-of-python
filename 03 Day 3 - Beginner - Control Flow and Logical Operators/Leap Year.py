year = int(input("Enter a year to check leap year or not: "))
if year%400==0:
    print("Leap Year.")
elif year%100==0:
    print("Not Leap Year.")
elif year%4==0:
    print("Leap Year.")
else:
    print("Not leap year.")