import click

@click.group()
def cli():
    """CLI oficial da Apex Groupd Ltda"""
    pass

@cli.command()
def version():
    """Exibe a versão da lib"""
    from apex_core.version import __version__
    click.echo(__version__)

@cli.command()
@click.option("--env", default="dev", help="Ambiente de execução")
def init(env):
    """Inicializa o projeto"""
    click.echo(f"Iniciando projeto no ambiente: {env}")