from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = ChromeService(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)


browser.get('http://uitestingplayground.com/textinput')

search_filed = browser.find_element(By.CSS_SELECTOR, "#newButtonName")
search_filed.send_keys("SkyPro")

button = WebDriverWait(browser, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary'))
)
button.click()

content = WebDriverWait(browser, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#updatingButton"))
    )
print(content.text)


input("Press Enter to continue...")
