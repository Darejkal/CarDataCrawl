import os
import argparse
import subprocess
from typing import List
import time
from threading import Timer
parser=argparse.ArgumentParser()
parser.add_argument('-i', required=True,type=int)
arg=vars(parser.parse_args())
num=arg["i"]
print("number of processes",num)
def getPopen():
    BRANDS=["Acura","Alfa Romeo","Audi","BMW","Buick","Cadillac","Chevrolet","Chrysler","Dodge","FIAT","Ford","Genesis","GMC","Honda","HUMMER","Hyundai","INFINITI","Jaguar","Jeep","Kia","Land Rover","Lexus","Lincoln","Lucid","Maserati","Mazda","Mercedes-Benz","MINI","Mitsubishi","Nissan","Polestar","Porsche","Ram","Rivian","Scion","smart","Subaru","Tesla","Toyota","Volkswagen","Volvo"]
    for brand in BRANDS:
        brand=brand.lower().replace(" ","-")
        popen= subprocess.Popen(["/home/rejk/Downloads/prj/dsproject/venv/bin/python","producer2.py","-b",f"{brand}"])
        yield popen
genPopen=getPopen()
worker:List[subprocess.Popen]=[]
for i in range(num):
    worker.append(next(genPopen))
stopflag=False
sleep_time=60
while not stopflag:
    for i in range(num):
        if worker[i].poll() is not None:
            print("WORKER ENDEDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
            sleep_time/=2
            p=next(genPopen,None)
            if p:
                worker[i]=p
            else: 
                stopflag=True
    sleep_time+=1
    time.sleep(sleep_time)