import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def driver():
    service = ChromeService(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()

    drv = webdriver.Chrome(service=service, options=options)
    drv.implicitly_wait(15)
    yield drv
    drv.quit()

def test_buttons(driver: WebDriver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    input = driver.find_element(By.CSS_SELECTOR, '#delay')
    input.clear()
    input.send_keys("45")

    driver.find_element(By.XPATH, '//span[text()="7"]').click()
    driver.find_element(By.XPATH, '//span[text()="+"]').click()
    driver.find_element(By.XPATH, '//span[text()="8"]').click()
    driver.find_element(By.XPATH, '//span[text()="="]').click()
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located(By.CSS_SELECTOR, ".screen"), "15")
    WebDriverWait(driver, 60).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

    result = driver.find_element(By.CSS_SELECTOR, ".screen").text

    assert result == "15"

