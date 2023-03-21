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
driver.find_element(By.XPATH, "//div[@class='form-group']/a").click()
driver.find_element(By.NAME, "search").send_keys("samsungwww")
driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()
assert driver.current_url == "http://tutorialsninja.com/demo/index.php?route=product/search&search=samsungwww"
message = driver.find_element(By.XPATH, "//div[@id='content']/p[2]").text
assert message == "There is no product that matches the search criteria.", "Un message different s'affiche"
driver.close()



