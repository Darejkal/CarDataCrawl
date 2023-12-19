import selenium  as sel
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox,Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver as webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import random
driver = Firefox()
f=open("links5.txt","a")
driver.get(f"https://www.autolist.com")
time.sleep(random.randint(2,5))
oldEle=None
for i in range(420,800):
    print(i)
    driver.get(f"https://www.autolist.com/listings#&limit=20&page={i}&radius=100")
    driver.implicitly_wait(1)
    if oldEle:
        try:
            WebDriverWait(driver,30).until(EC.staleness_of(oldEle))
        except:
            print("Old element not found? Redirected maybe?")

    links = driver.find_elements(By.XPATH,"//a[contains(@class,'details')]")
    while(len(list(links))==0):
        print("wait")
        links = driver.find_elements(By.XPATH,"//a[contains(@class,'details')]")

    for l in links:
        print(f"writing {l.get_attribute('href')}")
        f.write(l.get_attribute("href"))
        f.write("\n")
    oldEle=links[0]
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # driver.implicitly_wait(30)
    time.sleep(random.randint(2,10))
driver.quit()