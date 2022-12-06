from selenium import webdriver
from config import settings
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import undetected_chromedriver as uc # We are using it so that reCaptcha doesn't get us.

options = Options()
options.add_argument("start-maximized")
options.add_argument("--window-size=1920,1200")

# Creating the service providing the chrome driver so we don't need to install it on the machine.
driver = uc.Chrome()
# Calling the first page.
driver.get('https://www.mercadopago.com.br/shield?id=USER_BLOCKER&flow_id=ko-bacen#from-section=menu')
time.sleep(3) # Sleeping a little bit so that we seem more human to the page.

# Now we find the input responsible for the email.
email_input = driver.find_element(By.NAME, 'user_id')
# Also getting the continue button.
email_continue_button = driver.find_element(By.CLASS_NAME, 'login-form__actions--submit')

# Filling the input with the correct email and giving the webdriver the command to click the continue button.
email_input.send_keys(settings.bank_login.EMAIL)
email_continue_button.click()
