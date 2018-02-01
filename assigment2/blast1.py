"""
To build a blastp parser
"""
class BlastResult(object):
    """
    Object for blast result
    """
    def __init__(self, version, database_sequences, database_letters, descriptions):
        self.version = version
        self.database_sequences = database_sequences
        self.database_letters = database_letters
        self.descriptions = descriptions

class BlastDescription(object):
    """
    Object for the description line
    """
    def __init__(self, title, score, e):
        self.title = title
        self.score = score
        self.e = e

def blast_version(file_d):
    """
    Grab version and validate file
    """
    first_line = file_d.readline()
    if not first_line.startswith("BLASTP"):
        raise TypeError("Not a BLASTP file: %r" % version)
    # print "version", repr(first_line.rstrip())
    return first_line.rstrip()

def counts_line(file_d):
    """
    Get line after database with info regarding num of sequences and total letters
    ex. "72,615 sequences; 26,335,942 total letters"
    """
    while 1:
        line = file_d.readline()
        if line.startswith("Database:"):
            break
        if not line or line.startswith("Searching....."):
            raise TypeError("Could not find the 'Database: ' line")
    line = file_d.readline().strip().split()[:4:2]
    num_seq = int(line[0].replace(",", ""))
    num_letters = int(line[1].replace(",", ""))
    # print "%d sequences and %d letters" %(num_seq, num_letters)
    return num_seq, num_letters

def extract_line(description_line):
    """
    Extract title, scores, and e value from input line
    """
    new_line = description_line.split()
    title = " ".join(new_line[:len(new_line) - 2])
    score = int(new_line[len(new_line) - 2])
    e_val = float(new_line[len(new_line) - 1])
    return title, score, e_val

def descriptions_lines(file_d):
    """
    Collecting all description lines
    """
    descriptions = []
    while 1:
        line = file_d.readline()
        if not line:
            raise TypeError("Found end of file when reading summaries")
        if line.startswith("Sequences producing significant alignments: "):
            line = file_d.readline()
            break
    while 1:
        line = file_d.readline()
        if not line:
            raise TypeError("Found end of file when reading summaries")
        if line == "\n":
            break
        else:
            #print "'%s'\n\t%d bits; expectation value = %g" %(extract_line(line))
            title, score, e_val = extract_line(line)
            description = BlastDescription(title, score, e_val)
            descriptions.append(description)
    return descriptions

def parse_blastp(file_d):
    """
    Parse blastp output
    """
    version = blast_version(file_d)
    num_seq, num_letters = counts_line(file_d)
    descriptions = descriptions_lines(file_d)
    return BlastResult(version, num_seq, num_letters, descriptions)
