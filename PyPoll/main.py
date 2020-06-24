import os
import csv
import collections
from collections import Counter

# establish filepath
csvpath = os.path.join("resources", "election_data.csv")

# Store the contents of the variables into lists
votes_cast = []
vote_per_candidate = []
candidate_votes = []

# open and read csv; csv reader specifies delimiter and variable that holds contents
with open(csvpath,"r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

# Loop through all the rows of data after the header and rename header
    for row in csv_reader:
        votes_cast.append(str(row[0]))
        candidate_votes.append(str(row[2]))

# calculate the total number of votes cast
total_votes = len(votes_cast)

# sort the list ascending order
sorted_candidates = sorted(candidate_votes)

# organize list by most common candidate
sorted_list = sorted_candidates

# calculate votes per candidate based on most common list
count_candidate = Counter (sorted_list)
vote_per_candidate.append(count_candidate.most_common())

# percentage of votes per candidate and set format to percentage
# most common creates items for 1st 2nd 3rd 4th common strings in rows

for item in vote_per_candidate:
# first will correspond to string in row that is most common
    first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
    second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
    third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
    fourth = format((item[3][1])*100/(sum(count_candidate.values())),'.3f')


# print output
print("------------------------")
print("   Election Results     ")
print("------------------------")
print(f'Total Votes: {total_votes}')
print(f"{vote_per_candidate[0][0][0]}: {first}% ({vote_per_candidate[0][0][1]})")
print(f"{vote_per_candidate[0][1][0]}: {second}% ({vote_per_candidate[0][1][1]})")
print(f"{vote_per_candidate[0][2][0]}: {third}% ({vote_per_candidate[0][2][1]})")
print(f"{vote_per_candidate[0][3][0]}: {fourth}% ({vote_per_candidate[0][3][1]})")
print("-------------------------")
print(f"Winner:  {vote_per_candidate[0][0][0]}")
print("-------------------------")

# output to text file
output_file = os.path.join("resources", "election_data.txt")
with open(output_file, "w") as text_file:
    text_file.write("------------------------\n")
    text_file.write("   Election Results     \n")
    text_file.write("------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write(f"{vote_per_candidate[0][0][0]}: {first}% ({vote_per_candidate[0][0][1]})\n")
    text_file.write(f"{vote_per_candidate[0][1][0]}: {second}% ({vote_per_candidate[0][1][1]})\n")
    text_file.write(f"{vote_per_candidate[0][2][0]}: {third}% ({vote_per_candidate[0][2][1]})\n")
    text_file.write(f"{vote_per_candidate[0][3][0]}: {fourth}% ({vote_per_candidate[0][3][1]})\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Winner:  {vote_per_candidate[0][0][0]}\n")
    text_file.write("-------------------------\n")