import pytest
import requests
import allure

@allure.label("type", "parametrized")
@pytest.mark.parametrize(
    "endpoint,expected_status,expected_in_body",
    [
        ("https://httpbin.org/get", 200, "url"),
        ("https://httpbin.org/status/404", 404, None),
        ("https://httpbin.org/status/500", 500, None),
        ("", 0, None),  # Edge: empty URL
        (None, 0, None),  # Edge: None as URL
        ("https://httpbin.org/get?query=äöüß", 200, "äöüß"),  # Edge: special chars
        ("https://httpbin.org/bytes/0", 200, None),  # Edge: zero bytes
        ("https://httpbin.org/bytes/100000", 200, None),  # Edge: large response
    ]
)
def test_parametrized_api(endpoint, expected_status, expected_in_body):
    with allure.step(f"Request endpoint: {endpoint}"):
        if not endpoint:
            pytest.skip("Endpoint is empty or None")
        try:
            response = requests.get(endpoint, timeout=5)
        except Exception as e:
            if expected_status == 0:
                pytest.xfail(f"Expected failure for endpoint: {endpoint}")
            else:
                pytest.fail(f"Unexpected error: {e}")
        else:
            assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}"
            if expected_in_body:
                assert expected_in_body in response.text, f"'{expected_in_body}' not found in response body"


@pytest.mark.parametrize(
    "params,expected",
    [
        ({"a": 1, "b": 2}, 3),
        ({"a": -1, "b": -2}, -3),
        ({"a": 0, "b": 0}, 0),
        ({"a": 1e10, "b": 1e10}, 2e10),  # Edge: large numbers
        ({"a": None, "b": 2}, None),  # Edge: None value
        ({"a": "foo", "b": "bar"}, "foobar"),  # Edge: string concat
        ({"a": "", "b": ""}, ""),  # Edge: empty strings
    ]
)
def test_sum_api(params, expected):
    """
    Simulate a sum API (mocked locally for demonstration).
    """
    with allure.step(f"Sum params: {params}"):
        a = params.get("a")
        b = params.get("b")
        if a is None or b is None:
            assert expected is None
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            assert a + b == expected
        elif isinstance(a, str) and isinstance(b, str):
            assert a + b == expected
        else:
            pytest.fail("Unsupported types for sum")


@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("hello", "olleh"),
        ("", ""),  # Edge: empty string
        ("a", "a"),  # Edge: single character
        ("12345", "54321"),
        ("!@#$$#@!", "!@#$$#@!"),  # Edge: palindrome with special chars
        (None, None),  # Edge: None input
        ("racecar", "racecar"),  # Palindrome
        (" ", " "),  # Edge: whitespace
    ],
    ids=[
        "normal_word",
        "empty_string",
        "single_char",
        "numbers",
        "special_palindrome",
        "none_input",
        "palindrome_word",
        "whitespace_only",
    ]
)
def test_reverse_string(input_str, expected):
    """
    Test string reversal with custom IDs for each case.
    """
    
    with allure.step(f"Reverse string: {input_str}"):
        if input_str is None:
            assert expected is None
        else:
            assert input_str[::-1] == expected 


@pytest.mark.parametrize(
    "input_value,string_alias",
    [
        ("1", "one"),   # string '1'
        ("one", "1"),
        (1, "one"),      # integer 1
        ("", "None"),    # empty string
        (None, "None"),  # NoneType
        (0, "None"),      # integer zero
        (False, "None"), # boolean False
        ("False", "None"), # string 'False'
        ([], "Empty list"),    # empty list
        ("[]", "Empty list"),  # string '[]'
    ]
)
def test_type_collisions(input_value, string_alias):
    """
    Test to demonstrate pytest parameter collisions in test names.
    """
    with allure.step(f"Check type of {repr(input_value)} should be {string_alias}"):
        assert False, f"This is a forced failure for type collision demonstration. {input_value} is not {string_alias}"


