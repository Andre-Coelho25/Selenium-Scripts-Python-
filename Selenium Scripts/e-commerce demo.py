from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set Edge WebDriver path
webdriver_path = 'C:/Users/apcoelho/Downloads/edgedriver_win64/msedgedriver.exe'

# Set up Edge options
edge_options = Options()
edge_options.add_argument("inprivate")  # Incognito mode
edge_options.add_argument("window-size=1200,800")

# Initialize Edge WebDriver
service = Service(executable_path=webdriver_path)
driver = webdriver.Edge(service=service, options=edge_options)
driver.maximize_window()
username   = "standard_user"
password   = "secret_sauce"
firstName  = "Test"
lastName   = "User"
postalCode = "4000"

try:
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    inputUsername = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="user-name"]')))
    inputUsername.send_keys(username)

    inputPassword = driver.find_element(By.XPATH, '//*[@id="password"]')
    inputPassword.send_keys(password)

    login_Button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    login_Button.click()
    
    #Catalog Page

    itemChoose = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="item_4_title_link"]/div')))
    itemChoose.click()

    #Item Page

    getPrice = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[3]')))
    price = getPrice.text

    getProductName = driver.find_element(By.XPATH, '//*[@id="inventory_item_container"]/div/div/div[2]/div[1]')
    productName = getProductName.text

    addCart_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart"]')
    addCart_button.click()
    
    try:
        checkIfItemInCart = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
        if checkIfItemInCart.text != "1":
            raise ValueError("Num of items in the icon didnt change")    
    except Exception as e:
        raise ValueError('Cart icon didnt change')

    enterCart_button = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    enterCart_button.click()

    #Cart Page

    getPriceInCart = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')))
    if getPriceInCart.text != price:
        raise ValueError(f"Price doesnt Match: \nOriginal Price = {price} \nPrice Shown = {getPriceInCart.text}") 
    
    checkout_button = driver.find_element(By.XPATH, '//*[@id="checkout"]')
    checkout_button.click()

    #Checkout Page

    inputFirstName = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="first-name"]')))
    inputFirstName.send_keys(firstName)

    inputLastName = driver.find_element(By.XPATH, '//*[@id="last-name"]')
    inputLastName.send_keys(lastName)

    inputZipCode = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
    inputZipCode.send_keys(postalCode)

    nextPageOfCheckout_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
    nextPageOfCheckout_button.click()

    #Last Checkout Page

    getPriceInOverview1 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')))
    if getPriceInOverview1.text != price:
        raise ValueError(f"Price doesnt Match: \nOriginal Price = {price} \nPrice Shown = {getPriceInOverview1.text}")   
    
    getPriceInOverview2 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]')))
    if getPriceInOverview2.text != ("Item total: " + price):
        raise ValueError(f"Price doesnt Match: \nOriginal Price = {price} \nPrice Shown = {getPriceInOverview2.text}")    
    
    getProductNameInOverview = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    if getProductNameInOverview.text != productName:
        raise ValueError(f"Product Name doesnt Match: \nOriginal Product = {productName} \nProduct Name Shown = {getProductNameInOverview.text}")

    finishOrder_button = driver.find_element(By.XPATH, '//*[@id="finish"]')
    finishOrder_button.click()

    #Return Home Page

    backHome_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="back-to-products"]')))
    backHome_button.click()

    #Validate it returns home

    homeUrl = driver.current_url
    if homeUrl != "https://www.saucedemo.com/inventory.html":
        raise ValueError("Wrong route")
    
    print('\x1b[0;37;42m' + "Test Done Sucessfully" + '\x1b[0m')    

except Exception as e:
    print('\x1b[0;30;41m' + "Error! This is why: " + '\x1b[0m', e)

finally:
    driver.quit()