# Copyright (c) 2026, ALYF GmbH and contributors
# For license information, please see license.txt

import frappe
from frappe import _

from red_background.boot import allow_user_color_enabled, get_site_settings
from red_background.install import USER_CUSTOM_FIELD, USER_INTENSITY_FIELD
from red_background.presets import is_valid_intensity, is_valid_preset


def validate_user_desk_color(doc, method=None):
	preset_changed = doc.is_new() or doc.has_value_changed(USER_CUSTOM_FIELD)
	intensity_changed = doc.is_new() or doc.has_value_changed(USER_INTENSITY_FIELD)
	if not preset_changed and not intensity_changed:
		return

	settings = get_site_settings()
	allowed = allow_user_color_enabled(settings)

	preset = doc.get(USER_CUSTOM_FIELD)
	intensity = doc.get(USER_INTENSITY_FIELD)

	if not allowed:
		if preset:
			doc.set(USER_CUSTOM_FIELD, "")
		if intensity:
			doc.set(USER_INTENSITY_FIELD, "")
		return

	if preset and not is_valid_preset(preset):
		frappe.throw(_("Desk Colour must be one of the available presets."))

	if intensity and not is_valid_intensity(intensity):
		frappe.throw(_("Desk Colour Strength must be Tint or Strong."))
