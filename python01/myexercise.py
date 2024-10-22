#1
seq="ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
cA=seq.count("A")
cT=seq.count("T")
pro=(cA+cT)/len(seq)
print(cA, cT, pro)

#2
comp=seq.replace("A","t").replace("T","a").replace("C","g").replace("G","c").upper()
print(comp)

#3
seq2="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
pos=seq2.find("GAATTC")+1
print("this is position", pos)
len_sec=len(seq)-pos+1
print(len_sec)

#4
mydna="ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1=mydna[:63]
exon2=mydna[90:]
print(exon1)
print(exon2)
coding_seq=exon1+exon2
print(coding_seq)

len_coding=len(coding_seq)
pro_coding=len_coding/len(mydna)*100 #finding the proportion of the coding sequence
print(len_coding)
print(pro_coding)

#change the intron into lowercase
intron=mydna[63:90]
final=exon1+intron.lower()+exon2
print(final)
