"""ChD Computers bench commands extension module"""
from __future__ import unicode_literals, absolute_import, print_function
import chdnext_bench_commands
import click

@click.command("chd-version")
def chd_version():
	"""Prints the ChD Computers bench commands version"""

	print(f"ChD Computers Bench commands version {chdnext_bench_commands.__version__}")

def get_commands():
	# prevent circular imports
	from .chdtranslate import commands as translate_commands

	return list(set(translate_commands))

commands = [chd_version] + get_commands()
