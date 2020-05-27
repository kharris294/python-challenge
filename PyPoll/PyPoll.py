import os
import csv

# import OS module, create file paths across operating systems
# csvpath = os.path.join(/Users/kathrynharris/Desktop/election_data.csv)
csvpath = "/Users/kathrynharris/Desktop/election_data.csv"

# Declare variables
votes = 0
winner_votes = 0
total_candidates = 0
greatest_votes = ["", 0]
candidate_options = []
candidate_votes = {}


# Read the data
with open(csvpath) as election_data:
    reader = csv.DictReader(election_data)

# Create loop to do work within to find the finish products
    for row in reader:
        print(row)
        votes = votes + 1
  #      total_candidates = row["Candidate"]
#
  #      if row["Candidate not in candidate_options"]:
  #          candidate_options.append(row["Candidate"])
  #          candidate_votes[row["Candidate"]] = 1
#
 #       else: 
#
 #           candidate_votes[row["Candidate"]] = candidates_votes[row["Candidate"]] + 1

    #print information
    print()
    print()
    print()
    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(votes))
    print("-------------------------")
# results
    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
    
candidate_votes

winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)

# results
print("-------------------------")
print("Winner: " + str(winner[0]))
print("-------------------------")
   
   
        


