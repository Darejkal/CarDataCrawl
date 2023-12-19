import selenium  as sel
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox,Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver as webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import random
# driver = Firefox()
driver = webdriver.Remote(
    options=webdriver.FirefoxOptions(),
    # command_executor="chrome1:4444"\
    command_executor="http://web1:4444"
)
addon_id = webdriver.Firefox.install_addon(driver, "/ublock.xpi")
f=open("links.txt","a")
driver.get(f"https://www.autolist.com")
time.sleep(random.randint(2,5))
oldEle=None
for i in range(1,400):
    print(i)
    driver.get(f"https://www.autolist.com/pickup+truck-under+10000#body_style[]=truck&page={i}&radius=Any&sort_new_cars_last=true")
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