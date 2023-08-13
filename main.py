import json
from php.utils import *
from sushang.nouns import *
from sushang.verbs import *

'''
NOUNS
'''
nouns = {
	"filosofia": "phylosophy",
	"re": "person",
	"nin": "man",
	"kučara": "spoon"
}
htmls = []
htmls.append('<!doctype html>\n<html>\n<head>\n\t<title>{0}</title>\n\t<meta charset="UTF-8">\n</head>\n<body>'.format('Noun Declension'))
#
for n in nouns:
	noun = Noun(n)
	declension_table = noun.getDeclensionTable()
	print('made declension table for {0} "{1}"'.format(n,nouns[n]))
	#print("{0}\n    word: {1}\n{2}".format("=" * 65, n, "-" * 65))
	#print(json.dumps(declension_table, indent=4))
	#print("=" * 65)
	header = '<p><b>Noun:</b> <i>{0}</i> "{1}"</p>'.format(n,nouns[n])
	html = declensionToHtml(declension_table)
	htmls.append(header + html)
htmls.append('</html>')
filed_into = "table_declensions.html"
file_put_contents(filed_into,diacritics_to_entities("<hr>".join(htmls)))
print('saved into {0}'.format(filed_into))

'''
VERBS
'''
verbs = {
	"obda": "to forget",
	"obkenda": "to be able to forget",
	"obarada": "to make forget, to cause (someone) to forget",
	"ereda": "to make (someone) eat"
}
htmls = []
htmls.append('<!doctype html>\n<html>\n<head>\n\t<title>{0}</title>\n\t<meta charset="UTF-8">\n</head>\n<body>'.format('Verb Conjugation'))
#
for v in verbs:
	verb = Verb(v)
	conjugation_table = verb.getConjugationTable()
	print('made conjugation table for {0} "{1}", stem {2}'.format(v,verbs[v],verb.getStem()))
	#print("{0}\n    verb: {1}\n    stem: {2}\n{3}".format("=" * 65, v, verb.getStem(), "-" * 65))
	#print(json.dumps(conjugation_table, indent=4))
	#print("=" * 65)
	header = '<p><b>Verb:</b> <i>{0}</i> "{1}", stem <i>{2}-</i></p>'.format(v,verbs[v],verb.getStem())
	html = conjugationToHtml(conjugation_table)
	htmls.append(header + html)
htmls.append('</html>')
filed_into = "table_conjugations.html"
file_put_contents(filed_into,diacritics_to_entities("<hr>".join(htmls)))
print('saved into {0}'.format(filed_into))

