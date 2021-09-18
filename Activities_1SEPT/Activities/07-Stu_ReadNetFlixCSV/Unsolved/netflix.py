# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")
print(os.getcwd())
# Set path for file
#csvpath = os.path.join('netflix_ratings.csv')
# Open the CSV
with open('.\netflix_ratings.csv') as file_handler:
    csvreader = csv.reader(file_handler, delimiter=",")

    # Loop through looking for the video
    for row in csvreader:
        if video in row[0]:
            print(f"{in row[0]} ")
        else:
            print("not in row")
        

