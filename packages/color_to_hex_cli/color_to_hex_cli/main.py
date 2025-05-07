import typer
from typing import Annotated  # Keep this for potential future use with typer.Argument
import webcolors  # Changed from colour
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import warnings

# No longer need ColourUsageWarning or to filter it
# from colour.utilities.verbose import ColourUsageWarning
# warnings.filterwarnings("ignore", category=ColourUsageWarning, module="colour")

app = typer.Typer(
    name="color-to-hex-cli",
    help="A CLI tool to convert color names to their hexadecimal codes.",
    add_completion=False,
    invoke_without_command=True,
)
console = Console()


@app.callback()
def callback():
    """
    Color to Hex CLI: Converts color names to hex codes.
    """
    pass


# No longer need rgb_to_hex as webcolors.name_to_hex provides the hex directly
# def rgb_to_hex(rgb_tuple):
#     """Converts an RGB tuple (0-1 float scale) to a hex string."""
#     int_rgb = tuple(int(c * 255) for c in rgb_tuple)
#     return "#{:02x}{:02x}{:02x}".format(*int_rgb)


@app.command(name="convert")
def convert_command(
    color_name: str,  # Using simple str type hint, was working for Typer
):
    """
    Converts a given color name to its hexadecimal representation using 'webcolors'.
    """
    try:
        hex_code = webcolors.name_to_hex(color_name)

        panel_content = Text.assemble(
            (f"Color Name: ", "bold white"),
            (color_name, "italic yellow"),
            "\n",
            (f"Hex Code:   ", "bold white"),
            (hex_code, "bold cyan"),
        )
        console.print(
            Panel(
                panel_content,
                title="[bold green]Conversion Result[/bold green]",
                expand=False,
            )
        )

    except ValueError:  # webcolors raises ValueError for unknown names
        error_message = Text.assemble(
            ("Error: ", "bold red"),
            (
                f"Color '{color_name}' not recognized by 'webcolors' or invalid.\n",
                "white",
            ),
            (
                "Please try a standard CSS color name (e.g., 'red', 'lightgoldenrodyellow').",
                "dim white",
            ),
        )
        console.print(
            Panel(
                error_message,
                title="[bold red]Conversion Failed[/bold red]",
                expand=False,
                border_style="red",
            )
        )
        raise typer.Exit(code=1)
    except Exception as e:  # Catch any other unexpected errors
        error_message = Text.assemble(
            ("Unexpected Error: ", "bold red"),
            (f"{str(e)}\n", "white"),
            ("An unexpected error occurred during conversion.", "dim white"),
        )
        console.print(
            Panel(
                error_message,
                title="[bold red]Conversion Error[/bold red]",
                expand=False,
                border_style="red",
            )
        )
        raise typer.Exit(code=1)


def main():
    app()


if __name__ == "__main__":
    main()
