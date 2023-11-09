from . import __version__ as app_version

app_name = "expense_manager_app"
app_title = "Expense Manager App"
app_publisher = "Ideenkreise"
app_description = "Expense Manager App"
app_email = "info@ideenkreisetech.com"
app_license = "l"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/expense_manager_app/css/expense_manager_app.css"
# app_include_js = "/assets/expense_manager_app/js/expense_manager_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/expense_manager_app/css/expense_manager_app.css"
# web_include_js = "/assets/expense_manager_app/js/expense_manager_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "expense_manager_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "expense_manager_app.utils.jinja_methods",
#	"filters": "expense_manager_app.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "expense_manager_app.install.before_install"
# after_install = "expense_manager_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "expense_manager_app.uninstall.before_uninstall"
# after_uninstall = "expense_manager_app.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "expense_manager_app.utils.before_app_install"
# after_app_install = "expense_manager_app.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "expense_manager_app.utils.before_app_uninstall"
# after_app_uninstall = "expense_manager_app.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "expense_manager_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"expense_manager_app.tasks.all"
#	],
#	"daily": [
#		"expense_manager_app.tasks.daily"
#	],
#	"hourly": [
#		"expense_manager_app.tasks.hourly"
#	],
#	"weekly": [
#		"expense_manager_app.tasks.weekly"
#	],
#	"monthly": [
#		"expense_manager_app.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "expense_manager_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "expense_manager_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "expense_manager_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["expense_manager_app.utils.before_request"]
# after_request = ["expense_manager_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["expense_manager_app.utils.before_job"]
# after_job = ["expense_manager_app.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"expense_manager_app.auth.validate"
# ]
