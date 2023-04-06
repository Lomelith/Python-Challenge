# Shout out to my bro CG-JP for the recommendation on the previous challenge.
# I took it to heart and hopefully this lives up to your expectations.

###############################################################################
#                                                                             #
#                           Written By Ryan Krause                            #
#                          Directed By Ryan Krause                            #
#               Music Writen By No One... I'm too poor for that               #
#               Special thanks to... Mom                                      #
#                                    Dad                                      #
#                                    Brothers                                 #
#                                    Sister                                   #
#                                    Friends                                  #
#                                    Rodalfo the teacher guy                  #
#                                    Kyle the TA                              #
#                                    The rest of the class                    #
#                                    Central Grader JP                        #
#                                    Duke Nukem                               #
#                                    Goku                                     #
#                                                                             #
#    Movies used to do this you know. Credits before they start and stuff.    #
#                                                                             #
###############################################################################

# Import the OS module
import os

# Import this other module
import csv

# Get the current directory the file is in
currentDir = os.path.dirname(os.path.abspath(__file__))

# This is a comment I wrote to desribe how this fuction works within the os 
# module. You will see it again further down in the code.
# Change the current working directory to that files directory.

# Change the current working directory to that files directory.
# See the comment above for further description.
os.chdir(currentDir)

# Get the path to the thing
resourcePath = os.path.join("Resources", "election_data.csv")

# Get the path to the other thing
analysisPath = os.path.join("Analysis", "analysis.txt")

# This is a dictionary. Yeah i know, they are pretty cool
candidatesVotes = {}

# Here is a variable I defined.
# Hopefully it's pretty clear by it's name what it represents.
winningVotes = 0

# Open the provided resource file
with open(resourcePath, "r") as election_data:
    
    # This allows me to read the collumns by name
    election_data = csv.DictReader(election_data)

    # Loop through the rows in the resource file
    for row in election_data:
        
        # Here is a blank space.
        # I use them sometimes so people dont get confused
        
        
        # If a new candidate is found
        if row["Candidate"] not in candidatesVotes:
            
            # Add the candidate to the dictionary and give them one vote
            candidatesVotes[row["Candidate"]] = 1
        
        # If the candidate was already in the dictionary then you do this other thing.
        else:
            
            # I increment their vote by 1. Thats the other thing I do.
            candidatesVotes[row["Candidate"]] += 1

# Here is another variable. It takes the sum of all cadidate votes values
# and puts it into the variable votes.
# It's almost like as i describe it I'm programing it. (explosion) MIND BLOWN!!!
votes = sum(candidatesVotes.values())

# This is a with statement. It opens a program or something
with open(analysisPath, "w") as analysis:
    
    # Print that DATA!
    print(f"\nElection Results\n{'-'*30}\nTotal Votes: {votes}\n{'-'*30}")
    
    # DO IT AGAIN FOR SOME REASON!
    print(f"Election Results\n{'-'*30}\nTotal Votes: {votes}\n{'-'*30}", file = analysis)
    
    # for candidate and candidates votes in the candidatesVotes dictionary
    # ...man comments are so cool
    for candidate, candidatesVotes in candidatesVotes.items():
        
        # If a candidates votes are greater than the current
        # candidates winning votes then...
        if candidatesVotes > winningVotes:
            
            # Make the winner the current candidate.
            winner = candidate
            
            # winning votes equals the current candidates votes
            winningVotes = candidatesVotes

        # Calculate the percentage of total votes this candidate has
        percentVotes = candidatesVotes / votes * 100
        
        # PRINT SOME MORE STUFF!
        print(f"{candidate}: {'{:.2f}%'.format(percentVotes)} ({candidatesVotes})")

        # DOUBLE TROUBLE!!
        print(f"{candidate}: {'{:.2f}%'.format(percentVotes)} ({candidatesVotes})", file = analysis)

    # OMG IT"S MORE INFORMATION
    print(f"{'-'*30}\nWinner: {winner}\n{'-'*30}\n")

    # THERE IS IS AGAIN!
    print(f"{'-'*30}\nWinner: {winner}\n{'-'*30}", file = analysis)
    
    # Look another comment :)