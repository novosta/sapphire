from sapp.utils.os_helpers import get_os_type, check_elevation
from sapp.utils.command_helpers import run_command_with_feedback
from rich.console import Console
from rich.table import Table

# Initialize the rich console
console = Console()

def add_user(username, password=None):
    """Add a user to the system."""
    os_type = get_os_type()

    if not check_elevation():
        console.print("[bold red]Error: You need elevated privileges to run this operation.[/bold red]")
        return

    if os_type == "Windows":
        command = ['net', 'user', username, password or '*', '/add']
    elif os_type == "Linux":
        command = ['sudo', 'useradd', '-m', username]
        if password:
            command.extend(['-p', password])
    else:
        console.print("[bold red]Unsupported OS[/bold red]")
        return
    
    success = run_command_with_feedback(command, f"Adding user {username}")
    if success:
        console.print(f"[bold green]User {username} created successfully![/bold green]")

def list_users():
    """List all users in the system."""
    os_type = get_os_type()

    if os_type == "Windows":
        command = ['net', 'user']
    elif os_type == "Linux":
        command = ['cut', '-d:', '-f1', '/etc/passwd']
    else:
        console.print("[bold red]Unsupported OS[/bold red]")
        return
    
    result = run_command_with_feedback(command, "Listing users")

    # If the command succeeds, display the users in a table
    if result:
        users = result.stdout.splitlines()  # Get the list of users
        table = Table(title="System Users")
        table.add_column("Username", style="cyan")

        for user in users:
            table.add_row(user)

        console.print(table)
