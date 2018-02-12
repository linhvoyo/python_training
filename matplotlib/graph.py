"""
Compute hydrophobicity values for a sequence
"""

import fasta_reader
from pylab import plt
import numpy as np

def get_hydro_values(seq):
    """
    Get hydrophobicity values for each amino acid in sequence
    """
    kd = { 'A': 1.8,'R':-4.5,'N':-3.5,'D':-3.5,'C': 2.5,
           'Q':-3.5,'E':-3.5,'G':-0.4,'H':-3.2,'I': 4.5,
           'L': 3.8,'K':-3.9,'M': 1.9,'F': 2.8,'P':-1.6,
           'S':-0.8,'T':-0.7,'W':-0.9,'Y':-1.3,'V': 4.2 }
    values = []
    for residue in seq:
        values.append(kd[residue])
    return values

def label_axis(title,n):
    """
    Label plot
    """
    plt.xlabel("residue number")
    plt.ylabel("hydrophocity (moving avg over " + str(n) + " residues" )    
    plt.title("K+D hydrophocity for " + record.title.split()[0])


def mva(seq, n):
    """
    Data Smothing
    Finding moving average for specify window size.
    N has to be an odd number
    """
    mva = []
    seq = seq
    if n % 2 != 0:
        for residue in range(n/2, len(seq) - (n/2)):
            mva.append(sum(seq[residue - (n/2): residue + (n/2) + 1])/n)

    x_data = range((n/2), (len(mva) + n/2))
    return (x_data, mva)

def color_regions():
    """
    Draw the known helix and ribbon ranges.
    Yellow = helix 
    Red = sheet
    """
    plt.axvspan(9, 32, facecolor="yellow", alpha=0.4) # helix
    plt.axvspan(36, 61, facecolor="yellow", alpha=0.4)
    plt.axvspan(64, 71, facecolor="red", alpha=0.4)  # sheet
    plt.axvspan(72, 79, facecolor="red", alpha=0.4)  # sheet
    plt.axvspan(82, 100, facecolor="yellow", alpha=0.4)
    plt.axvspan(104, 126, facecolor="yellow", alpha=0.4)
    plt.axvspan(130, 159, facecolor="yellow", alpha=0.4)
    plt.axvspan(164, 190, facecolor="yellow", alpha=0.4)
    plt.axvspan(200, 224, facecolor="yellow", alpha=0.4)

def plot_graph(x_data, y_data, transmembrane_threshold):
    plt.plot(x_data, y_data, linewidth = 1.0)
    plt.axis(xmin = 1, xmax = len(hydro_values))
    plt.axhline(y = transmembrane_threshold)
    print transmembrane_threshold

def triangle_filter(seq, n):
    weights = range(1, n/2 + 2) + sorted(range(1, n/2 + 1), reverse=True)
    smooth_values = []
    for residue in range(n/2, len(seq) - (n/2)):
        new = seq[residue - (n/2): residue + (n/2) + 1]
        smooth_values.append(sum(np.multiply(new, weights)))
    x_data = range((n/2), len(smooth_values) + (n/2))
    return (x_data, smooth_values)



INPUT_FILE = open("bacteriorhodopsin.fasta")
record = fasta_reader.read_fasta_record(INPUT_FILE)
hydro_values = get_hydro_values(record.sequence)


window_size = 19
#x_axis, mva = mva(hydro_values, window_size)
x_axis, y_axis = triangle_filter(hydro_values, window_size)
plot_graph(x_axis, y_axis, 1.6)
label_axis(record.title.split()[0], window_size)
color_regions()
plt.savefig("ex.png", dpi = 80)



