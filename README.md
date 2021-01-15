# python-challenge
GT Bootcamp Python Project #1

This two-part project exercises importing csv files, use of lists and dictionaries in python to analyze data from csv files, and introduces generating an output report as a text file.

In the PyBank portion, the task is to create a Python script to analyze simple financial records. Given a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv), composed of two columns: `Date` and `Profit/Losses`, the script calculates the following:

  * The total number of months included in the dataset
  * The net total amount of "Profit/Losses" over the entire period
  * Calculate the changes in "Profit/Losses" over the entire period, and the average of those changes
  * The greatest increase in profits (date and amount) over the entire period
  * The greatest decrease in losses (date and amount) over the entire period
  
The script accomplishes this by reading and writing lists with a for loop, and doing some arithmetic on the generated lists. Finally, a summary report is printed to the terminal and exported as a text file.

In the PyPoll portion, given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv), composed of three columns: `Voter ID`, `County`, and `Candidate`, the task is to create a Python script that analyzes the votes and calculates each of the following:

  * The total number of votes cast
  * A complete list of candidates who received votes
  * The percentage of votes each candidate won
  * The total number of votes each candidate won
  * The winner of the election based on popular vote

In this case, the dataset is much larger (over three million items, as opposed to less than 100 for the PyBank dataset). Additionally, the information required for the summary requires sorting the vote totals by candidate. My script for this task uses dictionaries and for loops to categorize the candidates, keep track of their vote totals, and return the winner of the election. A final summary of the dataset is printed in the terminal and exported as a text file.
