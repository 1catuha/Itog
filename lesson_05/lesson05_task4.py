from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().
                                                  install()))


driver.get('http://the-internet.herokuapp.com/login')

search_filed = driver.find_element(By.CSS_SELECTOR, 'input#username')
search_filed.send_keys("tomsmith")

search_filed = driver.find_element(By.CSS_SELECTOR, 'input#password')
search_filed.send_keys("SuperSecretPassword!")

search_filed = driver.find_element(By.CSS_SELECTOR, 'button.radius')
search_filed.click()

search_filed = driver.find_element(By.CSS_SELECTOR, 'div#flash')
print(search_filed.text)


driver.quit()
