import numpy as np
'''
pseudocode or idea: 

we have two sequences of same lenght with different starts we need to align the starts and modulate(multiply)
we have to take as input the 2 sequences and the the two diferent starting point
if start of seq1 is less that start of seq2 we  pad seq1 with the difference in zeros at the start 
and pad seq2 with the diff in zeros at the end and multiply the respective elements
'''
##implementation##
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


