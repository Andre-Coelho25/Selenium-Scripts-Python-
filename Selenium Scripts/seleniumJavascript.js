const { Builder, By, Key, until } = require('selenium-webdriver');

(async function example() {
  // Create a new browser session (here, it's Chrome, but you can change to Firefox, etc.)
  let driver = await new Builder()
  .forBrowser('MicrosoftEdge')
  .setEdgeService(new (require('selenium-webdriver/edge').ServiceBuilder)('C:/Users/apcoelho/Downloads/edgedriver_win64/msedgedriver.exe')) // replace with your actual path to the Edge WebDriver
  .build();
  try {
    // Navigate to Google
    await driver.get('https://www.google.com');

    await driver.wait(until.elementLocated(By.xpath('//*[@id="L2AGLb"]')),10000).click()
    
    // Find the search box by name attribute and type 'Selenium WebDriver'
    await driver.findElement(By.name('q')).sendKeys('Selenium WebDriver', Key.RETURN);

    // Wait until the page title contains 'Selenium WebDriver'
    await driver.wait(until.titleContains('Selenium WebDriver'), 10000);

    // Print the title of the page
    let title = await driver.getTitle();
    console.log('Page title is:', title);
  } catch(err){

    print("Error: " + err)

  } finally {
    // Quit the browser
    await driver.quit();
  }
})();
