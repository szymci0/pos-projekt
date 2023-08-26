import asyncio
from functools import wraps
from pos_api.fixtures.utils import (
    drop_database,
    inject_fixtures
)
import click


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
    drop_database()
    await inject_fixtures()
    click.echo("initialised database")


if __name__ == "__main__":
    cli()
