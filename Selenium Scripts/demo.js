
const { error } = require('selenium-webdriver');
const { Select } = require('selenium-webdriver');
const { Builder, By, Key, until } = require('selenium-webdriver');
const { FetchError } = require('selenium-webdriver/bidi/networkTypes');
const edge = require('selenium-webdriver/edge'); // Import Edge options


// Custom sleep function
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function addDaysToToday(days) {
    const today = new Date(); // Get today's date
    today.setDate(today.getDate() + days); // Add the specified number of days
    return today;
}

function formatDateToString(date) {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0'); // Months are 0-indexed
    const day = String(date.getDate()).padStart(2, '0');
    return `${month}/${day}/${year}`; // Format: MM/DD/YYYY
}

(async function example() {
    let options = new edge.Options();
    options.addArguments('--window-size=1920,1080'); // Set window size for headless
    
    // Create a new browser session (here, it's Chrome, but you can change to Firefox, etc.)
    let driver = await new Builder()
    .forBrowser('MicrosoftEdge')
    .setEdgeOptions(options)
    .setEdgeService(new (require('selenium-webdriver/edge').ServiceBuilder)('../edgedriver_win64/msedgedriver.exe')) // replace with your actual path to the Edge WebDriver
    .build();
    try {
        
        await driver.get('https://sampleapp.tricentis.com/101/');

        await driver.wait(until.elementLocated(By.xpath('//*[@id="nav_automobile"]')),10000).click();



        //AUTOMOBILE DATA FORM

        //brand input
        let selectBrand = driver.wait(until.elementLocated(By.xpath('//*[@id="make"]')),10000);
        await selectBrand.findElement(By.xpath('//*[@id="make"]/option[3]')).click();
        
        //engine performance input
        await driver.findElement(By.xpath('//*[@id="engineperformance"]')).sendKeys('100');

        //date of manufacture input
        await driver.findElement(By.xpath('//*[@id="dateofmanufacture"]')).sendKeys('10/02/2012');

        //n of seat input
        let selectSeats = driver.wait(until.elementLocated(By.xpath('//*[@id="numberofseats"]')),10000);
        await selectSeats.findElement(By.xpath('//*[@id="numberofseats"]/option[5]')).click();

        //fuel type input
        let selectFuel = driver.wait(until.elementLocated(By.xpath('//*[@id="fuel"]')),10000);
        await selectFuel.findElement(By.xpath('//*[@id="fuel"]/option[3]')).click();

        //price of car input
        await driver.findElement(By.xpath('//*[@id="listprice"]')).sendKeys('10000');

        //mileage of car input
        await driver.findElement(By.xpath('//*[@id="annualmileage"]')).sendKeys('50000');

        await driver.findElement(By.xpath('//*[@id="nextenterinsurantdata"]')).click();



        //INSURANT DATA FORM

        //first name input
        await driver.wait(until.elementLocated(By.xpath('//*[@id="firstname"]')),10000).sendKeys('Test');

        //last name input
        await driver.findElement(By.xpath('//*[@id="lastname"]')).sendKeys('User');

        //birthday input
        await driver.findElement(By.xpath('//*[@id="birthdate"]')).sendKeys('09/10/2000');

        //male button select
        await driver.findElement(By.xpath('//*[@id="insurance-form"]/div/section[2]/div[4]/p/label[1]/span')).click();

        //country select
        let selectCountry = driver.findElement(By.xpath('//*[@id="country"]'));
        await selectCountry.findElement(By.xpath('//*[@id="country"]/option[178]')).click();

        //zipcode input
        await driver.findElement(By.xpath('//*[@id="zipcode"]')).sendKeys('4000');

        //occupation select
        let selectOccupation = driver.findElement(By.xpath('//*[@id="occupation"]'));
        await selectOccupation.findElement(By.xpath('//*[@id="occupation"]/option[4]')).click();

        //speeding button
        await driver.findElement(By.xpath('//*[@id="insurance-form"]/div/section[2]/div[10]/p/label[1]/span')).click();

        await driver.findElement(By.xpath('//*[@id="nextenterproductdata"]')).click();



        //PRODUCT DATA FORM

        //get current date and adds 1 more month
        let future_date = formatDateToString(addDaysToToday(32));
        
        //start date input (add the value above to it)
        await driver.wait(until.elementLocated(By.xpath('//*[@id="startdate"]')),10000).sendKeys(future_date);

        //insurance sum select
        let selectInsuranceSum = driver.findElement(By.xpath('//*[@id="insurancesum"]'));
        await selectInsuranceSum.findElement(By.xpath('//*[@id="insurancesum"]/option[8]')).click();

        //merit rating select
        let selectMeritRating = driver.findElement(By.xpath('//*[@id="meritrating"]'));
        await selectMeritRating.findElement(By.xpath('//*[@id="meritrating"]/option[7]')).click();

        //damage insurance select
        let selectDamageInsurance = driver.findElement(By.xpath('//*[@id="damageinsurance"]'));
        await selectDamageInsurance.findElement(By.xpath('//*[@id="damageinsurance"]/option[4]')).click();

        //euro protection button
        await driver.findElement(By.xpath('//*[@id="insurance-form"]/div/section[3]/div[5]/p/label[1]/span')).click();

        //courtesy car select
        let selectCourtesyCar = driver.findElement(By.xpath('//*[@id="courtesycar"]'));
        await selectCourtesyCar.findElement(By.xpath('//*[@id="courtesycar"]/option[3]')).click();
        
        await driver.findElement(By.xpath('//*[@id="nextselectpriceoption"]')).click();



        //PRICE OPTION SELECTION

        //silver option select
        await driver.wait(until.elementLocated(By.xpath('//*[@id="priceTable"]/tfoot/tr/th[2]/label[1]/span')),10000).click();
        
        let next_button = await driver.wait(until.elementLocated(By.xpath('//*[@id="nextsendquote"]')),10000);
        await driver.wait(until.elementIsVisible(next_button),10000).click();



        //QUOTE FORM

        //email input
        await driver.wait(until.elementLocated(By.xpath('//*[@id="email"]')),10000).sendKeys('testUser@company.com');

        //username input
        await driver.findElement(By.xpath('//*[@id="username"]')).sendKeys('Test_User');

        //password input
        await driver.findElement(By.xpath('//*[@id="password"]')).sendKeys('TestUser2001');
        
        //confirm password input
        await driver.findElement(By.xpath('//*[@id="confirmpassword"]')).sendKeys('TestUser2001');

        //send quote to mail button
        await driver.findElement(By.xpath('//*[@id="sendemail"]')).click();

        //confirmation of email sent button
        let confirmButton = await driver.wait(until.elementLocated(By.xpath('/html/body/div[4]/div[7]/div/button')),10000);
        await driver.wait(until.elementIsVisible(confirmButton),10000);
        await confirmButton.click();

        //main page button
        await driver.wait(until.elementLocated(By.xpath('//*[@id="backmain"]/span')),10000).click();

        //check if main page redirects to correct page
        let url = await driver.getCurrentUrl();
        if(url !== 'https://sampleapp.tricentis.com/101/index.php'){
            throw new Error(`Redirection failed, URL is incorrect. The URL received was ${url}`);
        }
      
        console.log('\x1b[42m', "Test sucessfull",'\x1b[0m');

    } catch(err){
      console.log('\x1b[31m',"Error: " + err,'\x1b[0m');

    } finally {
      await driver.quit();
    }
  })();