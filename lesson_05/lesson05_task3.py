from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().
                                                  install()))


driver.get('http://the-internet.herokuapp.com/inputs')

search_filed = driver.find_element(By.CSS_SELECTOR, 'input')
search_filed.send_keys("Sky")

search_filed.clear()


search_filed.send_keys("Pro")
driver.quit ()
