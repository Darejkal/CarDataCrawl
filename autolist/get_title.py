from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox,Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver as webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pandas as pd
import time
import random
def getTitleFromVIN(driver,vin:str):
    driver.get("https://vpic.nhtsa.dot.gov/decoder/")
    driver.implicitly_wait(1)
    driver.find_element(By.XPATH,"//input[contains(@id,'VIN')]").send_keys(vin)
    driver.find_element(By.XPATH,"//input[contains(@id,'btnSubmit')]").click()
    driver.implicitly_wait(1)
    for i in range(3):
        print(i)
        try:
            title=driver.find_element(By.XPATH,"//span[contains(@id,'decodedModelYear')]").text\
            +" "+driver.find_element(By.XPATH,"//span[contains(@id,'decodedMake')]").text\
            +" "+driver.find_element(By.ID,"decodedModel").text
            titlelist.append(title)
            return title
        except:
            if i==2:
                print(titlelist)
                exit()
            time.sleep(random.randint(0,3))
df=pd.read_csv("autolist_old.csv")
def getvinlist():
    vinlist=df["VIN"].tolist()
    for vin in vinlist:
        yield vin
vin_en=iter(getvinlist())
titlelist=[]
driver = Firefox()
cached=list(open("gettitlecache","r"))
with open("gettitlecache","w") as f:
    for line in cached:
        print(line[:-1])
        v=next(vin_en)
        if line.replace(" ","").replace("\n",""):
            titlelist.append(line[:-1])
        else:
            titlelist.append(getTitleFromVIN(driver,v))
        f.write(titlelist[-1])
        f.write("\n")
        f.flush()
    for vin in vin_en:
        titlelist.append(getTitleFromVIN(driver,vin))
        print(titlelist[-1])
        f.write(titlelist[-1])
        f.write("\n")    
        f.flush()
df["title"]=titlelist
df.to_csv("autolist.csv")