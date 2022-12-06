from selenium import webdriver
from config import settings
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = settings.web_scrapper.HEADLESS
options.add_argument("--window-size=1920,1200")

# Creating the service providing the chrome driver so we don't need to install it on the machine.
driver_service = Service(ChromeDriverManager().install())
# Instantiating the chrome webdriver
driver = webdriver.Chrome(service=driver_service, chrome_options=options)
# Calling the first page.
driver.get('https://www.mercadolivre.com/jms/mlb/lgz/msl/login/H4sIAAAAAAAEAy2OQQ7DIBAD_-IzSu4c-xG0SRaCCgEtm5Kq6t8r2h4t22O_kEqIh9NnZVjwVVNco8KgJlJfJLu4wSJXGLSo_JdpGRESyqwsDfY1QIG3G_siA6VyMgzo1N35VDrsbwoGsTm-lOWg5Dovj8jD9ZTaaIQCi121NjvPvfcps6y0lUqhTGvJ0yIzDIRDbMrC49537G3gqalTofUO--W9P0BZ4FvhAAAA/user')


# Now we find the input responsible for the email.
email_input = driver.find_element(By.NAME, 'user_id')
# Also getting the continue button.
email_continue_button = driver.find_element(By.CLASS_NAME, 'login-form__actions--submit')

# Filling the input with the correct email and giving the webdriver the command to click the continue button.
email_input.send_keys(settings.bank_login.EMAIL)
email_continue_button.click()

# captcha_box = driver.find_element(By.CLASS_NAME, 'recaptcha-checkbox-border')
# print(captcha_box)


while True:
    continue
# user_id
# driver.title, to get the page's title
# driver.current_url, to get the current URL (this can be useful when there are redirections on the website and you need the final URL)