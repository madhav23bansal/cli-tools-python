import random
import time
import os
import click
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt

console = Console()

# Symbols for the cards (ensure an even number for pairs)
SYMBOLS = ["@", "#", "$", "%", "&", "*", "+", "="]


def clear_screen():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def create_board(size=4):
    """Creates a shuffled board of symbol pairs."""
    if size % 2 != 0:
        raise ValueError("Board size must be even to create pairs.")

    num_pairs = (size * size) // 2
    if num_pairs > len(SYMBOLS):
        # If more pairs are needed than available symbols, repeat symbols
        extended_symbols = (SYMBOLS * (num_pairs // len(SYMBOLS) + 1))[:num_pairs]
    else:
        extended_symbols = SYMBOLS[:num_pairs]

    cards = extended_symbols * 2
    random.shuffle(cards)

    board = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append({"symbol": cards.pop(), "revealed": False, "matched": False})
        board.append(row)
    return board


def display_board(board, revealed_cards=None):
    """Displays the game board using rich.Table."""
    if revealed_cards is None:
        revealed_cards = []

    size = len(board)
    table = Table(show_header=True, header_style="bold magenta", border_style="dim")
    table.add_column("", justify="center")  # Row numbers
    for i in range(size):
        table.add_column(str(i + 1), justify="center")

    for r_idx, row in enumerate(board):
        row_display = [Text(str(r_idx + 1), style="bold")]  # Row number
        for c_idx, card in enumerate(row):
            card_id = (r_idx, c_idx)
            if card["matched"]:
                row_display.append(Text(card["symbol"], style="bold green"))
            elif card["revealed"] or card_id in revealed_cards:
                row_display.append(Text(card["symbol"], style="bold yellow"))
            else:
                row_display.append(Text("X", style="bold blue"))
        table.add_row(*row_display)

    console.print(table)


def get_player_choice(board_size, prompt_message):
    """Gets valid row and column choice from the player."""
    while True:
        try:
            row = IntPrompt.ask(f"{prompt_message} - Enter row (1-{board_size})")
            col = IntPrompt.ask(f"{prompt_message} - Enter column (1-{board_size})")
            if 1 <= row <= board_size and 1 <= col <= board_size:
                return row - 1, col - 1  # Adjust to 0-based index
            else:
                console.print(
                    Text(
                        f"Invalid input. Row and column must be between 1 and {board_size}.",
                        style="red",
                    )
                )
        except Exception:
            console.print(
                Text("Invalid input. Please enter numbers only.", style="red")
            )


@click.command()
@click.option(
    "--size",
    default=4,
    help="Size of the board (e.g., 4 for a 4x4 grid). Must be an even number.",
    type=int,
    show_default=True,
)
def play(size):
    """Plays a game of Memory (Concentration)."""
    if (
        size % 2 != 0 or size < 2 or size > 6
    ):  # Max 6x6 for 18 pairs, SYMBOLS has 8, so 8*2=16 cards. Max 4x4 for now.
        # Let's restrict to 4x4 for now as we only have 8 symbols.
        # (8 symbols * 2 = 16 cards = 4x4 board)
        # If we allow 6x6, we need 18 symbols.
        actual_symbols_needed = (size * size) // 2
        if actual_symbols_needed > len(SYMBOLS):
            console.print(
                Text(
                    f"Board size {size}x{size} requires {actual_symbols_needed} unique symbols. We only have {len(SYMBOLS)}. Please choose a smaller even size (e.g., 2 or 4).",
                    style="bold red",
                )
            )
            return
        if size < 2 or size > 4 or size % 2 != 0:  # Adjusted max size
            console.print(
                Text(
                    "Board size must be an even number between 2 and 4 (e.g., 2 for 2x2, 4 for 4x4).",
                    style="bold red",
                )
            )
            return

    clear_screen()
    console.print(
        Panel(
            Text("Welcome to the Memory Game!", justify="center", style="bold green"),
            title="[b]Memory Game[/b]",
            border_style="green",
        )
    )

    board = create_board(size)
    matched_pairs = 0
    total_pairs = (size * size) // 2
    attempts = 0

    first_choice = None

    while matched_pairs < total_pairs:
        clear_screen()
        console.print(
            Panel(
                Text("Memory Game", justify="center", style="bold green"),
                title="[b]Memory Game[/b]",
                border_style="green",
                subtitle=f"Matched: {matched_pairs}/{total_pairs} | Attempts: {attempts}",
            )
        )
        display_board(board)

        if first_choice is None:
            r1, c1 = get_player_choice(size, "First card")
            if board[r1][c1]["matched"] or board[r1][c1]["revealed"]:
                console.print(
                    Text(
                        "This card is already matched or revealed. Choose another.",
                        style="yellow",
                    )
                )
                time.sleep(1.5)
                continue
            board[r1][c1]["revealed"] = True
            first_choice = (r1, c1)
        else:
            r2, c2 = get_player_choice(size, "Second card")
            if (r1, c1) == (r2, c2):
                console.print(
                    Text(
                        "You picked the same card. Choose a different second card.",
                        style="yellow",
                    )
                )
                time.sleep(1.5)
                continue
            if board[r2][c2]["matched"] or board[r2][c2]["revealed"]:
                console.print(
                    Text(
                        "This card is already matched or revealed. Choose another.",
                        style="yellow",
                    )
                )
                time.sleep(1.5)
                continue

            board[r2][c2]["revealed"] = True
            attempts += 1

            clear_screen()
            console.print(
                Panel(
                    Text("Memory Game", justify="center", style="bold green"),
                    title="[b]Memory Game[/b]",
                    border_style="green",
                    subtitle=f"Matched: {matched_pairs}/{total_pairs} | Attempts: {attempts}",
                )
            )
            display_board(
                board, revealed_cards=[first_choice, (r2, c2)]
            )  # Show both revealed cards

            if board[r1][c1]["symbol"] == board[r2][c2]["symbol"]:
                console.print(Text("It's a match!", style="bold green blink"))
                board[r1][c1]["matched"] = True
                board[r2][c2]["matched"] = True
                matched_pairs += 1
            else:
                console.print(Text("Not a match. Try to remember!", style="bold red"))

            time.sleep(2)  # Let player see the result
            board[r1][c1]["revealed"] = False
            board[r2][c2]["revealed"] = False
            first_choice = None

    clear_screen()
    console.print(
        Panel(
            Text("Memory Game", justify="center", style="bold green"),
            title="[b]Memory Game[/b]",
            border_style="green",
            subtitle=f"Matched: {matched_pairs}/{total_pairs} | Attempts: {attempts}",
        )
    )
    display_board(board)  # Show final board
    console.print(
        Panel(
            Text(
                f"Congratulations! You found all {total_pairs} pairs in {attempts} attempts!",
                justify="center",
                style="bold bright_green",
            ),
            title="[b]Game Over[/b]",
            border_style="green",
        )
    )


if __name__ == "__main__":
    play()
