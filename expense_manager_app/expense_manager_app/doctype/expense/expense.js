// Copyright (c) 2023, Ideenkreise and contributors
// For license information, please see license.txt

frappe.ui.form.on('Expense', {
	refresh: function(frm) {
		// show hidden fields

	},
	expense_type:function(frm){
		if(frm.doc.expense_type=="MILEAGE")
		{
			frm.set_df_property("distance", "hidden", 0)
			frm.set_df_property("rate", "hidden", 0)
	}
	else{

		frm.set_df_property("distance", "hidden", 1)
			frm.set_df_property("rate", "hidden", 1)
	}

	},
	distance:function(frm){
		frm.trigger("calculate_amount")
	},
	rate:function(frm){
		frm.trigger("calculate_amount")
	},
	calculate_amount:function(frm){
		if(frm.doc.distance && frm.doc.rate)
		{
			let amount=parseFloat(frm.doc.distance)*parseFloat(frm.doc.rate)
			frm.doc.amount=amount
			frm.refresh_field("amount")
		}

	}
});
