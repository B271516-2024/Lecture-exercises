def undetermined(seq,n):
    count=0
    for nu in seq:
        if nu!="A" and nu!="T" and nu!="G" and nu!="C":
            count+=1
    percentage=count/len(seq)
    return percentage>n

assert undetermined("ATCGGTAGCGCGATGATnnnnnnnn",0.5) == False