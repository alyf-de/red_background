# Copyright (c) 2026, ALYF GmbH and contributors
# For license information, please see license.txt

from __future__ import annotations

STANDARD = "Standard"
DEFAULT_PRESET = "Light Red"

TINT = "Tint"
STRONG = "Strong"
DEFAULT_INTENSITY = TINT

# Light text on dark surfaces (Frappe dark mode)
DARK_TEXT = "#ededed"
# Dark text on light surfaces (Frappe light mode)
LIGHT_TEXT = "#171717"


def _tokens(surface: str, navbar: str, dark_surface: str, dark_navbar: str, outline: str) -> dict:
	return {
		"light": {"surface": surface, "navbar": navbar},
		"dark": {"surface": dark_surface, "navbar": dark_navbar, "outline": outline},
	}


def _preset(label: str, tint: dict, strong: dict) -> dict:
	return {"label": label, "tint": tint, "strong": strong}


PRESETS: dict[str, dict] = {
	STANDARD: {"label": STANDARD, "tint": None, "strong": None},
	"Off White": _preset(
		"Off White",
		_tokens("#fafafa", "#f0f0f0", "#1c1c1c", "#262626", "#333333"),
		_tokens("#f2f2f2", "#e4e4e4", "#242424", "#303030", "#3f3f3f"),
	),
	"Warm Gray": _preset(
		"Warm Gray",
		_tokens("#f7f6f4", "#ebe9e6", "#1c1b1a", "#262524", "#333130"),
		_tokens("#f0ebe4", "#e2d8cc", "#262320", "#342f2a", "#433c35"),
	),
	"Cool Gray": _preset(
		"Cool Gray",
		_tokens("#f5f6f7", "#e8eaed", "#1a1b1c", "#242628", "#303336"),
		_tokens("#e9edf1", "#d5dde5", "#22262a", "#2e343a", "#3d454d"),
	),
	"Fog": _preset(
		"Fog",
		_tokens("#f1f5f9", "#e2e8f0", "#1a1d22", "#242a32", "#303740"),
		_tokens("#e4ecf5", "#cfdceb", "#222833", "#2e3644", "#3d4858"),
	),
	"Sand": _preset(
		"Sand",
		_tokens("#faf8f5", "#f0ebe3", "#221f1c", "#2e2a26", "#3a3530"),
		_tokens("#f5efe6", "#e8dccb", "#2a251f", "#383128", "#483f34"),
	),
	"Wheat": _preset(
		"Wheat",
		_tokens("#faf9f6", "#f3efe4", "#221f1c", "#2e2b26", "#3a3630"),
		_tokens("#f5f0e4", "#ebe2c8", "#2a261e", "#383428", "#484230"),
	),
	"Cream": _preset(
		"Cream",
		_tokens("#fffdf5", "#faf3d9", "#222018", "#2e2b20", "#3a3728"),
		_tokens("#faf6e0", "#f3e8b8", "#2a271c", "#383420", "#484228"),
	),
	"Butter": _preset(
		"Butter",
		_tokens("#fffcef", "#faf0c8", "#222018", "#2e2c1e", "#3a3828"),
		_tokens("#faf3d4", "#f3e5a8", "#2a271a", "#38341e", "#484226"),
	),
	"Peach": _preset(
		"Peach",
		_tokens("#fff6f1", "#ffe8dc", "#2a1e18", "#3a2a22", "#4a3830"),
		_tokens("#ffe8dc", "#ffd0b8", "#35241c", "#483228", "#5a4034"),
	),
	"Apricot": _preset(
		"Apricot",
		_tokens("#fff7f0", "#ffead9", "#2a1f18", "#3a2c22", "#4a3a30"),
		_tokens("#ffe6d4", "#ffccaa", "#35261c", "#483528", "#5a4434"),
	),
	"Light Red": _preset(
		"Light Red",
		# Legacy soft red (original app look)
		_tokens("#fff7f7", "#ffd8d8", "#361515", "#521515", "#681916"),
		_tokens("#ffeaea", "#ffc8c8", "#3f1818", "#5a1c1c", "#722020"),
	),
	"Blush": _preset(
		"Blush",
		_tokens("#fff5f5", "#ffe8e8", "#2a1a1a", "#3a2222", "#4a2a2a"),
		_tokens("#ffe0e0", "#ffc4c4", "#351c1c", "#482828", "#5a3434"),
	),
	"Rose Quartz": _preset(
		"Rose Quartz",
		_tokens("#faf7f8", "#f5eaed", "#221a1c", "#2e2426", "#3a3032"),
		_tokens("#f5e8ec", "#ebcfd8", "#2c1e22", "#3a2a2e", "#4a383c"),
	),
	"Mint": _preset(
		"Mint",
		_tokens("#f5faf7", "#e8f5ee", "#1a221e", "#242e28", "#303a34"),
		_tokens("#e6f5ec", "#ccead9", "#1e2c24", "#2a3a30", "#384a3e"),
	),
	"Sage": _preset(
		"Sage",
		_tokens("#f6f8f6", "#e9efe9", "#1b1f1b", "#252a25", "#313631"),
		_tokens("#e8f0e8", "#d0e0d0", "#202820", "#2c362c", "#3a463a"),
	),
	"Sea Foam": _preset(
		"Sea Foam",
		_tokens("#f4fafa", "#e6f4f4", "#1a2222", "#242e2e", "#303a3a"),
		_tokens("#e0f2f2", "#c4e6e6", "#1e2c2c", "#2a3a3a", "#384a4a"),
	),
	"Sky": _preset(
		"Sky",
		_tokens("#f5f9fc", "#e8f2fa", "#1a1f24", "#242a32", "#303840"),
		_tokens("#e4f0fa", "#c8e0f4", "#1e2830", "#2a3642", "#384858"),
	),
	"Blue Gray": _preset(
		"Blue Gray",
		_tokens("#f4f7fa", "#e6edf3", "#1a1e24", "#242a32", "#303840"),
		_tokens("#e2ebf4", "#c6d6e8", "#1e2630", "#2a3442", "#384658"),
	),
	"Lavender": _preset(
		"Lavender",
		_tokens("#f8f6fa", "#ede9f5", "#1f1a24", "#2a2430", "#363040"),
		_tokens("#efe8f6", "#ddd0ee", "#261e30", "#342a40", "#443850"),
	),
	"Lilac": _preset(
		"Lilac",
		_tokens("#f9f7fb", "#f0ebf5", "#201e24", "#2a2830", "#363440"),
		_tokens("#f0e8f6", "#e0d2ee", "#282430", "#363040", "#463e50"),
	),
}


def get_select_options(include_standard: bool = True) -> str:
	"""Newline-separated Select options for DocType / Custom Field."""
	order = [
		STANDARD,
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
	if not include_standard:
		order = [label for label in order if label != STANDARD]
	return "\n".join(order)


def get_user_select_options() -> str:
	"""User field: empty first row (site default) plus tint presets."""
	return "\n" + get_select_options(include_standard=False)


def get_intensity_options(*, include_empty: bool = False) -> str:
	options = f"{TINT}\n{STRONG}"
	if include_empty:
		return "\n" + options
	return options


def get_preset(label: str | None) -> dict | None:
	if not label or label == STANDARD:
		return PRESETS[STANDARD]
	return PRESETS.get(label)


def normalize_intensity(intensity: str | None) -> str:
	if intensity == STRONG:
		return STRONG
	return TINT


def get_intensity_tokens(preset_label: str | None, intensity: str | None) -> dict | None:
	preset = get_preset(preset_label)
	if not preset or preset_label == STANDARD or preset_label is None:
		return None
	key = "strong" if normalize_intensity(intensity) == STRONG else "tint"
	tokens = preset.get(key)
	if not tokens:
		return None
	return {"light": tokens["light"], "dark": tokens.get("dark")}


def is_valid_preset(label: str | None, *, allow_empty: bool = False) -> bool:
	if not label:
		return allow_empty
	return label in PRESETS


def is_valid_intensity(label: str | None, *, allow_empty: bool = False) -> bool:
	if not label:
		return allow_empty
	return label in (TINT, STRONG)


def relative_luminance(hex_color: str) -> float:
	hex_color = hex_color.lstrip("#")
	if len(hex_color) == 8:
		hex_color = hex_color[:6]
	r, g, b = (int(hex_color[i : i + 2], 16) / 255 for i in (0, 2, 4))

	def channel(c: float) -> float:
		return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

	r, g, b = channel(r), channel(g), channel(b)
	return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(color1: str, color2: str) -> float:
	l1 = relative_luminance(color1)
	l2 = relative_luminance(color2)
	lighter = max(l1, l2)
	darker = min(l1, l2)
	return (lighter + 0.05) / (darker + 0.05)
