import os, sys, subprocess
import numpy as np
import pandas as pd
# os.system("cp /localdisk/data/BPSM/Lecture17/eukaryotes.txt python07/eukaryotes.txt")
dfr = pd.read_csv('python07/eukaryotes.txt',sep='\t',na_values=['-'])
#how many fungal species have genomes bigger than 100Mb? What are their names?
print('Fungi' in set(dfr['Group']))
dfr_fungi=dfr[(dfr['Group']=='Fungi') & (dfr['Size (Mb)']>100)]
print(dfr_fungi['#Organism/Name'].head())

#how many of each Kingdom/group (plants, animals, fungi and protists) have been sequenced?
print(dfr['Group'].value_counts())

print(dfr.columns)

#which Heliconius species genomes have been sequenced?
dfr['genus'] = dfr.apply(lambda x: x['#Organism/Name'].split(' ')[0],axis=1)

dfr_h=dfr[dfr['genus']=='Heliconius']
print(dfr_h['#Organism/Name'].value_counts())

#which sequencing centre has sequenced the most plant genomes? the most insect genomes?
print(dfr[dfr['Group']=='Plants']['Center'].value_counts().head())
print(dfr[dfr['SubGroup']=='Insects']['Center'].value_counts().head())

#add a column giving the number of proteins per gene. Which genomes have at least 10% more proteins than genes?
dfr['propergene']=dfr['Proteins']/dfr['Genes']
print(dfr[dfr['propergene']>1.1]['#Organism/Name'])