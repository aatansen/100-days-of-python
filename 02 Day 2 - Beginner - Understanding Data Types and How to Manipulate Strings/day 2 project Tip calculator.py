print("Welcome to the tip calculator")
total_bill= float(input("What was the total bill? $"))
tip= int(input("What percentage tip would you like to give? 10,12, or 15?"))
people = int(input("How many people to split the bill?"))
Tip_percentage_cal = (tip/100)*total_bill
total_have_to_pay=Tip_percentage_cal+total_bill
pay_bill = round((total_have_to_pay/people),2)
print(f"${pay_bill}")
