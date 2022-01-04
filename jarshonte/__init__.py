import click

from ._version import version


@click.command()
def main():
    click.echo('Hello world!')
    click.echo(f'This is version {version}.')
