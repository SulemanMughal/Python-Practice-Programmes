# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 00:43:03 2022

@author: Administrator
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import selenium
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time
from os import environ
from selenium.webdriver.common.action_chains import ActionChains


user = environ["USERPROFILE"]
timeout = 20

df = pd.read_excel("E:\chromedriver_win32\Data for feed python code.xlsx", sheet_name='datos')
#df_2 = pd.read_excel(r'C:\Users\Administrator\Documents\Python\Proyecto FIFA\FIFA 2022\Lucas FIFA.xlsx', sheet_name='Ticket Selection')

from aux_functions import *

    


    

    



for j in range(2,5):
##    driver = uc.Chrome(executable_path= user+"\\Desktop\\chromedriver.exe")
    driver = "E:\chromedriver_win32\chromedriver.exe"
    defaulturl = "https://www.fifa.com/tournaments/mens/worldcup/qatar2022/tickets"
    print(">>>>>>>>>>>>>>>>> Start >>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    driver.get(defaulturl)
    time.sleep(3)
    action = ActionChains(driver)
    action.send_keys(Keys.TAB)
    action.send_keys(Keys.TAB)
    action.send_keys(Keys.ENTER).perform()
    elem = driver.find_element_by_xpath("(//b[contains(.,'Apply for tickets now')])[1]")
    elem.click()
    print(elem)
    time.sleep(3)
    print("============")
    elem = driver.find_element_by_xpath("//a[contains(.,'LOG IN / CREATE YOUR TICKETING ACCOUNT')]")
    elem.click()
    print(elem)
    time.sleep(3)
    
    print('--------HAY QUE HACER LOGIN---------------------')
    
    
    WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, "//input[@id='signInName']"))
                )
    elem = driver.find_element_by_xpath("//input[@id='signInName']")
    elem.send_keys(df["Email"][j].strip())
    elem = driver.find_element_by_xpath("//input[@id='password']")
    password = df["Password"][j].strip()
    elem.send_keys(password)
    time.sleep(3)
    elem = driver.find_element_by_xpath("//button[@id='next']")
    elem.click()
    print(elem)
    time.sleep(5)
    print("===== NEW PAGE LOADED =======")
    elem = driver.find_element_by_xpath("//a[contains(.,'SUBMIT OR EDIT YOUR TICKET APPLICATION')]")
    elem.click()
    print(elem)
    time.sleep(5)
    
    print('--------AHORA HAY QUE SELECCIONAR LOS TICKETS---------------------')
    
    k = [12, 455, 930, 1404, 1870, 2321, 2762, 3204]
    for i in range(8):
        individual_match_tickets(i)
        select_ticket(k[i])
        select_category_and_more(i)
        if i!=7:
            add_more_tickets()
    
    xpath = "//a[@data-ng-click='finalize()'][contains(.,'SUBMIT MY TICKET APPLICATION')]"
    WebDriverWait(driver, timeout).until(
          EC.presence_of_element_located((By.XPATH, 
          xpath))
          )
    time.sleep(1)
    driver.find_element_by_xpath(xpath).click()
    time.sleep(3)
    
    print('antes de los terminos')
    elem = driver.find_element_by_xpath("//input[@data-ng-model='terms']")
    elem.click()
    time.sleep(1)
    xpath = "//a[contains(.,'I ACCEPT TICKET(S) IN ANOTHER CATEGORY')]"
    driver.find_element_by_xpath(xpath).click()
    time.sleep(1)
    driver.find_element_by_xpath("//span[contains(.,'Submit your application')]").click()
    print("===== SUBMITTED =======")
    driver.quit()  
