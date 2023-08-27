import json
from php.utils import *
from sushang.nouns import *
from sushang.verbs import *
from sushang.formatters import *

'''
NOUNS
'''
nouns = {
	"filosofia": "phylosophy",
	"re": "person",
	"nin": "man",
	"kučara": "spoon"
}
lines = []
htmls = []
htmls.append('<!doctype html>\n<html>\n<head>\n\t<title>{0}</title>\n\t<meta charset="UTF-8">\n</head>\n<body>'.format('Noun Declension'))
#
for n in nouns:
	noun = Noun(n)
	declension_table = noun.getDeclensionTable()
	header_print = 'made declension table for {0} "{1}"'.format(n,nouns[n])
	print(header_print)
	header = '<p><b>Noun:</b> <i>{0}</i> "{1}"</p>'.format(n,nouns[n])
	html = declensionToHtml(declension_table)
	htmls.append(header + html)
	lines_text = printDeclensionToText(declension_table)
	lines.append(header_print)
	lines.append(lines_text)
	lines.append('')
	print(lines_text)
	print('')
htmls.append('</html>')
filed_into = "table_declensions"
file_put_contents("{0}.html".format(filed_into),diacritics_to_entities("<hr>".join(htmls)))
file_put_contents("{0}.txt".format(filed_into),"\n".join(lines))
print('saved into {0}'.format(filed_into))

'''
VERBS
'''
verbs = {
	"obda": "to forget",
	"obkenda": "to be able to forget",
	"obarada": "to make forget, to cause (someone) to forget",
	"ereda": "to make eat"
}
lines = []
htmls = []
htmls.append('<!doctype html>\n<html>\n<head>\n\t<title>{0}</title>\n\t<meta charset="UTF-8">\n</head>\n<body>'.format('Verb Conjugation'))
#
for v in verbs:
	verb = Verb(v)
	conjugation_table = verb.getConjugationTable()
	header_print = 'made conjugation table for {0} "{1}", stem {2}'.format(v,verbs[v],verb.getStem())
	print(header_print)
	header = '<p><b>Verb:</b> <i>{0}</i> "{1}", stem <i>{2}-</i></p>'.format(v,verbs[v],verb.getStem())
	html = conjugationToHtml(conjugation_table)
	htmls.append(header + html)
	lines_text = printConjugationToText(conjugation_table)
	lines.append(header_print)
	lines.append(lines_text)
	lines.append('')
	print(lines_text)
	print('')
htmls.append('</html>')
filed_into = "table_conjugations"
file_put_contents("{0}.html".format(filed_into),diacritics_to_entities("<hr>".join(htmls)))
file_put_contents("{0}.txt".format(filed_into),"\n".join(lines))
print('saved into {0}'.format(filed_into))

