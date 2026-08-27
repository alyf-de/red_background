frappe.ui.form.on("Desk Background Settings", {
	reset_to_standard(frm) {
		frappe.confirm(__("Reset site colour to Standard?"), () => {
			frm.call("reset_to_standard").then(() => {
				frappe.ui.toolbar.clear_cache();
			});
		});
	},

	after_save() {
		frappe.ui.toolbar.clear_cache();
	},
});
