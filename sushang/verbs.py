'''
' verbs
'''
import json
import os

CONJUGATION_TABLE = None

if (CONJUGATION_TABLE == None):
	f = open(os.path.dirname(__file__) + "/conjugation.json", encoding="utf8")
	CONJUGATION_TABLE = json.load(f)
	f.close()
##
##


class VerbInfo:
	def __init__(self,verb):
		ve = verb.lower()
		# test if verb is actually a verb in its infinitive form
		if (ve[-2:] != "da"):
			raise ValueError("Verb '{0}' is NOT a Sushang infinitive verb!".format(verb))
		# extracts verb stem
		ve_stem = ve[:-2]
		# finds the vowel harmony
		ve2 = ve_stem
		last_vowel = ve2[-1:]
		while ("aueo".find(last_vowel) < 0):
			ve2 = ve2[:-1]
			if (len(ve2) < 1):
				break
			last_vowel = ve2[-1:]
		# stores info
		self.__verb = ve
		self.__stem = ve_stem
		self.__voweled = ("aiueo".find(ve_stem[-1:]) >= 0)
		self.__back = ("auo".find(last_vowel) >= 0)
		self.__front = ("auo".find(last_vowel) < 0)
	##
	def __str__(self):
		v, s, h, o = self.__verb, self.__stem, "back", "yes"
		if (self.__front):
			h = "front"
		if (not self.__voweled):
			o = "no"
		return "VerbInfo(\"{0}\"):\n\tstem: {1}\n\tharmony: {2}\n\tvoweled: {3}\n".format(v,s,h,o)	
	##
	def get(self):
		return self.__verb
	##
	def getStem(self):
		return self.__stem
	##
	def isVoweled(self):
		return self.__voweled
	##
	def isBack(self):
		return self.__back
	##
	def isFront(self):
		return self.__front
	##
	##


class Verb(VerbInfo):
	def __init__(self,verb):
		super().__init__(verb)
		self.__table = None
	##
	def __makeVoice(self,verbForm,voice):
		t_voweled = ""
		if ("passive" == voice):
			t_voweled = "ri"
		elif ("medial" == voice):
			if (self.isBack()):
				t_voweled = "ror"
			else:
				t_voweled = "rer"
		#
		t_consonanted = ""
		if ("passive" == voice):
			t_consonanted = "i"
		elif ("medial" == voice):
			if (self.isBack()):
				t_consonanted = "or"
			else:
				t_consonanted = "er"
		#
		if ("aiueoüö".find(verbForm[-1:]) >= 0):
			return verbForm + t_voweled
		return verbForm + t_consonanted
	##
	def getConjugationTable(self,voice="active"):
		if (self.__table != None):
			return self.__table
		#
		stem = self.getStem().lower()
		table = { "nopast": { "indefinite": [], "definite": [] }, "past": { "indefinite": [], "definite": [] }, "imperative": { "indefinite": [], "definite": [] }, "conditional": [] };
		guide = { "finite" : { "indefinite": None, "definite": None }, "participle": None }
		pronouns = CONJUGATION_TABLE["pronouns"]["finite"]
		#
		if (self.isVoweled()):
			guide["finite"]["indefinite"] = CONJUGATION_TABLE["indefinite"]["voweled"]["finite"]
			if (self.isBack()):
				guide["finite"]["definite"] = CONJUGATION_TABLE["definite"]["back"]["voweled"]["finite"]
				guide["participle"] = CONJUGATION_TABLE["definite"]["back"]["voweled"]["participle"]
			else:
				guide["finite"]["definite"] = CONJUGATION_TABLE["definite"]["front"]["voweled"]["finite"]
				guide["participle"] = CONJUGATION_TABLE["definite"]["front"]["voweled"]["participle"]
		else:
			guide["finite"]["indefinite"] = CONJUGATION_TABLE["indefinite"]["vowelLess"]["finite"]
			if (self.isBack()):
				guide["finite"]["definite"] = CONJUGATION_TABLE["definite"]["back"]["vowelLess"]["finite"]
				guide["participle"] = CONJUGATION_TABLE["definite"]["back"]["vowelLess"]["participle"]
			else:
				guide["finite"]["definite"] = CONJUGATION_TABLE["definite"]["front"]["vowelLess"]["finite"]
				guide["participle"] = CONJUGATION_TABLE["definite"]["front"]["vowelLess"]["participle"]
		#
		indices = (1, 3, 4)
		stem = self.getStem()
		for idx, pronoun in enumerate(pronouns):
			table["nopast"]["indefinite"].append(self.__makeVoice(stem + guide["finite"]["indefinite"]["simple"][idx], voice))
			table["nopast"]["definite"].append(self.__makeVoice(stem + guide["finite"]["definite"]["simple"][idx], voice))
			table["past"]["indefinite"].append(self.__makeVoice(stem + guide["finite"]["indefinite"]["perfect"][idx], voice))
			table["past"]["definite"].append(self.__makeVoice(stem + guide["finite"]["definite"]["perfect"][idx], voice))
			if (idx in indices):
				table["imperative"]["indefinite"].append(stem + guide["finite"]["indefinite"]["imperative"][idx])
				table["imperative"]["definite"].append(stem + guide["finite"]["definite"]["imperative"][idx])
			else:
				table["imperative"]["indefinite"].append("")
				table["imperative"]["definite"].append("")
		#
		for idx, participle in enumerate(guide["participle"]):
			table["conditional"].append(stem + participle)
		#
		self.__table = table
		return self.__table
	##
	##
