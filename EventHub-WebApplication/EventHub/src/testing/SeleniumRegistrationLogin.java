package testing;

import static org.junit.Assert.*;

import org.junit.Test;

import java.util.regex.Pattern;
import java.util.concurrent.TimeUnit;
import org.junit.*;
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.*;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.Select;

public class SeleniumRegistrationLogin {
  private WebDriver driver;
  private String baseUrl;
  private boolean acceptNextAlert = true;
  private StringBuffer verificationErrors = new StringBuffer();

  @Before
  public void setUp() throws Exception {
	//driver = new FirefoxDriver();
	    //System.setProperty("webdriver.chrome.driver", "C:\\Users\\Sweta\\Desktop\\selenium\\chromedriver.exe");
	    System.setProperty("webdriver.chrome.driver", "chromedriver.exe");
	    driver = new ChromeDriver();
	    //baseUrl = "http://localhost:8080/EventHub/index.jsp";
	    baseUrl =  "http://eventhubvrs.herokuapp.com/";
	    driver.manage().timeouts().implicitlyWait(60, TimeUnit.SECONDS);
  }

  @Test
  public void testNewReg() throws Exception {
    driver.get(baseUrl);
    
  //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    //Test case of invalid Registration scenarios
    //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    driver.findElement(By.cssSelector("#create-user > span.ui-button-text")).click();
    Thread.sleep(1000);
    driver.findElement(By.xpath("//button[@type='button']")).click();
    Thread.sleep(2000);
    driver.findElement(By.id("error1")).isDisplayed();
    String error1 =  driver.findElement(By.id("error1")).getText();
    Assert.assertEquals("Invalid Input.Please fill all the details", error1);
    Thread.sleep(2000);
    
    
    //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    //Test case of Successful Registration
    //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    
    driver.findElement(By.id("fname")).clear(); 
    driver.findElement(By.id("fname")).sendKeys("Sweta");
    Thread.sleep(1000);
    driver.findElement(By.id("lname")).clear();
 
    driver.findElement(By.id("lname")).sendKeys("Patel");
    Thread.sleep(1000);
    driver.findElement(By.id("email_reg")).clear();
    driver.findElement(By.id("email_reg")).sendKeys("sweta1@gmail.com");
    Thread.sleep(1000);
    driver.findElement(By.id("password_reg")).clear();
    driver.findElement(By.id("password_reg")).sendKeys("123456");
    Thread.sleep(1000);
    driver.findElement(By.id("question")).clear();
    driver.findElement(By.id("question")).sendKeys("my name");
    Thread.sleep(1000);
    driver.findElement(By.id("answer")).clear();
    driver.findElement(By.id("answer")).sendKeys("sweta");
    Thread.sleep(1000);
    driver.findElement(By.xpath("//button[@type='button']")).click();    
    Thread.sleep(2000);
    //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    //Test case of Cancel button click on Registration page
    //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    driver.findElement(By.cssSelector("#create-user > span.ui-button-text")).click();
    Thread.sleep(2000);
    driver.findElement(By.xpath("(//button[@type='button'])[2]")).click();
    Thread.sleep(2000);
    WebElement box = driver.findElement(By.id("dialog-form"));
    Thread.sleep(1000);
    Assert.assertEquals(false, box.isDisplayed());
    Thread.sleep(1000);
  
  //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    //Test case of Cancel button click on Login page
    //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    Thread.sleep(2000);
    driver.findElement(By.cssSelector("#login-user > span.ui-button-text")).click();
    Thread.sleep(2000);
    driver.findElement(By.xpath("(//button[@type='button'])[4]")).click();
    Thread.sleep(2000);
    WebElement loginbox = driver.findElement(By.id("dialog-form"));
    Thread.sleep(1000);
    Assert.assertEquals(false, loginbox.isDisplayed());
    Thread.sleep(1000);
    
    
    //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    //Test case of invalid inputs on login page
    //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    driver.findElement(By.cssSelector("#login-user > span.ui-button-text")).click();
    driver.findElement(By.id("email_login")).clear();
    driver.findElement(By.id("email_login")).sendKeys("sweta1@gmail.com");
    Thread.sleep(1000);
    driver.findElement(By.id("password_login")).clear();
    driver.findElement(By.id("password_login")).sendKeys("123");
    Thread.sleep(1000);
    driver.findElement(By.xpath("(//button[@type='button'])[3]")).click();
    Thread.sleep(2000);
    driver.findElement(By.id("errorMessage")).isDisplayed();
    String error =  driver.findElement(By.id("errorMessage")).getText();
    Assert.assertEquals("Invalid Input. Try again.", error);
    Thread.sleep(2000);
    
    //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    //Test case of valid inputs on login page
    //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    driver.findElement(By.id("password_login")).clear();
    driver.findElement(By.id("password_login")).sendKeys("123456");
    Thread.sleep(1000);
    driver.findElement(By.xpath("(//button[@type='button'])[3]")).click();
    Thread.sleep(2000);
    //Login box should be disappreared.
    WebElement loginbox1 = driver.findElement(By.id("dialog-form"));
    Thread.sleep(1000);
    Assert.assertEquals(false, loginbox1.isDisplayed());
    Thread.sleep(1000);
    //MyEvents button should be displayed on successful login
    Assert.assertEquals(true, driver.findElement(By.cssSelector("#viewSummary > span.ui-button-text")).isDisplayed());  
    
  }
  
  

  @After
  public void tearDown() throws Exception {
    driver.quit();
    String verificationErrorString = verificationErrors.toString();
    if (!"".equals(verificationErrorString)) {
      fail(verificationErrorString);
    }
  }

  private boolean isElementPresent(By by) {
    try {
      driver.findElement(by);
      return true;
    } catch (NoSuchElementException e) {
      return false;
    }
  }

  private boolean isAlertPresent() {
    try {
      driver.switchTo().alert();
      return true;
    } catch (NoAlertPresentException e) {
      return false;
    }
  }

  private String closeAlertAndGetItsText() {
    try {
      Alert alert = driver.switchTo().alert();
      String alertText = alert.getText();
      if (acceptNextAlert) {
        alert.accept();
      } else {
        alert.dismiss();
      }
      return alertText;
    } finally {
      acceptNextAlert = true;
    }
  }
}
