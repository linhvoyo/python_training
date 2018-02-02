"""
Assignment #2
Part 2
Write a new program called "count_hsps.py". This program will read in "blasp.txt".
Then print the number of alignments and total number of HSPs found in file
"""

def count_hsps(file_d):
    """
    Each alignment begins with ">"
    Each hsp begins with "Score = "
    """
    alignments = 0
    hsps = 0
    for i in file_d:
        if i[0] == '>':
            alignments += 1
        if "Score = " in i:
            hsps += 1
    return alignments, hsps

BLAST_FILE = open("blastp.txt", "r")

print count_hsps(BLAST_FILE)
