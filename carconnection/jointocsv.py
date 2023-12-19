import os
import json
import pandas as pd
_,_,files=next(os.walk("data"))
arr=[]
for f in files:
    for line in open(f"data/{f}"):
        if line:
            arr.append(json.loads(line))
pd.DataFrame(arr).to_csv("final.csv")