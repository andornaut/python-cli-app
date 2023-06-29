from typer.testing import CliRunner

from cliapp import cli


runner = CliRunner()


def test_default_command_is_usage():
    result = runner.invoke(cli.app, [])

    assert result.output.strip().startswith("Usage:")
    assert result.exit_code == 0


def test_version_flag_exists_successfully():
    result = runner.invoke(cli.app, ["--version"])

    assert "v0.1.0" in result.output.strip()
    assert result.exit_code == 0
