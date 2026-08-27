# Copyright (c) 2026, ALYF GmbH and contributors
# For license information, please see license.txt

from frappe.tests.utils import FrappeTestCase

from red_background.presets import (
	DARK_TEXT,
	LIGHT_TEXT,
	PRESETS,
	STANDARD,
	STRONG,
	TINT,
	contrast_ratio,
	get_intensity_tokens,
)


class TestPresets(FrappeTestCase):
	def test_all_intensities_meet_contrast_light(self):
		for label, preset in PRESETS.items():
			if label == STANDARD:
				continue
			for intensity in (TINT, STRONG):
				surface = preset[intensity.lower()]["light"]["surface"]
				ratio = contrast_ratio(surface, LIGHT_TEXT)
				self.assertGreaterEqual(
					ratio,
					4.5,
					msg=f"{label} {intensity} light surface contrast {ratio:.2f} below 4.5:1",
				)

	def test_all_intensities_meet_contrast_dark(self):
		for label, preset in PRESETS.items():
			if label == STANDARD:
				continue
			for intensity in (TINT, STRONG):
				surface = preset[intensity.lower()]["dark"]["surface"]
				ratio = contrast_ratio(surface, DARK_TEXT)
				self.assertGreaterEqual(
					ratio,
					4.5,
					msg=f"{label} {intensity} dark surface contrast {ratio:.2f} below 4.5:1",
				)

	def test_light_red_legacy_tint_values(self):
		tokens = get_intensity_tokens("Light Red", TINT)
		self.assertEqual(tokens["light"]["surface"], "#fff7f7")
		self.assertEqual(tokens["light"]["navbar"], "#ffd8d8")
		self.assertEqual(tokens["dark"]["surface"], "#361515")
		self.assertEqual(tokens["dark"]["navbar"], "#521515")

	def test_navbar_meets_contrast(self):
		for label, preset in PRESETS.items():
			if label == STANDARD:
				continue
			for intensity in (TINT, STRONG):
				block = preset[intensity.lower()]
				light_ratio = contrast_ratio(block["light"]["navbar"], LIGHT_TEXT)
				dark_ratio = contrast_ratio(block["dark"]["navbar"], DARK_TEXT)
				self.assertGreaterEqual(light_ratio, 4.5, msg=f"{label} {intensity} light navbar")
				self.assertGreaterEqual(dark_ratio, 4.5, msg=f"{label} {intensity} dark navbar")

	def test_warm_hue_presets_exist(self):
		for label in ("Peach", "Apricot", "Cream", "Butter"):
			self.assertIn(label, PRESETS)
			self.assertIsNotNone(PRESETS[label]["tint"])
			self.assertIsNotNone(PRESETS[label]["strong"])

	def test_removed_near_duplicate_neutrals(self):
		for label in ("Pearl", "Silver Mist", "Cloud", "Stone"):
			self.assertNotIn(label, PRESETS)
