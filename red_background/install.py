# Copyright (c) 2026, ALYF GmbH and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

from red_background.boot import SETTINGS_DOCTYPE
from red_background.presets import (
	DEFAULT_INTENSITY,
	DEFAULT_PRESET,
	get_intensity_options,
	get_select_options,
	get_user_select_options,
)

USER_CUSTOM_FIELD = "desk_color_preset"
USER_INTENSITY_FIELD = "desk_color_intensity"


def after_install():
	create_user_custom_field()
	ensure_default_settings()


def after_migrate():
	create_user_custom_field()
	ensure_default_settings()
	sync_preset_options()


def sync_preset_options():
	"""Keep Select options on Settings and User in sync with presets.py."""
	site_options = get_select_options(include_standard=True)
	user_options = get_user_select_options()
	intensity_options = get_intensity_options()
	user_intensity_options = get_intensity_options(include_empty=True)

	_sync_docfield("site_color_preset", site_options)
	_sync_docfield("site_color_intensity", intensity_options)

	_sync_custom_field(USER_CUSTOM_FIELD, user_options)
	_sync_custom_field(USER_INTENSITY_FIELD, user_intensity_options)


def _sync_docfield(fieldname: str, options: str):
	if not frappe.db.exists("DocType", SETTINGS_DOCTYPE):
		return
	docfield = frappe.db.get_value(
		"DocField",
		{"parent": SETTINGS_DOCTYPE, "fieldname": fieldname},
	)
	if docfield and frappe.db.get_value("DocField", docfield, "options") != options:
		frappe.db.set_value("DocField", docfield, "options", options, update_modified=False)
		frappe.clear_cache(doctype=SETTINGS_DOCTYPE)


def _sync_custom_field(fieldname: str, options: str):
	cf_name = frappe.db.get_value("Custom Field", {"dt": "User", "fieldname": fieldname})
	if not cf_name:
		return
	if frappe.db.get_value("Custom Field", cf_name, "options") != options:
		frappe.db.set_value("Custom Field", cf_name, "options", options, update_modified=False)
		frappe.clear_cache(doctype="User")


def ensure_default_settings():
	if not frappe.db.exists("DocType", SETTINGS_DOCTYPE):
		return

	if frappe.db.get_single_value(SETTINGS_DOCTYPE, "site_color_preset"):
		if not frappe.db.get_single_value(SETTINGS_DOCTYPE, "site_color_intensity"):
			frappe.db.set_single_value(SETTINGS_DOCTYPE, "site_color_intensity", DEFAULT_INTENSITY)
		return

	frappe.get_single(SETTINGS_DOCTYPE).update(
		{
			"site_color_preset": DEFAULT_PRESET,
			"site_color_intensity": DEFAULT_INTENSITY,
			"allow_user_color": 0,
		}
	).save(ignore_permissions=True)


def create_user_custom_field():
	if not frappe.db.exists("DocType", "User"):
		return

	create_custom_fields(
		{
			"User": [
				{
					"fieldname": USER_CUSTOM_FIELD,
					"label": _("Desk Colour"),
					"fieldtype": "Select",
					"insert_after": "desk_theme",
					"hidden": 1,
					"options": get_user_select_options(),
					"description": _("Leave empty to use the site default from Desk Background Settings."),
				},
				{
					"fieldname": USER_INTENSITY_FIELD,
					"label": _("Desk Colour Strength"),
					"fieldtype": "Select",
					"insert_after": USER_CUSTOM_FIELD,
					"hidden": 1,
					"options": get_intensity_options(include_empty=True),
					"description": _("Tint is softer, Strong is more vivid. Leave empty to use the site default."),
				},
			]
		}
	)
	for fieldname in (USER_CUSTOM_FIELD, USER_INTENSITY_FIELD):
		frappe.db.set_value(
			"Custom Field",
			{"dt": "User", "fieldname": fieldname},
			"hidden",
			1,
			update_modified=False,
		)
	frappe.clear_cache(doctype="User")
