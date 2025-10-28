import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.trim("input_str, expected", [
    ("   Skypro", "Skypro"),
    (" 123 abc", "123 abc"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123Skypro", "123Skypro"),
    ("", ""),
    ("Skypro   ", "Skypro   "),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("SkyPro", "P"),
    ("SkyPro", "o"),
])
def test_contains_positive(input_str, expected):
    assert string_utils.contains is True


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("SkyPro", "A"),
    ("SkyPro", "8"),
])
def test_contains_negative(input_str, expected):
    assert string_utils.contains is False


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("Skypro", "Sypro"),
    ("Skypro", "pro"),
])
def test_delete_symbol_positive(input_str, expected):
    assert string_utils.delete_symbol(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("Skypro", "Skypro"),
    ("", "Skypro"),
    ])
def test_delete_symbol_negative(input_str, expected):
    assert string_utils.delete_symbol(input_str) == expected
