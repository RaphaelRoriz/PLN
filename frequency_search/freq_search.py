import sys
import os
import re
import string

class FrequencySearcher:

	def __init__(self, directory_path, search_string):

		self.texts_path = directory_path
		self.search_string = search_string

		self.corpus = []
		# self.corpus['raw_texts'] = []
		# self.corpus['processed_texts'] = []
		# self.corpus['overlap_values'] = []
	
	def get_corpus(self):

		self.read_texts()

		self.process_corpus()

	def read_texts(self):

		os.chdir(self.texts_path)

		print(self.texts_path)
		print(self.search_string)
		print("oh droga")

		for file in os.listdir():
			print(file)
			if file.endswith(".txt"):
				# file_path = f"{self.texts_path}/{file}"
				self.read_text(file)

		# print("corpus")
		# for text in self.corpus:
		# 	print('texto')
		# 	print(text)

	def read_text(self,file_path):
		with open(file_path, 'r') as f:
			text = {}
			text['raw_text'] = f.read()
			self.corpus.append(text)

	def process_corpus(self):

		for text in self.corpus:
			text['processed_text'] = self.process_text(text['raw_text']) 

		print(self.corpus)
			

	def process_text(self, raw_text):

		#convert letters to lowercase
		raw_text = raw_text.lower()

		#remove punctuation
		processed_text = re.sub(r'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ ]', '', raw_text)

		#remove unwanted white spaces
		processed_text = " ".join(processed_text.split())

		return processed_text




	# def preProcessing(self):
		

if __name__ == "__main__":

	directory_path = sys.argv[1]
	search_string = sys.argv[2]

	# print(directory_path)
	# print(search_string)

	freq_searcher = FrequencySearcher(directory_path,search_string)
	freq_searcher.get_corpus()
	

	# frequency_searcher = FrequencySearcher()



#fontes para o desenvolvimento do trabalho:
#   https://www.geeksforgeeks.org/how-to-read-multiple-text-files-from-folder-in-python/
#   
