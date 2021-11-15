import pprint
import nltk 
nltk.download("omw")
from nltk.corpus import wordnet as wn 

def search_wordnet(word):

	synsets = wn.synsets(word, lang='por')

	result = {}
	result['searched_word'] = word
	result['synonyms'] = search_synonyms(synsets)
	result['hypernyms'] = search_hypernyms(synsets)
	result['hyponyms'] = search_hyponyms(synsets)

	return result


def search_synonyms(synsets):
	
	return synsets[0].lemma_names('por')

def search_hypernyms(synsets):
	
	hypernyms = []

	for element in synsets[0].hypernyms():
		hypernyms = hypernyms + element.lemma_names('por')

	return hypernyms

def search_hyponyms(synsets):

	hyponyms = []

	for element in synsets[0].hyponyms():
		hyponyms = hyponyms + element.lemma_names('por')

	return hyponyms


if __name__ == "__main__":

	print("\n".join("{}\t{}".format(k, v) for k, v in search_wordnet('comércio').items()))





