frappe.ui.form.on("User", {
	refresh(frm) {
		const allowed = frappe.boot.red_background?.allow_user_color === 1;
		for (const fieldname of ["desk_color_preset", "desk_color_intensity"]) {
			if (!frm.fields_dict[fieldname]) {
				continue;
			}
			frm.toggle_display(fieldname, allowed);
			frm.set_df_property(fieldname, "read_only", allowed ? 0 : 1);
		}
	},

	after_save(frm) {
		if (frm.doc.name !== frappe.session.user) {
			return;
		}

		const boot = frappe.boot.red_background;
		if (!boot || boot.allow_user_color !== 1) {
			return;
		}

		const prev_preset = boot.user_preset || "";
		const next_preset = frm.doc.desk_color_preset || "";
		const site_preset = boot.site_preset || "";
		const prev_effective_preset = prev_preset || site_preset;
		const next_effective_preset = next_preset || site_preset;

		const prev_intensity = boot.user_intensity || "";
		const next_intensity = frm.doc.desk_color_intensity || "";
		const site_intensity = boot.site_intensity || "Tint";
		const prev_effective_intensity = prev_intensity || site_intensity;
		const next_effective_intensity = next_intensity || site_intensity;

		if (
			prev_effective_preset !== next_effective_preset ||
			prev_effective_intensity !== next_effective_intensity
		) {
			frappe.ui.toolbar.clear_cache();
		}
	},
});
