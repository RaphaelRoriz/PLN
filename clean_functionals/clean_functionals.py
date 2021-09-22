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

		self.functional_words = ['PUNCT','SYMBOL','DET','ADP','INTJ','PRON','CONJ']

		#artigos, preposições, conjunções, interjeições e pronomes, assim como as pontuações
	
	
	def get_corpus(self):

		self.read_text(self.text_path)
		self.process_corpus()

		#print(self.corpus)


	def read_text(self,file_path):

		try:
		
			with open(file_path, 'r') as f:
				
				self.corpus['raw_text'] = f.read().splitlines()
				self.corpus['raw_text'] = "".join(self.corpus['raw_text']) 


		except IOError:

			print("Arquivo não existe!")

	def process_corpus(self):

		#remove punctuation
		self.corpus['processed_text'] = re.sub(r'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ ]', ' ', self.corpus['raw_text'])

		#remove unwanted white spaces
		self.corpus['processed_text'] = " ".join(self.corpus['processed_text'].split())

		#tokenize corpus
		self.corpus['tokens'] = self.tokenize(self.corpus['processed_text'])

	def tokenize(self,processed_text):
		
		return processed_text.split()

	def clean_functionals(self):

		# stopwords = sp.Defaults.stop_words

		# tokens_without_stopwords = [word for word in self.corpus['tokens'] if not word in stopwords]

		# aux = " ".join(tokens_without_stopwords)

		# #print(self.corpus['tokens'])
		# print(self.sp(self.corpus['raw_text']))

		doc = self.sp(self.corpus['processed_text'])

		cleaned_tokens = []

		for token in doc:
			if( not token.pos_ in self.functional_words):
				cleaned_tokens.append(token.text)

		print(" ".join(cleaned_tokens))




		






	
		
if __name__ == "__main__":

	text_path = sys.argv[1]

	cleaner = FunctionalsCleaner(text_path)
	cleaner.clean_functionals()
	


#fontes para o desenvolvimento do trabalho:
#   https://spacy.io/usage/linguistic-features
