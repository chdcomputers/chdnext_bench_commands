"""ChD Computers bench translate commands"""
from __future__ import unicode_literals, absolute_import, print_function
import click
import frappe
from frappe.commands import pass_context, get_site
from frappe.exceptions import SiteNotSpecifiedError

@click.command("chd-getallcodefiles")
@pass_context
def chd_getallcodefiles(context):
	"""Get all code files"""
	frappe.translate.clear_cache()
	apps = frappe.get_all_apps(True)
	for app in apps:
		print(app)


@click.command("chd-getuntranslated")
@click.argument("lang")
@click.argument("untranslated_file")
@click.option("--all", default = False, is_flag = True, help = "Get all message strings")
@pass_context
def chd_getuntranslated(context, lang, untranslated_file, all = None):
	"Get untranslated strings for language"
	import frappe.translate
	site = get_site(context)
	try:
		frappe.init(site=site)
		frappe.connect()
		frappe.translate.get_untranslated(lang, untranslated_file, get_all=all)
	finally:
		frappe.destroy()

commands = [chd_getallcodefiles, chd_getuntranslated]
