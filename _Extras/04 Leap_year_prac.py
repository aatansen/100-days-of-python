# Write a program that prints the next 20 leap years starting from the leap year closest to what the user enters
year = int(input("Enter a year:"))
for yr in range (year,year+80):
    if yr%400==0:
        print("Leap Year.")
    elif yr%100==0:
        print("Not Leap Year.")
    elif yr%4==0:
        print("Leap Year.")
    else:
        print("Not leap year.")


