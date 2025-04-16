# type: ignore[attr-defined]
from typing import Optional

from enum import Enum
from random import choice

import typer
from rich.console import Console

from mh_operator import version


class Color(str, Enum):
    white = "white"
    red = "red"
    cyan = "cyan"
    magenta = "magenta"
    yellow = "yellow"
    green = "green"


app = typer.Typer(
    name="mh-operator",
    help="Awesome `mh-operator` provide interfaces and common routines for the Agilent MassHunter official SDK.",
    add_completion=False,
)
console = Console()


def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]mh-operator[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


@app.command(name="")
def main(
    color: Color | None = typer.Option(
        None,
        "-c",
        "--color",
        "--colour",
        case_sensitive=False,
        help="Color for print. If not specified then choice will be random.",
    ),
    print_version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the mh-operator package.",
    ),
) -> None:
    """Print a greeting with a giving name."""
    if color is None:
        color = choice(list(Color))

    console.print(f"[bold {color}]hello, masshunter[/]")


if __name__ == "__main__":
    app()
