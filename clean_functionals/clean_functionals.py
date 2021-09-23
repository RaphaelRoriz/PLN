import sys
import os
import re
import spacy

class FunctionalsCleaner:

	def __init__(self, text_path):

		self.sp = spacy.load('pt_core_news_md')

		self.text_path = text_path
		
		self.corpus = {}

		self.get_corpus()

		self.functional_words = ['PUNCT','SYMBOL','DET','ADP','INTJ','PRON','CONJ','CCONJ','SCONJ','AUX']
	
	
	def get_corpus(self):

		self.read_text(self.text_path)
		#self.process_corpus()

		#print(self.corpus)

	def read_text(self,file_path):

		try:
		
			with open(file_path, 'r') as f:
				
				self.corpus['raw_text'] = f.read().splitlines()
				self.corpus['raw_text'] = " ".join(self.corpus['raw_text']) 

		except IOError:

			print("Arquivo não existe!")

	def clean_functionals(self):

		doc = self.sp(self.corpus['raw_text'])

		cleaned_tokens = self.get_cleaned_tokens(doc)

		cleaned_text = self.get_cleaned_text(cleaned_tokens)

		print(cleaned_text)

	def get_cleaned_tokens(self,doc):

		cleaned_tokens = []

		for token in doc:
			
			if( not token.pos_ in self.functional_words):
				cleaned_tokens.append(token.text)

		return cleaned_tokens

	def get_cleaned_text(self,cleaned_tokens):

		#build the text from the tokens
		cleaned_text = " ".join(cleaned_tokens)

		#remove quotes
		cleaned_text = cleaned_text.replace('"',"")

		#remove unwanted white spaces
		cleaned_text = " ".join(cleaned_text.split())

		return cleaned_text


if __name__ == "__main__":

	text_path = sys.argv[1]

	cleaner = FunctionalsCleaner(text_path)
	cleaner.clean_functionals()
	

#fontes para o desenvolvimento do trabalho:
#   https://spacy.io/usage/linguistic-features
#   https://machinelearningknowledge.ai/tutorial-on-spacy-part-of-speech-pos-tagging/#Why_POS_tag_is_used
#   https://medium.com/@dehhmesquita/natural-language-processing-com-a-biblioteca-spacy-f324a9eeb8dc
