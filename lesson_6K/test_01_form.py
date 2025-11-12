import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.webdriver import WebDriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions

@pytest.fixture
def driver():
   service = EdgeService(EdgeChromiumDriverManager().install())
   options = webdriver.EdgeOptions()
    

   drv = webdriver.Edge(service=service, options=options)
   drv.implicitly_wait(4)
   yield drv
   drv.quit


def test_buttons(driver: WebDriver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    driver.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, "[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, "[name='country']").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "[name='company']").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary").click()

    zip_code = driver.find_element(By.CSS_SELECTOR, "[name='zip-code']")
    bg = zip_code.value_of_css_property("background-color")
    assert bg in ("rgba(248, 215, 218, 1)", "rgb(248, 215, 218)")


    ok_fields = [ 
        "[name='first-name']",
        "[name='last-name']",
        "[name='address']",
        "[name='e-mail']",
        "[name='phone']",
        "[name='city']",
        "[name='country']",
        "[name='job-position']",
        "[name='company']",
        ]
    
    for selector in ok_fields:
        el = driver.find_element(By.CSS_SELECTOR, selector)
        color = el.value_of_css_property("background-color")
        assert color in ("rgba(209, 231, 221, 1)", "rgb(209, 231, 221)")
