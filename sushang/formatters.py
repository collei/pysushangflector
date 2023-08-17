'''
' formatters
'''

def textFormatInto(text,size=None,align=None,empties=None):
	align = align if align else 'left'
	empties = empties if empties else ' '
	text_len = len(text)
	if (size == None):
		return text
	elif (text_len >= size):
		return text[:size]
	else:
		falter_len = (size - text_len)
		if ('right' == align):
			text = (empties * falter_len) + text
		elif ('center' == align):
			falter_len_half = falter_len // 2
			text = (empties * falter_len_half) + text + (empties * falter_len_half)
			if (len(text) > size):
				text = text[:size]
		else:
			text = text + (empties * falter_len)
		return text


def coalesceIfEmpty(value,coalesce):
	value_empty = value.strip()
	if (len(value_empty) == 0):
		return coalesce
	return value


def declensionToHtml(table, panel_id=None):
	if not hasattr(declensionToHtml, "counter"):
		declensionToHtml.counter = 0
	if not panel_id:
		declensionToHtml.counter += 1
		panel_id = 'tabledecl{0}'.format(declensionToHtml.counter)
	#
	rows = []
	indexes_decl = ("nom.", "acc.", "gen.", "dat.", "abl.", "loc.", "instr.", "part.", "abess.", "comit.")
	indexes_poss = ("mi", "ti", "on", "biz", "tiz", "onk")
	#
	rows.append('<div id="{0}">'.format(panel_id))
	rows.append('<div style="width: 700px !important;">')
	rows.append('<table border="1" cellpadding="3" width="100%" style="border-collapse:collapse;">')
	rows.append('<tr><th>{0}</th><th>{1}</th><th>{2}</th><th>{3}</th></tr>'.format('Case','Singular','Dual','Plural'))
	for idx, cas in enumerate(indexes_decl):
		row_html = '<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td></tr>'.format(
			cas,
			table["cases"]["singular"][idx],
			table["cases"]["dual"][idx],
			table["cases"]["plural"][idx]
		)
		rows.append(row_html)
	rows.append('</table>')
	#
	rows.append('</div>')
	rows.append('<br>')
	rows.append('<div style="width: 700px !important;">')
	rows.append('<table border="1" cellpadding="3" width="100%" style="border-collapse:collapse;">')
	rows.append('<tr><th>{0}</th><th>{1}</th><th>{2}</th><th>{3}</th></tr>'.format('Person','Singular','Dual','Plural'))
	for idx, cas in enumerate(indexes_poss):
		row_html = '<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td></tr>'.format(
			cas,
			table["posession"]["singular"][idx],
			table["posession"]["dual"][idx],
			table["posession"]["plural"][idx]
		)
		rows.append(row_html)
	rows.append('</table>')
	rows.append('</div>')
	rows.append('</div>')
	#
	return '\n'.join(rows)


def printDeclensionToText(table):
	rows = []
	indexes_decl = ("nom.", "acc.", "gen.", "dat.", "abl.", "loc.", "instr.", "part.", "abess.", "comit.")
	indexes_poss = ("mi", "ti", "on", "biz", "tiz", "onk")
	#
	rows.append(' {0}\n {2} {3} {4} {5}\n {1}'.format(
		('=' * 76),
		('-' * 76),
		textFormatInto('Case', 8),
		textFormatInto('Singular', 20),
		textFormatInto('Dual', 20),
		textFormatInto('Plural', 20)
	))
	for idx, cas in enumerate(indexes_decl):
		row_html = ' {0} {1} {2} {3}'.format(
			textFormatInto(cas, 8),
			textFormatInto(table["cases"]["singular"][idx], 20),
			textFormatInto(table["cases"]["dual"][idx], 20),
			textFormatInto(table["cases"]["plural"][idx], 20)
		)
		rows.append(row_html)
	rows.append(' {0}\n {1}\n {0}'.format(
		('-' * 76),
		textFormatInto('Possessive Case', 48),
	))
	for idx, cas in enumerate(indexes_poss):
		row_html = ' {0} {1} {2} {3}'.format(
			textFormatInto(cas, 8),
			textFormatInto(table["posession"]["singular"][idx], 20),
			textFormatInto(table["posession"]["dual"][idx], 20),
			textFormatInto(table["posession"]["plural"][idx], 20)
		)
		rows.append(row_html)
	rows.append(' {0}'.format(('=' * 76)))
	#
	return '\n'.join(rows)
	

def conjugationToHtml(table, panel_id=None):
	if not hasattr(conjugationToHtml, "counter"):
		conjugationToHtml.counter = 0
	if not panel_id:
		conjugationToHtml.counter += 1
		panel_id = 'tableconj{0}'.format(conjugationToHtml.counter)
	#
	rows = []
	indexes = (0, 1, 2, 3, 4, 5)
	indexes_cond = (0, 1, 2, 3)
	#
	rows.append('<div id="{0}">'.format(panel_id))
	rows.append('<div style="width: 700px !important;">')
	rows.append('<table border="1" cellpadding="3" width="100%" style="border-collapse:collapse;">')
	rows.append('<tr><th colspan="2">{0}</th><th colspan="2">{1}</th><th colspan="2">{2}</th></tr>'.format('No-past','Past','Imperative'))
	rows.append('<tr><th>{0}</th><th>{1}</th><th>{0}</th><th>{1}</th><th>{0}</th><th>{1}</th></tr>'.format('Indefinite','Definite'))
	for idx in indexes:
		row_html = '<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td></tr>'.format(
			table["nopast"]["indefinite"][idx],
			table["nopast"]["definite"][idx],
			table["past"]["indefinite"][idx],
			table["past"]["definite"][idx],
			table["imperative"]["indefinite"][idx],
			table["imperative"]["definite"][idx]
		)
		rows.append(row_html)
	rows.append('</table>')
	#
	rows.append('</div>')
	rows.append('<br>')
	rows.append('<div style="width: 700px !important;">')
	rows.append('<table border="1" cellpadding="3" width="100%" style="border-collapse:collapse;">')
	rows.append('<tr><th colspan="2">{0}</th><th colspan="2">{1}</th></tr>'.format('Imperfect','Perfect'))
	rows.append('<tr><th>{0}</th><th>{1}</th><th>{0}</th><th>{1}</th></tr>'.format('Active','Passive'))
	rows.append('<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td></tr>'.format(
		table["conditional"][0],
		table["conditional"][1],
		table["conditional"][2],
		table["conditional"][3]
	))
	rows.append('</table>')
	rows.append('</div>')
	rows.append('</div>')
	#
	return '\n'.join(rows)


def printConjugationToText(table):
	rows = []
	indexes = (0, 1, 2, 3, 4, 5)
	indexes_cond = (0, 1, 2, 3)
	#
	rows.append(' {0}\n {2} {3} {4} {5}\n {1}'.format(
		('=' * 76),
		('-' * 76),
		textFormatInto('n.p.Indef', 16),
		textFormatInto('n.p.Def', 16),
		textFormatInto('past.Indef', 16),
		textFormatInto('past.Def', 16)
	))
	for idx in indexes:
		row_html = ' {0} {1} {2} {3}'.format(
			textFormatInto(table["nopast"]["indefinite"][idx], 16),
			textFormatInto(table["nopast"]["definite"][idx], 16),
			textFormatInto(table["past"]["indefinite"][idx], 16),
			textFormatInto(table["past"]["definite"][idx], 16)
		)
		rows.append(row_html)
	rows.append(' {0}\n {1} {2}\n {0}'.format(
		('-' * 76),
		textFormatInto('imperat.Indef', 16),
		textFormatInto('imperat.Def', 16),
	))
	for idx in indexes:
		row_html = ' {0} {1}'.format(
			textFormatInto(coalesceIfEmpty(table["imperative"]["indefinite"][idx], '  --  '), 16),
			textFormatInto(coalesceIfEmpty(table["imperative"]["definite"][idx], '  --  '), 16)
		)
		rows.append(row_html)
	rows.append(' {0}\n {1}\n {2} {3} {4} {5}\n {0}'.format(
		('-' * 76),
		textFormatInto('Participles', 48),
		textFormatInto('n.p.Act', 16),
		textFormatInto('n.p.Pasv', 16),
		textFormatInto('past.Act', 16),
		textFormatInto('past.Pasv', 16)
	))
	row_html = ' {0} {1} {2} {3}'.format(
		textFormatInto(table["conditional"][0], 16),
		textFormatInto(table["conditional"][1], 16),
		textFormatInto(table["conditional"][2], 16),
		textFormatInto(table["conditional"][3], 16)
	)
	rows.append(row_html)
	rows.append(' {0}'.format(('=' * 76)))
	#
	return '\n'.join(rows)