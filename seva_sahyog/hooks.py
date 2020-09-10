# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "seva_sahyog"
app_title = "Seva Sahyog"
app_publisher = "Indictrans"
app_description = "Seva Sahyog custom app"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "anuradha.k@indictranstech.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/seva_sahyog/css/seva_sahyog.css"
# app_include_js = "/assets/seva_sahyog/js/seva_sahyog.js"

# include js, css files in header of web template
# web_include_css = "/assets/seva_sahyog/css/seva_sahyog.css"
# web_include_js = "/assets/seva_sahyog/js/seva_sahyog.js"

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

# Website user home page (by function)
# get_website_user_home_page = "seva_sahyog.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "seva_sahyog.install.before_install"
# after_install = "seva_sahyog.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "seva_sahyog.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	# "*": {
	# 	"on_update": "method",
	# 	"on_cancel": "method",
	# 	"on_trash": "method"
	# }
	"Volunteer" :{
	    "autoname" : "seva_sahyog.seva_sahyog.custom_script.volunteer.volunteer.autoname"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"seva_sahyog.tasks.all"
# 	],
# 	"daily": [
# 		"seva_sahyog.tasks.daily"
# 	],
# 	"hourly": [
# 		"seva_sahyog.tasks.hourly"
# 	],
# 	"weekly": [
# 		"seva_sahyog.tasks.weekly"
# 	]
# 	"monthly": [
# 		"seva_sahyog.tasks.monthly"
# 	]
# }
fixtures = ['Custom Field', 'Property Setter', 'Print Format', 'Role', 'Letter Head', 'Print Style', 'Print Settings', 'Workflow', 'Workflow State', 'Workflow Action', 'Terms and Conditions', 'Payment Terms Template', 'Payment Term','Naming Series']

# Testing
# -------

# before_tests = "seva_sahyog.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "seva_sahyog.event.get_events"
# }

