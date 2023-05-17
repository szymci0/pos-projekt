import asyncio
from functools import wraps
from getpass import getpass

import click
from fastapi_users.password import get_password_hash
from pos_api.app import create_app


def coroutine(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.get_event_loop().run_until_complete(f(*args, **kwargs))
    
    return wrapper

@click.group()
def cli():
    "Management Scripts"

@cli.command()
@coroutine
async def database_defaults():
    click.echo("initialised database")


if __name__ == "__main__":
    cli()
