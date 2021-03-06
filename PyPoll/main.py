import os 
import csv



#Variable for the data set 
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0  

# Set path for the file 
csvpath = os.path.join('.','PyPoll','Resources','eletion_data.csv')

# Open and Read csv file 
with open(csvpath, newline='') as csvfile:
    # Set delimiter and variables 
    csvreader = csv.reader(csvfile, delimiter=',') 
    
    # Read the header of the row 
    csv_header = next(csvfile)

    # Set a Loop 
    for row in csvreader: 

        # to calculate total number of votes per candidate 
        total_votes += 1 

        # Calculate total number of votes each candidate won

        if (row[2] == "Khan"):
            khan_votes += 1 
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row [2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1
        
    # Calculate the percentage of votes for each candidate 
    khan_percent = khan_votes/ total_votes
    correy_percent = correy_votes / total_votes
    li_percent = li_votes / total_votes
    otooley_percent = otooley_votes / total_votes

    # Calculate winner of the election based on the maximum nuber of votes the candidate gets

    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "Otooley" 
    
# Print Analysis
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
print(f"Khan: {khan_percent}({khan_votes})")
print(f"Correy: {correy_percent}({correy_votes})")
print(f"Li: {li_percent}({li_votes})")
print(f"O'Tooley: {otooley_percent}({otooley_votes})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")

# Write File
output_file = os.path.join('.', 'PyPoll', 'Resources', 'election_data_revised.text')

# Open file with 'w'
with open(output_file, 'w',) as txtfile:

# Write New Data
    txtfile.write(f"Election Results")
    txtfile.write(f"---------------------------")
    txtfile.write(f"Total Votes: {total_votes}")
    txtfile.write(f"---------------------------")
    txtfile.write(f"Khan: {khan_percent}({khan_votes}")
    txtfile.write(f"Correy: {correy_percent}({correy_votes})")
    txtfile.write(f"Li: {li_percent}({li_votes})")
    txtfile.write(f"O'Tooley: {otooley_percent}({otooley_votes})")
    txtfile.write(f"---------------------------")
    txtfile.write(f"Winner: {winner_name}")
    txtfile.write(f"---------------------------")