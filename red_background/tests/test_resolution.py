# Copyright (c) 2026, ALYF GmbH and contributors
# For license information, please see license.txt

from frappe.tests.utils import FrappeTestCase

from red_background.boot import resolve_intensity_from_settings, resolve_preset_from_settings
from red_background.presets import STANDARD, STRONG, TINT


class TestResolution(FrappeTestCase):
	def test_site_standard_user_override(self):
		self.assertEqual(
			resolve_preset_from_settings(
				site_preset=STANDARD,
				allow_user_color=True,
				user_preset="Cool Gray",
			),
			"Cool Gray",
		)

	def test_site_standard_no_user_preset(self):
		self.assertIsNone(
			resolve_preset_from_settings(
				site_preset=STANDARD,
				allow_user_color=True,
				user_preset="",
			)
		)

	def test_site_light_red_user_override(self):
		self.assertEqual(
			resolve_preset_from_settings(
				site_preset="Light Red",
				allow_user_color=True,
				user_preset="Cool Gray",
			),
			"Cool Gray",
		)

	def test_site_light_red_user_override_disabled(self):
		self.assertEqual(
			resolve_preset_from_settings(
				site_preset="Light Red",
				allow_user_color=False,
				user_preset="Cool Gray",
			),
			"Light Red",
		)

	def test_site_light_red_empty_user(self):
		self.assertEqual(
			resolve_preset_from_settings(
				site_preset="Light Red",
				allow_user_color=True,
				user_preset="",
			),
			"Light Red",
		)

	def test_user_intensity_overrides_site(self):
		self.assertEqual(
			resolve_intensity_from_settings(
				site_intensity=TINT,
				allow_user_color=True,
				user_intensity=STRONG,
			),
			STRONG,
		)

	def test_site_intensity_when_user_empty(self):
		self.assertEqual(
			resolve_intensity_from_settings(
				site_intensity=STRONG,
				allow_user_color=True,
				user_intensity="",
			),
			STRONG,
		)

	def test_user_intensity_ignored_when_disallowed(self):
		self.assertEqual(
			resolve_intensity_from_settings(
				site_intensity=TINT,
				allow_user_color=False,
				user_intensity=STRONG,
			),
			TINT,
		)
