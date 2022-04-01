# -*- coding: utf-8 -*-
from __future__ import absolute_import

import click

@click.command(context_settings={'help_option_names': ['-h', '--help']})
def cli():
    click.echo("Hello World!")

if __name__ == '__main__':
    cli()
