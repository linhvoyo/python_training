"""
If statement and I/O
"""

def exercise1():
    """
    Exercise 1:
    Get sequence from user: print the number of times a base appears in the sequence.
    Do the same for T, C, and G. If a base does not exist, don't print anything.
    """
    sequence = raw_input("Enter a sequence: ")
    for i in list(set(sequence)):
        print i + " count: " + str(sequence.count(i))

# exercise1()

def exercise2():
    """
    Exercise 2:
    Get sequence from user: print the number of times a base appears in the sequence.
    Do the same for T, C, and G. If a base does not exist, print "[Base] not found"
    """
    sequence = raw_input("Enter a sequence: ")
    base = ['A', 'T', 'C', 'G']
    for i in base:
        if sequence.count(i) > 0:
            print i + " count: " + str(sequence.count(i))
        else:
            print i + " not found"

# exercise2()

def exercise3():
    """
    Exercise 3:
    Read in "10_sequences.seq"
    Print out the line number starting with one then the line.
    Remember to use rstrip() to remove the extra newline
    """
    seq_file = open("10_sequences.seq")
    for index, line in enumerate(seq_file):
        print str(index + 1) + " " + line.rstrip()

# exercise3()

def exercise4(file_d):
    """
    Exercise 4:
    Read in "10_sequences.seq"
    List the sequences which have the pattern CTATA
    """
    seq_file = open("10_sequences.seq")
    for i in seq_file:
        if "CTATA" in i:
            print i + "index: " + str(i.find("CTATA"))

# exercise4()

def exercise5():
    """
    Excercise 5:
    How many sequences are in sequences.seq file?
    How many have the pattern CTATA?
    How many have more than 1000 bases?
    How many have over 50% GC composition?
    How many have more than 2000 bases and more than 50% GC composition?
    Note:for %GC use float to convert the counts into floats before doin the division for percentage
    """
    seq_file = open("sequences.seq")
    ctata_count = 0
    thousand_count = 0
    gc_over_fifty = 0
    long_and_high_gc = 0
    for index, line in enumerate(seq_file):
        line = line.rstrip()
        if "CTATA" in line:
            ctata_count += 1
        if len(line) > 1000:
            thousand_count += 1
        if 100 * (float(line.count("G")) + float(line.count("C"))) / float(len(line)) > 50:
            gc_over_fifty += 1
        if len(line) > 2000 and \
            100 * (float(line.count("G")) + float(line.count("C"))) / float(len(line)) > 50:
            long_and_high_gc += 1
    print "There are %d sequences in sequences.seq file" %(index + 1)
    print "There are %d sequences with CTATA pattern" %(ctata_count)
    print "There are %d sequences with more than 1000 bases" %(thousand_count)
    print "There are %d sequences that have over 50 percent GC composition" %(gc_over_fifty)
    print "There are %d sequences that have more than 2000 bases " %(long_and_high_gc) + \
    "and more than 50 percent GC composition"

exercise5()
