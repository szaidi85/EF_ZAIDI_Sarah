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
driver.find_element(By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-right']/li[1]/a").click()
driver.find_element(By.NAME, "firstname").send_keys("Sarah")
driver.find_element(By.NAME, "lastname").send_keys("ZAIDI")
driver.find_element(By.NAME, "email").send_keys("lescarnetsdesally@gmail.com")
driver.find_element(By.NAME, "telephone").send_keys("4388352525")
driver.find_element(By.NAME, "password").send_keys("12345678")
driver.find_element(By.NAME, "confirm").send_keys("12345678")
driver.find_element(By.NAME, "agree").click()
driver.find_element(By.XPATH, "//input[@class='btn btn-primary']").click()
assert driver.current_url == "http://tutorialsninja.com/demo/index.php?route=account/success"
message = driver.find_element(By.XPATH, "//div[@id='content']/p").text
assert message == "Congratulations! Your new account has been successfully created!", "Le message ne s'est pas affiche"
driver.close()

