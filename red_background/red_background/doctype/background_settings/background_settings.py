# Copyright (c) 2026, ALYF GmbH and contributors
# For license information, please see license.txt

from frappe.model.document import Document


class BackgroundSettings(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		dark_background_color: DF.Color | None
		dark_navbar_color: DF.Color | None
		light_background_color: DF.Color | None
		light_navbar_color: DF.Color | None

	# end: auto-generated types
	pass
