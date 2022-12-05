from selenium import webdriver
from config import settings

driver = webdriver.Chrome(executable_path=settings.scrapper.WEBDRIVER_PATH)
driver.get('https://google.com')