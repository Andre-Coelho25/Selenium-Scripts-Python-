import logging
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date

# THIS TEST IS FOR:  OLIVEIRA DE HOSPITAL  |  PB PRESS  |  TEMPERATURA ENCOLADORA  |  ENGLISH 

# Set Edge WebDriver path
webdriver_path = 'C:/Users/apcoelho/Downloads/edgedriver_win64/msedgedriver.exe'

# Set up Edge options
edge_options = Options()
edge_options.add_argument("window-size=1200,800")

# Initialize Edge WebDriver
service = Service(executable_path=webdriver_path)
driver = webdriver.Edge(service=service, options=edge_options)
driver.maximize_window()

# SET VARIABLES

today = date.today()
                                                                                                                                                            
# BEGIN SCRIPT

try:

    wait = WebDriverWait(driver, 30)
    driver.get("https://iotimdm-p-we-wa01.azurewebsites.net/Dashboard/Index")
    
    # ENTER OLIVEIRA DE HOSPITAL FACTORY

    oliveiraFactory_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="plantMapPanel_73b534ae-7c7e-4877-b826-f1c0ea339f65"]/div')))
    oliveiraFactory_button.click()
    
    #VERIFY IF DATE IN INDEX PAGE IS CORRECT
    
    time_index = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="spanWithRefreshRate"]')))
    getTimeIndexPage = time_index.text
    while getTimeIndexPage == "Last Update:":
        time_index = driver.find_element(By.XPATH, '//*[@id="spanWithRefreshRate"]')
        getTimeIndexPage = time_index.text
        time.sleep(0.1)
    getTimeIndexPageFirstSplit = getTimeIndexPage.split(": ",1)
    getDateInIndexPage = getTimeIndexPageFirstSplit[1].split(" ",1)
    if getDateInIndexPage[0] != today.strftime("%d/%m/%Y"):
        raise ValueError("Date in Index Page don't match with today date")

    # OPEN PB PRESS DETAIL PAGE

    pbPress_button = driver.find_element(By.XPATH, '//*[@id="panel_Main_d2854e60-9cfa-4fdb-a796-a5a6667db66d"]/a')
    driver.execute_script("arguments[0].click();", pbPress_button)

    # GET VALUE OF TEMPERATURE ENCOLADORA

    temperaturaEncoladora_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="aLastsa:oh:boards:press:273:statusi=1309"]')))
    temperaturaEncoladora_button.click()

    # VERIFY IF ANY GRAPH SHOW

    try:
        lastHour_Graph = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dashboardContextpanelOnehourHistory > svg > g:nth-child(2) > g.c3-chart > g.c3-chart-lines > g > g.c3-shapes.c3-shapes-data.c3-lines.c3-lines-data")))
        last24Hour_Graph = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dashboardContextpanelOnedayHistory > svg > g:nth-child(2) > g.c3-chart > g.c3-chart-lines > g > g.c3-shapes.c3-shapes-data.c3-lines.c3-lines-data")))
        last7Days_Graph = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dashboardContextpanelOneweekHistory > svg > g:nth-child(2) > g.c3-chart > g.c3-chart-lines > g > g.c3-shapes.c3-shapes-data.c3-lines.c3-lines-data")))
    except Exception as e:
        raise ValueError("Element not found" + e)
    
    # ENTER KPI BOARD

    getTemperaturaEncoladora = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="spanLastsa:oh:boards:press:273:statusi=1309"]'))).text

    kpiBoard_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nodeDetailLink"]')))
    driver.execute_script("arguments[0].click();", kpiBoard_button)

    # CHECK IF GRAPHS LOAD ON KPIBoard

    getTemperaturaEncoladoraKpiBoard = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="spanLastsa:oh:boards:press:273:statusi=1309"]'))).text
    if getTemperaturaEncoladoraKpiBoard != getTemperaturaEncoladora:
        raise ValueError(f"Values don't Match:\nIn KPI Board = {getTemperaturaEncoladoraKpiBoard}\nIn Index Page = {getTemperaturaEncoladora}")

    getDateinKpiBoard = driver.find_element(By.XPATH, '//*[@id="browser_container_header"]/div[4]/input').get_attribute("value")
    if getDateinKpiBoard != today.strftime("%Y-%m-%d"):
        raise ValueError("Date in KPI Board don't match with today date")    

    graph1 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="canvasChart1"]')))

    graph2 = wait.until(EC.invisibility_of_element_located((By.XPATH, '//*[@id="canvasChart2:loader"]')))

    print('\x1b[0;37;42m' + "Test Done Sucessfully" + '\x1b[0m')   

except Exception as e:
    print('\x1b[0;30;41m' + "Error! This is why: " + '\x1b[0m', e)

finally:
    driver.quit()