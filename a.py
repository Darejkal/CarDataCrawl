# import os
# import re
import pandas as pd
# _,_,files=next(os.walk("carconnect"))
# lbs=['Make', 'Model', 'Year', 'MSRP', 'Front Wheel Size (in)', 'SAE Net Horsepower @ RPM',
# 'Displacement', 'Engine Type', 'Width, Max w/o mirrors (in)', 'Height, Overall (in)',
# 'Length, Overall (in)', 'Gas Mileage', 'Drivetrain', 'Passenger Capacity', 'Passenger Doors',
# 'Body Style']
# pattern=re.compile(". *jpg *$")
# arr=[]
# for f in files:
#     arr.append(re.sub(pattern,"",f).split("_"))
# df=pd.DataFrame(arr)
# df.columns=[""]+lbs
# df.to_csv("extra.csv")
a=pd.read_csv("autolist/autolist.csv")
b=pd.read_csv("carconnection/carconnection.csv")
c=pd.concat([a,b],ignore_index=True)
c=c.drop_duplicates(subset=['VIN'], keep=False)
c=c.rename(columns={'title':'Title'})
c = c.loc[:, ~c.columns.str.contains('^Unnamed')]
def fixTitle(title):
    if not pd.isnull(title):
        return title.partition('\n')[0]
    else:
        return ""
c['Title']=c['Title'].apply(fixTitle).astype(pd.StringDtype())

c.to_csv("data.csv",index=False)