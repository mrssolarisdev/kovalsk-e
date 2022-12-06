from selenium import webdriver
from config import settings
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)
driver.get('https://www.mercadolivre.com/jms/mlb/lgz/msl/login/H4sIAAAAAAAEAy2OQQ7DIBAD_-IzSu4c-xG0SRaCCgEtm5Kq6t8r2h4t22O_kEqIh9NnZVjwVVNco8KgJlJfJLu4wSJXGLSo_JdpGRESyqwsDfY1QIG3G_siA6VyMgzo1N35VDrsbwoGsTm-lOWg5Dovj8jD9ZTaaIQCi121NjvPvfcps6y0lUqhTGvJ0yIzDIRDbMrC49537G3gqalTofUO--W9P0BZ4FvhAAAA/user')