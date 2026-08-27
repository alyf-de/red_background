# Copyright (c) 2026, ALYF GmbH and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

from red_background.install import USER_CUSTOM_FIELD, USER_INTENSITY_FIELD
from red_background.presets import DEFAULT_INTENSITY, STANDARD


class DeskBackgroundSettings(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		allow_user_color: DF.Check
		clear_user_choices_on_reset: DF.Check
		site_color_intensity: DF.Literal["Tint", "Strong"]
		site_color_preset: DF.Literal[
			"Standard",
			"Off White",
			"Warm Gray",
			"Cool Gray",
			"Fog",
			"Sand",
			"Wheat",
			"Cream",
			"Butter",
			"Peach",
			"Apricot",
			"Light Red",
			"Blush",
			"Rose Quartz",
			"Mint",
			"Sage",
			"Sea Foam",
			"Sky",
			"Blue Gray",
			"Lavender",
			"Lilac",
		]
	# end: auto-generated types

	@frappe.whitelist()
	def reset_to_standard(self):
		frappe.only_for("System Manager")
		self.site_color_preset = STANDARD
		self.site_color_intensity = DEFAULT_INTENSITY
		if self.clear_user_choices_on_reset:
			clear_all_user_presets()
		self.save()

	def on_update(self):
		# Tint tokens live in bootinfo; clear so every user gets the new preset
		frappe.cache.delete_key("bootinfo")


def clear_all_user_presets():
	sets = []
	conditions = []
	if frappe.db.has_column("User", USER_CUSTOM_FIELD):
		sets.append("`desk_color_preset` = ''")
		conditions.append("IFNULL(`desk_color_preset`, '') != ''")
	if frappe.db.has_column("User", USER_INTENSITY_FIELD):
		sets.append("`desk_color_intensity` = ''")
		conditions.append("IFNULL(`desk_color_intensity`, '') != ''")
	if not sets:
		return
	frappe.db.sql(
		f"""
		UPDATE `tabUser`
		SET {", ".join(sets)}
		WHERE {" OR ".join(conditions)}
		"""
	)
