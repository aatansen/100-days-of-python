# Function to calculate parameters of Basic COCOMO
def calculate(table ,mode ,size):
    effort = 0
    time = 0
    staff = 0
    model = 0
     
    # Check the mode according to size
    if(size >= 2 and size <= 50):
        model = 0
    elif(size > 50 and size <= 300):
        model = 1
    elif(size > 300):
        model = 2
     
    print(f"The mode is {mode[model]}")
     
    # Calculate Effort
    effort = table[model][0]*pow(size, table[model][1])
     
    # Calculate Time
    time = table[model][2]*pow(effort, table[model][3])
     
    #Calculate Persons Required
    staff = (effort/time)
     
    # Output the values calculated
    print(f"Effort = {round(effort,3)} Person-Month")
    print(f"Development Time = {round(time,3)} Months")
    print(f"Average Staff Required = {round(staff)} Persons")
 
table = [[2.4,1.05,2.5,0.38],[3.0,1.12,2.5,0.35],[3.6,1.20,2.5,0.32]]
mode = ["Organic","Semi-Detached","Embedded"]
size = int(input("Enter KLOC Size:"))
calculate(table, mode, size)