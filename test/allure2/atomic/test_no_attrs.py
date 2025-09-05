import pytest
import allure


def test_always_passes():
    assert True


def test_fails_50_percent():
    import random
    assert random.choice([True, False])

def test_always_fails():
    assert False

def test_raises_before_assert():
    raise ValueError("This error occurs before assertion")
    assert True  # This line will never be reached

