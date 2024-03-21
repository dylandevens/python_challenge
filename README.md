# python_challenge
A repository for the python challenge - UCB Module 3 Challenge


Included in this repository shoudl be the two folders for the two mini projects(pyBank and PyPoll) that each contain the reference data, my code, and the results printed directly to a .txt file within the analysis directories




# Directions:
Before You Begin
Before starting the assignment, be sure to complete the following steps:

Create a new repository for this project called python-challenge. Do not add this homework assignment to an existing repository.

Clone the new repository to your computer.

Inside your local Git repository, create a folder for each Python assignment and name them PyBank and PyPoll.

In each folder that you just created, add the following content:

A new file called main.py. This will be the main script to run for each analysis.

A Resources folder that contains the CSV files you used. Make sure that your script has the correct path to the CSV file.

An analysis folder that contains your text file that has the results from your analysis.

Push these changes to GitHub or GitLab.




## PyBank Instructions
In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following values:

The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The changes in "Profit/Losses" over the entire period, and then the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period

Your analysis should align with the following results:

Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
In addition, your final script should both print the analysis to the terminal and export a text file with the results.





## PyPoll Instructions
In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.

You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote

Your analysis should align with the following results:

Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
In addition, your final script should both print the analysis to the terminal and export a text file with the results.








### GradingRequirements
Correctly Reads in the CSV (10 points)
Reads in the CSVs for both PyBank and PyPoll using Python (5 points)

Successfully stores the header row (5 points)

Results Printed out to correctly to terminal (40 points)
Results correctly display for PyBank:

Total Months (5 points)

Total (5 points)

Average Change (5 points)

Greatest Increase (5 points)

Greatest Decrease (5 points)

Results correctly display for PyPoll:

Total Votes (5 points)

Each candidate’s total votes and percent of votes (5 points)

Winner (5 points)

Code Runs Error Free (10 points)
Error Free (5 points)

Producing consistent results (5 points)

Exports results to text file (30 points)
The text file contains for PyBank:

Total Months (2.5 points)

Total (2.5 points)

Average Change (5 points)

Greatest Increase (5 points)

Greatest Decrease (5 points)

The text file contains for Pypoll:

Total Votes (2.5 points)

Each candidate’s total votes and percent of votes (2.5 points)

Winner (5 points)

Code is cleaned and commented (10 points)
Has additional tests and debugging removed (5 points)

Commented (5 points)




I used a lot of online resources to muscle through the multitude of errors that showed up. I used class materials and videos on https://pythonprogramming.net/ as my main reference points and for understanding the key concepts. LLM ChatGPT was my tutor to describe, in a more precise and relevant way, the concepts that documentation was difficult to find. 