import csv
#import os
#Assign a variable for the file to load the path.
file_to_load = 'election_results.csv'
#Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
     # Read and print the header row.
    headers = next(file_reader)
    print(headers)