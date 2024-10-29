finalseq=""
with open("genomic_dna2.txt") as file1:
    seq=file1.read().strip()
    with open("exons.txt") as file2:
        for line in file2:
            positions=line.split(",")
            start=int(positions[0]) - 1
            stop=int(positions[1])
            finalseq+=seq[start:stop]
print(finalseq)
print(len(finalseq))