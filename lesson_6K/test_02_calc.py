import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

@pytest.fixture
def test_buttons():
    browser = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))


    browser.get(
        'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    input = browser.find_element(By.CSS_SELECTOR, '#delay')
    input.send_keys('1')

    button_7 = browser.find_element(By.XPATH, '//span[text()="7"]').click()
    button_plus = browser.find_element(By.XPATH, '//span[text()="+"]').click()
    button_8 = browser.find_element(By.XPATH, '//span[text()="8"]').click()
    button_equals = browser.find_element(By.XPATH, '//span[text()="="]').click()
    waiter = WebDriverWait(browser, 52)
    waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div.screen'), '15')
        )

    result = browser.find_element(By.CSS_SELECTOR, 'div.screen').text
    print(result)

    assert result =='15'
