import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")
found = False

# Open the CSV
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    #define each variables as a list according to the headers of the file
    ballout_id =[]
    county = []
    candidate = []

    #add the information of each column to the list
    for poll in csvreader:
        ballout_id.append(poll[0])
        county.append(poll[1])
        candidate.append(poll[2]) 
    
    total_ballout = len(ballout_id)
    #print(total_ballout)

    #count the candidates and only retrieve the unique values
    candidate_names = []
    for i in range(total_ballout - 1):
        if candidate[i+1] != candidate[i] and candidate[i+1] not in candidate_names:
            candidate_names.append(candidate[i+1])
    #print(candidate_names) to double check that the if does it's work

    total_votes = []
    percentage = []
    #count the votes for each candidate
    for j in range (len(candidate_names)):
        total_votes.append(candidate.count(candidate_names[j]))
        votes_percentage = total_votes[j]/len(ballout_id)
        percentage.append(votes_percentage)
    
    winner = total_votes.index(max(total_votes))   

    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_ballout:,}")
    print("----------------------------")
    for k in range (0,len(candidate_names)): 
        print(f"{candidate_names[k]}: {percentage[k]:.3%} ({total_votes[k]:,})")
    print("----------------------------")
    print(f"Winner: {candidate_names[winner]}")
    print("----------------------------")

with open("PyPoll.txt", "w") as result:
    result.write("Election Results"+ "\n")
    result.write("----------------------------"+ "\n")
    result.write(f"Total Votes: {total_ballout:,}"+ "\n")
    result.write("----------------------------"+ "\n")
    for k in range (0,len(candidate_names)): 
        result.write(f"{candidate_names[k]}: {percentage[k]:.3%} ({total_votes[k]:,})" + "\n")
    result.write("----------------------------"+ "\n")
    result.write(f"Winner: {candidate_names[winner]}"+ "\n")
    result.write("----------------------------")
    

    

    

        