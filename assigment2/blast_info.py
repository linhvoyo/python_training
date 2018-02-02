"""
Assignment #2
Part 3
Use biopython parser to write a program that opens blastp.txt to answer the following questions:
- What was the query length?
- What was the score for P48435?
- How many HSPs are there with more than 50% identity?
"""

from Bio.Blast import NCBIStandalone

def query_length(parsed_file):
    """
    Return query length from input file
    """
    return parsed_file.query_length

def p48435(parsed_file):
    """
    Return the score for P48435
    """
    score = []
    for i in parsed_file.alignments:
        if "P48435" in i.title:
            for num in i.hsps:
                score.append(num.score)
    return score

def hsps_over_50(parsed_file):
    """
    Return the number of hsps with over 50% identity
    """
    identities = []
    for i in parsed_file.alignments:
        for k in i.hsps:
            identities.append(k.identities)
    return len([x for x in identities if 100 * x[0]/x[1] > 50])
    # return len(filter(lambda x: 100 *  x[0]/x[1] > 50, identities))

RESULT = NCBIStandalone.BlastParser().parse_file("blastp.txt")
print "Query length: %d" %(query_length(RESULT))
print "Scores for P48435: %d, %d" %(p48435(RESULT)[0], p48435(RESULT)[1])
print "Number of HSPs with more than 50 percent identity: %d" %(hsps_over_50(RESULT))
