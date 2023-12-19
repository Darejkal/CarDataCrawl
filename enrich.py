import pandas as pd 
import selenium as sel
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
driver=Firefox()
df=pd.read_csv("data.csv")
for vin in df['VIN']:
    driver.get("https://vpic.nhtsa.dot.gov/decoder/")
    driver.implicitly_wait(1)
    vin_input=driver.find_element(By.XPATH,"//input[contains(@id,'VIN')]")
    if(not vin_input):
        with open("error1.txt","a") as f:
            f.write(vin,"\n")
        continue
    vin_input.send_keys(vin)
    button=driver.find_element(By.XPATH,"//button[contains(@id,'btnSubmit')]")
    if(not vin_input):
        with open("error2.txt","a") as f:
            f.write(vin,"\n")
        continue
    button.click()
    driver.implicitly_wait(1)

    
