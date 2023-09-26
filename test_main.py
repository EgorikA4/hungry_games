from main import possible_values
from typing import List
import pytest


valid_passwords = (
    ('00', ['00', '08', '80']),
    ('56', ['56', '66', '26', '46', '86', '53', '59', '55']),
    ('123', ['123', '423', '223', '113', '153', '133', '122', '126']),
)


@pytest.mark.parametrize('password, expected', valid_passwords)
def test_check_valid_passwords(password: str, expected: List[str]):
    assert sorted(possible_values(password)) == sorted(expected)


invalid_passwords = (
    ('5a', '"a" it\'s not a number.'),
    ('6b', '"b" it\'s not a number.'),
)

@pytest.mark.parametrize('password, expected', invalid_passwords)
def test_check_invalid_passwords(password: str, expected: List[str]):
    assert possible_values(password) == expected
