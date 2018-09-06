# Import a FASTQ file, calculate the hamming distances for each sequence,
# and plot these distances in a way you think is useful.

# Script must ultimately be contained in one fluid .py file merged via GitHub
import numpy as np
import matplotlib.pyplot as plt

#f = open('./CTGATC.fastq')

def getSeqs(fastq_file):
	#Parse a FASTQ for sequence identities and corresponding sequences
	seqences = {}
	return sequences

def hamDist(str1, str2):
   #Count the # of differences between equal length strings str1 and str2
   diffs = 0
   return diffs

example_seqNameList = ['A','B','C','D','E']
example_hamArray = np.array([
    [0,6,3,1,10], # A vs a,b,c,d,e
    [6,0,2,6,8],  # B vs a,b,c,d,e
    [3,2,0,9,2],  # C vs a,b,c,d,e
    [1,6,9,0,7],  # D vs a,b,c,d,e
   [10,8,2,7,0], # E vs a,b,c,d,e
])



fig, ax = plt.subplots()
im = ax.imshow(example_hamArray)

ax.invert_yaxis() # so that the axes lists both start at the origin; not default for imshow
ax.set_xticks(np.arange(len(example_seqNameList)))
ax.set_yticks(np.arange(len(example_seqNameList)))
ax.set_xticklabels(example_seqNameList)
ax.set_yticklabels(example_seqNameList)
ax.set_title("Hamming Distance of Sequence Pairs")
fig.tight_layout()
fig.colorbar(im)
#Make some kind of plot that contains the data you've calculated.
plt.show()