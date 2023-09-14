import json
from php.utils import *
from sushang.nouns import *
from sushang.verbs import *
from sushang.formatters import *

VOICES = ["active","passive","medial"]

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
	header = '<div style="padding: 6px;"><b>Noun:</b> <i>{0}</i> "{1}"</div>'.format(n,nouns[n])
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
	"obarakenda": "to be able to make forget, to be able to cause (someone) to forget",
	"obkenereda": "to make be able to forget, to cause (someone) to be able to forget",
	"ereda": "to make eat"
}
lines = []
htmls = []
htmls.append('<!doctype html>\n<html>\n<head>\n\t<title>{0}</title>\n\t<meta charset="UTF-8">\n</head>\n<body>'.format('Verb Conjugation'))
#
for v in verbs:
	verb = Verb(v)
	header_print = 'made conjugation table for {0} "{1}", stem {2}'.format(v,verbs[v],verb.getStem())
	print(header_print)
	header = '<hr><div style="padding: 6px;"><b>Verb:</b> <i>{0}</i> "{1}", stem <i>{2}-</i></div>'.format(v,verbs[v],verb.getStem())
	htmls.append(header)
	for voice in VOICES:
		conjugation_table = verb.getConjugationTable(voice)
		subheader = '<div style="padding: 6px; padding-left: 120px;">&bull; <b>Voice:</b> <i>{0}</i></div>'.format(voice)
		html = conjugationToHtml(conjugation_table)
		htmls.append(subheader + html)
		lines_text = printConjugationToText(conjugation_table)
		lines.append(header_print)
		lines.append(lines_text)
		lines.append('')
		print(lines_text)
	print('')
htmls.append('</html>')
filed_into = "table_conjugations"
file_put_contents("{0}.html".format(filed_into),diacritics_to_entities("".join(htmls)))
file_put_contents("{0}.txt".format(filed_into),"\n".join(lines))
print('saved into {0}'.format(filed_into))

