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
from datetime import datetime, timedelta

# Set Edge WebDriver path
webdriver_path = 'C:/Users/apcoelho/Downloads/edgedriver_win64/msedgedriver.exe'

# Set up Edge options
edge_options = Options()
edge_options.use_chromium = True
#edge_options.add_argument('--disable-features=IsolateOrigins,site-per-process')  # Adjust as needed
#edge_options.add_argument('--disable-blink-features=AutomationControlled')
#edge_options.add_argument("inprivate")  # Incognito mode
edge_options.add_argument("window-size=1200,800")

# Initialize Edge WebDriver
service = Service(executable_path=webdriver_path)
driver = webdriver.Edge(service=service, options=edge_options)
driver.maximize_window()

def take_screenshot(step_name):
    screenshots_folder = 'C:/Users/apcoelho/Desktop/Selenium Scripts/Screenshots'
    if not os.path.exists(screenshots_folder):
        os.makedirs(screenshots_folder)
    screenshot_path = os.path.join(screenshots_folder, f'{step_name}.png')
    driver.save_screenshot(screenshot_path)
    print(f'Screenshot saved for {step_name} at: {screenshot_path}')

log_file_path = "selenium_test.log"
logging.basicConfig(
    filename=log_file_path,
    level=logging.ERROR,  # Set the logging level (use logging.INFO for more verbosity)
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

try:
    wait = WebDriverWait(driver, 10)
    
    driver.get('https://sampleapp.tricentis.com/101/')

    Automobile_Button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav_automobile"]')))
    Automobile_Button.click()
    
    #VEHICLE DATA FORM

    waitforload = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="engineperformance"]')))

    select_brand = Select(driver.find_element(By.XPATH, '//*[@id="make"]'))
    select_brand.select_by_visible_text('BMW')

    input_enginePerformance = driver.find_element(By.XPATH, '//*[@id="engineperformance"]')
    input_enginePerformance.send_keys('100')

    input_dateManufacture = driver.find_element(By.XPATH, '//*[@id="dateofmanufacture"]')
    input_dateManufacture.send_keys('10/02/2012')
    
    select_seats = Select(driver.find_element(By.XPATH, '//*[@id="numberofseats"]'))
    select_seats.select_by_visible_text('4')

    select_fuelType = Select(driver.find_element(By.XPATH, '//*[@id="fuel"]'))
    select_fuelType.select_by_visible_text('Diesel')

    input_listPrice = driver.find_element(By.XPATH, '//*[@id="listprice"]')
    input_listPrice.send_keys("10000")

    input_listPrice = driver.find_element(By.XPATH, '//*[@id="annualmileage"]')
    input_listPrice.send_keys("50000")

    nextPage2_button = driver.find_element(By.XPATH, '//*[@id="nextenterinsurantdata"]')
    nextPage2_button.click()
 
    #INSURANCE DATA FORM

    input_firstName = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="firstname"]')))
    input_firstName.send_keys('Test')

    input_lastName = driver.find_element(By.XPATH, '//*[@id="lastname"]')
    input_lastName.send_keys('User')

    input_dateBirth = driver.find_element(By.XPATH, '//*[@id="birthdate"]')
    input_dateBirth.send_keys('09/10/2000')

    male_button = driver.find_element(By.XPATH, '//*[@id="insurance-form"]/div/section[2]/div[4]/p/label[1]/span')
    male_button.click()

    female_button = driver.find_element(By.XPATH, '//*[@id="insurance-form"]/div/section[2]/div[4]/p/label[2]/span')
    female_button.click()

    select_country = Select(driver.find_element(By.XPATH, '//*[@id="country"]'))
    select_country.select_by_visible_text('Portugal')

    input_zipCode = driver.find_element(By.XPATH, '//*[@id="zipcode"]')
    input_zipCode.send_keys('4000')

    select_occupation = Select(driver.find_element(By.XPATH, '//*[@id="occupation"]'))
    select_occupation.select_by_visible_text('Farmer')

    speedingHobby_Button = driver.find_element(By.XPATH, '//*[@id="insurance-form"]/div/section[2]/div[10]/p/label[1]/span')
    speedingHobby_Button.click()
    
    nextPage3_button = driver.find_element(By.XPATH, '//*[@id="nextenterproductdata"]')
    nextPage3_button.click()

    #PRODUCT DATA FORM

    input_dateStart = driver.find_element(By.XPATH, '//*[@id="startdate"]')
    today = datetime.today()
    future_date = today + timedelta(days=31)
    input_dateStart.send_keys(future_date.strftime('%m/%d/%Y'))

    select_insuranceSum = Select(driver.find_element(By.XPATH, '//*[@id="insurancesum"]'))
    select_insuranceSum.select_by_visible_text('3.000.000,00')

    select_meritRating = Select(driver.find_element(By.XPATH, '//*[@id="meritrating"]'))
    select_meritRating.select_by_visible_text('Bonus 1')

    select_damageInsurance = Select(driver.find_element(By.XPATH, '//*[@id="damageinsurance"]'))
    select_damageInsurance.select_by_visible_text('Full Coverage')

    euroProtection_Button = driver.find_element(By.XPATH, '//*[@id="insurance-form"]/div/section[3]/div[5]/p/label[1]/span')
    euroProtection_Button.click()

    select_courtesyCar = Select(driver.find_element(By.XPATH, '//*[@id="courtesycar"]'))
    select_courtesyCar.select_by_visible_text('Yes')

    nextPage4_button = driver.find_element(By.XPATH, '//*[@id="nextselectpriceoption"]')
    nextPage4_button.click()

    #SELECT PRICE PAGE

    chooseSilver_Button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="priceTable"]/tfoot/tr/th[2]/label[1]/span')))
    chooseSilver_Button.click()

    chooseGold_Button = driver.find_element(By.XPATH, '//*[@id="priceTable"]/tfoot/tr/th[2]/label[2]/span')
    chooseGold_Button.click()

    choosePlatinum_Button = driver.find_element(By.XPATH, '//*[@id="priceTable"]/tfoot/tr/th[2]/label[3]/span')
    choosePlatinum_Button.click()

    chooseUltimate_Button = driver.find_element(By.XPATH, '//*[@id="priceTable"]/tfoot/tr/th[2]/label[4]/span')
    chooseUltimate_Button.click()

    nextPage5_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nextsendquote"]')))
    nextPage5_button.click()

    #SEND QUOTE FORM

    input_email = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')))
    input_email.send_keys('Test_User@Company.com')

    input_username = driver.find_element(By.XPATH, '//*[@id="username"]')
    input_username.send_keys('Test_User')

    input_password = driver.find_element(By.XPATH, '//*[@id="password"]')
    input_password.send_keys('TestUser2001')

    input_passwordConfirmation = driver.find_element(By.XPATH, '//*[@id="confirmpassword"]')
    input_passwordConfirmation.send_keys('TestUser2001')

    send_button = driver.find_element(By.XPATH, '//*[@id="sendemail"]')
    send_button.click()

    print('\x1b[0;37;42m' + "Test Done Sucessfully" + '\x1b[0m')

except Exception as e:
    take_screenshot("Failed_Step")
    print('\x1b[0;30;41m' + "ERROR! This is why: " + '\x1b[0m', e)
    logging.error(f"Error Log:\n\n\n {e}")

finally:
    driver.quit()