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
driver.find_element(By.ID, "input-email").send_keys("lescarnetsdesally@gmail.com")
driver.find_element(By.ID, "input-password").send_keys("12345678")
driver.find_element(By.XPATH, "//input[@class='btn btn-primary']").click()
driver.find_element(By.XPATH, "//div[@class='list-group']/a[12]").click()
driver.find_element(By.XPATH, "//label[@class='radio-inline'] [1]").click()
driver.find_element(By.XPATH, "//input[@class='btn btn-primary']").click()
message = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
assert message == "Your newsletter subscription has been successfully updated!", "Le message ne s'est pas affiche"
driver.close()
