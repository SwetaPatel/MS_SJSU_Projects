package testing;

import static org.junit.Assert.*;

import org.junit.Test;
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
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.Select;


public class SeleniumSingleEventFlow {

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
		    driver.manage().timeouts().implicitlyWait(120, TimeUnit.SECONDS);
	  }

	  @Test
	  public void testNewReg() throws Exception {
	    driver.get(baseUrl);
	    
		  //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		  //Do login 
		  //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		    Thread.sleep(4000);
		    driver.findElement(By.cssSelector("#login-user > span.ui-button-text")).click();
		    Thread.sleep(4000);
		    driver.findElement(By.id("email_login")).clear();
		    driver.findElement(By.id("email_login")).sendKeys("sweta@gmail.com");
		    Thread.sleep(2000);		    
		    driver.findElement(By.id("password_login")).clear();
		    driver.findElement(By.id("password_login")).sendKeys("123456");
		    Thread.sleep(2000);
		    driver.findElement(By.xpath("(//button[@type='button'])[3]")).click();
		    Thread.sleep(4000);	
		    
		  //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		  // Test case of Birthday Event creation, Details view and summary check
		  //@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		    Thread.sleep(2000);
		    driver.findElement(By.id("birthday")).click();
		    //driver.findElement(By.id("7$item7$600")).click();
		    Thread.sleep(4000);
		    driver.findElement(By.id("event_name")).clear();
		    driver.findElement(By.id("event_name")).sendKeys("Seventh Bday");
		    Thread.sleep(4000);
		    
		   
		    WebElement element1 = driver.findElement(By.xpath("//ul[@id='sortable1']/li[1]"));
		    WebElement target1 = driver.findElement(By.id("sortable2"));
		    (new Actions(driver)).dragAndDrop(element1, target1).perform();
		    Thread.sleep(4000);
		    
		    WebElement element2 = driver.findElement(By.xpath("//ul[@id='sortable1']/li[2]"));
		    WebElement target2 = driver.findElement(By.id("sortable2"));
		    (new Actions(driver)).dragAndDrop(element2, target2).perform();
		    Thread.sleep(4000);
		    
		    WebElement element3 = driver.findElement(By.xpath("//ul[@id='sortable1']/li[3]"));
		    WebElement target3 = driver.findElement(By.id("sortable2"));
		    (new Actions(driver)).dragAndDrop(element3, target3).perform();
		    Thread.sleep(4000);
		    driver.findElement(By.id("continue")).click();
		    Thread.sleep(4000);
		    
		    Assert.assertEquals(true, driver.findElement(By.id("eventNameSpace")).getText().contains("Seventh Bday"));
		    driver.findElement(By.id("piechrt")).click();
		    Thread.sleep(4000);
		    Assert.assertEquals(true, driver.findElement(By.id("piechart")).isDisplayed());
		    
		    driver.findElement(By.id("donutchrt")).click();
		    Thread.sleep(4000);
		    Assert.assertEquals(true, driver.findElement(By.id("piechart")).isDisplayed());
		    
		    driver.findElement(By.id("txtCost2")).clear();
		    Thread.sleep(4000);
		    driver.findElement(By.id("txtCost2")).sendKeys("189");
		    Thread.sleep(4000);
		    
		    driver.findElement(By.id("btnUpdate")).click();
		    Thread.sleep(4000);
		    Assert.assertEquals(true, driver.findElement(By.id("piechart")).isDisplayed());
		    
		    driver.findElement(By.id("btnSave")).click();
		    Thread.sleep(4000);
		    
		    Assert.assertEquals(true, driver.findElement(By.cssSelector("h2")).getText().contains("My Planned Events"));
		    Thread.sleep(4000);
		    driver.findElement(By.id("Seventh Bday")).click();
		    Thread.sleep(4000);
		    Assert.assertEquals(true, driver.findElement(By.id("summarySpace")).getText().contains("Seventh Bday"));
		    Thread.sleep(4000);
		    
			//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
			// Click on Home button to go to home page and start new event
			//@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		    
		    driver.findElement(By.cssSelector("span.ui-button-text")).click();
		    Thread.sleep(4000);
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