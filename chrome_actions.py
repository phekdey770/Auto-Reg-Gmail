# chrome_actions.py

import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

class ChromeActions:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def perform_action(self):
        # Click on the button to create Gmail
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div/div/div/div[3]/div[1]/details/summary/div[1]").click()
        time.sleep(2)
        # Click on the button to create a new Gmail account
        self.driver.find_element(By.XPATH, "/html/body/main/div[1]/div/div/div/div/div[3]/div[1]/details/div/a[1]").click()
        time.sleep(2)
        
        # Enter First Name
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div/div[1]/div[1]/div/div[1]/div/div[1]/input").send_keys("Jack")
        time.sleep(2)
        # Enter Last Name
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div/div[1]/div[2]/div/div[1]/div/div[1]/input").send_keys("Rokaa")
        time.sleep(2)

        # Click on the Next button
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div/div/div/button/span").click()
        time.sleep(4)
        
        # Select a random month from the dropdown
        month_dropdown = self.driver.find_element(By.ID, "month")
        select = Select(month_dropdown)
        months = select.options[1:]  # Exclude the empty option
        random_month = random.choice(months)
        select.select_by_visible_text(random_month.text)
        time.sleep(2)
        
        # Enter Day
        self.driver.find_element(By.ID, "day").send_keys(15)
        time.sleep(2)
        
        # Enter Year
        self.driver.find_element(By.ID, "year").send_keys(1997)
        time.sleep(3)
        
        # Select a random gender from the dropdown
        gender_dropdown = self.driver.find_element(By.ID, "gender")
        select = Select(gender_dropdown)
        genders = select.options[1:3]  # Only include Male and Female
        random_gender = random.choice(genders)
        select.select_by_visible_text(random_gender.text)
        time.sleep(4)
        
        #Enter Username Gamil
        self.driver.find_element(By.XPATH, "//input[@name='Username']").send_keys("jack.rokaa232")
        time.sleep(3)
        
        # Click on the Next button on Username Gamil
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div/div/div/button/span").click()
        time.sleep(4)
        
        #Enter Password 
        self.driver.find_element(By.NAME, value="Passwd").send_keys("$1232.RoKKa4#")
        time.sleep(2)
        
        #Enter Confirm Password 
        self.driver.find_element(By.NAME, value="PasswdAgain").send_keys("$1232.RoKKa4#")
        time.sleep(2)
        
        #Enter Phone Number
        self.driver.find_element(By.ID, value="phoneNumberId").send_keys("+14844608127")
        time.sleep(2)
        
        
    
    def close_browser(self):
        self.driver.quit()
