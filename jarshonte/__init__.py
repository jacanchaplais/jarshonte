from setuptools_scm import get_version
import click


my_version = get_version()

@click.command()
def main():
    click.echo('Hello world!')
    click.echo(f'This is version {my_version}.')
