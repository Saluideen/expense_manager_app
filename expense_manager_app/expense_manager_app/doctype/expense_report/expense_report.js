// Copyright (c) 2023, Ideenkreise and contributors
// For license information, please see license.txt

frappe.ui.form.on('Expense Report', {
	refresh: function(frm) {
	// set description
	frm.events.set_description(frm)

	},

	//custom functions
	set_description:function(frm){
		let description
		
	}
});
frappe.ui.form.on("Expense list", {
	expense_doc: function (frm, cdt, cdn) {

  
	  // Calculate total
	  var total = 0;
	  frm.doc.expense.forEach(function (row) {
		total += row.amount;
	  });
console.log("total",total);
	  // Update master total field
	  frm.set_value('total', total);
	  refresh_field('total');
	},
  });
  
