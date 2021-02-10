import pathlib
import yaml

import click

DEFAULT_CONFIG_FILEPATH = pathlib.Path("~/.me.yml").expanduser()


def _config():
    return yaml.safe_load(open(DEFAULT_CONFIG_FILEPATH))


@click.group()
def cli():
    pass


@cli.command()
def config():
    print(yaml.dump(_config()))


@cli.command()
def hello():
    print("hello")


if __name__ == "__main__":
    cli()
