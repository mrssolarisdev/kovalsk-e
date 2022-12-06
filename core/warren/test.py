from selenium import webdriver
from config import settings
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import undetected_chromedriver as uc

options = Options()

options.add_argument("start-maximized")
options.add_argument("--window-size=1920,1200")

driver = uc.Chrome()
driver.get('https://www.mercadopago.com.br/shield?id=USER_BLOCKER&flow_id=ko-bacen#from-section=menu')
# # Creating the service providing the chrome driver so we don't need to install it on the machine.
# driver_service = Service(ChromeDriverManager().install())
# # Instantiating the chrome webdriver
# driver = webdriver.Chrome(service=driver_service, chrome_options=options)
# # Calling the first page.

# Now we find the input responsible for the email.
email_input = driver.find_element(By.NAME, 'user_id')
# Also getting the continue button.
email_continue_button = driver.find_element(By.CLASS_NAME, 'login-form__actions--submit')

# Filling the input with the correct email and giving the webdriver the command to click the continue button.
email_input.send_keys(settings.bank_login.EMAIL)
time.sleep(5)
email_continue_button.click()


# document.getElementById('recaptcha-token').value

while True:
    continue
# user_id
# driver.title, to get the page's title
# driver.current_url, to get the current URL (this can be useful when there are redirections on the website and you need the final URL)