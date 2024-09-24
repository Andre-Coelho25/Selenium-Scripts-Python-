import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def take_screenshot(step_name):
    screenshots_folder = 'C:/Users/apcoelho/Desktop/screenshots'
    if not os.path.exists(screenshots_folder):
        os.makedirs(screenshots_folder)
    screenshot_path = os.path.join(screenshots_folder, f'{step_name}.png')
    driver.save_screenshot(screenshot_path)
    print(f'Screenshot saved for {step_name} at: {screenshot_path}')


# Set Edge WebDriver path
webdriver_path = 'C:/Users/apcoelho/Downloads/edgedriver_win64/msedgedriver.exe'

# Set up Edge options
edge_options = Options()
edge_options = Options()
edge_options.add_argument("inprivate")  # Incognito mode
edge_options.add_argument("window-size=1200,800")

# Initialize Edge WebDriver
service = Service(executable_path=webdriver_path)
driver = webdriver.Edge(service=service, options=edge_options)
driver.maximize_window()

try:
    # 1. Open Google's homepage
    driver.get("https://www.google.com")

    # 2. Wait for the page to load fully
    wait = WebDriverWait(driver, 10)

    # 3. Close cookie consent or pop-ups if they appear
    try:
        consent_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Aceitar tudo']")))
        consent_button.click()
    except Exception as e:
        print("No pop-up appeared:", e)

    # 4. Wait until the search box is visible and interactable
    search_box = wait.until(EC.element_to_be_clickable((By.NAME, "q")))

    # 5. Enter the search query and submit
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)

    # 6. Wait for the results to load and click on the first result
    first_result = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h3")))
    first_result.click()

    # 7. Wait for the page to load fully
    time.sleep(3)

    # 8. Take a screenshot
    take_screenshot("Sucessfull_Test")
    
    # 9. Close the browser
    driver.quit()
    print('\x1b[0;37;42m' + "Test Done Sucessfully" + '\x1b[0m')

except Exception as e:
    print('\x1b[0;30;41m' + "ERROR! This is why: " + '\x1b[0m', e)
    take_screenshot("Failed_Test")