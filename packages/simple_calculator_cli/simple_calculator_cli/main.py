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


if __name__ == "__main__":
    cli()
