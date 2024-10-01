const { Builder, By, Key, until } = require('selenium-webdriver');
const edge = require('selenium-webdriver/edge'); // Import Edge options

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

(async function e_commerce() {
    let options = new edge.Options();
    options.addArguments('--window-size=1920,1080'); // Set window size for headless
    
    // Create a new browser session (here, it's Chrome, but you can change to Firefox, etc.)
    let driver = await new Builder()
    .forBrowser('MicrosoftEdge')
    .setEdgeOptions(options)
    .setEdgeService(new (require('selenium-webdriver/edge').ServiceBuilder)('../edgedriver_win64/msedgedriver.exe')) // replace with your actual path to the Edge WebDriver
    .build();

    let username   = "standard_user"
    let password   = "secret_sauce"
    let firstName  = "Test"
    let lastName   = "User"
    let postalCode = "4000"

    try{
    
        await driver.get('https://www.saucedemo.com/');

        //username input
        await driver.wait(until.elementLocated(By.xpath('//*[@id="user-name"]')),10000).sendKeys(username)

        //password input
        await driver.findElement(By.xpath('//*[@id="password"]')).sendKeys(password)

        //login button
        await driver.findElement(By.xpath('//*[@id="login-button"]')).click()



        //CATALOG PAGE
        
        //choose item through the picture
        await driver.wait(until.elementLocated(By.xpath('//*[@id="item_4_title_link"]/div')),10000).click()



        //CHOSEN ITEM PAGE

        //get price shown in the page
        getPrice = await driver.wait(until.elementLocated(By.xpath('//*[@id="inventory_item_container"]/div/div/div[2]/div[3]')),10000).getText()

        //get the name of the product in the page
        getProductName = await driver.wait(until.elementLocated(By.xpath('//*[@id="inventory_item_container"]/div/div/div[2]/div[1]')),10000).getText()

        //add to cart button
        await driver.findElement(By.xpath('//*[@id="add-to-cart"]')).click()

        //checks if the icon of the cart changes when something is added to it
        try{
            let checkIfItemInCart = await driver.wait(until.elementLocated(By.xpath('//*[@id="shopping_cart_container"]/a/span')),10000).getText()
            if (checkIfItemInCart !== "1")
                throw Error;
        } catch(err){
            throw new Error("ERROR : Cart Icon didn't change when item added" + err);
        }

        //cart page button
        await driver.findElement(By.xpath('//*[@id="shopping_cart_container"]/a')).click()



        //CART PAGE

        //compares the price in the [Cart Page] and the price in the [Chosen Item Page]
        getPriceCart = await driver.wait(until.elementLocated(By.xpath('//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/div')),10000).getText()
        if(getPriceCart !== getPrice)
            throw new Error(`Price doesnt Match: \nOriginal Price = ${getPrice} \nPrice Shown = ${getPriceCart}`)

        //checkout button
        await driver.findElement(By.xpath('//*[@id="checkout"]')).click()



        //CHECKOUT PAGE [1/2]

        //first name input
        await driver.wait(until.elementLocated(By.xpath('//*[@id="first-name"]')),10000).sendKeys(firstName)

        //last name input
        await driver.wait(until.elementLocated(By.xpath('//*[@id="last-name"]')),10000).sendKeys(lastName)

        //postal code input
        await driver.wait(until.elementLocated(By.xpath('//*[@id="postal-code"]')),10000).sendKeys(postalCode)

        //continue button
        await driver.wait(until.elementLocated(By.id('continue')),10000).click()



        //CHECKOUT PAGE [2/2]

        //compares the price in the [Checkout Page (1)] and the price in the [Chosen Item Page]
        getPriceCheckout = await driver.wait(until.elementLocated(By.xpath('//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div[2]/div')),10000).getText()
        if(getPriceCheckout !== getPrice)
            throw new Error(`Price doesnt Match: \nOriginal Price = ${getPrice} \nPrice Shown [Checkout 1] = ${getPriceCheckout}`)

        //compares the price in the [Checkout Page (2)] and the price in the [Chosen Item Page]
        getPriceCheckout2 = await driver.wait(until.elementLocated(By.xpath('//*[@id="checkout_summary_container"]/div/div[2]/div[6]')),10000).getText()
        if(getPriceCheckout2 !== ("Item total: " + getPrice))
            throw new Error(`Price doesnt Match: \nOriginal Price = ${getPrice} \nPrice Shown [Checkout 2] = ${getPriceCheckout2}`)

        //compares the name of the product in the [Checkout Page] and the name of the product in the [Chosen Item Page]
        getProductNameCheckout = await driver.wait(until.elementLocated(By.xpath('//*[@id="item_4_title_link"]/div')),10000).getText()
        if(getProductNameCheckout !== getProductName)
            throw new Error(`Product Name dont Match: \nOriginal Name = ${getProductName} \nName Shown = ${getProductNameCheckout}`)

        //finish order button
        await driver.findElement(By.xpath('//*[@id="finish"]')).click()



        //RETURN HOME PAGE

        //return home page button
        await driver.wait(until.elementLocated(By.xpath('//*[@id="back-to-products"]')),10000).click()

        //check if main page redirects to correct page
        let url = await driver.getCurrentUrl();
        if(url !== 'https://www.saucedemo.com/inventory.html'){
            throw new Error(`Redirection failed, URL is incorrect. The URL received was ${url}`);
        }

        console.log('\x1b[42m', "Test sucessfull",'\x1b[0m');

    } catch(err){
        console.log('\x1b[31m',"Error: " + err,'\x1b[0m');

    } finally{
        await driver.quit();
    }
})();