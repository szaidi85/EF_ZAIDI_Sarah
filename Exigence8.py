from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)
driver.get("http://tutorialsninja.com/demo/index.php?route=common/home")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//a[@title='My Account']").click()
driver.find_element(By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-right']/li[2]/a").click()
driver.find_element(By.ID, "input-email").send_keys("2225646@bdeb.qc.ca") #lescarnetsdesally@gmail.com
driver.find_element(By.XPATH, "//div[@class='form-group']/a").click()
driver.find_element(By.NAME, "search").send_keys("sumsung")
driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
driver.find_element(By.XPATH, "//*[@id='content']/div[3]/div[1]/div/div[2]/div[1]/h4/a").click()
driver.find_element(By.XPATH, "//button[@id='button-cart']").click()
driver.find_element(By.XPATH, "//*[@id='content']/div[3]/div[2]/a").click()
message = driver.find_element(By.XPATH, "//*[@id='product-product']/div[1]/a[1]").text
assert message == "Success: You have added Samsung SyncMaster 941BW to your shopping cart!"
driver.find_element(By.XPATH, "//*[@id='cart-total']").click()
driver.find_element(By.XPATH, "//*[@id='cart']/ul/li[2]/div/p/a[2]").click()
message = driver.find_element(By.XPATH, "//*[@id='checkout-cart']/div[1]").text
assert message == " Products marked with *** are not available in the desired quantity or not in stock!"
driver.close()




