"""
strings pdf
"""

SEQ = raw_input("Enter a sequence: ")

def assignment1(sequence):
    """
    Assignment 1
    Ask the user for a sequence then print its length
    """
    print "It is %d bases long" %((len(sequence)))

# assignment1(SEQ)

def assignment2(sequence):
    '''
    Assignment 2
    Modify the program so it also prints the number of ATCG characters in the sequence
    '''
    print "adenine: %d\nthymine: %d\ncytosine: %d\nguanine: %d" %(sequence.upper().count('A'), \
    sequence.upper().count('T'), sequence.upper().count('C'), sequence.upper().count('G'))

# assignment2(SEQ)

def assignment3(sequence):
    """
    Assignment 3
    Modify the program to allow both lower-ase and upper-case characters in the sequence
    """
    print "adenine: %d\nthymine: %d\ncytosine: %d\nguanine: %d" %(sequence.upper().count('A'), \
    sequence.upper().count('T'), sequence.upper().count('C'), sequence.upper().count('G'))

# assignment3(SEQ)

def assingment4(sequence):
    """
    Assignment 4
    Modify the program to print the number of unknown characters in the sequence
    """
    print "unknown %d" %(len(sequence) - sequence.upper().count('A') - \
    sequence.upper().count('T') - sequence.upper().count('C') - sequence.upper().count('G'))

# assignment4(SEQ)
