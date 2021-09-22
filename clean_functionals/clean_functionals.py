import sys
import os
import re
import spacy

sp = spacy.load('pt_core_news_md')

class FunctionalsCleaner:

	def __init__(self, text_path):

		self.text_path = text_path
		
		self.corpus = {}

		self.get_corpus()
	
	
	def get_corpus(self):

		self.read_text(self.text_path)

		#self.process_corpus()


	def read_text(self,file_path):

		try:
		
			with open(file_path, 'r') as f:
				
				self.corpus['raw_text'] = f.read().splitlines()
				self.corpus['raw_text'] = "".join(self.corpus['raw_text']) 

			print(self.corpus)

		except IOError:

			print("Arquivo não existe!")

		

	
		
if __name__ == "__main__":

	text_path = sys.argv[1]

	cleaner = FunctionalsCleaner(text_path)
	


#fontes para o desenvolvimento do trabalho:
