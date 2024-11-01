import os
base_path="./sizes"

for i in range(100,1000,100):
    path1=f"{i}_{i+99}"
    path=os.path.join(base_path,path1)
    os.makedirs(path)

i=1
with open("xaa.dna") as file1:
    for line in file1:
        #find the right range
        lrange=(len(line)//100)*100
        urange=lrange+99
        #joining the path of the directory
        path2=f"{lrange}_{urange}"
        path3=os.path.join(base_path,path2)
        #joining the path of the file
        file_name=f"{i}.dna"
        path4=os.path.join(path3,file_name)
        i+=1
        with open(path4,"w") as file2:
            file2.write(line)