"""
How many records are in the file?
How many records have a sequence of length 249?
What is the title for the record with the shortest sequence? Is there more than one record with that length?
What is the title for the record with the longest sequence? Is there more than one record with that length?
How long is the sequence for the GenBank identifier gi|114812?
Which records have 3D structures submitted to the PDB? (Give me the 4 character PDB identifier.)
Some records contain identical sequences. How many unique sequences are present?
Give the titles for two different records which have identical sequences (any two will do)
"""

class FastaRecord(object):
    '''
    object to model each read
    '''
    def __init__(self, title, sequence):
        self.title = title
        self.sequence = sequence

    def cal_seq_len(self):
        """
        cal length of all item in list.
        subtract index due to newline at the end of each item
        """
        total = 0
        for index, i in enumerate(self.sequence):
            total = total + len(i)
        return total - (index + 1)

def shortest_seq(short_seq, shortest, length):
    if shortest == None or length <= shortest:
        if shortest == None or length < shortest:
            short_seq = []
            shortest = length
            short_seq.append(read.title[0][:len(read.title[0]) - 1])
        else:
            short_seq.append(read.title)
    return(short_seq, shortest)

def longest_seq(long_seq, longest, length):
    if longest == None or length >= longest:
        if longest == None or length > longest:
            long_seq = []
            longest = length
            long_seq.append(read.title[0][:len(read.title[0]) - 1])
        else:
            long_seq.append(read.title)
    return(long_seq, longest)


seq = []
title = []
i = 0
len_249 = 0
shortest = None
short_seq = []
longest = None
long_seq = []
gi_114812 = None
s_dict = {}
input_file = open("br_sequences.fasta", "r")

for line in input_file:
    if line[0] == '>':
        title.append(line)
    elif line[0] == '\n':
        read = FastaRecord(title, seq)
        if read.title[0][0] != '>':
            print "invalid FASTA format"
            break
        if read.cal_seq_len() == 249:
            len_249 += 1
        short_seq, shortest = shortest_seq(short_seq, shortest, read.cal_seq_len())
        long_seq, longest = longest_seq(long_seq, longest, read.cal_seq_len())
        if "gi|114812" in read.title[0]:
            gi_114812 = read.cal_seq_len()
        seq = []
        title = []
        s_dict[read.title[0]] = "".join(read.sequence)
        i += 1
    else:
        seq.append(line)

def filtered_pdb(list_keys):
    pdb = filter(lambda x: "pdb" in x, s_dict.keys())
    pdb_id = map(lambda x: x.split("|")[3:4][0], pdb)
    return pdb_id


print "There are %d records in the file." %(i)
print "%d records have sequence length of 248." % (len_249)
print "The shortest sequence is titled '%s'" % (short_seq[0])
if len(short_seq) == 1:
    print "No other records have a sequence with that length"
elif len(short_seq) > 1:
    for i in short_seq[1:]:
        print "The record %s has the same sequence" %(i[0])
print "The longest sequence is titled '%s'" % (long_seq[0])
if len(long_seq) == 1:
    print "No other records have a sequence with that length"
elif len(long_seq) > 1:
    for i in long_seq[1:]:
        print "The record %s has the same sequence" %(i[0])
print "The length of sequence for GenBank identifier gi|114812 is %d"  %(gi_114812)
print "These that records have 3D structures submitted to the PDB (4 character PDB identifier):"
print "|".join(filtered_pdb(s_dict.keys()))
print "The number of uniq sequences are %s" %(len(set(s_dict.values())))
print "Titles with identical sequences:" 
print "".join([k for k,v in s_dict.items() if v == s_dict.values()[0]])



# print s_dict.values()
# print len(max(s_dict.values(), key = len))
# print s_dict['>gi|47059697|gb|AAQ16277.2| chlamyopsin-5 [Chlamydomonas reinhardtii]\n']
# mylist = ['123','123456','1234', '123459']
# print max(mylist, key=len)