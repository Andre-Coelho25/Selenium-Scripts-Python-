import logging
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from datetime import datetime, timedelta

# Set Edge WebDriver path
webdriver_path = 'C:/Users/apcoelho/Downloads/edgedriver_win64/msedgedriver.exe'

# Set up Edge options
edge_options = Options()
edge_options.use_chromium = True
edge_options.add_argument('--disable-features=IsolateOrigins,site-per-process')  # Adjust as needed
edge_options.add_argument('--disable-blink-features=AutomationControlled')
#edge_options.add_argument("inprivate")  # Incognito mode
edge_options.add_argument("window-size=1200,800")

# Initialize Edge WebDriver
service = Service(executable_path=webdriver_path)
driver = webdriver.Edge(service=service, options=edge_options)
driver.maximize_window()

try:
    wait = WebDriverWait(driver, 10)

    driver.get('https://the-internet.herokuapp.com/drag_and_drop')

    A = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="column-a"]')))
    B = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="column-b"]')))

    ActionChains(driver).drag_and_drop(A, B).perform()
    time.sleep(3)
    
except Exception as e:
    print("Error: ", e)