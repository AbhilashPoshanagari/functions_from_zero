import click
from mylib.bot import scrape

@click.command()
@click.option('--length', help='A person to greet')
@click.option('--name', help='Web page ')
def cli(name, length):
    result = scrape(name, length)
    click.echo(click.style(f'{result}', fg='blue'))

if __name__ == '__main__':
    cli()
