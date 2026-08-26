# Copyright (c) 2026, ALYF GmbH and contributors
# For license information, please see license.txt

import frappe


def boot_session(bootinfo):
	"""Add configured background colors to bootinfo, if any are set.

	Falls back to the default red (set in red_background.css) when
	Background Settings is left empty.
	"""
	settings = frappe.get_cached_doc("Background Settings")
	colors = {
		"light_bg_color": settings.light_background_color,
		"light_navbar_color": settings.light_navbar_color,
		"dark_bg_color": settings.dark_background_color,
		"dark_navbar_color": settings.dark_navbar_color,
	}

	if any(colors.values()):
		bootinfo.background_settings = colors
