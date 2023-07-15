import click

@click.command()
@click.option("--name", prompt="Enter your name", help="this would be a username")
def hello(name):
    click.echo(f"Hello {name}!!")

PRIORITIES = {
    'high' : "crucial",
    'medium' : "within 1 day",
    'low' : "within a week"
}

@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys()),default="low")   
@click.argument("todofile", type=click.Path(exists=False))
def add_todo(name, description, priority, todofile):
    
    
if __name__ == "__main__":
    hello()    