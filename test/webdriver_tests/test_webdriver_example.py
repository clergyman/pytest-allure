import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.step('Open Python.org and check title')
def test_python_org_title():
    with allure.step('Start WebDriver'):
        driver = webdriver.Chrome()
    try:
        with allure.step('Open python.org homepage'):
            driver.get('https://www.python.org')
            assert 'Python' in driver.title
        with allure.step('Check presence of Donate button'):
            donate = driver.find_element(By.LINK_TEXT, 'Donate')
            assert donate.is_displayed()
    finally:
        driver.quit() 