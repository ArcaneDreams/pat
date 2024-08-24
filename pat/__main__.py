#  Copyright Arcane Dreams Limited (c) 2024. All rights reserved.

import rich_click as click
from click import Context


@click.group("cli", help="The entrypoint of the Python Automation Tool.")
@click.option("--log-filepath", "log_filepath", type=str, multiple=True)
@click.pass_context
def cli(ctx: Context):
    """

    :param ctx:
    :return:
    """
    if ctx is None:
        raise ValueError("The runtime context is invalid or null")


@cli.group("run", help="Run the command based on the parameters")
@click.option("--parameter", "parameters", type=str, multiple=True)
@click.option("--target", "targets", type=str, multiple=True)
@click.pass_context
def cli_run(ctx: Context, parameters, targets, **kwargs):
    """

    :param parameters:
    :param targets:
    :param ctx:
    :param kwargs:
    :return:
    """
    if ctx is None:
        raise ValueError("The runtime context is invalid or null")
    ctx.ensure_object(dict)

    if not parameters:
        raise ValueError("The parameters are empty")

    if not targets:
        raise ValueError("The targets are empty")


if __name__ == "__main__":
    try:
        cli()
    except:
        pass
