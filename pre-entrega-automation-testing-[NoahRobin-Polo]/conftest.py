import pytest
from selenium import webdriver 
# Importamos la función de login definida en utils.py
from utils import login

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver
