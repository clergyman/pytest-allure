# Allure Pytest question with pytest fixtures

npx allure run -- pytest --alluredir "./allure-results"
allure open

Go to main page of the report and navigate to any test result under test.api_tests -> looks normal
Go to main page of the report and navogate to any test result under test.webdriver_tests -> layout is broken

probably because that tests use a fixture defined in /test/conftest.py