import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # make a python list out of our csv data 
    data_list = [row for row in csvreader]
    
    # HW requirement #1: find total number of months in the data set (which is the length of the list)
    num_months = (len(data_list))

    # HW requirements #2-5
    # The strategy to go through the budget data with a for loop, collecting info to answer the remaining requirements.
    # #2, total profits and losses is found by keeping a running total, called "net"
    # #3-5 depend on month by month changes. To get there, build 3 separate lists: 
    # one to hold the months ("months"), one for the monthly profit/loss (called "money"), and one to store the monthly change (called "changes").

    #Begin by initializing our variables to empty lists or 0
    net = 0
    months = []
    money = []
    changes = []
    
    # The lists "months" and "money" simply rewrite from the appropriate locations from the original data_list. 
    # "changes" is generated by calculating the monthly change (subtracting the previous month's total from the current month).
    for _ in range(num_months):
        net += int(data_list[_][1])
        months.append(data_list[_][0])
        money.append(int(data_list[_][1]))
        m_change = money[_] - money[(_-1)]
        changes.append(m_change)

    # Since there's no change to look at for the first month, and we don't want an extra zero when we find the average, remove the first item in "changes".
    changes.pop(0)

    # Use some math functions to find variables of interest
    avg_change = round(sum(changes)/len(changes),2)    
    greatest_increase = max(changes)
    greatest_decrease = min(changes)

    # In order to return the month where the greatest increase and decrease took place, we'll need to zip our lists of months and changes back together.
    # First, remove the first item from months to make it the same size as changes.
    months.pop(0)
    changes_data = zip(months,changes)

    # Now find the previously calculated greatest increase and decrease within the new list and return the list item containing [<month>,<monthly change>].
    for row in changes_data:
        if row[1] == greatest_increase:
            high = row

        if row[1] == greatest_decrease:
            low = row

# Print the results in the terminal.
print("Financial Analysis")
print("------------------")
print(f'Total Months: {num_months}''')
print(f'Total: ${net}''')
print(f'Average Change: ${avg_change}''')
print(f'Greatest Increase in Profits: {high[0]} ${high[1]}''')
print(f'Greatest Decrease in Profits: {low[0]} ${low[1]}''')

# Write the same results to a text file called "results.txt" and put it in the PyBank folder.
# The text file will be created if it doesn't already exist. If it does exist, it will be overwritten.
text_report = open("results.txt","w+")
text_report.write("Financial Analysis\r")
text_report.write("------------------\r")
text_report.write("Total Months: " + str(num_months) +"\r")
text_report.write("Total: $" + str(net) + "\r")
text_report.write("Average Change: $" + str(avg_change) + "\r")
text_report.write("Greatest Increase in Profits: " + str(high[0]) + " $" + str(high[1]) + "\r")
text_report.write("Greatest Decrease in Profits: " + str(low[0]) + " $" + str(low[1]) + "\r")