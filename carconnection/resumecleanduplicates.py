import os
fileList=[]
for d in ["data","data-vin","error"]:
    fileList.extend([os.path.join(d,d_f) for d_f in next(os.walk(d))[2]])
for f in fileList:
    print(f)
    lines_seen = set() # holds lines already seen
    for line in open(f, "r"):
        if line not in lines_seen: # not a duplicate
            lines_seen.add(line)
    with open(f,"w") as outFile:
        for line in lines_seen:
            outFile.write(line)