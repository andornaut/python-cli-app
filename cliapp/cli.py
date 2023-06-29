from typing import Optional

import typer
from cliapp import __app_name__, __version__

app = typer.Typer(add_completion=False, no_args_is_help=True)


@app.command()
def hello(name: str = "world"):
    print(f"Hello {name}")


@app.callback(invoke_without_command=True)
def default(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        is_eager=True,
    )
) -> None:
    """
    Project scaffolding to develop Command Line Interface (CLI) applications
    """
    if version:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()
