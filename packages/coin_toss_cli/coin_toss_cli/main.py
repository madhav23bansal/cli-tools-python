import random
import time
import click
from rich.console import Console
from rich.text import Text
from rich.panel import Panel

console = Console()


def get_coin_art(side):
    """Returns ASCII art for the coin side."""
    if side == "Heads":
        return Text(
            """
    .--""--.
   /        \\
  |  H E A D S  |
   \\        /
    `--""--'
            """,
            style="bold yellow",
        )
    else:
        return Text(
            """
    .--""--.
   /        \\
  |  T A I L S  |
   \\        /
    `--""--'
            """,
            style="bold cyan",
        )


@click.command()
@click.option(
    "--flips",
    default=1,
    help="Number of times to flip the coin.",
    type=int,
    show_default=True,
)
def toss(flips):
    """Simulates tossing a coin a specified number of times."""
    console.print(
        Panel(
            Text(
                "Welcome to the Coin Toss Simulator!",
                justify="center",
                style="bold green",
            ),
            title="[b]Coin Toss[/b]",
            border_style="green",
        )
    )

    if flips <= 0:
        console.print(
            Text("Number of flips must be a positive integer.", style="bold red")
        )
        return

    results = {"Heads": 0, "Tails": 0}

    for i in range(flips):
        console.print(f"\n[b]Flipping coin (Toss {i + 1} of {flips})...[/b]")
        # Simulate a brief pause for drama
        time.sleep(0.5)

        outcome = random.choice(["Heads", "Tails"])
        results[outcome] += 1

        coin_display = get_coin_art(outcome)
        console.print(coin_display)
        console.print(
            f"Outcome: [bold { 'yellow' if outcome == 'Heads' else 'cyan' }]{outcome}[/bold { 'yellow' if outcome == 'Heads' else 'cyan' }]!"
        )

    console.print("\n" + "=" * 30)
    console.print(Text("Tossing Complete!", justify="center", style="bold green"))
    console.print("=" * 30 + "\n")

    console.print(
        Panel(
            Text(
                f"Heads: {results['Heads']}\nTails: {results['Tails']}",
                justify="center",
            ),
            title="[b]Results[/b]",
            border_style="blue",
        )
    )


if __name__ == "__main__":
    toss()
