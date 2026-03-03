from typing import Optional

import typer
from cliapp import __app_name__, __version__

app = typer.Typer(add_completion=False)


@app.command()
def hello(name: str = "world"):
    print(f"Hello {name}")


@app.callback(invoke_without_command=True)
def default(
    ctx: typer.Context,
    version: bool = typer.Option(
        False,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        is_eager=True,
        flag_value=True,
    )
) -> None:
    """
    Project scaffolding to develop Command Line Interface (CLI) applications
    """
    if version:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()
    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())
        raise typer.Exit()
