# The data we need to retrive
# 1. Total number of votes cast
# 2. Complete list of candidates who received vote
# 3. The percentage votes each candidate received
# 4. The total number of votes each candidate won
# 5. The winners of election based on popular votes
# Start loading election result csv file
# Assign a varibale for the file to lad and path
import csv
from distutils import text_file
from fileinput import close


file_to_load='Resources/election_results.csv'
election_data = open(file_to_load, 'r')
election_data.close()
# Open the election results and read the file
with open(file_to_load) as election_data:
    # To do: perform analysis
     print(election_data)
     election_data.close
     # Indirect metho of opening a file
     import csv
     import os
     # Assign a variable for the file to load and the path
     file_to_load = os.path.join("Resources", "election_results.csv")
     # Open the election results and read the file.
     with open(file_to_load) as election_data:
 # Print the file object
       print(election_data)
 # Write to files with Python
file_to_save='Analysis/election_Analysis.txt'
election_data = open(file_to_save, 'w')
# Use the open statement to open the file as a text file
outfile = open(file_to_save, "w")
# Write some data to the file
outfile.write("Hello World")
# Close the file
outfile.close()
# write data to file without open and close function i.e using with function

with open(file_to_save, "w") as txt_file:
# Write three counties to the file.if we put just thye name of counties within quotes, the output will be horizontal, 
# if you want vertical put back slach and wtite n before name of counties after first county
 
 
 txt_file.write("Arapahoe\nDenver\nJefferson")
 import csv
 file_to_load='Resources/election_results.csv'
 file_to_save='Analysis/election_Analysis.txt'
 # Open the election results and read the file.
 with open(file_to_load) as election_data:
 # Read the file object with the reader function.
  file_reader = csv.reader(election_data)
  # Print each row in the CSV file.
 
    # Read and print the header row.
headers = next(file_reader)
print(headers)
