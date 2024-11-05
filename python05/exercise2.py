#calculate the total percentage of the wanted amino acids
def pp(seq,code=["A","I","L","M","F","W","Y","V"]):
    percentage=0
    for aa in code:
        count=seq.count(aa)
        percentage+=count/len(seq)
    return percentage*100

#try
def tryy(n,seq,code=["A","I","L","M","F","W","Y","V"]):
    try:
        assert round(pp(seq,code)) == n
    except Exception as e:
        print("there is an error", n,e)

tryy(5,"MSRSLLLRFLLFLLLLPPLP", ["M"])
tryy(70,"MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])
tryy(65,"MSRSLLLRFLLFLLLLPPLP")
