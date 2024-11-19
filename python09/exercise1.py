'''Use the ecoli.txt file and, using the code above as a starting point, make a chart which shows the AT content in a sliding 1000 base window
for the first 50000 bases
for the first 100000 bases
for the whole genome'''
import numpy as np
import matplotlib.pyplot as plt
with open('ecoli.txt','r') as f:
    content=f.read().replace('\n','')

def atcontent(window,length,dna):
    l=[]
    for i in range(0,length-window):
        DNA=dna[i:i+window]
        AT=(DNA.count('A')+DNA.count('T'))/window
        l.append(AT)
    return l

k50=atcontent(1000,50000,content)
k100=atcontent(1000,100000,content)
kwhole=atcontent(1000,len(content),content)

plt.figure(figsize=(20,10))
plt.subplot(311)
plt.plot(k50,label='k50')
plt.xlabel('frame position')
plt.ylabel('AT content')
plt.legend()

plt.subplot(312)
plt.plot(k100,label='k100')
plt.xlabel('frame position')
plt.ylabel('AT content')
plt.legend()

plt.subplot(313)
plt.plot(kwhole,label='kwhole')
plt.xlabel('frame position')
plt.ylabel('AT content')
plt.legend()
plt.savefig('chat_1.png',transparent=True)
plt.show()