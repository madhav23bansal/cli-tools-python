import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(
    help="A CLI to manage and display available tools from the 'packages' directory."
)
console = Console()

tools_info = [
    {
        "name": "Color to Hex Converter",
        "command": "color_to_hex_cli",
        "usage": "color_to_hex_cli <color_name>",
        "description": "Converts color names to their corresponding hexadecimal codes.",
    },
    {
        "name": "Countdown Timer",
        "command": "countdown_timer",
        "usage": "countdown_timer <seconds>",
        "description": "A simple command-line interface (CLI) tool to start a countdown timer.",
    },
    {
        "name": "Git Helper",
        "command": "git_helper",
        "usage": "git_helper <command_name> OR git_helper --list",
        "description": "A simple CLI tool to quickly get help with common Git commands.",
    },
    {
        "name": "Random Password Generator",
        "command": "random_password",
        "usage": "random_password --length <number_of_characters>",
        "description": "A CLI tool to generate random passwords.",
    },
    {
        "name": "Simple Calculator",
        "command": "simple-calculator",
        "usage": "simple-calculator <add|sub|mul|div|pow|sqrt> <number1> [<number2>]",
        "description": "Performs arithmetic operations like addition, subtraction, multiplication, division, exponentiation, and square root.",
    },
    {
        "name": "BMI Calculator",
        "command": "bmi-calculator",
        "usage": "bmi-calculator --weight <weight_in_kg> --height <height_in_meters>",
        "description": "Calculates Body Mass Index (BMI).",
    },
    {
        "name": "Hangman Game",
        "command": "hangman_game",
        "usage": "hangman_game",
        "description": "Plays a classic game of Hangman in the CLI.",
    },
    {
        "name": "Word Scramble Game",
        "command": "word_scramble",
        "usage": "word_scramble [--rounds <number_of_rounds>]",
        "description": "Plays a word scramble game in the CLI.",
    },
]


@app.command(name="list", help="List all available tools with their usage information.")
def list_tools():
    """
    Displays a table of available CLI tools, their commands, usage, and descriptions.
    """
    table = Table(title="Available CLI Tools")
    table.add_column("Tool Name", style="cyan", no_wrap=True)
    table.add_column("Command", style="magenta")
    table.add_column("Usage", style="green")
    table.add_column("Description", style="yellow")

    for tool in tools_info:
        table.add_row(tool["name"], tool["command"], tool["usage"], tool["description"])

    console.print(table)
    console.print(
        "\nTo use a tool, first ensure it's installed (e.g., via 'pip install -r requirements.txt')."
    )
    console.print("Then, run the respective command in your terminal.")


@app.command(name="usage", help="Show usage for a specific tool.")
def tool_usage(
    tool_command: str = typer.Argument(
        ..., help="The command of the tool to get usage for (e.g., 'countdown_timer')."
    )
):
    """
    Displays usage information for a specific tool.
    """
    found_tool = None
    for tool in tools_info:
        if tool["command"] == tool_command:
            found_tool = tool
            break

    if found_tool:
        console.print(f"[bold cyan]Tool:[/bold cyan] {found_tool['name']}")
        console.print(f"[bold magenta]Command:[/bold magenta] {found_tool['command']}")
        console.print(f"[bold green]Usage:[/bold green] {found_tool['usage']}")
        console.print(
            f"[bold yellow]Description:[/bold yellow] {found_tool['description']}"
        )
    else:
        console.print(
            f"[bold red]Error:[/bold red] Tool with command '{tool_command}' not found."
        )
        console.print("Available commands are:")
        for tool in tools_info:
            console.print(f"  - {tool['command']}")


if __name__ == "__main__":
    app()
