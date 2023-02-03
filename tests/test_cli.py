import pytest
from keys.cli import main
from click.testing import CliRunner


# initialize click runner
runner = CliRunner()


@pytest.mark.parametrize(
    "cmd, results", [("-l 12", 12), ("-l 6", 6), ("-l 22", 22), ("-l 31", 31)]
)
def test_main_length(cmd, results):
    result = runner.invoke(main, cmd)
    assert result.exit_code == 0
    assert len(result.output[:-1]) == results
