import subprocess
from rich.console import Console
from sapp.utils.os_helpers import check_elevation

# Initialize the rich console for styled output
console = Console()

def run_command_with_feedback(command, description):
    """Run a shell command and provide user feedback (success or failure)."""
    # Check for elevated privileges
    if not check_elevation():
        console.print("[bold red]Error: This operation requires elevated privileges (Admin or sudo).[/bold red]")
        return False

    console.print(f"[yellow]{description}...[/yellow]")

    # Execute the command
    result = subprocess.run(command, capture_output=True, text=True)

    # Check the result and provide appropriate feedback
    if result.returncode == 0:
        console.print(f"[green]Success: {description}[/green]")
        return True
    else:
        console.print(f"[red]Failed: {description}[/red]")
        console.print(f"[bold red]Error Details:[/bold red] {result.stderr}")
        return False
