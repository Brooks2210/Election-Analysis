# The data we need to retrieve.
# The total number of votes cast.
# A complete list of candidates who recieved votes.
# The total number of votes each candidate won.
# the Winner of the election based on popular vote.
    #import csv
    #import os
    #file_to_load = os.path.join("Resources", "election_results.csv")
    #with open(file_to_load) as election_data:
        #print(election_data)
    #file_to_load = 'Election-Analysis/Resources/election_results.csv'
    #with open(file_to_load) as election_data:
        #print(election_data)
    #file_to_save = os.path.join("analysis", "election_analysis.txt")
    #open(file_to_save, "w")
    #file_to_save = os.path.join("analysis", "election_analysis.txt")
    #with open(file_to_save, "w") as txt_file:
        #txt_file.write("Counties in the Election\n")
        #txt_file.write("-------------------------\n")
        #txt_file.write("Arapahoe\nDenver\nJefferson")
 # Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = 'Election-Analysis/Resources/election_results.csv'
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []

# Declare the empty dictinary
candidate_votes ={}

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Print the candidate list.
print(candidate_votes)
