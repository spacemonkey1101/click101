import click

#annotation followed by function

@click.command()
@click.option("--name", prompt="Enter your name", help="this would be a username")
def hello(name):
    click.echo(f"Hello {name}!!")
    
if __name__ == "__main__":
    hello()    