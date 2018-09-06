# Import a FASTQ file, calculate the hamming distances for each sequence,
# and plot these distances in a way you think is useful.

# Script must ultimately be contained in one fluid .py file merged via GitHub
import numpy as np
import matplotlib.pyplot as plt

#f = open('./CTGATC.fastq', 'r')

def getSeqs(fastq_file):
	#Parse a FASTQ for sequence identities and corresponding sequences
	sequences = {}
	return sequences

def hamDist(str1, str2):
   #Count the # of differences between equal length strings str1 and str2
   counts = 0
   for ch1,ch2 in zip(str1,str2):
       if ch1 != ch2:
           counts += 1
   return counts


sequences = {
    "A": "ATGGCA",
    "B": "TTCGAC",
    "C": "GCGGCA",
    "D": "GCTGCA"
}        #getSeqs(f)
ids_list = sorted(sequences.keys())
hammArray = np.zeros( (len(sequences),len(sequences)) )

for index,id in enumerate(ids_list):
    print("calculating for:", index, id, sequences[id])
    for next_index,next_id in enumerate(ids_list[index+1:], start=index+1):
        print(index,next_index)
        seq1 = sequences[id]
        seq2 = sequences[next_id]
        hd = hamDist(seq1,seq2)
        hammArray[index][next_index] = hd
        hammArray[next_index][index] = hd

print()
print(hammArray)

example_seqNameList = ['A','B','C','D','E']
example_hamArray = np.array([
    [0,6,3,1,10], # A vs a,b,c,d,e
    [6,0,2,6,8],  # B vs a,b,c,d,e
    [3,2,0,9,2],  # C vs a,b,c,d,e
    [1,6,9,0,7],  # D vs a,b,c,d,e
   [10,8,2,7,0], # E vs a,b,c,d,e
])



fig, ax = plt.subplots()
im = ax.imshow(hammArray)

ax.invert_yaxis() # so that the axes lists both start at the origin; not default for imshow
ax.set_xticks(np.arange(len(ids_list)))
ax.set_yticks(np.arange(len(ids_list)))
ax.set_xticklabels(ids_list)
ax.set_yticklabels(ids_list)
ax.set_title("Hamming Distance of Sequence Pairs")
fig.tight_layout()
fig.colorbar(im)
#Make some kind of plot that contains the data you've calculated.
plt.show()