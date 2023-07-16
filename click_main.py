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
@click.option("-n", "--name", prompt="Enter the task name", help="Name of the new task")
@click.option("-d","--desc", prompt="Enter the task description", help="Description of the new task")
def add_todo(name, description, priority, todofile):
    #if filename provided just take it, else ignore it
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename, "a+") as f:
        f.write(f"{name} : {description} [Prioirity : {PRIORITIES[priority]}]") 
    
@click.command() 
@click.argument("index", type=int, required=1) # required is set to True
@click.argument("todofile", type=click.Path(exists=False))
def delete_todo(index,todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    #read the text and modify it
    with open(filename,"r") as f:
        todo_list = f.read().splitlines()
        todo_list.pop(index)
    #paste the modified text
    with open(filename,"w") as f:
        f.write("\n".join(todo_list))
        f.write("\n")
        
if __name__ == "__main__":
    hello()    