import numpy as np
'''
pseudocode:

we have two sequences of same lenght with different starts we need to align the starts and modulate(multiply)
we have to take as input the 2 sequences ad the the two diferent start 
if start of 1 is less that start of 2 we we pad sequemce 1 with the difference with zero oat the start 
and pad sequece 2 with the diff at the ened and multiply the respective elements
'''

def modulate(seq1,seq2,start_seq1,start_seq2):
    if start_seq1<start_seq2:
        padding = start_seq2-start_seq1
        seq1 = np.pad(seq1,(padding,0),'constant')
        seq2 = np.pad(seq2,(0,padding),'constant')
        result = seq1*seq2
    elif start_seq1>start_seq2:
        padding = start_seq1-start_seq2
        seq2 = np.pad(seq2,(padding,0),'constant')
        seq1 = np.pad(seq1,(0,padding),'constant')
        result = seq1*seq2
    return [round(x,1) for x in result.tolist()]

print(modulate([1.0,0.8,0.6,0.4],[0.5,0.4,0.3,0.2],0,2))
