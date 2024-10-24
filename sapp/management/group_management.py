from sapp.utils.os_helpers import get_os_type, check_elevation
from sapp.utils.command_helpers import run_command_with_feedback
from rich.console import Console
from rich.table import Table

# Initialize the rich console
console = Console()

def add_group(groupname):
    """Add a group to the system."""
    os_type = get_os_type()

    if not check_elevation():
        console.print("[bold red]Error: You need elevated privileges to run this operation.[/bold red]")
        return

    if os_type == "Windows":
        command = ['net', 'localgroup', groupname, '/add']
    elif os_type == "Linux":
        command = ['sudo', 'groupadd', groupname]
    else:
        console.print("[bold red]Unsupported OS[/bold red]")
        return
    
    success = run_command_with_feedback(command, f"Adding group {groupname}")
    if success:
        console.print(f"[bold green]Group {groupname} created successfully![/bold green]")

def list_groups():
    """List all groups in the system."""
    os_type = get_os_type()

    if os_type == "Windows":
        command = ['net', 'localgroup']
    elif os_type == "Linux":
        command = ['cut', '-d:', '-f1', '/etc/group']
    else:
        console.print("[bold red]Unsupported OS[/bold red]")
        return
    
    result = run_command_with_feedback(command, "Listing groups")

    if result:
        groups = result.stdout.splitlines()  # Get the list of groups
        table = Table(title="System Groups")
        table.add_column("Groupname", style="cyan")

        for group in groups:
            table.add_row(group)

        console.print(table)
