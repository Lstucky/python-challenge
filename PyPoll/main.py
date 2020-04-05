import csv
import os

file = "Resources/election_data.csv"

output = ""
line_count = 0
candidates = {}
voter_count = 0

with open (file, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    for row in reader:
        if row[2] not in candidates:
            candidates[row[2]] = 0
        candidates[row[2]] +=1    
        voter_count +=1

output += "Election Results\n"
output += "-"*36 + "\n"
output += "Total Votes: " + str(voter_count) + "\n"
output += "-"*36 + "\n"

winner_votes = 0
winner_name = ""

for k in candidates:
    output += f'{k}: {round(candidates[k] / voter_count * 100,2)}% {candidates[k]}\n' 
    if candidates[k] > winner_votes:
        winner_votes = candidates[k]
        winner_name = k

output += "-"*36 + "\n"
output += f'Winner: {winner_name}'

print(output)

with open("Election-results.txt", 'w') as textfile:
    textfile.write(output)

