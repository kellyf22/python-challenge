import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #make a python list out of our csv data 
    data_list = [row for row in csvreader]
    #print(data_list)
    #print(data_list[0])
    #print(data_list[0][1])


    #HW requirement #1: find total number of months in the data set (which is the length of the list, which doesn't include the header)
    num_months = (len(data_list))
    #print(num_months)

    months = []
    money = []
    changes = []
    #HW requirement #2: find net total of profits and losses over the entire period
    net = 0
    for _ in range(num_months):
        net = net + int(data_list[_][1])
        months.append(data_list[_][0])
        money.append(int(data_list[_][1]))
        m_change = money[_] - money[(_-1)]
        changes.append(m_change)

    #print(net)
    #print(money)

    #remove the first item, since there's no change to look at for the first month, and we don't want the extra zero in there making our list too long when we find the average.
    changes.pop(0)
    #print(changes)

    avg_change = round(sum(changes)/len(changes),2)
    #print(avg_change)
    
    greatest_increase = max(changes)
    greatest_decrease = min(changes)

    #need to make a new list of lists to zip months and changes together
    months.pop(0)
    #print(months)
    changes_data = zip(months,changes)

    # Read through each row of data after the header
    for row in changes_data:
        #print(row)
        if row[1] == greatest_increase:
            #print(row)
            high = row

        if row[1] == greatest_decrease:
            #print(row)
            low = row

print("Financial Analysis")
print("------------------")
print(f'Total Months: {num_months}''')
print(f'Total: ${net}''')
print(f'Average Change: ${avg_change}''')
print(f'Greatest Increase in Profits: {high[0]} ${high[1]}''')
print(f'Greatest Decrease in Profits: {low[0]} ${low[1]}''')