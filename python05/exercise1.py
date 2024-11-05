def pp(seq,code):
    count=seq.count(code)
    persentage=count/len(seq)
    return persentage*100


try:
    assert round(pp("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
except Exception as e:
    print("An error occured:1", e)

try:
    assert round(pp("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
except Exception as e:
    print("An error occured:2", e)

try:
    assert round(pp("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
except Exception as e:
    print("An error occured:3", e)

try:
    assert round(pp("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)
except Exception as e:
    print("An error occured:4", e)