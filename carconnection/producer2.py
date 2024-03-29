import bs4 as bs
import os
from urllib.request import Request, urlopen
import argparse
import selenium as sel
from selenium.webdriver import Firefox,Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import re
driver = Firefox()
def fetchpage(page):
    return bs.BeautifulSoup(urlopen(Request(page,
                            headers={'User-Agent': 'Opera/9.80 (X11; Linux i686; Ub'
                                     'untu/20.10) Presto/2.12.388 Version/12.16'})).read(),
                                     'lxml')
parser=argparse.ArgumentParser()
parser.add_argument('-b', required=True,type=str)
arg=vars(parser.parse_args())
brand:str=arg["b"]
# price,mileage,Trim,Transmission,Engine,Drivetrain,VIN,Fuel Type,Exterior Color,Interior Color,Condition,Mileage,Gas Mileage,Body Style,Doors,Stock,Cabin,Bed,Rear Wheel
if __name__=='__main__':
    if not os.path.isdir("data-vin"):
        os.makedirs("data-vin")
    existing_vin=set()
    for line in open(f"data-vin/{brand}","r"):
        existing_vin.add(line.replace("\n",""))
    f=open(f"data-vin/{brand}","a")
    driver.get(f"https://www.thecarconnection.com/inventory?make={brand}")
    driver.implicitly_wait(1)
    page_select=driver.find_element(By.XPATH,"//div[contains(@class,'sort-buttons page-buttons')]")
    page_num=int(re.findall("\d+",page_select.find_element(By.XPATH,"child::span").text)[0])
    p=1
    while(p<=page_num):
        page_select=driver.find_element(By.XPATH,"//div[contains(@class,'sort-buttons page-buttons')]")
        jump_dropdown=Select(page_select.find_element(By.XPATH,"child::select"))
        next_button=page_select.find_element(By.XPATH,"child::input[contains(@class,'page page-next')]")
        eles=driver.find_elements(By.XPATH,"//div[contains(@class,'car')]")
        for el in eles:
            vin=el.get_attribute("data-vin")
            if(vin and vin not in existing_vin):
                # print(vin)
                f.write(vin)
                existing_vin.add(vin)
                f.write("\n")
        f.flush()
        p+=1
        _count=0
        while _count<3:
            try:
                driver.execute_script("arguments[0].scrollIntoView();", next_button)
                next_button.click()
                _count=10
            except:
                _count+=1
        time.sleep(5)
driver.close()