import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.title('Open Python.org and check title')
@allure.description('This test checks if the Python.org homepage title is correct')
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('WebDriver')
@allure.story('Test Python.org title')
@allure.issue('https://github.com/pytest-dev/pytest/issues/1234')
@allure.testcase('https://github.com/pytest-dev/pytest/pull/1234')
@allure.link('https://www.python.org', name='Python.org')   
@allure.tag('webdriver', 'python', 'selenium')     
@allure.label("os", "windows")
def test_python_org_title(simple_fixture):
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


@allure.title('Failing test with screenshot')
@allure.description('This test intentionally fails and attaches a screenshot to the Allure report')
@allure.severity(allure.severity_level.CRITICAL)
@allure.feature('WebDriver')
@allure.story('Fail and screenshot')
@allure.tag('webdriver', 'python', 'selenium', 'fail')
def test_fail_and_screenshot(simple_fixture):
    with allure.step('Start WebDriver'):
        driver = webdriver.Chrome()
    try:
        with allure.step('Open python.org homepage'):
            driver.get('https://www.python.org')
        with allure.step('Intentionally fail and take screenshot'):
            try:
                # This will fail: element does not exist
                driver.find_element(By.ID, 'non-existent-element')
            except Exception as e:
                screenshot = driver.get_screenshot_as_png()
                allure.attach(screenshot, name='Failure Screenshot', attachment_type=allure.attachment_type.PNG)
                raise AssertionError('Intentional failure for screenshot demo') from e
    finally:
        driver.quit() 


