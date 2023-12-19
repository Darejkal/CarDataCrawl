from selenium.webdriver.common.by import By
import selenium
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import FirefoxOptions
import time
import random
import json
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('-b', required=True,type=str)
arg=vars(parser.parse_args())
brand:str=arg["b"]
print(brand)
vin_set=set()
for line in open(f"data/{brand}.jsonl","r"):
    try:
        vin=json.loads(line)["VIN"] 
        vin_set.add(vin)
    except:
        continue
f= open(f"data-vin/{brand}","r")
outFile=open(f"data/{brand}.jsonl","a")
driver=Firefox()
driver.install_addon("ublock.xpi")
# driver.get("https://www.autolist.com")
# driver.implicitly_wait(1)
# driver.get(f"https://www.autolist.com/listings#limit=20&page=1&radius=100")
# driver.implicitly_wait(1)
for line in f:
    if line.replace(" ","").replace("\n","") in vin_set:
        continue
    attempts=10
    print(line,end="")
    while attempts>0:
        print(attempts)
        try:
            row={}
            driver.get(f"https://www.autolist.com/listings#limit=20&page=1&radius=100&vin={line[:-1]}")
            driver.implicitly_wait(1)
            title_container=driver.find_element(By.XPATH,"//div[contains(@class,'title-container')]")
            title=title_container.find_element(By.XPATH,"child::div[contains(@class,'title')]")
            title=title_container.text
            row.update({"title":title})
            price_container=title_container.find_element(By.XPATH,"child::div[contains(@class,'price-container')]")
            price=price_container.find_element(By.XPATH,"child::div[contains(@class,'price')]")
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
        except Exception as e:
            print(e)
            attempts-=1
            if attempts==0:
                with open(f"error/{brand}.log","a") as f:
                    f.write(line)   
            time.sleep(3)
            continue
print(brand,"end...")
driver.close()