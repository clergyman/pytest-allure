import allure
import random

from examples_allure_pytest import get_message


def test_examples_allure_pytest():
    with allure.step("Welcome to Allure Report!"):
        #assert get_message() == "Hello from examples.allure-pytest!"
        assert 1 == 2

def test_flaky_time_based():
    with allure.step('Test with 50 percent probability failure'):
        if random.random() < 0.5:
            assert False, 'This is a forced failure for stack trace demonstration.'
        else:
            assert True