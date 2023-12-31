'''
@description
	Some useful PHP functions ported
@author
	Collei Inc., <collei@collei.com.br>
	Alarido <alarido.su@gmail.com>
'''
import os

def file_put_contents(arquivo,dados):
	with open(arquivo, "w", encoding="utf8") as f:
		f.write(dados)
		f.close()


def diacritics_to_entities(text,verbatim=False):
	text_changed = ""
	for ch in text:
		ch_alt = ch
		if ch in diacritics_to_entities.__ENTITIES:
			ch_alt = diacritics_to_entities.__ENTITIES[ch][1]
		elif verbatim:
			if ch in diacritics_to_entities.__ENTITIES_VERBATIM:
				ch_alt = diacritics_to_entities.__ENTITIES_VERBATIM[ch][1]
		text_changed += ch_alt
	return text_changed


diacritics_to_entities.__ENTITIES_VERBATIM = {
	"\"": ("&#34;", "&quot;", "quotation mark"),
	"'": ("&#39;", "&apos;", "apostrophe "),
	"&": ("&#38;", "&amp;", "ampersand"),
	"<": ("&#60;", "&lt;", "less-than"),
	">": ("&#62;", "&gt;", "greater-than"),
	" ": ("&#160;", "&nbsp;", "non-breaking space"),
}
diacritics_to_entities.__ENTITIES = {
	"¡": ("&#161;", "&iexcl;", "inverted exclamation mark"),
	"¢": ("&#162;", "&cent;", "cent"),
	"£": ("&#163;", "&pound;", "pound"),
	"¤": ("&#164;", "&curren;", "currency"),
	"¥": ("&#165;", "&yen;", "yen"),
	"¦": ("&#166;", "&brvbar;", "broken vertical bar"),
	"§": ("&#167;", "&sect;", "section"),
	"¨": ("&#168;", "&uml;", "spacing diaeresis"),
	"©": ("&#169;", "&copy;", "copyright"),
	"ª": ("&#170;", "&ordf;", "feminine ordinal indicator"),
	"«": ("&#171;", "&laquo;", "angle quotation mark (left)"),
	"¬": ("&#172;", "&not;", "negation"),
	"­": ("&#173;", "&shy;", "soft hyphen"),
	"®": ("&#174;", "&reg;", "registered trademark"),
	"¯": ("&#175;", "&macr;", "spacing macron"),
	"°": ("&#176;", "&deg;", "degree"),
	"±": ("&#177;", "&plusmn;", "plus-or-minus "),
	"²": ("&#178;", "&sup2;", "superscript 2"),
	"³": ("&#179;", "&sup3;", "superscript 3"),
	"´": ("&#180;", "&acute;", "spacing acute"),
	"µ": ("&#181;", "&micro;", "micro"),
	"¶": ("&#182;", "&para;", "paragraph"),
	"·": ("&#183;", "&middot;", "middle dot"),
	"¸": ("&#184;", "&cedil;", "spacing cedilla"),
	"¹": ("&#185;", "&sup1;", "superscript 1"),
	"º": ("&#186;", "&ordm;", "masculine ordinal indicator"),
	"»": ("&#187;", "&raquo;", "angle quotation mark (right)"),
	"¼": ("&#188;", "&frac14;", "fraction 1/4"),
	"½": ("&#189;", "&frac12;", "fraction 1/2"),
	"¾": ("&#190;", "&frac34;", "fraction 3/4"),
	"¿": ("&#191;", "&iquest;", "inverted question mark"),
	"×": ("&#215;", "&times;", "multiplication"),
	"÷": ("&#247;", "&divide;", "division"),
	"À": ("&#192;", "&Agrave;", "capital a, grave accent"),
	"Á": ("&#193;", "&Aacute;", "capital a, acute accent"),
	"Â": ("&#194;", "&Acirc;", "capital a, circumflex accent"),
	"Ã": ("&#195;", "&Atilde;", "capital a, tilde"),
	"Ä": ("&#196;", "&Auml;", "capital a, umlaut mark"),
	"Å": ("&#197;", "&Aring;", "capital a, ring"),
	"Æ": ("&#198;", "&AElig;", "capital ae"),
	"Ç": ("&#199;", "&Ccedil;", "capital c, cedilla"),
	"È": ("&#200;", "&Egrave;", "capital e, grave accent"),
	"É": ("&#201;", "&Eacute;", "capital e, acute accent"),
	"Ê": ("&#202;", "&Ecirc;", "capital e, circumflex accent"),
	"Ë": ("&#203;", "&Euml;", "capital e, umlaut mark"),
	"Ì": ("&#204;", "&Igrave;", "capital i, grave accent"),
	"Í": ("&#205;", "&Iacute;", "capital i, acute accent"),
	"Î": ("&#206;", "&Icirc;", "capital i, circumflex accent"),
	"Ï": ("&#207;", "&Iuml;", "capital i, umlaut mark"),
	"Ð": ("&#208;", "&ETH;", "capital eth, Icelandic"),
	"Ñ": ("&#209;", "&Ntilde;", "capital n, tilde"),
	"Ò": ("&#210;", "&Ograve;", "capital o, grave accent"),
	"Ó": ("&#211;", "&Oacute;", "capital o, acute accent"),
	"Ô": ("&#212;", "&Ocirc;", "capital o, circumflex accent"),
	"Õ": ("&#213;", "&Otilde;", "capital o, tilde"),
	"Ö": ("&#214;", "&Ouml;", "capital o, umlaut mark"),
	"Ø": ("&#216;", "&Oslash;", "capital o, slash"),
	"Ù": ("&#217;", "&Ugrave;", "capital u, grave accent"),
	"Ú": ("&#218;", "&Uacute;", "capital u, acute accent"),
	"Û": ("&#219;", "&Ucirc;", "capital u, circumflex accent"),
	"Ü": ("&#220;", "&Uuml;", "capital u, umlaut mark"),
	"Ý": ("&#221;", "&Yacute;", "capital y, acute accent"),
	"Þ": ("&#222;", "&THORN;", "capital THORN, Icelandic"),
	"ß": ("&#223;", "&szlig;", "small sharp s, German"),
	"à": ("&#224;", "&agrave;", "small a, grave accent"),
	"á": ("&#225;", "&aacute;", "small a, acute accent"),
	"â": ("&#226;", "&acirc;", "small a, circumflex accent"),
	"ã": ("&#227;", "&atilde;", "small a, tilde"),
	"ä": ("&#228;", "&auml;", "small a, umlaut mark"),
	"å": ("&#229;", "&aring;", "small a, ring"),
	"æ": ("&#230;", "&aelig;", "small ae"),
	"ç": ("&#231;", "&ccedil;", "small c, cedilla"),
	"è": ("&#232;", "&egrave;", "small e, grave accent"),
	"é": ("&#233;", "&eacute;", "small e, acute accent"),
	"ê": ("&#234;", "&ecirc;", "small e, circumflex accent"),
	"ë": ("&#235;", "&euml;", "small e, umlaut mark"),
	"ì": ("&#236;", "&igrave;", "small i, grave accent"),
	"í": ("&#237;", "&iacute;", "small i, acute accent"),
	"î": ("&#238;", "&icirc;", "small i, circumflex accent"),
	"ï": ("&#239;", "&iuml;", "small i, umlaut mark"),
	"ð": ("&#240;", "&eth;", "small eth, Icelandic"),
	"ñ": ("&#241;", "&ntilde;", "small n, tilde"),
	"ò": ("&#242;", "&ograve;", "small o, grave accent"),
	"ó": ("&#243;", "&oacute;", "small o, acute accent"),
	"ô": ("&#244;", "&ocirc;", "small o, circumflex accent"),
	"õ": ("&#245;", "&otilde;", "small o, tilde"),
	"ö": ("&#246;", "&ouml;", "small o, umlaut mark"),
	"ø": ("&#248;", "&oslash;", "small o, slash"),
	"ù": ("&#249;", "&ugrave;", "small u, grave accent"),
	"ú": ("&#250;", "&uacute;", "small u, acute accent"),
	"û": ("&#251;", "&ucirc;", "small u, circumflex accent"),
	"ü": ("&#252;", "&uuml;", "small u, umlaut mark"),
	"ý": ("&#253;", "&yacute;", "small y, acute accent"),
	"þ": ("&#254;", "&thorn;", "small thorn, Icelandic"),
	"ÿ": ("&#255;", "&yuml;", "small y, umlaut mark"),
	"∀": ("&#8704;", "&forall;", "for all"),
	"∂": ("&#8706;", "&part;", "part"),
	"∃": ("&#8707;", "&exists;", "exists"),
	"∅": ("&#8709;", "&empty;", "empty"),
	"∇": ("&#8711;", "&nabla;", "nabla"),
	"∈": ("&#8712;", "&isin;", "isin"),
	"∉": ("&#8713;", "&notin;", "notin"),
	"∋": ("&#8715;", "&ni;", "ni"),
	"∏": ("&#8719;", "&prod;", "prod"),
	"∑": ("&#8721;", "&sum;", "sum"),
	"−": ("&#8722;", "&minus;", "minus"),
	"∗": ("&#8727;", "&lowast;", "lowast"),
	"√": ("&#8730;", "&radic;", "square root"),
	"∝": ("&#8733;", "&prop;", "proportional to"),
	"∞": ("&#8734;", "&infin;", "infinity"),
	"∠": ("&#8736;", "&ang;", "angle"),
	"∧": ("&#8743;", "&and;", "and"),
	"∨": ("&#8744;", "&or;", "or"),
	"∩": ("&#8745;", "&cap;", "cap"),
	"∪": ("&#8746;", "&cup;", "cup"),
	"∫": ("&#8747;", "&int;", "integral"),
	"∴": ("&#8756;", "&there4;", "therefore"),
	"∼": ("&#8764;", "&sim;", "simular to"),
	"≅": ("&#8773;", "&cong;", "approximately equal"),
	"≈": ("&#8776;", "&asymp;", "almost equal"),
	"≠": ("&#8800;", "&ne;", "not equal"),
	"≡": ("&#8801;", "&equiv;", "equivalent"),
	"≤": ("&#8804;", "&le;", "less or equal"),
	"≥": ("&#8805;", "&ge;", "greater or equal"),
	"⊂": ("&#8834;", "&sub;", "subset of"),
	"⊃": ("&#8835;", "&sup;", "superset of"),
	"⊄": ("&#8836;", "&nsub;", "not subset of"),
	"⊆": ("&#8838;", "&sube;", "subset or equal"),
	"⊇": ("&#8839;", "&supe;", "superset or equal"),
	"⊕": ("&#8853;", "&oplus;", "circled plus"),
	"⊗": ("&#8855;", "&otimes;", "cirled times"),
	"⊥": ("&#8869;", "&perp;", "perpendicular"),
	"⋅": ("&#8901;", "&sdot;", "dot operator"),
	"Α": ("&#913;", "&Alpha;", "Alpha"),
	"Β": ("&#914;", "&Beta;", "Beta"),
	"Γ": ("&#915;", "&Gamma;", "Gamma"),
	"Δ": ("&#916;", "&Delta;", "Delta"),
	"Ε": ("&#917;", "&Epsilon;", "Epsilon"),
	"Ζ": ("&#918;", "&Zeta;", "Zeta"),
	"Η": ("&#919;", "&Eta;", "Eta"),
	"Θ": ("&#920;", "&Theta;", "Theta"),
	"Ι": ("&#921;", "&Iota;", "Iota"),
	"Κ": ("&#922;", "&Kappa;", "Kappa"),
	"Λ": ("&#923;", "&Lambda;", "Lambda"),
	"Μ": ("&#924;", "&Mu;", "Mu"),
	"Ν": ("&#925;", "&Nu;", "Nu"),
	"Ξ": ("&#926;", "&Xi;", "Xi"),
	"Ο": ("&#927;", "&Omicron;", "Omicron"),
	"Π": ("&#928;", "&Pi;", "Pi"),
	"Ρ": ("&#929;", "&Rho;", "Rho"),
	"Σ": ("&#931;", "&Sigma;", "Sigma"),
	"Τ": ("&#932;", "&Tau;", "Tau"),
	"Υ": ("&#933;", "&Upsilon;", "Upsilon"),
	"Φ": ("&#934;", "&Phi;", "Phi"),
	"Χ": ("&#935;", "&Chi;", "Chi"),
	"Ψ": ("&#936;", "&Psi;", "Psi"),
	"Ω": ("&#937;", "&Omega;", "Omega"),
	"α": ("&#945;", "&alpha;", "alpha"),
	"β": ("&#946;", "&beta;", "beta"),
	"γ": ("&#947;", "&gamma;", "gamma"),
	"δ": ("&#948;", "&delta;", "delta"),
	"ε": ("&#949;", "&epsilon;", "epsilon"),
	"ζ": ("&#950;", "&zeta;", "zeta"),
	"η": ("&#951;", "&eta;", "eta"),
	"θ": ("&#952;", "&theta;", "theta"),
	"ι": ("&#953;", "&iota;", "iota"),
	"κ": ("&#954;", "&kappa;", "kappa"),
	"λ": ("&#955;", "&lambda;", "lambda"),
	"μ": ("&#956;", "&mu;", "mu"),
	"ν": ("&#957;", "&nu;", "nu"),
	"ξ": ("&#958;", "&xi;", "xi"),
	"ο": ("&#959;", "&omicron;", "omicron"),
	"π": ("&#960;", "&pi;", "pi"),
	"ρ": ("&#961;", "&rho;", "rho"),
	"ς": ("&#962;", "&sigmaf;", "sigmaf"),
	"σ": ("&#963;", "&sigma;", "sigma"),
	"τ": ("&#964;", "&tau;", "tau"),
	"υ": ("&#965;", "&upsilon;", "upsilon"),
	"φ": ("&#966;", "&phi;", "phi"),
	"χ": ("&#967;", "&chi;", "chi"),
	"ψ": ("&#968;", "&psi;", "psi"),
	"ω": ("&#969;", "&omega;", "omega"),
	"ϑ": ("&#977;", "&thetasym;", "theta symbol"),
	"ϒ": ("&#978;", "&upsih;", "upsilon symbol"),
	"ϖ": ("&#982;", "&piv;", "pi symbol"),
	"Œ": ("&#338;", "&OElig;", "capital ligature OE"),
	"œ": ("&#339;", "&oelig;", "small ligature oe"),
	"Š": ("&#352;", "&Scaron;", "capital S with caron"),
	"š": ("&#353;", "&scaron;", "small S with caron"),
	"Ÿ": ("&#376;", "&Yuml;", "capital Y with diaeres"),
	"ƒ": ("&#402;", "&fnof;", "f with hook"),
	"ˆ": ("&#710;", "&circ;", "modifier letter circumflex accent"),
	"˜": ("&#732;", "&tilde;", "small tilde"),
	" ": ("&#8194;", "&ensp;", "en space"),
	" ": ("&#8195;", "&emsp;", "em space"),
	" ": ("&#8201;", "&thinsp;", "thin space"),
	"‌": ("&#8204;", "&zwnj;", "zero width non-joiner"),
	"‍": ("&#8205;", "&zwj;", "zero width joiner"),
	"‎": ("&#8206;", "&lrm;", "left-to-right mark"),
	"‏": ("&#8207;", "&rlm;", "right-to-left mark"),
	"–": ("&#8211;", "&ndash;", "en dash"),
	"—": ("&#8212;", "&mdash;", "em dash"),
	"‘": ("&#8216;", "&lsquo;", "left single quotation mark"),
	"’": ("&#8217;", "&rsquo;", "right single quotation mark"),
	"‚": ("&#8218;", "&sbquo;", "single low-9 quotation mark"),
	"“": ("&#8220;", "&ldquo;", "left double quotation mark"),
	"”": ("&#8221;", "&rdquo;", "right double quotation mark"),
	"„": ("&#8222;", "&bdquo;", "double low-9 quotation mark"),
	"†": ("&#8224;", "&dagger;", "dagger"),
	"‡": ("&#8225;", "&Dagger;", "double dagger"),
	"•": ("&#8226;", "&bull;", "bullet"),
	"…": ("&#8230;", "&hellip;", "horizontal ellipsis"),
	"‰": ("&#8240;", "&permil;", "per mille "),
	"′": ("&#8242;", "&prime;", "minutes"),
	"″": ("&#8243;", "&Prime;", "seconds"),
	"‹": ("&#8249;", "&lsaquo;", "single left angle quotation"),
	"›": ("&#8250;", "&rsaquo;", "single right angle quotation"),
	"‾": ("&#8254;", "&oline;", "overline"),
	"€": ("&#8364;", "&euro;", "euro"),
	"™": ("&#8482;", "&trade;", "trademark"),
	"←": ("&#8592;", "&larr;", "left arrow"),
	"↑": ("&#8593;", "&uarr;", "up arrow"),
	"→": ("&#8594;", "&rarr;", "right arrow"),
	"↓": ("&#8595;", "&darr;", "down arrow"),
	"↔": ("&#8596;", "&harr;", "left right arrow"),
	"↵": ("&#8629;", "&crarr;", "carriage return arrow"),
	"⌈": ("&#8968;", "&lceil;", "left ceiling"),
	"⌉": ("&#8969;", "&rceil;", "right ceiling"),
	"⌊": ("&#8970;", "&lfloor;", "left floor"),
	"⌋": ("&#8971;", "&rfloor;", "right floor"),
	"◊": ("&#9674;", "&loz;", "lozenge"),
	"♠": ("&#9824;", "&spades;", "spade"),
	"♣": ("&#9827;", "&clubs;", "club"),
	"♥": ("&#9829;", "&hearts;", "heart"),
	"♦": ("&#9830;", "&diams;", "diamond"),
}

