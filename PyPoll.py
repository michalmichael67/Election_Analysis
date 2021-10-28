# Import the datetime class from the datetime module
import datetime
now = dt.datetime.now()
print("The time right now is", now)

import csv
import random
import numpy
import os

#work on csv doc
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysist.txt")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    print(headers)

    for row in file_reader:
        print(row)

    # The data we need to retrieve
    # 1. The total number of votes cast
    # 2. A complete list of candidates who received votes
    # 3. The percentage of votes each candidate won
    # 4. The total number of votes each candidate won
    # 5. The winner of the elecation based on popular vote
    print(election_data)
