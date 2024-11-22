from Bio.Seq import Seq
from Bio import SeqIO
from Bio import Entrez
import subprocess

Entrez.email = 's2667265@ed.ac.uk'
Entrez.api_key=subprocess.check_output('echo ${NCBI_API_KEY}', shell=True).rstrip().decode('utf-8')
record = Entrez.read(Entrez.esearch(db="protein", term="Mammalia COX1 complete", retmax="10"))

mammle = 0
length = 0

for accession in record['IdList']:
    genebank=Entrez.efetch(db='protein', id=accession, rettype='gb')
    record1=SeqIO.read(genebank,'genbank')
    mammle+=1
    length+=len(record1.seq)

print('total number of complete COX1 protein for mammals is:', record['Count'])

print('the average length of the protein is: ', length/mammle)