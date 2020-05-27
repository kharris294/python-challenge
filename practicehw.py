# import file

import csv
with open(/Users/kathrynharris/Desktop/PythonData.csv', newline= ') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter= ',')
    
    print(csvreader)
    
    # Each row is read as row
    for row in csvreader:
        print(row)
        
    
        


