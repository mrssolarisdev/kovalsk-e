from config import settings

import requests
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
import time
import json
import undetected_chromedriver as uc # We are using it so that reCaptcha doesn't get us.
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

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
# Also getting the continue button. We cannot get it by the name as there is no such tag.
email_continue_button = driver.find_element(By.CLASS_NAME, 'login-form__actions--submit')


# Filling the input with the correct email and giving the webdriver the command to click the continue button.
email_input.send_keys(settings.WARREN.BANK_EMAIL) 
time.sleep(1)
email_continue_button.click()

time.sleep(1) # waiting a little bit more. Then, getting to the next page so that the driver waits for the page to load before getting the other elements.
driver.get('https://www.mercadolivre.com/jms/mlb/lgz/msl/login/H4sIAAAAAAAEAy1OTUsDMRD9L-_gKe7eA0Wo9KQgtHgOs5tJGprdhMnUrZT-d4l6fN_vjlxiWp1-V4YF32pOc1IY1EwaiiwueVgsFQYtKf_DPHULCS2sLA323osi-z2HIr1K5cowoKueXchlg_2bgkFqjm_KslJ2G09fibsaKLeeiAUWZ9Xa7Dhu2zYsLDP5UimWYS7LMMn4kvzu83Q4uv37x-vb4fjUF1zyu0t5nmjmFQbCMTVl4f7_983DIFBTp0LzBbZzjx-xiONyAQEAAA/enter-pass')

password_input = driver.find_element(By.NAME, 'password')
time.sleep(1)
submit_password_button = driver.find_element(By.ID, 'action-complete') # there are two buttons with the same value for the tag 'name'

# Confirming password
password_input.send_keys(settings.WARREN.BANK_PASSWORD)
time.sleep(1)
submit_password_button.click()

time.sleep(5)
qr_code_image = driver.find_element(By.CLASS_NAME, 'validation-card__qrcode').screenshot('core/modules/warren/temp_files/temp_qrcode_html.png')

# Sending telegram request so that Kovalski warns us that Warren needs us to scan the qrcode for him.
api_route = 'sendPhoto'
files = {
    "photo": open("core/modules/warren/temp_files/temp_qrcode_html.png", "rb")
}
request_url = f"https://api.telegram.org/bot{settings.KOVALSKI.API_BOT_KEY}/{api_route}"
params = {
    "chat_id": settings.KOVALSKI.API_BOT_ID
}
response = requests.post(request_url, params, files=files)
print(files, response.text)
if not response.ok:
    raise requests.HTTPError

while True:
    continue
