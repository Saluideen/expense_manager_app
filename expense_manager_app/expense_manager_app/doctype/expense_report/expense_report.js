// Copyright (c) 2023, Ideenkreise and contributors
// For license information, please see license.txt

frappe.ui.form.on('Expense Report', {
	refresh: function(frm) {
		console.log("hello");
	// set description
	frm.events.set_description(frm)

	},

	//custom functions
	set_description:function(frm){
		let formattedDate = getCurrentFormattedDate();
		let description="Expense Statement For "+formattedDate
		frm.doc.description=description
		frm.refresh_field("description")
		
	}
});
function getCurrentFormattedDate() {
    const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    
    const currentDate = new Date();
    const dayOfWeek = currentDate.toLocaleDateString('en-US', { weekday: 'short' });
    const month = months[currentDate.getMonth()];
    const day = currentDate.getDate();
    const year = currentDate.getFullYear();

    const formattedDate = `${dayOfWeek} ${month} ${day} ${year}`;

    return formattedDate;
}
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
  
