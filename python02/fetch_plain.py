import os
#download the fasta file
os.system('efetch -db nucleotide -id AJ223353 -format fasta > sequence.fasta')
#separate the fasta header line with the plain dna sequence
with open('sequence.fasta') as myfile:
	header=myfile.readline()
	plain=myfile.read()
#modify the plain DNA to a string without new lines
realplain=str(plain).replace('\n','')
#write the plain DNA into a file
file2=open('plaindna2.txt','w')
file2.write(realplain)
file2.close()
#write the header into a file
file3=open('header.txt','w')
file3.write(header)
file3.close()
