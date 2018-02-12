"""
Compute hydrophobicity values for a sequence
"""

from pylab import plt
import numpy as np
import fasta_reader

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

def label_axis(size, method):
    """
    Label plot
    """
    plt.xlabel("residue number")
    plt.ylabel("hydrophocity ( " + method + " over " + str(size) + " values" )
    plt.title("K+D hydrophocity for " + INPUT_SEQ.title.split()[0])

def moving_avg(seq, size):
    """
    Data Smothing
    Finding moving average for specify window size.
    N has to be an odd number
    """
    averages = []
    seq = seq
    if size % 2 != 0:
        for residue in range(size/2, len(seq) - (size/2)):
            averages.append(sum(seq[residue - (size/2): residue + (size/2) + 1])/size)
    x_data = range((size/2), (len(averages) + size/2))
    return (x_data, averages)

def color_regions():
    """
    Draw the known helix and ribbon ranges.
    Yellow = helix and Red = sheet
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

def triangle_filter(seq, size):
    """
    Data Smoothing
    Applying triangle filter function
    """
    weights = range(1, size/2 + 2) + sorted(range(1, size/2 + 1), reverse=True)
    sw = sum(weights)
    smooth_values = []
    for residue in range(size/2, len(seq) - (size/2)):
        new = seq[residue - (size/2): residue + (size/2) + 1]
        smooth_values.append(sum(np.multiply(new, weights)/sw))
    x_data = range((size/2), len(smooth_values) + (size/2))
    return (x_data, smooth_values)

INPUT_FILE = open("bacteriorhodopsin.fasta")
INPUT_SEQ = fasta_reader.read_fasta_record(INPUT_FILE)
HYDRO_VALUES = get_hydro_values(INPUT_SEQ.sequence)
WINDOW_SIZE = 19
X_AXIS, TRIANGLE = triangle_filter(HYDRO_VALUES, WINDOW_SIZE)
plt.plot(X_AXIS, TRIANGLE, linewidth = 1.0)
X_AXIS, MVA = moving_avg(HYDRO_VALUES, WINDOW_SIZE)
plt.plot(X_AXIS, MVA, linewidth = 1.0)
plt.axis(xmin = 1, xmax = len(HYDRO_VALUES))
plt.axhline(y = 1.6)
label_axis(WINDOW_SIZE, "triangle average")
color_regions()
plt.savefig("ex.png", dpi = 80)
