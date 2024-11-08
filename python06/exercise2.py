gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

def translate(seq):
    aaseq=""
    for i in range (0,len(seq)-2,3):
        codon=seq[i:i+3]
        #if there is no "N" in the codon
        if "N" not in codon:
            aaseq+=gencode[codon]
        #if the first base of the codon is N (including NXX, NNX, NXN, NNN) or the second base is "N" including (XNX, XNN)
        elif codon[1]=="N" or codon[0]=="N":
            aaseq+="X"
        #if the last base of the codon is N
        elif codon[2]=="N":
            co=codon[0:1]
            co1=co+"A"
            co2=co+"T"
            co3=co+"G"
            co4=co+"C"
            #if all four different codons translate to same amino acid
            if gencode[co1]==gencode[co2]==gencode[co3]==gencode[co4]:
                aaseq+=gencode[co1]
            else:
                aaseq+="X"
    return aaseq

#reverse the sequence
def reverse(seq):
    newseq=""
    re={"A":"T", "G":"C", "T":"A", "C":"G"}
    #complementary sequence
    for base in seq:
        newseq+=re[base]
    #reverse the sequence
    newseq=newseq[::-1]
    print("the reversed sequence is:", newseq)
    return newseq


def what():
    seq=input("what is the DNA sequence?")
    reverseornot=input("yes/no")
    frame=int(input("which frame? 1/2/3"))-1
    if reverseornot=="yes":
        seq=reverse(seq)
    print(f"the query sequence is: {seq[frame:].upper()}")
    tran=translate(seq[frame:].upper())
    print(f"the translated amino acid sequence is: {tran}")
    return tran

what()