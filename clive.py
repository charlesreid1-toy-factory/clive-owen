import click


@click.group()
@click.version_option()
def cli():
    """
    The Clive Owen CLI Demo
    """


@cli.group()
def movie():
    """Get information about movies."""


@movie.command("new")
@click.argument("name")
def movie_new(name):
    """Creates a new Clive Owen movie."""
    click.echo(f"Created movie {name}, starring Clive Owen")


@movie.command("contract")
@click.argument("movie_name")
@click.argument("amount", type=int)
@click.option("--agent/--no-agent", default=True, help="Sign a movie contract with/without an agent")
def movie_contract(movie_name, amount, agent):
    """Sign a contract for a movie for amount."""
    if agent:
        click.echo(f'Signing contract for movie "{movie_name}" for amount {amount}')
    else:
        click.echo(f'Signing contract WITHOUT AN AGENT for movie "{movie_name}" for amount {amount}')
