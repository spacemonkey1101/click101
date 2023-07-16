import click


# we group click commands using a click group
@click.group()
def myCommands():
    pass


@click.command()
@click.option("--name", prompt="Enter your name", help="this would be a username")
def hello(name):
    click.echo(f"Hello {name}!!")


PRIORITIES = {"high": "crucial", "medium": "within 1 day", "low": "within a week"}


@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="low")
@click.argument("todofile", type=click.Path(exists=False),required=0)
@click.option("-n", "--name", prompt="Enter the task name", help="Name of the new task")
@click.option(
    "-d",
    "--desc",
    prompt="Enter the task description",
    help="Description of the new task",
)
def add_todo(name, description, priority, todofile):
    # if filename provided just take it, else ignore it
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename, "a+") as f:
        f.write(f"{name} : {description} [Prioirity : {PRIORITIES[priority]}]")


@click.command()
@click.argument("index", type=int, required=1)  # required is set to True
@click.argument("todofile", type=click.Path(exists=False))
def delete_todo(index, todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    # read the text and modify it
    with open(filename, "r") as f:
        todo_list = f.read().splitlines()
        todo_list.pop(index)
    # paste the modified text
    with open(filename, "w") as f:
        f.write("\n".join(todo_list))
        f.write("\n")


@click.command()
@click.option("-p", "--priority", type=click.Choice(PRIORITIES.keys()))
@click.argument("todofile", type=click.Path(exists=True))
def list_todo(priority, todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename, "r") as f:
        todo_list = f.read().splitlines()
    if priority is None:
        for index, todo_item in enumerate(todo_list):
            print(f"{index} : {todo_item}")
    else:
        for index, todo_item in enumerate(todo_list):
            if f"[Prioirity : {PRIORITIES[priority]}]" in todo_item:
                print(f"{index} : {todo_item}")


# add defined commands to the click group
myCommands.add_command(hello)
myCommands.add_command(add_todo)
myCommands.add_command(delete_todo)
myCommands.add_command(list_todo)

if __name__ == "__main__":
    myCommands()
