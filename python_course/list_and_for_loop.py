"""
list and for loops pdf
"""

SEQ = raw_input("Enter a sequence: ")
def exercise1(sequence):
    """
    Excercise 1
    Write a program that asks for a sequence (use the raw_input function) then prints it 10 times.
    Include the loop count in the output
    """
    for i in range(0, 10):
        print str(i) + " " + sequence

# exercise1(SEQ)

def exercise2(sequence):
    """
    Exercise 2
    Write a program that asks for a sequence then numbers each base,
    one base per line.
    """
    for index, seq in enumerate(sequence):
        print "base " + str(index) + " is " + seq

# exercise2(SEQ)

def exercise3():
    """
    Exercise 3
    Write a programe that prints each restriction site pattern
    """
    restriction_sites = ["GAATTC", "GGATCC", "AAGCTT"]

    for i in restriction_sites:
        print i + " is a restriction site"

#exercise3()

def exercise4(sequence):
    """
    Modify the program from ex3 to ask for a sequence then say whether
    each restriction site is or is not present
    """
    restriction_sites = ["GAATTC", "GGATCC", "AAGCTT"]
    for i in restriction_sites:
        if i in sequence:
            print i + " is in the sequence: True"
        else:
            print i + " is in the sequence: False"

#exercise4(SEQ)
