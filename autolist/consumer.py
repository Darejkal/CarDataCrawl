from selenium.webdriver.common.by import By
import selenium
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import json
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('-i', required=True)
arg=vars(parser.parse_args())
_i:int=arg["i"]
f= open(f"links{_i}.txt","r")
outFile=open(f"data{_i}.jsonl","a")
driver=Firefox()
oldEle=None
# for i in range(0):
#     next(f)
for line in f:
    attempts=3
    print(line,end="")
    while attempts>0:
        print(attempts)
        try:
            row={}
            driver.get(line)
            driver.implicitly_wait(1)
            if oldEle:
                try:
                    WebDriverWait(driver,2).until(EC.staleness_of(oldEle))
                except:
                    print("Old element not found? Redirected maybe?")
            price=driver.find_element(By.XPATH,"//div[contains(@class,'price-container')]").find_element(By.XPATH,"child::div[contains(@class,'price')]")
            price=price.text
            row.update({"price":price})
            mileage=driver.find_element(By.XPATH,"//div[contains(@class,'mileage-desktop')]")
            mileage=mileage.text
            row.update({"mileage":mileage})
            infos=driver.find_elements(By.XPATH,"//div[contains(@class,'vehicle-info')]")
            for inf in infos:
                try:
                    info_label=inf.find_element(By.XPATH,"child::div[contains(@class,'info-label')]").text
                    info_data=inf.find_element(By.XPATH,"child::div[contains(@class,'info-data')]").text
                    row.update({str(info_label):info_data})
                finally:
                    continue
            print(row)
            outFile.write(json.dumps(row))
            outFile.write("\n")
            outFile.flush()
            oldEle=infos[0]
            time.sleep(random.randint(0,3))
            break
        except:
            attempts-=1
            if attempts==0:
                with open(f"error{_i}.log","a") as f:
                    f.write(line)    
            continue