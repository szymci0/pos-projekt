from os import environ
from pathlib import Path

from dotenv import load_dotenv
from pkg_resources import DistributionNotFound, get_distribution

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass


dotenv_path = Path(environ.get("VIRTUAL_ENV", "")) / "pos.conf"
if dotenv_path.is_file():
    load_dotenv(dotenv_path=dotenv_path)
