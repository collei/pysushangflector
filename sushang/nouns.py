import json
import os

DECLENSION_TABLE = None

if (DECLENSION_TABLE == None):
	f = open(os.path.dirname(__file__) + "/declension.json", encoding="utf8")
	DECLENSION_TABLE = json.load(f)
	f.close()
##
##

class NounInfo:
	def __init__(self,noun):
		nb = noun.lower()
		# finds the vowel harmony
		nb2 = nb
		last_vowel = nb2[-1:]
		while ("aueo".find(last_vowel) < 0):
			nb2 = nb2[:-1]
			if (len(nb2) < 1):
				break
			last_vowel = nb2[-1:]
		# stores info
		self.__voweled = ("aiueo".find(nb[-1:]) >= 0)
		self.__subvoweled = ("aiueorsštn".find(nb[-1:]) >= 0)
		self.__back = ("auo".find(last_vowel) >= 0)
		self.__front = ("e".find(last_vowel) >= 0)
		self.__special = (nb in DECLENSION_TABLE["special"]["exclusions"])
		self.__specialx = (nb in DECLENSION_TABLE["special"]["exclusions2"])
	##
	def isVoweled(self):
		return self.__voweled
	##
	def isSubvoweled(self):
		return self.__subvoweled
	##
	def isBack(self):
		return self.__back
	##
	def isFront(self):
		return self.__front
	##
	def isSpecial(self):
		return self.__special
	##
	def isSpecial2(self):
		return self.__specialx
	##
	##


class Noun(NounInfo):
	def __init__(self,noun):
		super().__init__(noun)
		self.__noun = noun
		self.__table = None
	##
	def plural(self):
		the_noun = self.get().lower()
		plurals = DECLENSION_TABLE["plural"]["patternList"]
		plural_suffix = "k"
		#
		for sg, pl in plurals:
			plural_length = len(sg)
			if (the_noun[-len(sg):] == sg):
				plural_suffix = pl
				return the_noun[:-len(sg)] + pl
		#
		if (self.isVoweled()):
			return the_noun + plural_suffix
		elif (self.isBack()):
			return the_noun + 'o' + plural_suffix
		elif (self.isFront()):
			return the_noun + 'e' + plural_suffix
		#
		return the_noun + plural_suffix
	##
	def japanesePlural(self):
		return self.plural()
	##
	def hebrewPlural(self):
		return self.plural()
	##
	def dual(self):
		the_noun = self.get().lower()
		duals = DECLENSION_TABLE["dual"]
		if (self.isBack()):
			return the_noun + duals["back"]
		elif (self.isFront()):
			return the_noun + duals["front"]
		return the_noun + duals["front"]
	##
	def get(self):
		return self.__noun
	##
	def getDeclensionTable(self):
		if (self.__table != None):
			return self.__table
		#
		table = { "cases": { "singular": [], "dual": [], "plural": [] }, "posession": { "singular": [], "dual": [], "plural": [] } }
		noun = self.get().lower()
		dual = self.dual().lower()
		plural = self.plural().lower()
		info_dual = NounInfo(dual)
		info_plural = NounInfo(plural)
		t_naming = DECLENSION_TABLE["naming"]
		#//
		t_guide = None
		if (self.isVoweled()):
			if (self.isBack()):
				t_guide = DECLENSION_TABLE["endings"]["voweled"]["back"]
			else:
				t_guide = DECLENSION_TABLE["endings"]["voweled"]["front"]
		else:
			if (self.isBack()):
				t_guide = DECLENSION_TABLE["endings"]["vowelLess"]["back"]
			else:
				t_guide = DECLENSION_TABLE["endings"]["vowelLess"]["front"]
		#//
		noun_dual = self.dual().lower()
		for idx, abbreviation in enumerate(t_naming["cases"]["abbr"]):
			noun_ex = noun
			pl_empty = False
			#//
			if ("" == t_guide["cases"]["plural"][idx]):
				noun_ex = self.plural().lower()
				pl_empty = True
			#//
			if (self.isSpecial()):
				table["cases"]["singular"].append("")
				table["cases"]["dual"].append("")
				table["cases"]["plural"].append("")
			else:
				if (1==idx):
					if (self.isSubvoweled()):
						table["cases"]["singular"].append(noun + "t")
						table["cases"]["dual"].append(noun_dual + "t")
						table["cases"]["plural"].append(noun_ex + "t")
					else:
						table["cases"]["singular"].append(noun + t_guide["cases"]["singular"][idx])
						table["cases"]["dual"].append(noun_dual + t_guide["cases"]["singular"][idx])
						table["cases"]["plural"].append(noun_ex + t_guide["cases"]["singular"][idx])
				else:
					table["cases"]["singular"].append(noun + t_guide["cases"]["singular"][idx])
					table["cases"]["dual"].append(noun_dual + t_guide["cases"]["singular"][idx])
					if (pl_empty):
						table["cases"]["plural"].append(noun_ex + t_guide["cases"]["singular"][idx])
					else:
						table["cases"]["plural"].append(noun_ex + t_guide["cases"]["plural"][idx])
		#//
		for idx, abbreviation in enumerate(t_naming["pronouns"]):
			if (self.isSpecial2()):
				table["posession"]["singular"].append("")
				table["posession"]["dual"].append("")
				table["posession"]["plural"].append("")
			else:
				table["posession"]["singular"].append(noun + t_guide["posession"]["singular"][idx])
				table["posession"]["dual"].append(noun + t_guide["posession"]["dual"][idx])
				table["posession"]["plural"].append(noun + t_guide["posession"]["plural"][idx])
		#//
		self.__table = table
		return self.__table
	##
	##


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

