import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless") # Важно для CI!
    driver = webdriver.Chrome(options=chrome_options)
    # Путь к файлу (в CI это будет текущая папка)
    path = "file://" + os.getcwd() + "/index.html"
    driver.get(path)
    yield driver
    driver.quit()

def test_title(browser):
    assert "Моя Лабораторная" in browser.title

def test_form_elements(browser):
    assert browser.find_element(By.ID, "username").is_displayed()
    assert browser.find_element(By.ID, "submit-button").is_displayed()

def test_submit(browser):
    input_field = browser.find_element(By.ID, "username")
    input_field.send_keys("Ivan")
    browser.find_element(By.ID, "submit-button").click()
    message = browser.find_element(By.ID, "message")
    assert message.is_displayed()