import pytest
import string
from keys.tools import CmdLine, strength_checker

# initialize variable containing chars
test_values: str = string.ascii_letters + string.digits + string.punctuation


@pytest.mark.parametrize(
    "vals, length, solution",
    [(test_values, 8, True), (test_values, 13, True), (test_values, 35, True)],
)
def test_create_pw(vals, length, solution) -> None:
    cli = CmdLine(list(vals), length)
    cli.create_password()
    assert (len(cli.get_password()) == length) == solution


@pytest.mark.parametrize(
    "vals, length, removals, solution",
    [
        (test_values, 6, "xyz", True),
        (test_values, 18, "123", True),
        (test_values, 22, "@#$%", True),
    ],
)
def test_removing_chars(vals, length, removals, solution) -> None:
    cli = CmdLine(list(vals), length)
    cli.create_password()
    cli.remove_chars(removals)
    pw = cli.get_password()
    assert all([True if x not in pw else False for x in removals]) == solution


@pytest.mark.parametrize(
    "vals, length, solution",
    [(test_values, 9, True), (test_values, 12, True), (test_values, 29, True)],
)
def test_remove_repeats(vals, length, solution) -> None:
    cli = CmdLine(list(vals), length)
    cli.create_password()
    cli.remove_repeats()
    assert (len(set(cli.get_password())) == length) == solution


@pytest.mark.parametrize(
    "password, solution",
    [("AAAAAAA", "\33[30m\33[41m\33[1mWEAK PASSWORD STRENGTH\033[0m")],
)
def test_strength_checker(password, solution) -> None:
    result = strength_checker(password)
    assert result == solution
