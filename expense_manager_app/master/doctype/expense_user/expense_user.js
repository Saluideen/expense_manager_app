// Copyright (c) 2023, Ideenkreise and contributors
// For license information, please see license.txt

frappe.ui.form.on('Expense User', {
	refresh: function(frm) {
		if(frm.doc.user){
			frm.set_df_property('email', 'read_only', 1)
		}

	}
});
