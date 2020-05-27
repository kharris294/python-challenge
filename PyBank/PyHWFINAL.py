# Dependencies

import os
import csv

# import OS module, create file paths across operating systems
csvpath = os.path.join ('PyHW.csv')
pathout = os.path.join ("/Users/kathrynharris/Desktop/PythonStuff", "PyHWBank.txt")

 # Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Begin to loop through the rows
    next(csvreader)
    row = next(csvreader)
    
    # Identify our variables
    total_months = 1
    
    net_profits = int(row[1])
    
    profit = int(row[1])

    sum_change = 0
    
    greatest_increase = ["", 0]
    greatest_decrease = ["", 99999999]

    # Loop through looking for the values
    for row in csvreader:
        print(row)
        # Loop through total months
        total_months += 1
        print(total_months)
        # Loop through net_profits
        net_profits += int(row[1])
        # Find sum_change 
        sum_change += int(row[1]) - profit
        # Check profits
        profit = int(row[1])
        print(profit)       
        
    # Greatest increase value
        if (sum_change > greatest_increase [1]):
            greatest_increase[1] = sum_change
            greatest_increase[0] = row[0]
            print("Greatest Increase:" + str(greatest_increase))
        
        if (sum_change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = sum_change
            print("Greatest Decrease:" + str(greatest_decrease))
print()       
print(net_profits)

# Find average change by dividing sum_change by total_months, round value
average_change = (sum_change/(total_months-1))
print(round(average_change, 2))

# output 
output = (
    f"Total Months: {total_months}\n"
    f"Total Profit: {net_profits}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} ${greatest_increase[1]}\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} ${greatest_decrease[1]}\n"
    )

print(output)

#write to text path
with open(pathout, "w") as txt_file:
        PyHwBank.write(output)



        
        
   


