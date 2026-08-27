import frappe

from red_background.install import after_migrate


def execute():
	after_migrate()
