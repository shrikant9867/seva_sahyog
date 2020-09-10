from __future__ import unicode_literals
from frappe.model.document import Document
import frappe
from six import string_types
import json
from datetime import datetime
from frappe.utils import fmt_money

def autoname(doc, method=None):
	update_naming_series(doc)

def update_naming_series(doc):
	if doc.naming_series == 'SSF/VOL/#####':
		current_count = frappe.db.sql("""select MAX(current) AS current from `tabSeries` where name = '{0}'""".format(doc.naming_series),as_dict=1)
		current = current_count[0].get('current')
		series_initial = doc.naming_series
		if current is None:
			current = 1
			series = str(current).zfill(5)
			doc.name = series_initial.replace("#####","") + series
			frappe.db.sql("""insert into tabSeries (name, current) values ('{0}','{1}')""".format(doc.naming_series,current))
		else:
			current = current + 1
			series = str(current).zfill(5)
			doc.name = series_initial.replace("#####","") + series
			frappe.db.sql("""update tabSeries set current = {0} where name = '{1}'""".format(current,doc.naming_series))