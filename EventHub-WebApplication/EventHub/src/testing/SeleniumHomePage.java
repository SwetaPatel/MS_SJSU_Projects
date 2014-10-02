package testing;

import static org.junit.Assert.*;

import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
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

public class SeleniumHomePage {

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
	  //Do login 
	  //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
	    Thread.sleep(2000);
	    driver.findElement(By.cssSelector("#login-user > span.ui-button-text")).click();
	    Thread.sleep(2000);
	    driver.findElement(By.id("email_login")).clear();
	    driver.findElement(By.id("email_login")).sendKeys("sm@gmail.com");
	    Thread.sleep(1000);		    
	    driver.findElement(By.id("password_login")).clear();
	    driver.findElement(By.id("password_login")).sendKeys("123456");
	    Thread.sleep(1000);
	    driver.findElement(By.xpath("(//button[@type='button'])[3]")).click();
	    Thread.sleep(2000);	
	    
	    //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		// Check Home page elements 
		//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		Thread.sleep(2000);
		//MyEvents button should be displayed on Home page
	    Assert.assertEquals(true, driver.findElement(By.cssSelector("#viewSummary > span.ui-button-text")).isDisplayed());
	    Thread.sleep(2000);
	    //Logout button should be displayed on Home page
	    Assert.assertEquals(true, driver.findElement(By.cssSelector("#logout-user > span.ui-button-text")).isDisplayed());
	    Thread.sleep(2000);
	    //Home button should be displayed on Home page
	    Assert.assertEquals(true, driver.findElement(By.cssSelector("span.ui-button-text")).isDisplayed());
	    Thread.sleep(2000);
	    //Birthday button should be displayed on Home page
	    Assert.assertEquals(true, driver.findElement(By.id("birthday")).isDisplayed());
	    Thread.sleep(2000);
	    //Wedding button should be displayed on Home page
	    Assert.assertEquals(true, driver.findElement(By.id("wedding")).isDisplayed());
	    Thread.sleep(2000);
	    //Newyear button should be displayed on Home page
	    Assert.assertEquals(true, driver.findElement(By.id("newyear")).isDisplayed());
	    Thread.sleep(2000);
		    
	    
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
