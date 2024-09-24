from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set Edge WebDriver path
webdriver_path = 'C:/Users/apcoelho/Downloads/edgedriver_win64/msedgedriver.exe'

# Set up Edge options
edge_options = Options()
edge_options.add_argument("inprivate")  # Use Incognito mode
edge_options.add_argument("window-size=1200,800")  # Set window size

# Initialize Edge WebDriver
service = Service(executable_path=webdriver_path)
driver = webdriver.Edge(service=service, options=edge_options)

try:
    # 1. Open Google's homepage
    driver.get("https://www.google.com")
    driver.maximize_window()
    # 2. Wait for the page to load fully
    wait = WebDriverWait(driver, 10)

    # 3. Close cookie consent or pop-ups if they appear
    try:
        consent_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Aceitar tudo']")))
        consent_button.click()
    except Exception as e:
        print("No pop-up appeared:", e)

    # 4. Wait until the search box is visible and interactable
    search_box = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
    driver.execute_script("arguments[0].scrollIntoView();", search_box)

    # 5. Enter the search query and submit
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)

    # 6. Introduce a failure: try to interact with a non-existent element
   # non_existent_element = wait.until(EC.visibility_of_element_located((By.ID, "non_existent_id")))  # This will fail
    first_result = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "h3")))
    first_result.click()

    
except Exception as e:
    # 7. Take a screenshot when an exception occurs
    print(f"Test failed due to: {e}")
    screenshot_path = 'C:/Users/apcoelho/Desktop/failure_screenshot.png'
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved at: {screenshot_path}")

finally:
    # 8. Close the browser
    driver.quit()
