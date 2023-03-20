import os
import csv

# total number of votes
total_votes = 0

# total number of votes for each candidate
candidate_info = {}

# max value (max votes) of 'candidate_info' dictionary
max = 0

# winner (name of candidate who has max votes)
winner = ""

# if exists, deletes "analysis" directory created during the previous run
parent_path = "./analysis"

# file path to read the data from
budget_csv = os.path.join(".", "Resources", "election_data.csv")

# create "analysis" directory it does not exist
if not (os.path.exists(parent_path)):
    os.mkdir(parent_path)

# file path to write to
output_path = os.path.join(".", "analysis", "output.txt")

# Open the input csv file to read data.
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # skip the header
    next(csv_file)

    # Read through each row of data after the header
    for row in csv_reader:
        if row[2] in candidate_info:
            candidate_info[f"{row[2]}"] = candidate_info[f"{row[2]}"] + 1
        else:
            candidate_info[f"{row[2]}"] = 1
        
        total_votes = total_votes + 1



# Open a new logfile using "write" mode.
with open(output_path, 'w') as file_w:
    file_w.write("Election Results" + "\n\n")
    file_w.write("-------------------------" + "\n")
    #file_w.write(""+ "\n")
    file_w.write(f"Total Votes: {total_votes} \n")
    file_w.write("-------------------------" + "\n")
    file_w.write(""+ "\n")
    print()
    print("Election Results\n")    
    print("---------------------------\n")
    print(f"Total Votes: {total_votes}\n")
    print("---------------------------\n")

    for candidate in candidate_info.keys():

        # Calculate percentage of votes for each candidate.
        # For each key (name) get the value (votes' count) from the dictionary, divide by total number of votes and then mult. by 100
        percent = round(((candidate_info[candidate])*100/total_votes),3)

        # 'info' variable stores all info for each candidate as a string.
        # For each key (name) get the value (votes' count) from the dictionary, concatenate everything with 'percent'.
        info = f"{candidate}:   {percent}%   ({(candidate_info[candidate])})"

        print(info + "\n")
        file_w.write(info + "\n")

        # Find the winner (name of candidate who has max votes)
        # Find max value of 'candidate_info' dictionary
        if (candidate_info[candidate]) > max:
            max = candidate_info[candidate]
            winner = candidate

  
    file_w.write("\n-------------------------" + "\n")
    file_w.write(f"Winner: {winner} \n")
    file_w.write("-------------------------" + "\n")

    print("---------------------------\n")
    print(f"Winner:   {winner}\n")
    print("---------------------------\n")

