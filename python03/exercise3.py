slide=[]
with open("plaindna2.txt_out") as f:
    content=f.read()
    for i in range(0,len(content)-30,3):
        segment=content[i:i+30]
        slide.append(segment)
        print("slide",i,"is: ",segment)
        GC=segment.count("G")+segment.count("C")
        print("persentage GC count is:", GC, segment)
        outpath=f"slide{i}"
        with open(outpath,"w") as file:
            output=open("header.txt").read() + segment
            file.write(output)