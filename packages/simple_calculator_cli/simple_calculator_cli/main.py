import click


@click.group()
def cli():
    """A simple CLI calculator."""
    pass


@cli.command()
@click.argument("n1", type=float)
@click.argument("n2", type=float)
def add(n1, n2):
    """Adds two numbers."""
    click.echo(n1 + n2)


@cli.command()
@click.argument("n1", type=float)
@click.argument("n2", type=float)
def mul(n1, n2):
    """Multiplies two numbers."""
    click.echo(n1 * n2)


@cli.command()
@click.argument("n1", type=float)
@click.argument("n2", type=float)
def sub(n1, n2):
    """Subtracts second number from the first."""
    click.echo(n1 - n2)


@cli.command()
@click.argument("n1", type=float)
@click.argument("n2", type=float)
def div(n1, n2):
    """Divides first number by the second. Handles division by zero."""
    if n2 == 0:
        click.echo("Error: Cannot divide by zero.")
    else:
        click.echo(n1 / n2)


@cli.command()
@click.argument("base", type=float)
@click.argument("exponent", type=float)
def pow(base, exponent):
    """Raises the base to the power of the exponent."""
    click.echo(base**exponent)


@cli.command()
@click.argument("number", type=float)
def sqrt(number):
    """Calculates the square root of a number. Handles negative numbers."""
    if number < 0:
        click.echo("Error: Cannot calculate square root of a negative number.")
    else:
        click.echo(number**0.5)


if __name__ == "__main__":
    cli()
