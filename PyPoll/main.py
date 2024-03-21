import os
import csv


pypoll_csv_path = os.path.join("Resources", "election_data.csv")

#csv_math will define variables and iterate through the csv to update the variabels and lists and finally return the values at the end
def pypoll_summary():
    with open(pypoll_csv_path, encoding = "UTF-8") as pypoll_csv:
        csvreader = csv.reader(pypoll_csv, delimiter = ",")
        csvheader = next(csvreader)
    #Below are the variables I am initializing
        total_votes = 0
        candidate_unique = []
        candidate_votes = []
        vote_count = []
        vote_percent = []
    #Below is the best option I have found for skipping the header row as we gather data
        next(csvreader)
        # Find Unique candidates and tally their votes (stored in candidate_votes as a GIANT list. Is there a better temporary way to do this?)
        for row in csvreader:
            total_votes += 1
            candidate = row[2]
            if candidate in candidate_unique:
                #candidate_votes will hold all unique data points by counting the candidate's name. We can then count using the names on the ballot
                candidate_votes.append(candidate)
            else:
                candidate_unique.append(candidate)
                candidate_votes.append(candidate)
        for person in candidate_unique:
            #total votes as a number, derived from the list of names in cadidate_votes
            vote_count.append(candidate_votes.count(person))
            #vote percentage calculated from the now numerical tallied votes
            vote_percent.append((candidate_votes.count(person) / total_votes) * 100)
        #let's find the winner 
        winner_by_count = max(vote_count)
        winner = candidate_unique[vote_count.index(winner_by_count)]
        return total_votes, candidate_unique, vote_count, vote_percent, winner
                


def result_print(total_votes, candidate_unique, vote_count, vote_percent, winner):
    result =(f"""
              

Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{candidate_unique[0]}: {vote_percent[0]: .3f}% ({vote_count[0]})

{candidate_unique[1]}: {vote_percent[1]: .3f}% ({vote_count[1]})

{candidate_unique[2]}: {vote_percent[2]: .3f}% ({vote_count[2]})

    

-------------------------
Winner: {winner}
-------------------------

""")
    #I would have liked to iterate through the candidates as below in order to print all candidate reuslts, regardless of how many there are
        #This would print this data to the terminal correctly, but when I tried to export the result_print function, python could not export the below function
    # for number in candidate_unique:
    #     print()
    #     print(f"{candidate_unique[number]}: {vote_percent[number]}% ({vote_count[number]})")
    #     print()

    #error code: 
#     (base) Dylan@Lorenas-iMac PyPoll % python main.py 
# Traceback (most recent call last):
#   File "/Users/Dylan/Desktop/DABC/python_challenge/PyPoll/main.py", line 81, in <module>
#     Pypoll_results.write(to_print)
# TypeError: write() argument must be str, not function
    

    print(result)   
    return result


#Here is where I call the functions and correct variables
total_votes, candidate_unique, vote_count, vote_percent, winner = pypoll_summary()
result_print(total_votes, candidate_unique, vote_count, vote_percent, winner)


#This is declaring the path where I would like the results printed in a txt file for easy viewing
result = result_print(total_votes, candidate_unique, vote_count, vote_percent, winner)
result_output_path = os.path.join("analysis", "Pypoll_results.txt")
with open(result_output_path, "w") as Pypoll_results:
    Pypoll_results.write(result)

