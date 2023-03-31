from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture()
def setup():
    ser_obj=Service("/Users/khushbooagarwal/Downloads/chromedriver_mac64/chromedriver")
    driver=webdriver.Chrome(service=ser_obj)
    return driver

