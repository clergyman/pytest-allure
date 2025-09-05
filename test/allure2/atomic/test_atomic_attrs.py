import pytest
import allure



@allure.title("Always passes with absolute links")
@allure.description("This test always passes, because it's always true")
@allure.severity(allure.severity_level.NORMAL)
@allure.feature("Atomic")
@allure.tag("smoke", "fast")
@allure.issue("https://github.com/pytest-dev/pytest/issues/1234")
@allure.testcase("https://github.com/pytest-dev/pytest/pull/1234")
@allure.link("https://www.python.org", name="Python.org")
def test_always_passes_with_attrs():
    assert True

@allure.title("Fails 50% with attrs")
@allure.description("""
#This test fails 50% of the time, because it's a random choice

This test is intentionally flaky to simulate real-world instability.

- :warning: **Flaky tests** can pass or fail unpredictably, often due to timing issues, race conditions, or external dependencies.
- Use this test to verify how your reporting and CI systems handle non-deterministic outcomes.
- For more on flaky tests, see [Martin Fowler’s article](https://martinfowler.com/articles/nonDeterminism.html).

> “A flaky test is a test that sometimes passes and sometimes fails, even when no code has changed.”  
> — Martin Fowler

**Tip:** Investigate and stabilize flaky tests to maintain trust in your test suite!
""")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("regression", "randomized")
def test_fails_50_percent_with_attrs():
    import random
    assert random.choice([True, False])

@allure.title("Always fails with attrs")
@allure.severity(allure.severity_level.TRIVIAL)
@allure.tag("negative", "slow")
def test_always_fails_with_attrs():
    """
    #This test always fails, because it's always false

   This is a docstring description for it

    - :warning: **Flaky tests** can pass or fail unpredictably, often due to timing issues, race conditions, or external dependencies.

    """
    assert False

@allure.title("Broken with HTML description")
@allure.description("""
    <div>
    <h3>About This Broken Test</h3>
    <p>
        <strong>Status:</strong> <span style="color: violet;">Broken</span>
    </p>
    <ul>
        <li>This test is marked as <b>broken</b> because it raises an unexpected exception.</li>
        <li>Broken tests often indicate unhandled errors, missing implementations, or unexpected changes in dependencies.</li>
        <li>Review the stack trace and error message to identify the root cause.</li>
    </ul>
    <blockquote>
        <em>
        "A broken test is not a failing assertion, but a sign that something went wrong before the test could even complete."
        </em>
    </blockquote>
    <p>
        <a href="https://docs.qameta.io/allure/#_broken" target="_blank">Learn more about broken tests in Allure</a>
    </p>
    </div>
""")
@allure.severity(allure.severity_level.BLOCKER)
@allure.tag("exception", "edge-case")
def test_raises_before_assert_with_attrs():
    raise ValueError("This error occurs before assertion")
    assert True  # This line will never be reached

@allure.title("Empty minor with attrs")
@allure.description("This test is empty, so it's always passes")
@allure.severity(allure.severity_level.MINOR)
@allure.tag("empty", "manual")
def test_empty_minor_with_attrs():
    raise NotImplementedError("This test is intentionally broken for unknown/violet status in Allure")


