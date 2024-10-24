import click
from sapp.management.user_management import list_users, add_user
from sapp.management.group_management import add_group, list_groups


@click.group()
def cli():
    """Sapphire CLI for managing users and groups."""
    pass

@cli.command('list_users')
def list_users_cmd():
    """List all users."""
    list_users()

if __name__ == '__main__':
    cli()
