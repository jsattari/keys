import pytest
from keys.cli import main
from click.testing import CliRunner


# initialize click runner
runner = CliRunner()


# test for lengths
@pytest.mark.parametrize(
    "cmd, solution", [("-l 12", 12), ("-l 6", 6), ("-l 22", 22), ("-l 31", 31)]
)
def test_main_lengths(cmd, solution) -> None:
    result = runner.invoke(main, cmd)
    assert result.exit_code == 0
    assert len(result.output[:-1]) == solution


# test for removed chars
@pytest.mark.parametrize(
    "cmd, solution",
    [
        ("-r 'xyz'", True),
        ("-r '123'", True),
        ("-r '1A2B3C'", True),
        ("-r '%@!-'", True),
    ],
)
def test_remove_characters(cmd, solution) -> None:
    result = runner.invoke(main, cmd)
    chars = cmd.split(" ")[1].replace("'", "")
    output = result.output[:-1]
    assert result.exit_code == 0
    assert all([True if x not in output else False for x in chars]) == solution


@pytest.mark.parametrize("cmd, solution", [("-n", True)])
def test_no_repeats(cmd, solution) -> None:
    result = runner.invoke(main, cmd)
    assert result.exit_code == 0
    assert (
        len(set(result.output[:-1])) == len(result.output[:-1])
    ) == solution  # noqa: E501


@pytest.mark.parametrize(
    "cmd, solution",
    [
        ("-c 'AAAAAAA'", "WEAK PASSWORD STRENGTH"),
        ("-c 'sa239@#k)-wEEr'", "MEDIUM PASSWORD STRENGTH"),
        ("-c 'A#n-klEX!'", "STRONG PASSWORD"),
    ],
)
def test_strength_checker(cmd, solution) -> None:
    result = runner.invoke(main, cmd)
    assert result.exit_code == 0
    assert result.output[:-1] == solution
