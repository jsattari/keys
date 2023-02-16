import pytest
from typing import List
from keys.tools import CmdLine, strength_checker


@pytest.mark.parametrize(
    "length, strong, solution",
    [(8, False, True), (13, False, True), (35, False, True)],
)
def test_create_pw(length, strong, solution) -> None:
    cli = CmdLine(length=length, strong=strong)  # type: ignore[call-arg]
    cli.create_password()
    assert (len(cli.get_password()) == length) == solution


@pytest.mark.parametrize(
    "length, strong, removals, solution",
    [
        (6, False, "xyz", True),
        (18, False, "123", True),
        (22, False, "@#$%", True),
    ],
)
def test_removing_chars(length, strong, removals, solution) -> None:
    cli = CmdLine(length=length, strong=strong)  # type: ignore[call-arg]
    cli.create_password()
    cli.remove_chars(removals)
    pw = cli.get_password()
    exempt: List[str] = removals.split()
    assert all([0 if char in pw else 1 for char in exempt]) == solution


@pytest.mark.parametrize(
    "length, strong, solution",
    [(9, False, True), (12, False, True), (29, False, True)],
)
def test_remove_repeats(length, strong, solution) -> None:
    cli = CmdLine(length=length, strong=strong)  # type: ignore[call-arg]
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
