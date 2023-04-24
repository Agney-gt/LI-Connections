#from urllib.request import Request, urlopen

#req = Request('https://www.topstockresearch.com/INDIAN_STOCKS/COMPUTERS_SOFTWARE/Wipro_Ltd.html')
#webpage = urlopen(req).read()
#print(webpage)
import time
import pandas as pd
from bs4 import BeautifulSoup, NavigableString, SoupStrainer
import requests
from random import shuffle
import re
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import InvalidArgumentException
from time import sleep
from selenium.common.exceptions import WebDriverException
import random
import pyautogui
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
#chrome_options.add_argument("--headless") #For AWS/GCP 
driver=webdriver.Chrome(options=chrome_options, executable_path='D:/Downloads/chromedriver.exe')
driver.delete_all_cookies()
driver.maximize_window()
action = ActionChains(driver)
dfaf=pd.DataFrame()

df=pd.DataFrame()
#dff=pd.read_csv("c2c-vendor-posts.csv")#, encoding = "ISO-8859-1")

url=dff["Profile URL"].to_list()
action = webdriver.ActionChains(driver)

driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
##put your fb email here
time.sleep(5)
driver.find_element(By.XPATH,"//input[@id='username']").send_keys("@gmail.com")
##put your fb password here
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("abc")
sleep(2)

# click on the sign in button
# we're finding Sign in text button as it seems this element is seldom to be changed
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(15)
y=120

#www.linkedin.com/in/nelson-moran-657aa31a9/recent-activity/shares/"]
for k in url[y:y+30]:
    
    try:
        
        driver.get(k)#+"/recent-activity/shares/")
        name=driver.find_elements(By.XPATH,'//h1[contains(@class, "text")]')[0].text.split(" ")[0]
        #company=driver.find_elements_by_xpath('//div[contains(@aria-label, "Current")]')[0].text.split(" ")[0]
        print(name)
       # print(company)
        
        print(k)
        ymod=y%4
        
        
        time.sleep(random.randint(10,15))
        try:
            more=driver.find_elements(By.XPATH,'//button[contains(@aria-label, "More")]')
            more[1].click()
            time.sleep(random.randint(10,15))
            connect=driver.find_elements(By.XPATH,'//span[contains( text( ), "Connect")]')
            connect[1].click()
            time.sleep(random.randint(10,15))
            #pyautogui.press('enter', presses=30, interval=0.1)
        except Exception as e:
            driver.find_element(By.XPATH,'//div[contains(@class, "top-card")]//button[contains(@aria-label, "Invite")]').click()
            print(e)
            pass
        try:
            reason=driver.find_element(By.XPATH,'//button[contains(@aria-label, "We don")]')
            
            reason.click()
            
            
            #pyautogui.press('enter', presses=30, interval=0.1)
            con=driver.find_element(By.XPATH,'//button[contains(@aria-label, "Connect")]')
            con.click()
            time.sleep(random.randint(10,15))
            con2=driver.find_element(By.XPATH,'//button[contains(@aria-label, "Connect")]')
            
            con2.click()
            #pyautogui.press('enter', presses=30, interval=0.1)
            time.sleep(random.randint(10,15))
            #pyautogui.press('enter', presses=30, interval=0.1)
        except Exception as e:
            print(e)
            
            try:
                first=driver.find_elements(By.XPATH,'//button[contains(@aria-label, "Invite")]')
                first[1].click()
                
            except Exception as e:
                print(e)
                
                pass
            pass
        

        driver.find_element(By.XPATH,'//button[contains(@aria-label, "Add a note")]').click()
        #print("clicked")
        time.sleep(random.randint(10,15))
        text="Dear "+name+", Would be glad to connect and be a part of your network!" 
        driver.find_element(By.XPATH,'//textarea[contains(@class, "text-area")]').send_keys("",text)
        #dff.at[y,"A/B"]=abtest[ymod]#print("text")
        time.sleep(random.randint(10,15))
        driver.find_element(By.XPATH,'//button[contains(@aria-label, "Send")]').click()
        #dff.at[y,"Sent"]="Yes"
        dff.to_csv("Linkedin-Connections-Output.csv")
        time.sleep(5)
        
        y=y+1
    except Exception as e:
        print(e)
        y=y+1
        pass
    

      
    
 
    
