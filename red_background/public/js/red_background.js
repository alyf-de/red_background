// Copyright (c) 2026, ALYF GmbH and contributors
// For license information, please see license.txt

frappe.after_ajax(function () {
	const settings = frappe.boot.background_settings;
	if (!settings) {
		// Nothing configured in Background Settings, keep the default red.
		return;
	}

	function apply_theme() {
		const theme = document.documentElement.getAttribute("data-theme");
		const bg = theme === "dark" ? settings.dark_bg_color : settings.light_bg_color;
		const navbar = theme === "dark" ? settings.dark_navbar_color : settings.light_navbar_color;
		const root_style = document.documentElement.style;

		if (bg) {
			root_style.setProperty("--bg-color", bg);
		} else {
			// No override for this theme, fall back to red_background.css.
			root_style.removeProperty("--bg-color");
		}
		if (navbar) {
			root_style.setProperty("--navbar-bg", navbar);
		} else {
			root_style.removeProperty("--navbar-bg");
		}
	}

	apply_theme();

	// Re-apply when the user switches between light/dark theme without a page reload.
	new MutationObserver(apply_theme).observe(document.documentElement, {
		attributes: true,
		attributeFilter: ["data-theme"],
	});
});
