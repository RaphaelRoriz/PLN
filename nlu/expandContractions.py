from contractions import CONTRACTION_MAP
import re
import nltk

def expand_contractions(text,contraction_mapping = CONTRACTION_MAP):

	contractions_pattern = re.compile('({})'.format('|'.join(contraction_mapping.keys())),flags=re.IGNORECASE|re.DOTALL)

	def expand_match(contraction):
		match = contraction.group(0)
		first_char = match[0]
		expanded_contraction = contraction_mapping.get(match)\
								if contraction_mapping.get(match)\
								else contraction_mapping.get(match.lower())
		expanded_contraction = first_char+expanded_contraction[1:]
		return expanded_contraction

	expanded_text = contractions_pattern.sub(expand_match, text)
	expanded_text = re.sub("'","",expanded_text)
	return expanded_text


#print(expand_contractions("Y'all can't expand contractions I'd think"))