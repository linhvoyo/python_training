"""
How many records are in the file?
How many records have a sequence of length 260?
What are the first 20 residues of 143X_MAIZE?
What is the identifier for the record with the shortest sequence? Is there more than one record with that length?
What is the identifier for the record with the longest sequence? Is there more than one record with that length?
How many contain the subsequence "ARRA"?
How many contain the substring "KCIP-1" in the description?
"""

class SwissRecord(object):
    def __init__(self, title, sequence_id, sequence, description):
        self.title = title
        self.sequence_id = sequence_id
        self.sequence = "".join(sequence)
        self.description = "".join(description)


input_file = open("swissprot.dat", "r")


def shortest_seq(short_seq, shortest, length):
    if shortest == None or length <= shortest:
        if shortest == None or length < shortest:
            short_seq = []
            shortest = length
            short_seq.append(read.title)
        else:
            short_seq.append(read.title)
    return(short_seq, shortest)

def longest_seq(long_seq, longest, length):
    if longest == None or length >= longest:
        if longest == None or length > longest:
            long_seq = []
            longest = length
            long_seq.append(read.title)
        else:
            long_seq.append(read.title)
    return(long_seq, longest)



short_seq = []
shortest = None
long_seq =[]
longest = None

seq = []
de = []
x_maize = ""
count = 0;
r_260 = 0;
seq_id = ""
count_arra = 0
count_kcip = 0
for i in input_file:
    if i[0:2] == "ID":
        title = i[:len(i)-1]
    elif i[0:2] == "//":
        read = SwissRecord(title, seq_id, seq, de)
        if len(read.sequence) == 260:
            r_260 += 1
        if "143X_MAIZE" in read.title:
            x_maize = read.sequence
        if "ARRA" in read.sequence:
            count_arra += 1
        if "KCIP-1" in read.description:
            count_kcip += 1
        short_seq, shortest = shortest_seq(short_seq, shortest,len(read.sequence))
        long_seq, longest = longest_seq(long_seq, longest, len(read.sequence))
        seq = []
        de = []
        count += 1 
        # break;
    elif i[0:2] == "DE":
        de.append(i[:len(i)-1])
    elif i[0:2] == "SQ":
        seq_id = i[:len(i)-1]
    elif i[0:2] == "  ":
        seq.append(i[5:len(i)-1].replace(" ",""))


print "There are %d records in the file" %(count)
print "There are %d records with sequence length of 260" %(r_260)
print "The first 20 residues of 143X_MAIZE are: %s" %(x_maize[:20])
print 'There are %d records contain subsequence "ARRA"' %(count_arra)
print 'There are %d records contain the substring "KCIP-1" in the description' %(count_kcip)
print "The shortest sequence ID is: %s" %(short_seq[0])
print "The longest sequence ID is: %s" %(long_seq[0])