import sys
import os
import re

class FrequencySearcher:

	def __init__(self, directory_path, search_string):

		self.texts_path = directory_path
		self.search_string = {}
		self.search_string['raw'] =  search_string
		self.search_string['processed'] = self.process_text(self.search_string['raw'])
		self.search_string['tokens'] = self.tokenize(self.search_string['processed'])

		self.corpus = []

	def get_higher_overlap_text(self):

		self.get_corpus()
		self.get_higher_overlap(self.corpus)
		
	
	def get_corpus(self):

		self.read_texts()

		self.process_corpus()

	def read_texts(self):

		os.chdir(self.texts_path)

		for file in os.listdir():
			
			if file.endswith(".txt"):
				self.read_text(file)

	def read_text(self,file_path):
		with open(file_path, 'r') as f:
			text = {}
			text['raw_text'] = f.read()
			self.corpus.append(text)

	def process_corpus(self):

		for text in self.corpus:
			text['processed_text'] = self.process_text(text['raw_text']) 
			text['tokens'] = self.tokenize(text['processed_text'])
			text['overlap_score'] = self.overlap(self.search_string['tokens'],text['tokens'])

	def process_text(self, raw_text):

		#convert letters to lowercase
		raw_text = raw_text.lower()

		#remove punctuation
		processed_text = re.sub(r'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ ]', '', raw_text)

		#remove unwanted white spaces
		processed_text = " ".join(processed_text.split())

		return processed_text

	def tokenize(self,processed_text):
		
		return processed_text.split()

	def overlap(self,search_string_tokens,text_tokens):

		common_tokens_sum = self.sum_common_tokens(search_string_tokens,text_tokens)

		longer_list_size = self.get_longer_list_size(search_string_tokens,text_tokens)

		return common_tokens_sum / longer_list_size

	def sum_common_tokens(self, search_string_tokens,text_tokens):

		sum = 0

		for search_string_token in search_string_tokens:	
			for text_token in text_tokens:
				if search_string_token == text_token:
					sum += 1

		return sum

	def get_longer_list_size(self,l1,l2):

		return len(l1) if len(l1) > len(l2) else len(l2)

	def get_higher_overlap(self,corpus):
		
		higher_overlap = {}
		higher_overlap['overlap_score'] = 0
		higher_overlap['text'] = []

		for text in corpus:
			if text['overlap_score'] > higher_overlap['overlap_score']:
				higher_overlap['overlap_score'] = text['overlap_score']
				higher_overlap['text'] = text['raw_text']

		print("\n")
		print(higher_overlap['text'])
		print("\n")
		
if __name__ == "__main__":

	directory_path = sys.argv[1]
	search_string = sys.argv[2]

	freq_searcher = FrequencySearcher(directory_path,search_string)
	freq_searcher.get_higher_overlap_text()


#fontes para o desenvolvimento do trabalho:
#   https://www.geeksforgeeks.org/how-to-read-multiple-text-files-from-folder-in-python/
#   https://pt.stackoverflow.com/questions/124088/remover-pontua%C3%A7%C3%A3o-e-s%C3%ADmbolos-em-python 
