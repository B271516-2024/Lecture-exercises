def kmerr(seq,k,n):
    kmers=[]
    occurance=[]

    for i in range(0,len(seq)-k+1):
        kmer=seq[i:i+k]
        count=seq.count(kmer)
        if kmer not in kmers and count>n:
            kmers.append(kmer)
            occurance.append(count)
    
    return kmers

assert kmerr("ATGCATCATG",2,2)==["AT"]