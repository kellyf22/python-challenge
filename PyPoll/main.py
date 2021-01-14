import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #make a python list out of our csv data 
    election_data_list = [row for row in csvreader]
    #print(election_data_list)
    #print(data_list[0])
    #print(data_list[0][1])


    #HW requirement #1: find total number of votes cast (which is the length of the list, which doesn't include the header)
    num_votes = (len(election_data_list))

    #make a dictionary of candidates to store their name and running vote total, as in:
    #candidates = {'name1': number of votes,
    #              'name2': number of votes
    #               }
    candidates = {}
    
    #HW requirement #2: find vote totals (absolute and percent) for each candidate
    
    for row in election_data_list:
        name = row[2]
        
        #if candidate's name is in our dictionary, update his/her vote total
        if name in candidates: 
            candidates[name] = candidates[name]+1
            
        #otherwise, add that candidate and their first vote to the dictionary   
        else:
            candidates[name] = 1

print("Election Results")
print("-----------------------")
print(f'Total votes: {num_votes}''')
print("-----------------------")
for name, number in candidates.items():
    print(f'{name}: {round(100*number/num_votes,3)}% ({number})''')
print("-----------------------")
max_votes = max(candidates.values())
winner = [name for name, number in candidates.items() if number == max_votes]
print(f'Winner: {winner[0]}''')
print("-----------------------")

# Write the same results to a text file called "results.txt" and put it in the PyBank folder.
# The text file will be created if it doesn't already exist. If it does exist, it will be overwritten.
text_report = open("results.txt","w+")
text_report.write("Election Results\r")
text_report.write("-----------------------\r")
text_report.write("Total Votes: " + str(num_votes) +"\r")
text_report.write("-----------------------\r")
for name, number in candidates.items():
    text_report.write(f'{name}: {round(100*number/num_votes,3)}% ({number})''\r')
text_report.write("-----------------------\r")
text_report.write("Winner: "+ winner[0] +"\r")
text_report.write("-----------------------")
